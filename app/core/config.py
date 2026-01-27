from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "mysql+pymysql://user:password@localhost:3306/industrial_maintenance"

    class Config:
        env_file = ".env"

settings = Settings()
print(settings.DATABASE_URL)