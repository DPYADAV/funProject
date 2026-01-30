import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Step 1: Define the tool(s) the LLM can call
def get_weather(location):
    """Get the current weather in a given location (Mock)"""
    print(f"\n[Tool Call] Getting weather for {location}...")
    if "mars" in location.lower():
        return json.dumps({"location": "Mars", "temperature": "-60 C", "condition": "Dusty"})
    return json.dumps({"location": location, "temperature": "22 C", "condition": "Sunny"})

def main():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY not found.")
        return

    client = OpenAI(api_key=api_key)

    # Step 2: Define the tools for the OpenAI API
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_weather",
                "description": "Get the current weather in a given location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city and state, e.g. San Francisco, CA",
                        },
                    },
                    "required": ["location"],
                },
            },
        }
    ]

    messages = [{"role": "user", "content": "What's the weather like on Mars?"}]

    print("Sending message to the agent...")

    try:
        # Step 3: First call to the model
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            tools=tools,
            tool_choice="auto",
        )

        response_message = response.choices[0].message
        tool_calls = response_message.tool_calls

        # Step 4: Check if the model wants to call a tool
        if tool_calls:
            # Add the model's response to the conversation history
            messages.append(response_message)

            for tool_call in tool_calls:
                function_name = tool_call.function.name
                function_args = json.loads(tool_call.function.arguments)

                if function_name == "get_weather":
                    function_response = get_weather(
                        location=function_args.get("location")
                    )

                    # Add the tool result to the conversation
                    messages.append(
                        {
                            "tool_call_id": tool_call.id,
                            "role": "tool",
                            "name": function_name,
                            "content": function_response,
                        }
                    )

            # Step 5: Send the updated conversation back to the model
            second_response = client.chat.completions.create(
                model="gpt-4o",
                messages=messages,
            )

            print("\nAgent Response:")
            print(second_response.choices[0].message.content)
        else:
            print("\nThe model did not call any tools.")
            print(response_message.content)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
