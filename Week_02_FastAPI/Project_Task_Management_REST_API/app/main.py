from fastapi import FastAPI , Request
from fastapi.responses import JSONResponse
from app.database import Base, engine
from app.routers.auth import auth_router
from app.routers.tasks import task_router
from fastapi.middleware.cors import CORSMiddleware


Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "message": "Internal Server Error",
            "detail": str(exc)
        }
    )

origins=[
    "http://localhost" ,
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods =["*"],
    allow_headers =["*"]

)

app.include_router(auth_router)
app.include_router(task_router)