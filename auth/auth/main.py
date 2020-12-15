import uvicorn

from fastapi import FastAPI
from auth.routers import users

app = FastAPI()

subapi = FastAPI(openapi_prefix="/auth/v1")
app.mount("/auth/v1", subapi)

general_responses = {404: {"description": "Not found"}}

def main():
    subapi.include_router(users.router)

if __name__ == "__main__":
    main()
