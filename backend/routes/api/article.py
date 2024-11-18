from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session
from typing import List

from schemas.article import ArticleCreate, ArticleUpdate, ArticleShow
from core.database import get_db
from service.article import ArticleService
from models.user import User
from routes.login import get_current_user


router = APIRouter(
    prefix = "/api/articles",
    tags=["API - Articles"],
    responses={
        status.HTTP_201_CREATED: {"description": "Article has been created."},
        status.HTTP_404_NOT_FOUND: {"description": "Article not found"},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"description": "Internal server error"},
    }
)

@router.get(
    "/",
    response_model=list[ArticleShow],
    status_code=status.HTTP_200_OK,
    summary="Get all articles",
    response_description="List of all articles"
)
def get_articles(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
) -> List[ArticleShow]:
    """Retrieve all articles."""
    try:
        return ArticleService.get_articles(db, skip, limit)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving articles: {str(e)}"
        )

@router.get(
    "/{article_id}",
    response_model=ArticleShow,
    status_code=status.HTTP_200_OK,
    summary="Get a specific article",
    response_description="The requested article"
)
def get_article_by_id(article_id: int, db: Session = Depends(get_db)) -> ArticleShow:
    """Retrieve a specific article by its ID."""
    try:
        article = ArticleService.get_article_by_id(article_id, db)
        if article is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Article with ID {article_id} not found"
            )
        return article
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving article: {str(e)}"
        )


@router.post(
    "/",
    response_model=ArticleShow,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new article",
    response_description="The created article"
)
def create_article(
    article: ArticleCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    response: Response = None
) -> ArticleShow:
    """Create an article"""
    try:
        created_article = ArticleService.create_article(article, db, author_id=current_user.id)
        response.headers["Location"] = f"/articles/{created_article.id}"
        return created_article
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error creating article: {str(e)}"
        )


@router.put(
    "/{article_id}",
    response_model=ArticleShow,
    status_code=status.HTTP_200_OK,
    summary="Update an article (full update)"
)
def update_article(
    article_id: int,
    article: ArticleUpdate,
    db: Session = Depends(get_db)
) -> ArticleShow:
    """
    Update an article (full update).
    All fields must be provided.
    """
    return ArticleService.update_article(
        article_id=article_id,
        article_data=article,
        db=db,
        partial=False
    )


@router.patch(
    "/{article_id}",
    response_model=ArticleShow,
    status_code=status.HTTP_200_OK,
    summary="Update an article (partial update)"
)
def patch_article(
    article_id: int,
    article: ArticleUpdate,
    db: Session = Depends(get_db)
) -> ArticleShow:
    """
    Update an article (partial update).
    Only provided fields will be updated.
    """
    return ArticleService.update_article(
        article_id=article_id,
        article_data=article,
        db=db,
        partial=True
    )


@router.delete(
    "/{article_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete an article",
    response_description="Article succesfully deleted"
)
def delete_article(article_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    """Delete a article by its ID."""
    try:
        ArticleService.delete_article(article_id, db)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error deleting article: {str(e)}"
        )
