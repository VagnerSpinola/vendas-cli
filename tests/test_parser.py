import pytest
from pathlib import Path
from vendas_cli.parser import parse_csv
from vendas_cli.errors import FormatoCSVError, ValidacaoDataError


def test_parse_csv_sucesso(tmp_path: Path):
    file = tmp_path / "vendas.csv"
    file.write_text(
        "data,produto,quantidade,preco\n"
        "2025-01-01,A,2,10.0\n"
    )

    vendas = parse_csv(str(file))
    assert len(vendas) == 1
    assert vendas[0].produto == "A"


def test_parse_csv_coluna_ausente(tmp_path: Path):
    file = tmp_path / "vendas.csv"
    file.write_text("data,produto,quantidade\n")

    with pytest.raises(FormatoCSVError):
        parse_csv(str(file))


def test_parse_csv_valor_invalido(tmp_path: Path):
    file = tmp_path / "vendas.csv"
    file.write_text(
        "data,produto,quantidade,preco\n"
        "2025-01-01,A,abc,10.0\n"
    )

    with pytest.raises(ValidacaoDataError):
        parse_csv(str(file))
