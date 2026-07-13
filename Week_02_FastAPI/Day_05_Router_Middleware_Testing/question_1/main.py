# Split your app into at least two routers: routers/users.py and routers/auth.py. Register both in main.py with appropriate prefixes and tags.

from fastapi import FastAPI
from routers.users import router
from routers.auth import auth_router

app= FastAPI()
app.include_router(router)
app.include_router(auth_router)