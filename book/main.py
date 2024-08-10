from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer

from book.auth import get_current_user

import book.schemas
from .schemas import Book, BookCreate, UserCreate

import book.models
from book.database import engine, db_dependency
import book.crud
import book.auth
import book.logger as logger
from book.logger import get_logger

logger = get_logger(__name__)

from sentry_sdk.integrations.logging import LoggingIntegration

import logging
# Enable sending logs from the standard Python logging module to Sentry
logging_integration = LoggingIntegration(
    level=logging.INFO,  # Capture info and above as breadcrumbs
    event_level=logging.ERROR  # Send errors as events
)

import sentry_sdk


sentry_sdk.init(
    dsn="https://ee3ca659cdc5658bf02659af610f818b@o4507693153386496.ingest.de.sentry.io/4507693158629456",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
    integrations= [logging_integration]
)

app = FastAPI()

book.models.Base.metadata.create_all(bind=engine)

# @app.get("/sentry-debug")
# async def trigger_error():
#     division_by_zero = 1 / 0


@app.get("/sentry-debug")
async def trigger_error():
    try:
        sentry_sdk.capture_message('about to start function...')
        [1,2,3][1]
    except Exception as e:
        sentry_sdk.capture_exception(e)
        raise e



@app.post("/auth/token") 
def login(db : db_dependency, payload : OAuth2PasswordRequestForm = Depends()):
   
    logger.info("Generating auth token....")
    user = book.auth.authenticate_user(db, payload.username, payload.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    access_token = book.auth.create_access_token(data = {"sub" :user.username})
    logger.info(f"User Logged in successfully and user is {user.username}")
    return {"access_token": access_token, "token_type": "bearer"}



@app.post("/signup")
def signup(payload : UserCreate, db : db_dependency):
    logger.info('Creating user...')
    db_user = book.crud.get_user_by_username(db, username = payload.username)
    
    if db_user:
        logger.warning(f"User with {payload.username} already exists.")
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Username already exists")
    new_user = book.crud.create_user(db, payload)
    logger.info("Created new user")
    return {
        "message": "User created successfully",
        "data": new_user
    }
    

@app.get("/books/")
def get_books(
    db : db_dependency, 
    current_user : book.schemas.User = Depends(get_current_user), 
    offset: int = 0, limit: int = 10
    ):
    logger.info(f'Getting books for {current_user.username} ...')
    books = book.crud.get_all_books(
        db,
        user_id = current_user,
        offset = offset,
        limit = limit
        )
    logger.info(f'Books gotten for {current_user.username} successfully.')
    return {
        "message": "Success",
        "data" : books
    }

@app.post("/books/")
def create_book(db : db_dependency , payload: BookCreate, user : book.schemas.User = Depends(get_current_user)):
    print(user)
    print(type(user))
    new_book = book.crud.create_book(db, payload, user_id = user)
    return {
        "message": "Book created successfully",
        "data": new_book
    }


@app.get("/books/{id}")
def get_book_by_id(id: int, db : db_dependency):
    book_curr = book.crud.get_book_by_id(db, id)
    if book_curr is not None:
         return {
            "message": "Success",
            "data": book_curr
        }
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

@app.put("/books/{id}")
def update_book(db : db_dependency, id : int, payload: BookCreate):
    updated_book = book.crud.update_book(db, id, payload)
    if updated_book is not None:
        return {
            "message": "Book updated successfully",
            "data": updated_book
        }

       
    
   
    
    
