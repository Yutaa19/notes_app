from app.config import Settings
from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError

settings = Settings()

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

if __name__ == "__main__":
    try:
        with engine.connect() as conn:
            print("✅ Sukses: FastAPI configuration berhasil koneksi ke Database!")
    except OperationalError as e:
        print(f"❌ Gagal koneksi: {e}")