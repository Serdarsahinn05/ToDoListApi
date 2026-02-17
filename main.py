from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional
from sqlalchemy.orm import Session
import models
import database

# 1. Tabloları Oluştur (Program başlarken çalışır)
# Eğer todos.db yoksa oluşturur, varsa dokunmaz.
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()


# --- BAĞIMLILIK (DEPENDENCY) ---
# Veritabanı oturumunu açar, iş bitince kapatır.
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


# --- PYDANTIC MODELLERİ (Schema) ---
# API ile konuşurken kullandığımız veri tipleri (Validation için)
class TodoCreate(BaseModel):
    title: str
    completed: bool = False


class TodoResponse(BaseModel):
    id: int
    title: str
    completed: bool

    # Bu ayar, Pydantic'in ORM nesnelerini (SQLAlchemy) okumasını sağlar
    class Config:
        from_attributes = True


# --- ENDPOINTLER ---

# 1. EKLEME (CREATE)
@app.post("/todos", response_model=TodoResponse)
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    # SQL Modeline dönüştür
    db_todo = models.TodoDB(title=todo.title, completed=todo.completed)

    db.add(db_todo)  # Ekle
    db.commit()  # Kaydet (Enter tuşuna basmak gibi)
    db.refresh(db_todo)  # ID'si oluşmuş veriyi geri al
    return db_todo


# 2. LİSTELEME (READ)
@app.get("/todos", response_model=List[TodoResponse])
def read_todos(db: Session = Depends(get_db)):
    # "SELECT * FROM todos" komutunun Pythoncası:
    todos = db.query(models.TodoDB).all()
    return todos


# 3. SİLME (DELETE)
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    # Önce silinecek kaydı bul
    todo = db.query(models.TodoDB).filter(models.TodoDB.id == todo_id).first()

    if todo is None:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(todo)
    db.commit()  # Değişikliği onayla
    return {"message": "Task deleted successfully"}