from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
)

from app.config.settings import settings
from app.infrastructure.telegram.handlers import TelegramHandlers


class TelegramBot:

    def __init__(self, handlers: TelegramHandlers):
        self.handlers = handlers

        self.application = (
            Application
            .builder()
            .token(settings.telegram_bot_token)
            .build()
        )

        self._register_handlers()

    def _register_handlers(self):
        self.application.add_handler(
            CommandHandler(
                "start",
                self.handlers.start
            )
        )

        self.application.add_handler(
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                self.handlers.handle_message
            )
        )

    def run(self):
        print("SmartBuyer Telegram Bot iniciado...")

        self.application.run_polling()