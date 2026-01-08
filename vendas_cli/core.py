import sys
import csv

from collections import defaultdict
from datetime import date
from typing import Dict, Iterable, List

from vendas_cli.errors import VendasError
from vendas_cli.parser import parse_csv
from vendas_cli.models import Venda
from vendas_cli.config import logger


def filtra_por_data(
    vendas: Iterable[Venda],
    inicio: date | None,
    fim: date | None,
) -> List[Venda]:
    return [
        s for s in vendas
        if (not inicio or s.data >= inicio)
        and (not fim or s.data <= fim)
    ]


def valor_total_de_vendas(vendas: Iterable[Venda]) -> float:
    return sum(v.total for v in vendas)


def vendas_por_produtos(vendas: Iterable[Venda]) -> Dict[str, float]:
    result: Dict[str, float] = defaultdict(float)
    for venda in vendas:
        result[venda.produto] += venda.total
    return dict(result)


def produto_mais_vendido(vendas: Iterable[Venda]) -> list[str]:
    quantidade = defaultdict(int)

    for v in vendas:
        quantidade[v.produto] += v.quantidade

    if not quantidade:
        return []

    max_qtd = max(quantidade.values())
    return [p for p, q in quantidade.items() if q == max_qtd]


def carrega_arquivo(args):
    try:
        vendas = parse_csv(args.file)
        logger.info("Arquivo carregado com sucesso: %s", args.file)
        logger.info("Total de registros lidos: %d", len(vendas))

    except VendasError as exc:
        logger.error(exc)
        sys.exit(1)

    except Exception:
        logger.exception("Falha ao carregar o arquivo de vendas")
        sys.exit(2)

    return vendas