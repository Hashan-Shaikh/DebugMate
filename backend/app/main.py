from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db.session import Base, engine
from api import user


app = FastAPI()

# Create tables in DB
Base.metadata.create_all(bind=engine)


# Allow origins (Frontend URL or use "*" for all origins)
origins = [
    "http://localhost:3000",  # If using React locally
    "http://127.0.0.1:3000",  # Another possible local address
    "https://your-frontend-domain.com"  # If deployed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # List of allowed origins
    allow_credentials=True,  # Allow cookies and authentication
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

app.include_router(user.router)


