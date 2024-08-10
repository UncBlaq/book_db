from book.database import db_dependency
from book.models import Book, User
from book.schemas import BookCreate, UserCreate
from book.hash import pwd_context

from book.logger import get_logger

logger = get_logger(__name__)





def create_user(db: db_dependency, payload : UserCreate):
    hashed_password = pwd_context.hash(payload.password)
   
    db_user = User(
        username = payload.username,
          full_name = payload.full_name, 
          password = hashed_password
          )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_username(db : db_dependency, username : str):
    return db.query(User).filter(User.username == username).first()


def get_book_by_id(db : db_dependency, id : int):
    
    logger.info('Querying Book model')

    return db.query(Book).filter(Book.id == id).first()

def get_book_by_author(db : db_dependency, author: str):
    return db.query(Book).filter(Book.author == author).first()

def get_all_books(
        db : db_dependency, 
        user_id : int = None, offset : int = 0, limit : int = 3):
    return db.query(Book).filter(Book.id == user_id).offset(offset).limit(limit).all()

def create_book(db : db_dependency, book: BookCreate, user_id: int = None):
    db_book = Book(**book.dict(), user_id = user_id)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def update_book():
    pass
   