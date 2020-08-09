from fastapi import FastAPI
from app.api.status_checker import router as status_router

app = FastAPI(title="PulseFix: Self-Healing CI/CD")

# Register Routes
app.include_router(status_router)

@app.get("/")
def read_root():
    return {"message": "PulseFix is Live!"}
