from services.embedding_service import generate_embedding
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Load API key from environment variables
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

index_name = "ai-dev-assistant"

def search_similar_issues(query, top_k=5):
    pc = Pinecone(api_key=PINECONE_API_KEY)

    # Connect to the index
    index = pc.Index(index_name)

    """Find similar Express.js issues using Pinecone."""
    query_embedding = generate_embedding(query)
    
    results = index.query(vector=query_embedding, top_k=top_k, include_metadata=True)
    
    return [
        {"title": res["metadata"]["title"], "body": res["metadata"]["body"]}
        for res in results["matches"]
    ]
