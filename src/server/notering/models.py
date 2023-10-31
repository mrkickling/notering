from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, Table
from sqlalchemy.orm import relationship

from .database import Base

note_categories = Table('note_categories', Base.metadata,
    Column('note_id', ForeignKey('notes.id'), primary_key=True),
    Column('category_id', ForeignKey('categories.id'), primary_key=True)
)

class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(Text)
    folder_id = Column(Integer, ForeignKey("folders.id"))

    categories = relationship("Category", secondary="note_categories", back_populates="notes")
    folder = relationship("Folder", back_populates="notes")


class Folder(Base):
    __tablename__ = "folders"

    id = Column(Integer, primary_key=True, index=True)
    folder_parent_id = Column(Integer, ForeignKey("folders.id"))
    title = Column(String, index=True)
    description = Column(String, index=True)

    parent = relationship("Folder")
    notes = relationship("Note", back_populates="folder")
    

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    notes = relationship("Note", secondary="note_categories", back_populates="categories")
