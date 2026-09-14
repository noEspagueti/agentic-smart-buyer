from typing import Literal

from pydantic import BaseModel, ConfigDict


class ShoppingIntent(BaseModel):

    model_config = ConfigDict(
        extra="forbid"
    )

    intent: Literal[
        "SEARCH_PRODUCT",
        "UNKNOWN"
    ]

    product: str | None

    brand: str | None

    budget: float | None

    currency: Literal[
        "PEN",
        "USD",
        "UNKNOWN"
    ]