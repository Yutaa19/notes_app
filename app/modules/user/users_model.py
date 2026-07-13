import uuid
import jwt
from datetime import datetime, timezone, timedelta
from app.db.database import Base
from app.config.config import JwtToken
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String,  DateTime
from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()
tokenjwt = JwtToken()

class User(Base):
    # name table
    __tablename__ = "users"
    
    id :Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    username : Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    email : Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    password : Mapped[str] = mapped_column(String(255), nullable=False)
    profile_img : Mapped[str] = mapped_column(String(255), nullable=True)
    thumbnail : Mapped[str] = mapped_column(String(255), nullable=True)
    created_at : Mapped[datetime] = mapped_column(
        DateTime,
        default=lambda: datetime.now(timezone.utc)
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc)
    )

    notes: Mapped[list["Note"]] = relationship(back_populates="users")
    likes: Mapped[list["Likes"]] = relationship(back_populates="user")


    def get_password_hash(self, password):
        self.password = password_hash.hash(password)

    def verify_password(self, input_password):
        return password_hash.verify(input_password, self.password)

    def create_access_token(data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(hours=tokenjwt.ACCESS_TOKEN_EXPIRE_HOURS)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, tokenjwt.SECRECT_KEY, algorithm=tokenjwt.ALGORITHM)
        return encoded_jwt

    def to_json(self):
        data = {
            "user": {
                "username": self.username,
                "email": self.email,
                "profile_img": self.profile_img,
                "thumbnail_img": self.thumbnail,
                 "created_at": self.created_at
            },
            "messages": {
                "status": 200,
                "detail": "data user berhasil"
            }
        }
        
        return data