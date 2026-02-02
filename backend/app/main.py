from fastapi import FastAPI
from app.auth import router as auth_router
from app.leave import router as leave_router
from app.users import router as user_router
from app.ai import router as ai_router

app = FastAPI(title="WorkSphere360 API")

app.include_router(auth_router, prefix="/auth")
app.include_router(user_router, prefix="/users")
app.include_router(leave_router, prefix="/leaves")
app.include_router(ai_router, prefix="/ai")

@app.get("/")
def root():
    return {"status": "WorkSphere360 API Running"}
