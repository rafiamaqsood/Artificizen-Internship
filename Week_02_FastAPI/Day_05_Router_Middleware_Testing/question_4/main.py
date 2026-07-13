# Write a global exception handler for HTTPException that always returns JSON in the shape {"error": true, "detail": "...", "status": 404} instead of FastAPI’s default

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": True,
            "detail": exc.detail,
            "status": exc.status_code
        }
    )

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    if user_id != 1:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "id": 1,
        "name": "Rafia"
    }