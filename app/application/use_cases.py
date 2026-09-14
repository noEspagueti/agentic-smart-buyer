from app.agent.agent import ShoppingAgent


class ProcessMessageUseCase:

    def __init__(
        self,
        shopping_agent: ShoppingAgent
    ):
        self.shopping_agent = shopping_agent

    async def execute(
        self,
        message: str
    ) -> str:

        return await self.shopping_agent.process(
            message
        )