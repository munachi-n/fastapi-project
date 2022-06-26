from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health_check():
    return {"status": "healthy"}


@router.get("/ping")
def ping():
    return {"message": "pong"}
