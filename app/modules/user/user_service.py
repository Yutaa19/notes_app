import os, uuid, shutil
from werkzeug.utils import secure_filename
from app.modules.user.users_model import User
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select

def is_valid_image(filename):
    valid_text = [".jpg", ".png", ".jpeg"]

    #split nama file sama ext
    _, ext = os.path.splitext(filename.lower())
    
    return ext in valid_text

def random_name(filename):
    ext = os.path.splitext(filename)[1].lower()

    #random filename
    name = f"{uuid.uuid4()}{ext}"
    return name

def get_user_by_id(db: Session, user_id):
    query = select(User).where(user_id == User.id)
    user = db.execute(query).scalar_one_or_none()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail= "user tidak di temukan"
        )

    return user

def update_user(user_id, db: Session, data: dict, profile_img_file=None, thumbnail_img_file=None):
    query = select(User).where(user_id == User.id)
    user = db.execute(query).scalar_one_or_none()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail= "user tidak di temukan"
        )
    
    try:
        # update password
        if data.get("password"):
            hash_password = User.get_password_hash(data["password"])
            user.password = hash_password
        
        # update username dan email
        for field in ["username", "email"]:
            if data.get(field):
                setattr(user, field, data[field])

        # buat folder uploads
        os.makedirs("uploads", exist_ok=True)

        # update profile img
        
        if profile_img_file and is_valid_image(profile_img_file.filename):
            name = random_name(profile_img_file.filename)
            filename = secure_filename(name)
            path = os.path.join("uploads", filename)

            with open(path, "wb") as buffer:
                shutil.copyfileobj(profile_img_file.filename, buffer)
                

            # mengecek apakah foto sudah exist atau belum
            if user.profile_img:
                filename_old = user.profile_img.replace("/uploads/", "")
                path = os.path.join("uploads", filename_old)

                if os.path.exists(path):
                    os.remove(path)

            user.profile_img = f"/uploads/{filename}"

        if thumbnail_img_file and is_valid_image(thumbnail_img_file.filename):
            name = random_name(thumbnail_img_file.filename)
            filename = secure_filename(name)
            path = os.path.join("uploads", filename)


            with open(path, "wb") as buffer:
                shutil.copyfileobj(profile_img_file.filename, buffer)
        
                    # mengecek apakah foto sudah exist atau belum
            if user.profile_img:
                filename_old = user.thumbnail.replace("/uploads/", "")
                path = os.path.join("uploads", filename_old)
        
                if os.path.exists(path):
                    os.remove(path)
        
            user.thumbnail = f"/uploads/{filename}"
        
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"update user gagal {e}"
        )