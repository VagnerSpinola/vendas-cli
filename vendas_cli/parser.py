import csv
from datetime import datetime
from typing import List
from vendas_cli.models import Venda
from vendas_cli.config import logger, EXPECTED_COLUMNS
from vendas_cli.errors import FileLoadError, ValidacaoDataError, FormatoCSVError



def parse_csv(path: str) -> list[Venda]:
    try:
        with open(path, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            colunas = set(reader.fieldnames or [])

            colunas_faltando = EXPECTED_COLUMNS - colunas
            if colunas_faltando:
                raise FormatoCSVError(
                    f"Cabeçalhos obrigatórios ausentes: {', '.join(sorted(colunas_faltando))}"
                )

            sales = []
            for row in reader:
                try:
                    sales.append(
                        Venda(
                            data=datetime.strptime(row["data"], "%Y-%m-%d").date(),
                            produto=row["produto"],
                            quantidade=int(row["quantidade"]),
                            preco=float(row["preco"]),
                        )
                    )
                except Exception as exc:
                    logger.debug("Linha inválida: %s", row)
                    raise ValidacaoDataError(f"Linha inválida: {row}") from exc

            return sales

    except FileNotFoundError as exc:
        raise FileLoadError("Arquivo não encontrado.") from exc

    except PermissionError as exc:
        raise FileLoadError("Sem permissão para acessar o arquivo.") from exc

    except UnicodeDecodeError as exc:
        raise FileLoadError("Arquivo deve estar em UTF-8.") from exc
