from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="Book API")


class BookCreate(BaseModel):
    title: str
    author: str
    publication_year: int


class Book(BookCreate):
    id: int


books: dict[int, Book] = {}
next_book_id = 1


@app.get("/")
def read_root():
    return {"message": "Welcome to the Book API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


# TODO: Add the book endpoints described in README.md.


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)