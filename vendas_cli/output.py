import json
from typing import Dict


def renderizar_texto(
    total: float,
    vendas_por_produtos: Dict[str, float],
    melhor_produto: str | None,
) -> str:
    lines = [
        "RELATÓRIO DE VENDAS",
        "-" * 30,
        f"Total geral: R$ {total:.2f}",
        "",
        "Total por produto:",
    ]

    for product, value in vendas_por_produtos.items():
        lines.append(f"- {product}: R$ {value:.2f}")

    lines.append("")
    lines.append(f"Produto mais vendido: {melhor_produto}")

    return "\n".join(lines)


def renderizar_json(
    total: float,
    vendas_por_produtos: Dict[str, float],
    melhor_produto: str | None,
) -> str:
    return json.dumps(
        {
            "total_vendas": total,
            "vendas_por_produtos": vendas_por_produtos,
            "produto_mais_vendido": melhor_produto,
        },
        indent=2,
        ensure_ascii=False,
    )
