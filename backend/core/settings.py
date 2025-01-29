from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    TEST_DATABASE_URL: str
    ALGORITHM: str

    class Config:
        env_file = '.env'


settings = Settings()
