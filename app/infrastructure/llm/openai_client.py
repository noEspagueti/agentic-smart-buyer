from openai import AsyncOpenAI

from app.agent.prompts import SHOPPING_INTENT_PROMPT
from app.application.ports import LLMPort
from app.domain.models import ShoppingIntent


class OpenAILLMClient(LLMPort):

    def __init__(
        self,
        api_key: str,
        model: str
    ):
        self.client = AsyncOpenAI(
            api_key=api_key
        )

        self.model = model

    async def extract_shopping_intent(
        self,
        message: str
    ) -> ShoppingIntent:

        schema = ShoppingIntent.model_json_schema()

        response = await self.client.responses.create(
            model=self.model,
            instructions=SHOPPING_INTENT_PROMPT,
            input=message,
            text={
                "format": {
                    "type": "json_schema",
                    "name": "shopping_intent",
                    "strict": True,
                    "schema": schema
                }
            }
        )

        return ShoppingIntent.model_validate_json(
            response.output_text
        )