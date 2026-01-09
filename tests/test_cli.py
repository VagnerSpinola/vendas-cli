import builtins
from datetime import date
import sys
import pytest
from vendas_cli.cli import main
from vendas_cli.models import Venda


def test_cli_text(monkeypatch, capsys):
    monkeypatch.setattr(
        "vendas_cli.cli.carrega_arquivo",
        lambda args: [
            Venda(date(2025, 1, 1), "A", 2, 10)
        ],
    )

    main(["fake.csv", "--format", "text"])
    out, _ = capsys.readouterr()
    assert "RELATÓRIO DE VENDAS" in out


def test_cli_json(monkeypatch, capsys):
    monkeypatch.setattr(
        "vendas_cli.cli.carrega_arquivo",
        lambda args: [
            Venda(date(2025, 1, 1), "A", 2, 10)
        ],
    )

    main(["fake.csv", "--format", "json"])
    out, _ = capsys.readouterr()
    assert '"total_vendas"' in out
