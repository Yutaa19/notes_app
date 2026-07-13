from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
ENV_PATH = BASE_DIR / ".env"

class Settings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str 
    POSTGRES_PORT: int          

    model_config = SettingsConfigDict(
        env_file= ENV_PATH,
        extra="ignore"
    )  


class JwtToken(BaseSettings):
    SECRECT_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_HOURS: int

    model_config = SettingsConfigDict(
        env_file= ENV_PATH,
        extra= "ignore"
    )

class RegisterUser(BaseModel):
    username: str
    email: str
    password: str

class LoginUser(BaseModel):
    username: str
    password: str

class UpdateUser(BaseModel):
    data: dict
    profile_img: str
    thumbnail: str