from typing import List, Optional
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from schemas.article import ArticleCreate, ArticleShow, ArticleUpdate
import data.article as data

class ArticleService:

    @staticmethod
    def create_article(article: ArticleCreate, db: Session, author_id) -> ArticleShow:
        try:
            return data.db_create_article(article, db, author_id)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Failed to create article: {str(e)}"
            )


    @staticmethod
    def get_article_by_id(article_id: int, db: Session) -> ArticleShow:
        article = data.db_get_article_by_id(article_id, db)

        if not article:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Article with id {article_id} not found"
            )

        return article


    @staticmethod
    def get_articles(db: Session, skip: int = 0, limit: int = 10) -> List[ArticleShow]:

        return data.db_get_articles(db, skip, limit)


    @staticmethod
    def update_article(
        article_id: int,
        article_data: ArticleUpdate,
        db: Session,
        partial: bool = False,
        author_id: int = None
    ) -> ArticleShow:
        existing_article = data.db_get_article_by_id(article_id, db)

        if not existing_article:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Article with ID {article_id} not found"
            )

        if not existing_article.author_id == author_id:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=f"Only the owner of the article with ID {article_id} can update it."
            )

        # Convert article_data to dict, excluding None values if partial update
        update_data = article_data.model_dump(
            exclude_unset=partial,  # True for PATCH, False for PUT
            exclude_none=partial
        )

        try:
            updated_article = data.db_update_article(article_id, update_data, db, author_id)
            return updated_article
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Failed to update article: {str(e)}"
            )


    @staticmethod
    def delete_article(article_id: int, db: Session, author_id: int) -> bool:
        existing_article = data.db_get_article_by_id(article_id, db)

        if not existing_article:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Article with ID {article_id} not found"
            )

        if not existing_article.author_id == author_id:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=f"Only the owner of the article with ID {article_id} can delete it."
            )

        if not data.db_delete_article(article_id, db):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Article with id {article_id} not found"
            )

        return True
