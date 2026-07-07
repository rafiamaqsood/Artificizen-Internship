from fastapi import FastAPI, HTTPException, status

app = FastAPI()

# Create a FastAPI app with a GET / route that returns {"message": "Hello, Artificizen"}.

@app.get("/")
def home():
    return {"message": "Hello, Artificizen"}

# Add a GET /users/{user_id} route that returns the user ID as an integer. Test what happens when you pass a string.
# Raise an HTTPException with status 404 and a custom message when a user ID greater than 100 is requested.

@app.get("/users/{user_id}")
def get_user(user_id: int):

    if user_id > 100:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    return {
        "user_id": user_id
    }

# Add a GET /items route with optional query parameters skip (default 0) and limit (default 10) that return a fake paginated list.

@app.get("/items")
def get_items(skip: int = 0, limit: int = 10):

    items = [
        "Laptop",
        "Phone",
        "Tablet",
        "Keyboard",
        "Mouse",
        "Monitor",
        "Camera",
        "Speaker",
        "Printer",
        "Microphone",
        "SSD",
        "GPU"
    ]

    return items[skip: skip + limit]

# Add a POST /ping route that returns status code 201 with {"status": "created"}.
@app.post("/ping", status_code=status.HTTP_201_CREATED)
def ping():
    return {
        "status": "created"
    }