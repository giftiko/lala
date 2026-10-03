from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS so your HTML file can talk to FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins (good for local testing)
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)


@app.get("/sup")
def read_root():
  return {"message": "Hello, sup!"}


@app.get("/name")
def read_name():
  return {"message": "Hello, lala!"}


@app.get("/age")
def read_age():
  return {"message": "Hello, lala! You are 20 years old."}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
  return {"item_id": item_id, "query": q}