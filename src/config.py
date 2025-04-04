from pydantic import BaseModel, RedisDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class ServerConfig(BaseModel):
    host: str
    port: int
    debug: bool


class RedisConfig(BaseModel):
    user: str
    password: str
    host: str
    port: int
    url: RedisDsn


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="APP_CONFIG__",
    )

    server: ServerConfig
    redis: RedisConfig


settings = Settings()
