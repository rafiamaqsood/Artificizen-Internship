from fastapi import APIRouter

auth_router= APIRouter(
    prefix= "/auth",
    tags= ["Authorization"]
)

@auth_router.get("/")
def auth_user():
    return ["Rafia"]