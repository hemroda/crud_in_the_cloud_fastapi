from fastapi import APIRouter

router = APIRouter(prefix = "/explorers")

@router.get("/")
def get_All_explorer():
    return "All the explorers"