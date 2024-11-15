from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from schemas.user import UserCreate, UserShow
from core.database import get_db
import data.user as service


router = APIRouter(
    prefix = "/users",
    tags=["Books"],
    responses={
        status.HTTP_201_CREATED: {"description": "User has been created."},
        status.HTTP_404_NOT_FOUND: {"description": "User not found"},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"description": "Internal server error"},
    }
)

# @router.get("/", response_model=list[User])
# def get_all(session: Session = Depends(get_session)) -> list[User]:

#     return service.get_all(session)

# @router.get("/{user_id}", response_model=User)
# def get_one(user_id: int, session: Session = Depends(get_session)) -> User:
#     """Endpoint to get a user by its ID."""
#     user = service.get_one(user_id, session)
#     if user is None:
#         raise HTTPException(status_code=404, detail="User not found.")
#     return user

@router.post("/", response_model=UserShow, status_code=status.HTTP_201_CREATED)
def create(user: UserCreate, db: Session = Depends(get_db)) -> UserCreate:
    user = service.create_new_user(user_data=user, db=db)
    return user

# @router.patch("/{user_id}", response_model=User)
# def modify(user_id: int, user: User, session: Session = Depends(get_session)) -> User:
#     updated_user = service.modify(user_id, user, session)

#     if not updated_user:
#         raise HTTPException(status_code=404, detail="User not found.")

#     return updated_user

# @router.delete("/{user_id}")
# def delete(user_id: int, user: User, session: Session = Depends(get_session)) -> dict:
#     user = session.get(User, user_id)

#     if not user:
#         raise HTTPException(status_code=404, detail="User not found.")

#     service.delete(user_id, session)

#     return {"detail": "User deleted successfully"}
