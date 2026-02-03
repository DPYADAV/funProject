# GenAI Beginner Learning Hub 🚀

Welcome! This project is designed to help you learn the fundamentals of Generative AI step-by-step using Python and the OpenAI API.

## Project Structure

- `lessons/`: Step-by-step Python scripts.
- `data/`: Sample data for RAG (Retrieval-Augmented Generation).
- `requirements.txt`: Necessary Python libraries.

## Getting Started

1.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Set Up API Key**:
    Create a `.env` file in the root directory and add your OpenAI API key:
    ```env
    OPENAI_API_KEY=your_actual_key_here
    ```

## Lessons

### 1. Hello LLM (`lessons/01_hello_llm.py`)
Learn how to make a basic call to an LLM. This script sends a simple prompt and prints the response.
- **Key Concepts**: API Clients, Chat Completions, System vs. User messages.

### 2. Structured Output (`lessons/02_structured_output.py`)
Learn how to get JSON-formatted data from an LLM. We use **Pydantic** models to define the expected structure, ensuring the AI's response is easy to parse programmatically.
- **Key Concepts**: JSON Mode, Pydantic, Schema Validation.

### 3. Simple RAG (`lessons/03_simple_rag.py`)
Learn **Retrieval-Augmented Generation**. The script reads a local knowledge base (`data/knowledge_base.txt`), finds relevant information for a user query, and provides that context to the LLM.
- **Key Concepts**: Context Augmentation, Grounding, Knowledge Retrieval.

### 4. AI Agents (`lessons/04_simple_agent.py`)
Learn about **Function Calling**. See how an LLM can decide to use a "tool" (a Python function) to perform a specific task, like getting weather data, and then incorporate the result into its final answer.
- **Key Concepts**: Tools, Function Calling, Multi-turn Conversation.

## How to Run a Lesson
Simply run the script with python:
```bash
python3 lessons/01_hello_llm.py
```

Happy Learning!
