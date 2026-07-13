from app.modules.user.users_model import User
from app.config.config import RegisterUser, LoginUser
from sqlalchemy.orm import Session
from sqlalchemy import select, or_
from fastapi import HTTPException, status

def register_user(db:Session, user_data: RegisterUser):

    query = select(User).where(or_(
        User.username == user_data.username,
        User.email == user_data.email
    ))

    existing_user = db.execute(query).scalar_one_or_none()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,detail="User sudah terdaftar"
        )

    new_user = User(
        username=user_data.username,
        email= user_data.email,

    )
    new_user.get_password_hash(user_data.password)

    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail=f"gagal melakukan registrasi user {e}"
        )

def login_user(db: Session, user_data: LoginUser):

    query = select(User).where(user_data.username == User.username)
    user = db.execute(query).scalar_one_or_none()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail= "user belum terdaftar"
        )

    if not user.verify_password(user_data.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail= "password yang anda masukan salah"
        )

    token = User.create_access_token({"sub": user.id})
    user_login = {
            "message": "login sukses",
            "user":{"username": user.username,
                "email": user.email,
                "profile_img": user.profile_img,
                "thumbnail_img": user.thumbnail,
                "created_at": user.created_at,
                },
            "status": status.HTTP_202_ACCEPTED,   
            "token": token,
            "token_type": "bearer"
            },

    return user_login