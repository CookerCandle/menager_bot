from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr
from typing import List


class Config(BaseSettings):
    bot_token: SecretStr # Bot token for authentication
    admins: List[int] = []  # List of admin user IDs
    group_id: int = 0  # Group ID for the bot to operate in
    chat_id: int = 0

    model_config = SettingsConfigDict(
        env_file=".env",  # Load environment variables from .env file
        env_file_encoding="utf-8",  # Encoding for the .env file
    )

config = Config()  # Create an instance of the Config class to access settings
