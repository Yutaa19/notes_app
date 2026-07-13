from app.modules.user.user_service import get_user_by_id, update_user
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.config.config import UpdateUser
from app.db.database import get_db

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/")
def get_user(user_id, db: Session = Depends(get_db)):
    
    user = get_user_by_id(db, user_id)

    if not user:
        return None, "user tidak di temukan"
    
    return user

@router.put("/")
def update(user_id, update: UpdateUser, db: Session = Depends(get_db)):

    user_update = update_user(user_id, db, update.data, update.profile_img, update.thumbnail)

    if not user_update:
        return None, "update tidak terbarui"

    return user_update