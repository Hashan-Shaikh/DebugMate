from fastapi import FastAPI
from app.services.generator import generate_response

app = FastAPI()

@app.get("/ask")
def ask_expressjs(query: str):
    return {"response": generate_response(query)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
