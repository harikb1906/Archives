from fastapi import FastAPI
from mangum import Mangum


app = FastAPI()


@app.get("/")
def home():
    return {
        "status": 200,
        "message": "Hello world!"
    }


handler = Mangum(app)