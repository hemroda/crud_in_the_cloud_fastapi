from sqlalchemy.orm import Session

from schemas.article import ArticleCreate, ArticleShow
from models.article import Article

def db_get_articles(db: Session, skip: int = 0, limit: int = 10):
    """Retrieve all articles"""
    articles = db.query(Article).offset(skip).limit(limit).all()
    return articles

def db_get_article_by_id(article_id: int, db: Session) -> Article:
    """Retrieve a single article by its ID."""
    article = db.query(Article).filter(Article.id == article_id).first()
    return article

def db_create_article(article_data: ArticleCreate,db: Session, author_id) -> Article:
    """Create a new article"""
    db_article = Article(
        title=article_data.title,
        slug=article_data.slug,
        content=article_data.content,
        author_id=author_id,
        published=False
    )
    try:
        db.add(db_article)
        db.commit()
        db.refresh(db_article)
        return db_article
    except Exception as e:
        db.rollback()
        raise Exception(f"Failed to create article: {str(e)}")

def db_update_article(article_id: int, article_data: dict, db: Session) -> Article:
    db_article = db_get_article_by_id(article_id, db)
    if db_article:
        for key, value in article_data.items():
            if value is not None:  # Only update fields that are provided
                setattr(db_article, key, value)
        db.commit()
        db.refresh(db_article)
    return db_article

def db_delete_article(article_id: int, db: Session) -> bool:
    """Delete a book"""
    article = db_get_article_by_id(article_id, db)
    if article:
        db.delete(article)
        db.commit()
        return True
    return False
