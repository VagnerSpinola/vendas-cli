from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class Venda:
    data: date
    produto: str
    quantidade: int
    preco: float

    @property
    def total(self) -> float:
        return self.quantidade * self.preco
