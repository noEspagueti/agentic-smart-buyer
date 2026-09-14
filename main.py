from app.application.use_cases import ProcessMessageUseCase
from app.infrastructure.telegram.bot import TelegramBot
from app.infrastructure.telegram.handlers import TelegramHandlers


def main():

    process_message_use_case = ProcessMessageUseCase()

    telegram_handlers = TelegramHandlers(
        process_message_use_case=process_message_use_case
    )

    telegram_bot = TelegramBot(
        handlers=telegram_handlers
    )

    telegram_bot.run()


if __name__ == "__main__":
    main()