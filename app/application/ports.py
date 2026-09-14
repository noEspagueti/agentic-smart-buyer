from abc import ABC, abstractmethod

from app.domain.models import ShoppingIntent


class LLMPort(ABC):

    @abstractmethod
    async def extract_shopping_intent(
        self,
        message: str
    ) -> ShoppingIntent:
        pass