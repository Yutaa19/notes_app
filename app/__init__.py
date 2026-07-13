from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.db.database import engine, Base, db_connection
from app.modules.auth.auth_controller import router as auth_router
from app.modules.user.user_controller import router as user_router
from app.modules.user.users_model import User
from app.modules.note.notes_model import Note
from app.modules.like.likes_model import Likes

@asynccontextmanager
async def lifespan(app: FastAPI):
    db_connection()
    Base.metadata.create_all(bind=engine)
    
    yield
    
    engine.dispose()
    
    
def create_app() -> FastAPI:
    
    app = FastAPI(
        title="Notes App",
        description="Backend berbasis Fastapi dengan desain pattern MVC",
        version="1.0.0",
        lifespan=lifespan
    )

    app.include_router(auth_router)
    app.include_router(user_router)
    
    return app