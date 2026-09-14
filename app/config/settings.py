import os

from dotenv import load_dotenv


load_dotenv()


class Settings:

    def __init__(self):
        self.telegram_bot_token = os.getenv(
            "TELEGRAM_BOT_TOKEN"
        )

        self.openai_api_key = os.getenv(
            "OPENAI_API_KEY"
        )

        self.openai_model = os.getenv(
            "OPENAI_MODEL",
            "gpt-5.6-luna"
        )

        if not self.telegram_bot_token:
            raise ValueError(
                "TELEGRAM_BOT_TOKEN no está configurado."
            )

        if not self.openai_api_key:
            raise ValueError(
                "OPENAI_API_KEY no está configurado."
            )


settings = Settings()