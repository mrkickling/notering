from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/notes")
def create_notes(q = None):
    return {"q": q}

@app.get("/notes")
def get_notes():
    """ Return all notes """
    return {"halloj": "hej"}

@app.get("/notes/{note_id}")
def get_notes(note_id = None, q = None):
    """ Return note with id, use optional query """
    return {"note_id": note_id, "q": q}

@app.put("/notes/{note_id}")
def edit_note(note_id, q = None):
    return {"note_id": note_id, "q": q}


