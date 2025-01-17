from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware
from sqlalchemy.sql import text

from contextlib import asynccontextmanager

from core.config import settings
from routes import login, utils
from routes.api import article as api_article, task as api_task, user as api_user
from routes.web import article as web_article, dashboard, task as web_task, website


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


# Initialize the FastAPI app
app = FastAPI(lifespan=lifespan, title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)

origins = settings.ALLOW_ORIGINS_LIST.split(" ")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Include routers for different modules
app.include_router(dashboard.router)
app.include_router(login.router)
app.include_router(utils.router)
app.include_router(api_article.router)
app.include_router(api_task.router)
app.include_router(api_user.router)
app.include_router(web_article.router)
app.include_router(web_task.router)
app.include_router(website.router)


# System
@app.get("/health", tags=["System"],)
async def health_check():
    health_status = {
        "status": "healthy",
        "checks": {
            "database": "healthy",
            "api": "healthy"
        }
    }
    # TODO: update this since we switched to SQLAlchemy
    # Currently ruterning
    # {
    #   "status": "unhealthy",
    #   "checks": {
    #     "database": "unhealthy",
    #     "api": "healthy"
    #   }
    # }
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
