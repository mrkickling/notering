from typing import Union
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from . import models
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/notes")
def create_notes(q = None, db = Depends(get_db)):
    db_note = models.Note(title="test", content="test texten" * 1000)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

@app.get("/notes")
def get_notes(db = Depends(get_db)):
    """ Return all notes """ 
    return db.query(models.Note).all()

@app.get("/notes/{note_id}")
def get_notes(note_id = None, q = None):
    """ Return note with id, use optional query """
    return {"note_id": note_id, "q": q}

@app.put("/notes/{note_id}")
def edit_note(note_id, q = None):
    return {"note_id": note_id, "q": q}

