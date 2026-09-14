from app.agent.agent import ShoppingAgent
from app.application.use_cases import ProcessMessageUseCase
from app.config.settings import settings
from app.infrastructure.llm.openai_client import (
    OpenAILLMClient
)
from app.infrastructure.telegram.bot import TelegramBot
from app.infrastructure.telegram.handlers import (
    TelegramHandlers
)


def main():

    llm_client = OpenAILLMClient(
        api_key=settings.openai_api_key,
        model=settings.openai_model
    )

    shopping_agent = ShoppingAgent(
        llm=llm_client
    )

    process_message_use_case = ProcessMessageUseCase(
        shopping_agent=shopping_agent
    )

    telegram_handlers = TelegramHandlers(
        process_message_use_case=process_message_use_case
    )

    telegram_bot = TelegramBot(
        handlers=telegram_handlers
    )

    telegram_bot.run()


if __name__ == "__main__":
    main()