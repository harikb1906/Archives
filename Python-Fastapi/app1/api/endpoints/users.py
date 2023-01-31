from fastapi import APIRouter


router = APIRouter()


@router.get("/")
async def get_users():
    return {"message": ["User list!"]}


@router.get("/{user_id}")
async def get_users(user_id):
    return {
        "message": ["User detail!"],
        "data": {
            "user_id": user_id
        }
    }


