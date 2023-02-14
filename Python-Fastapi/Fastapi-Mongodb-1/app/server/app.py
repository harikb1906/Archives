from fastapi import FastAPI
from server.routes.student import router as StudentRouter


app = FastAPI()


@app.get("/", tags=["ROOT"])
async def read_root():
    return {"message": "Welcome to the fantastic app"}


app.include_router(StudentRouter, tags=["Student"], prefix="/student")