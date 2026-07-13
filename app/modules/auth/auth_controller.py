from app.config.config import RegisterUser, LoginUser
from app.modules.auth.auth_service import register_user, login_user
from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.db.database import get_db

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(user_in: RegisterUser, db: Session = Depends(get_db)):

    new_user = register_user(db=db, user_data=user_in)
    return {
        "message": "user berhasil terdaftar",
        "username": new_user.username,
        "email": new_user.email
    }


@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):

    user_data = LoginUser(
        username=form_data.username,
        password=form_data.password
    )

    user_login = login_user(db=db, user_data=user_data)
    return user_login
    