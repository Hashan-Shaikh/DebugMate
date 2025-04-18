import os
from dotenv import load_dotenv
from groq import Groq
from services.retriever import search_similar_issues
from sqlalchemy.orm import Session
from models.user import User

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize Groq client
client = Groq(api_key=GROQ_API_KEY)

def generate_response(query: str, db: Session):
    """Generate an LLM-based response for a query using Groq API, ensuring Markdown formatting."""
    related_issues = search_similar_issues(query)
    print(len(related_issues))

    # Format the context from related GitHub issues
    context = "\n".join([f"**{issue['title']}**\n\n{issue['body']}" for issue in related_issues])

    # Construct the Markdown-enforced prompt
    prompt = f"""
    You are an expert in Express.js. Your work is to help people to solve their debugging isssues. People will give you their express.js related issues and difficulty they are facing using it and you have to debug the problem and tell them the write solution.Provide detailed and well-formatted answers using Markdown if and only if you want to generate code else normal string. 
    - Use triple backticks for code blocks.
    - Use the correct language identifier for syntax highlighting (e.g., ```javascript).
    - Format important points in **bold**.
    - Use bullet points for lists.
    
    **These can be Related Issues:**
    {context}

    **User Query:** {query}
    """

    # Generate response using Groq API
    response = client.chat.completions.create(
        model="llama3-8b-8192",  # Choose a suitable Groq model
        messages=[{"role": "system", "content": prompt}]
    )

    db_user = User(query=query, response=response.choices[0].message.content)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)


    return response.choices[0].message.content
