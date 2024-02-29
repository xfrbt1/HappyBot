from functools import lru_cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    token: str = "6423073194:AAEcldYxenzKdN3Al7sV0iU1jPa52AWY6j4"
    admin_id: str | None = "6288131392 501796953"
    users_db: str | None = "users"
    info_db: str | None = "static"
    diagram: str = "diagram.png"


@lru_cache
def get_settings() -> Settings:
    return Settings()
