from pydantic import BaseSettings

class Settings(BaseSettings):
    server_hort: str = '127.0.0.1'
    server_port: int = 8000
    database_url = "sqlite:///./database.sqlite3"
    jwt_secret : str
    jwt_algoritm: str = 'HS256'
    jwt_expire: int = 3600


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8',
)
