import os
from dotenv import load_dotenv
from groq import Groq
from services.retriever import search_similar_issues

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize Groq client
client = Groq(api_key=GROQ_API_KEY)

def generate_response(query):
    """Generate an LLM-based response for a query using Groq API."""
    related_issues = search_similar_issues(query)
    print(len(related_issues))

    # Format the context from related GitHub issues
    context = "\n".join([f"{issue['title']} - {issue['body']}" for issue in related_issues])

    # Construct the prompt
    prompt = f"""You are an Express.js expert. Answer the user's query based on the following related issues:
    {context}
    User Query: {query}"""

    # Generate response using Groq API
    response = client.chat.completions.create(
        model="llama3-8b-8192",  # Choose a suitable Groq model
        messages=[{"role": "system", "content": prompt}]
    )

    return response.choices[0].message.content

