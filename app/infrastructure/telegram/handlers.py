from telegram import Update
from telegram.ext import ContextTypes

from app.application.use_cases import ProcessMessageUseCase


class TelegramHandlers:

    def __init__(
        self,
        process_message_use_case: ProcessMessageUseCase
    ):
        self.process_message_use_case = process_message_use_case

    async def start(
        self,
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
    ):
        if update.message is None:
            return

        await update.message.reply_text(
            "Hola 👋 Soy SmartBuyer.\n"
            "Envíame un mensaje para comenzar."
        )

    async def handle_message(
        self,
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
    ):
        if update.message is None:
            return

        message = update.message.text

        response = self.process_message_use_case.execute(
            message
        )

        await update.message.reply_text(response)