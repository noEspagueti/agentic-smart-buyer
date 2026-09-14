from app.application.ports import LLMPort


class ShoppingAgent:

    def __init__(
        self,
        llm: LLMPort
    ):
        self.llm = llm

    async def process(
        self,
        message: str
    ) -> str:

        intent = await self.llm.extract_shopping_intent(
            message
        )

        print(
            "[ShoppingAgent] intent:",
            intent.model_dump()
        )

        if intent.intent == "UNKNOWN":
            return (
                "Por ahora puedo ayudarte con búsquedas "
                "y decisiones de compra."
            )

        if not intent.product:
            return (
                "¿Qué producto quieres comprar?"
            )

        product_description = intent.product

        if intent.brand:
            product_description += (
                f" de {intent.brand}"
            )

        if intent.budget is None:
            return (
                f"Entendido. Buscas "
                f"{product_description}. "
                f"¿Cuál es tu presupuesto máximo?"
            )

        if intent.currency == "UNKNOWN":
            return (
                f"Entendido. Tu presupuesto es "
                f"{intent.budget:.2f}. "
                f"¿Ese monto está en soles o dólares?"
            )

        currency_symbol = (
            "S/"
            if intent.currency == "PEN"
            else "$"
        )

        return (
            f"Entendido. Buscas {product_description} "
            f"con un presupuesto máximo de "
            f"{currency_symbol}{intent.budget:.2f}."
        )