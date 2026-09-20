from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    scraper_concurrency: int = 10
    scraper_delay_min: float = 1.0
    scraper_delay_max: float = 3.0
    proxy_list: Optional[str] = None
    headless: bool = True
    database_url: str = 'postgresql://user:pass@localhost:5432/scraper'
    redis_url: str = 'redis://localhost:6379/0'
    cdp_endpoint: str = 'http://localhost:9222'
    log_level: str = 'INFO'

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        extra = 'ignore'


settings = Settings()