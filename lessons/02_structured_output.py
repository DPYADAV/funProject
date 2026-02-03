import os
import json
from typing import List
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Define a Pydantic model for the structured output
class MovieInfo(BaseModel):
    title: str
    year: int
    genres: List[str]
    director: str
    rating: float

def main():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY not found.")
        return

    client = OpenAI(api_key=api_key)

    print("Requesting structured data about a movie...")

    try:
        # Use the 'response_format' parameter to ensure JSON output
        # In newer versions of OpenAI SDK, you can use parse() for even better integration with Pydantic
        completion = client.beta.chat.completions.parse(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Extract movie information."},
                {"role": "user", "content": "Inception is a 2010 science fiction action film written and directed by Christopher Nolan. It stars Leonardo DiCaprio. It has a rating of 8.8 on IMDb. Genres: Action, Sci-Fi, Adventure."}
            ],
            response_format=MovieInfo,
        )

        movie = completion.choices[0].message.parsed

        print("\nStructured Response:")
        print(f"Title: {movie.title}")
        print(f"Year: {movie.year}")
        print(f"Director: {movie.director}")
        print(f"Rating: {movie.rating}")
        print(f"Genres: {', '.join(movie.genres)}")

        # You can also get it as a dict or JSON
        # print(movie.model_dump_json(indent=2))

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
