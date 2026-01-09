from vendas_cli.output import renderizar_texto, renderizar_json


def test_renderizar_texto():
    output = renderizar_texto(
        total=100.0,
        vendas_por_produtos={"A": 60.0, "B": 40.0},
        melhor_produto="A",
    )

    assert "Total geral: R$ 100.00" in output
    assert "- A: R$ 60.00" in output
    assert "Produto mais vendido: A" in output


def test_renderizar_json():
    output = renderizar_json(
        total=100.0,
        vendas_por_produtos={"A": 60.0},
        melhor_produto="A",
    )

    assert '"total_vendas"' in output
    assert '"A": 60.0' in output
