from datetime import date
from vendas_cli.core import (
    filtra_por_data,
    valor_total_de_vendas,
    vendas_por_produtos,
    produto_mais_vendido,
)
from vendas_cli.models import Venda


def vendas_mock():
    return [
        Venda(date(2025, 1, 1), "A", 2, 10),
        Venda(date(2025, 1, 2), "B", 3, 5),
        Venda(date(2025, 1, 3), "A", 1, 10),
    ]


def test_filtra_por_data_sem_filtro():
    vendas = vendas_mock()
    assert filtra_por_data(vendas, None, None) == vendas


def test_filtra_por_data_com_intervalo():
    vendas = vendas_mock()
    result = filtra_por_data(vendas, date(2025, 1, 2), date(2025, 1, 3))
    assert len(result) == 2


def test_valor_total_de_vendas():
    assert valor_total_de_vendas(vendas_mock()) == 45


def test_vendas_por_produtos():
    result = vendas_por_produtos(vendas_mock())
    assert result == {"A": 30, "B": 15}


def test_produto_mais_vendido():
    assert produto_mais_vendido(vendas_mock()) == ["A", "B"]


def test_produto_mais_vendido_vazio():
    assert produto_mais_vendido([]) == []
