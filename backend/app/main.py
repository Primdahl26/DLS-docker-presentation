from fastapi import FastAPI, Depends
from schemas import User
from db.database import get_db, engine
from db.crud import create_user, get_user, get_users
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from db import models
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

models.Base.metadata.create_all(bind=engine)


origins = [
    "http://localhost:3000",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/create_user", response_model=User)
async def post_user(user: User, db: Session = Depends(get_db)):
    """Creates a user to the database"""
    db_user = get_user(db=db, user_id=user.id)
    if db_user:
        raise HTTPException(status_code=400, detail="User already exists")
    return create_user(db=db, user=user)


@app.get("/get_users", response_model=list[User])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_users(db=db, skip=skip, limit=limit)


@app.get("/get_user/{user_id}", response_model=User)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db=db, user_id=user_id)
    if db_user:
        return db_user
    raise HTTPException(status_code=404, detail="User doesn't exist")

