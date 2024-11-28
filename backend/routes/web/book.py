from fastapi import APIRouter, Depends, Form, HTTPException, Request, responses, status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.security.utils import get_authorization_scheme_param
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse
from typing import Optional

from core.database import get_db
from models.user import User
from routes.login import get_current_user
from service.book import BookService
from schemas.book import BookCreate, BookUpdate

templates = Jinja2Templates(directory="templates")

router = APIRouter(prefix="/books", tags=["Website - Books"], )


@router.get("/", response_class=HTMLResponse)
async def books(
    request: Request,
    db: Session = Depends(get_db),
    limit: int = 10,
    skip: int = 0,
):
    try:
        token = request.cookies.get("access_token")
        _, token = get_authorization_scheme_param(token)
        current_user = get_current_user(token=token, db=db)
    except HTTPException as http_exc:
        if http_exc.status_code == status.HTTP_401_UNAUTHORIZED:
            return responses.RedirectResponse("/login")

    try:
        books = BookService.get_books(db, skip, limit)

        return templates.TemplateResponse(
            request=request,
            name="website/books/index.html",
            context={"books": books, "current_user": current_user}
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error creating task: {str(e)}"
        )


@router.get("/new", response_class=HTMLResponse)
async def new_book(
    request: Request,
    db: Session = Depends(get_db),
):
    try:
        token = request.cookies.get("access_token")
        _, token = get_authorization_scheme_param(token)
        current_user = get_current_user(token=token, db=db)
    except HTTPException as http_exc:
        if http_exc.status_code == status.HTTP_401_UNAUTHORIZED:
            return responses.RedirectResponse("/login")

    return templates.TemplateResponse(
        request=request,
        name="website/books/new.html",
        context={"current_user": current_user}
    )


@router.post("/new", response_class=HTMLResponse)
async def create_book(
    request: Request,
    db: Session = Depends(get_db),
    description: Optional[str] = Form(None),
    published_year: int = Form(...),
    title: str = Form(...),
):
    try:
        book_data = BookCreate(title=title, description=description,
                               published_year=published_year)
        create_book = BookService.create_book(book_data, db=db)

        return templates.TemplateResponse(
            request=request,
            name="website/books/show.html",
            context={"book": create_book}
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error creating the book: {str(e)}"
        )


@router.get("/{book_id}", response_class=HTMLResponse)
async def get_book_by_id(
    request: Request,
    book_id: int,
    db: Session = Depends(get_db)
) -> HTMLResponse:
    try:
        token = request.cookies.get("access_token")
        _, token = get_authorization_scheme_param(token)
        current_user = get_current_user(token=token, db=db)
    except HTTPException as http_exc:
        if http_exc.status_code == status.HTTP_401_UNAUTHORIZED:
            return responses.RedirectResponse("/login")

    try:
        book = BookService.get_book_by_id(book_id=book_id, db=db)

        return templates.TemplateResponse(
            request=request,
            name="website/books/show.html",
            context={"book": book, "current_user": current_user}
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving the book: {str(e)}"
        )


@router.get("/{book_id}/edit", response_class=HTMLResponse)
async def edit_book(
    request: Request,
    book_id: int,
    db: Session = Depends(get_db)
):
    try:
        token = request.cookies.get("access_token")
        _, token = get_authorization_scheme_param(token)
        current_user = get_current_user(token=token, db=db)
    except HTTPException as http_exc:
        if http_exc.status_code == status.HTTP_401_UNAUTHORIZED:
            return responses.RedirectResponse("/login")

    book = BookService.get_book_by_id(book_id=book_id, db=db)

    return templates.TemplateResponse(
        request=request,
        name="website/books/edit.html",
        context={
            "title": book.title,
            "description": book.description,
            "published_year": book.published_year,
            "current_user": current_user
        }
    )


@router.post("/{book_id}/edit", response_class=HTMLResponse)
async def patch_book(
    request: Request,
    book_id: int,
    db: Session = Depends(get_db),
    description: Optional[str] = Form(None),
    published_year: int = Form(...),
    title: str = Form(...),
) -> RedirectResponse:
    try:
        book_data = BookUpdate(title=title, description=description,
                               published_year=published_year)
        updated_book = BookService.update_book(
            book_data=book_data,
            book_id=book_id,
            db=db,
            partial=True
        )

        return RedirectResponse(
            url=f"/books/{book_id}",
            status_code=status.HTTP_303_SEE_OTHER
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error updating the book: {str(e)}"
        )


@router.post("/{book_id}/delete", response_class=HTMLResponse)
def delete_book(
    book_id: int,
    db: Session = Depends(get_db),
):
    """Delete a book by its ID."""
    try:
        BookService.delete_book(book_id, db)

        return RedirectResponse(
            url="/books",
            status_code=status.HTTP_303_SEE_OTHER
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error deleting book: {str(e)}"
        )
