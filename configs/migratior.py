from pydantic import BaseSettings


class MigratorConfig(BaseSettings):
    SQLALCHEMY_DATABASE_URI: str

    class Config:
        env_prefix = "MIGRATOR_"
        env_file = ".env"
