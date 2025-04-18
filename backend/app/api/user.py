from fastapi import FastAPI, Depends, APIRouter, HTTPException
from services.generator import generate_response
from db.session import Base, engine, SessionLocal
from sqlalchemy.orm import Session
from schemas.query import QueryCreate

router = APIRouter()

# Dependency for DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/chat")
def ask_expressjs(query_data: QueryCreate , db: Session = Depends(get_db)):
    query = query_data.query  # Extract the query from the Pydantic model
    response = generate_response(query, db)  # Generate the response from LLM
    return {"query": query, "response": response}