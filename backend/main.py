from fastapi import FastAPI, Depends
from database import Base, engine, get_db
from sqlalchemy.orm import Session

from web import book
from web import creature
from web import explorer
from web import task

app = FastAPI()

# Create the tables on startup
@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

@app.get("/")
async def root(db: Session = Depends(get_db)):
    return {"message": "Vroum vroum API"}

app.include_router(book.router)
app.include_router(creature.router)
app.include_router(explorer.router)
app.include_router(task.router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)
