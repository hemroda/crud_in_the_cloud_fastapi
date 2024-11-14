from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware
from sqlalchemy.sql import text

from contextlib import asynccontextmanager

from core.config import settings
from web import website # book, task, user,


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

# Initialize the FastAPI app
app = FastAPI(lifespan=lifespan, title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOW_ORIGINS_LIST.split(" "),
    allow_methods=["GET", "POST"],
)

# Include routers for different modules
# app.include_router(book.router)
# app.include_router(task.router)
# app.include_router(user.router)
app.include_router(website.router)

# System
@app.get("/health")
async def health_check():
    health_status = {
        "status": "healthy",
        "checks": {
            "database": "healthy",
            "api": "healthy"
        }
    }

    try:
        engine = create_engine(settings.DATABASE_URL)
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
    except Exception as e:
        health_status["checks"]["database"] = "unhealthy"
        health_status["status"] = "unhealthy"

    return JSONResponse(
        status_code=200 if health_status["status"] == "healthy" else 500,
        content=health_status
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)
