import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def main():
    # Initialize the OpenAI client
    # It will automatically look for OPENAI_API_KEY in environment variables
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        print("Error: OPENAI_API_KEY not found in environment variables.")
        print("Please create a .env file with your OPENAI_API_KEY=your_key_here")
        return

    client = OpenAI(api_key=api_key)

    print("Sending a simple message to the LLM...")

    try:
        response = client.chat.completions.create(
            model="gpt-4o", # You can also use "gpt-3.5-turbo"
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Hello! Can you briefly explain what an LLM is?"}
            ]
        )

        # Print the response from the LLM
        print("\nLLM Response:")
        print(response.choices[0].message.content)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
