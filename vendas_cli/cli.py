import argparse

import vendas_cli.core
print(vendas_cli.core.__file__)

from datetime import datetime

from vendas_cli.core import (
    carrega_arquivo,
    filtra_por_data,
    vendas_por_produtos,
    valor_total_de_vendas,
    produto_mais_vendido,
)
from vendas_cli.output import renderizar_json, renderizar_texto
from vendas_cli.config import logger

def main(argv: list[str] | None = None) -> None:

    parser = argparse.ArgumentParser(description="Gerador de Relatório de Vendas")
    parser.add_argument("file", help="Arquivo CSV de vendas")
    parser.add_argument("--format", choices=["text", "json"], default="text")
    parser.add_argument("--start", help="Data inicial YYYY-MM-DD")
    parser.add_argument("--end", help="Data final YYYY-MM-DD")

    args = parser.parse_args(argv)

    logger.info(
        "Parâmetros recebidos | arquivo=%s | formato=%s | start=%s | end=%s",
        args.file,
        args.format,
        args.start,
        args.end,
    )

    vendas = carrega_arquivo(args)

    start = datetime.strptime(args.start, "%Y-%m-%d").date() if args.start else None
    end = datetime.strptime(args.end, "%Y-%m-%d").date() if args.end else None

    logger.debug("Aplicando filtro de datas | start=%s | end=%s", start, end)

    vendas = filtra_por_data(vendas, start, end)
    logger.info("Registros após filtro: %d", len(vendas))

    total = valor_total_de_vendas(vendas)
    total_vendas_por_produtos = vendas_por_produtos(vendas)
    melhor_produto = produto_mais_vendido(vendas)

    logger.debug("Valor total calculado: %.2f", total)
    logger.debug("Vendas por produto: %s", total_vendas_por_produtos)
    logger.debug("Produto mais vendido: %s", melhor_produto)

    if args.format == "json":
        print(renderizar_json(total, total_vendas_por_produtos, melhor_produto))
    else:
        print(renderizar_texto(total, total_vendas_por_produtos, melhor_produto))

    logger.info("Execução finalizada com sucesso")

if __name__ == "__main__":
    main()
