from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session
from typing import List

from schemas.user import UserCreate, UserShow, UserUpdate
from core.database import get_db
from service.user import UserService
from models.user import User
from routes.login import get_current_user


router = APIRouter(
    prefix = "/api/users",
    tags=["API - Users"],
    responses={
        status.HTTP_201_CREATED: {"description": "User has been created."},
        status.HTTP_404_NOT_FOUND: {"description": "User not found"},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"description": "Internal server error"},
    }
)


@router.get(
    "/",
    response_model=list[UserShow],
    status_code=status.HTTP_200_OK,
    summary="Get all users",
    response_description="List of all users"
)
def get_users(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
) -> List[UserShow]:
    """Retrieve all users."""
    try:
        return UserService.get_users(db, skip, limit)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving users: {str(e)}"
        )


@router.get(
    "/{user_id}",
    response_model=UserShow,
    status_code=status.HTTP_200_OK,
    summary="Get a specific user",
    response_description="The requested user"
)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)) -> UserShow:
    """Retrieve a specific user by its ID."""
    try:
        user = UserService.get_user_by_id(user_id, db)
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with ID {user_id} not found"
            )
        return user
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving user: {str(e)}"
        )


@router.post(
    "/",
    response_model=UserShow,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new user",
    response_description="The created user")
def create_user(user: UserCreate, db: Session = Depends(get_db)) -> UserCreate:
    """Create a user"""
    try:
        created_user = UserService.create_user(user=user, db=db)
        return created_user
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error creating user: {str(e)}"
        )


@router.patch(
    "/{user_id}",
    response_model=UserShow,
    status_code=status.HTTP_200_OK,
    summary="Update a user (partial update)"
)
def patch_user(
    user_id: int,
    user: UserUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> UserShow:
    """
    Update an user (partial update).
    Only provided fields will be updated.
    Only current user can update his account
    """
    if current_user.id != user_id:
        # Raise an exception if the current user tries to update someone else's account
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to update this account"
        )

    return UserService.update_user(
        user_id=user_id,
        user_data=user,
        db=db,
        partial=True
    )


@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete an user",
    response_description="User succesfully deleted"
)
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Delete a user by its ID."""
    try:
        if current_user.id != user_id:
            # Raise an exception if the current user tries to update someone else's account
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Not authorized to delete this account"
            )

        UserService.delete_user(user_id, db)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error deleting user: {str(e)}"
        )
