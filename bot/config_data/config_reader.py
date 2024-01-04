from pydantic_settings import SettingsConfigDict, BaseSettings


class Settings(BaseSettings):
    DB_URL: str
    BOT_TOKEN: str

    @property
    def database_url(self) -> str:
        return f"{self.DB_URL}"

    @property
    def bot_token(self) -> str:
        return f"{self.BOT_TOKEN}"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
