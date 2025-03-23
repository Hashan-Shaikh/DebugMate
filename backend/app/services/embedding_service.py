from sentence_transformers import SentenceTransformer

# Load embedding model (can use OpenAI, Cohere, etc.)
embed_model = SentenceTransformer("all-MiniLM-L6-v2")

def generate_embedding(text):
    """Generate an embedding for a given text."""
    return embed_model.encode(text).tolist()
