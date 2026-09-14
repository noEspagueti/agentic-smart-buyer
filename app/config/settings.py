import os

from dotenv import load_dotenv

load_dotenv()

class Settings:
    def __init__(self):
        self.telegram_bot_token = os.getenv("TELEGRAM_BOT_TOKEN")

        if not self.telegram_bot_token:
            raise ValueError(
                "TELEGRAM_BOT_TOKEN no está configurado."
            )


settings = Settings()