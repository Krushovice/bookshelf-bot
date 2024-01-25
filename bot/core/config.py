from pydantic_settings import SettingsConfigDict, BaseSettings


class Settings(BaseSettings):
    DB_URL: str
    BOT_TOKEN: str
    OPENAI_KEY: str
    DEBUG: bool
    API_KEY: str
    PROXY_URL: str
    ECHO: bool = False

    @property
    def db_url(self) -> str:
        if self.DEBUG:
            return "sqlite+aiosqlite:///./db.sqlite3"
        else:
            return f"{self.DB_URL}"

    @property
    def bot_token(self) -> str:
        return f"{self.BOT_TOKEN}"

    @property
    def api_token(self) -> str:
        return f"{self.OPENAI_KEY}"

    @property
    def proxy_url(self) -> str:
        return f"{self.PROXY_URL}"

    @property
    def api_key(self) -> str:
        return f"{self.API_KEY}"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
