from app.config.config import Settings
from app.config.logger import get_logger
from sqlalchemy import create_engine, URL
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import sessionmaker, declarative_base

settings = Settings()
logger = get_logger(__name__)


DATABASE_URL = URL.create(
    "postgresql+psycopg2", 
    username=settings.POSTGRES_USER,
    password=settings.POSTGRES_PASSWORD,
    host=settings.POSTGRES_HOST,
    port=settings.POSTGRES_PORT,
    database=settings.POSTGRES_DB
)

# Engine: mesin utama SQLAlchemy
engine = create_engine(DATABASE_URL, echo=True)

# SessionLocal: "Pabrik" pembuat sesi koneksi untuk tiap request
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
def db_connection():
    try:
        with engine.connect() as connection:
            logger.info("Database succesfully connection")
    except OperationalError as e:
        logger.error(f"Database failed connected {e}")