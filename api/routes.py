from fastapi import APIRouter

router = APIRouter()


@router.get("/users/{user_id}")
def get_user(user_id: int):
    return {"id": user_id, "username": "johndoe", "email": "john@example.com"}


@router.post("/users/")
def create_user(user: dict):
    return {"id": 1, "username": user.get("username")}


@router.put("/users/{user_id}")
def update_user(user_id: int, user: dict):
    return {"id": user_id, "username": user.get("username")}


@router.delete("/users/{user_id}")
def delete_user(user_id: int):
    return {"message": "User deleted", "id": user_id}
