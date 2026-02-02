from fastapi import APIRouter

router = APIRouter()

@router.post("/apply")
def apply_leave(employee_id: int, from_date: str, to_date: str, reason: str):
    return {"status": "Leave Applied", "employee_id": employee_id}

@router.post("/approve")
def approve_leave(leave_id: int, manager_id: int):
    return {"status": "Approved"}
