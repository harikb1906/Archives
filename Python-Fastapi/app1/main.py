from fastapi import FastAPI
from mangum import Mangum
from api.api import router as api_router


app = FastAPI()


@app.get("/")
async def root():
    return {
        "status": 200,
        "message": "Hello world!"
    }


# Replace
# @app.get("/users")
# async def get_users():
#     return {"message": "Get users!"}


app.include_router(api_router, prefix="/api")


handler = Mangum(app)