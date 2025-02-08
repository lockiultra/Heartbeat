from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    TEST_DATABASE_URL: str
    ALGORITHM: str
    SECRET_KEY: str

    class Config:
        env_file = '.env'


settings = Settings()
