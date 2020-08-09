from fastapi import APIRouter

router = APIRouter(prefix="/status", tags=["Status"])

@router.get("/health")
def health_check():
    return {"status": "PulseFix Service is healthy!"}
