from fastapi import APIRouter, Form, Depends, HTTPException
from fastapi.responses import RedirectResponse

import utils.utils
from database.database import SessionLocal, engine
from database import crud
from models import models, schemas
from sqlalchemy.orm import Session
from utils import utils
import hashlib
import base64

models.Base.metadata.create_all(bind=engine)

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get('/short/create')
def create_short_url(url: str = Form(), db: Session = Depends(get_db)):
    new_hash = utils.create_random_string(10)
    new_url = schemas.Url(hash_url=new_hash, original_url=url)
    return crud.create_url(db, new_url)


@router.get('/{hash_id}', response_class=RedirectResponse)
def redirect_to_hash(hash_id: str, db: Session = Depends(get_db)):
    url = crud.get_url(db, hash_id)
    if url:
        return url.original_url
    raise HTTPException(404, 'Short link not found')
