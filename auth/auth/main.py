from fastapi import FastAPI
from auth.routers import users

app = FastAPI()
subapi = FastAPI(openapi_prefix="/auth/v1")
app.mount("/auth/v1", subapi)


subapi.include_router(users.router)


