# from fastapi import APIRouter, Depends, HTTPException

# from models.user import User
# import data.user as service

# router = APIRouter(prefix = "/users")

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

# @router.post("/", response_model=User)
# def create(user: User, session: Session = Depends(get_session)) -> User:

#     return service.create(user, session)

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
