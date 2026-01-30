import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def read_knowledge_base(filepath):
    with open(filepath, 'r') as f:
        return f.read()

def simple_search(query, knowledge_base):
    # For a beginner lesson, we use a very simple search:
    # Split by double newline to get paragraphs/sections
    sections = knowledge_base.split('\n\n')
    relevant_sections = []

    # Simple keyword match
    for section in sections:
        if any(word.lower() in section.lower() for word in query.split()):
            relevant_sections.append(section)

    return "\n\n".join(relevant_sections) if relevant_sections else "No relevant information found."

def main():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY not found.")
        return

    client = OpenAI(api_key=api_key)

    kb_path = "data/knowledge_base.txt"
    knowledge_base = read_knowledge_base(kb_path)

    query = "Who leads Project Nebula and what is the budget?"
    print(f"User Query: {query}")

    # Step 1: Retrieve relevant context
    context = simple_search(query, knowledge_base)
    print("\n--- Retrieved Context ---")
    print(context)
    print("-------------------------\n")

    # Step 2: Augment the prompt and Generate response
    prompt = f"""
    You are a helpful assistant for AstroCorp. Use the following context to answer the user's question.
    If the answer is not in the context, say you don't know.

    Context:
    {context}

    Question: {query}
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )

        print("LLM Answer:")
        print(response.choices[0].message.content)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
