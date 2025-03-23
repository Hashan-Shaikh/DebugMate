import json
from services.embedding_service import generate_embedding  # Assuming you have this function defined
from pinecone import Pinecone
import os
from dotenv import load_dotenv
from pinecone import ServerlessSpec


load_dotenv()

# Pinecone setup
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
pc = Pinecone(api_key=PINECONE_API_KEY)

# Create or connect to Pinecone index
index_name = "ai-dev-assistant"
if index_name not in [i.name for i in pc.list_indexes()]:
    pc.create_index(
        name=index_name,
        vector_type="dense",
        metric="cosine",
        dimension=384,
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        ),
        deletion_protection="disabled",
        tags={
            "environment": "development"
        }
    )

# Connect to the index
index = pc.Index(index_name)

# Load the data from the external JSON file in the `data` folder
def load_data():
    with open("../data/express_issues.json", "r") as file:
        return json.load(file)

# Function to upsert the data into Pinecone
def upsert_data():
    data = load_data()  # Load data from external file
    vectors = []

    for issue in data:
        issue_text = f"{issue['title']} - {issue['body']} - {issue['comments_text']}"
        embedding = generate_embedding(issue_text)  # Generate embedding for the issue text

        vectors.append({
            "id": str(issue["id"]),
            "values": embedding,
            "metadata": {
                "title": issue["title"],
                "body": issue["body"],
                "comments_text": issue["comments_text"]
            }
        })

    # Upsert vectors into Pinecone
    index.upsert(vectors)
    print(f"Upserted {len(vectors)} issues into Pinecone.")

# Example call to upsert data
if __name__ == "__main__":
    upsert_data()
