from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.post("/login")
def login(username: str, password: str):
    if username == "admin" and password == "admin":
        return {"role": "admin"}
    raise HTTPException(status_code=401, detail="Invalid credentials")
