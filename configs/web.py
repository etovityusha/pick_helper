import enum
from typing import Any

from pydantic import BaseSettings, root_validator


class DataStorage(enum.Enum):
    POSTGRES = "POSTGRES"


class WebConfig(BaseSettings):
    SECRET_KEY: str
    LOGGER_LEVEL: str
    LISTEN_HOST: str
    LISTEN_PORT: str
    DATA_STORAGE: DataStorage

    POSTGRES_HOST: str | None
    POSTGRES_PORT: int | None
    POSTGRES_USER: str | None
    POSTGRES_PASSWORD: str | None
    POSTGRES_DATABASE: str | None

    class Config:
        env_prefix = "WEB_"
        env_file = ".env"

    @root_validator
    def validate_storage_fields(cls: "WebConfig", values: dict[str, Any]) -> Any:
        if values.get("DATA_STORAGE") == DataStorage.POSTGRES:
            for field in ("POSTGRES_HOST", "POSTGRES_PORT", "POSTGRES_USER", "POSTGRES_DATABASE"):
                if values.get(field) is None:
                    msg = f"Value {field} cannot be None when DATA_STORAGE is POSTGRES"
                    raise ValueError(msg)
        return values
