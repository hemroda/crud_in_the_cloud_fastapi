from fastapi import FastAPI, Depends
from database import Base, engine, get_db
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware

from web import book
from web import task
from web import website

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    # Update with specific origins in production
    allow_origins=["localhost"],
    allow_methods=["GET", "POST"],
)

# Create the tables on startup
@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)


app.include_router(book.router)
app.include_router(task.router)
app.include_router(website.router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)
