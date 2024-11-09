from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from core.config import settings
from core.database import init_db
from web import book, task, user, website


# Create the tables on startup
@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

# Initialize the FastAPI app
app = FastAPI(lifespan=lifespan, title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost"],  # Update with specific origins in production
    allow_methods=["GET", "POST"],
)

# Include routers for different modules
app.include_router(book.router)
app.include_router(task.router)
app.include_router(user.router)
app.include_router(website.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)