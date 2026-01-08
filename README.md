# 📊 Vendas CLI — Gerador Avançado de Relatórios de Vendas

CLI em Python para processamento de arquivos CSV de vendas e geração de relatórios ricos, desenvolvida com **boas práticas de engenharia de software**, foco em **qualidade, testes e observabilidade**.

> Projeto criado como **desafio de nível Python Sênior**.

---

## 🚀 Funcionalidades

- Leitura de arquivos CSV via linha de comando
- Cálculo de:
  - Valor total das vendas
  - Total de vendas por produto
  - Produto mais vendido (com soma correta de quantidades)
- Filtro opcional por intervalo de datas
- Saída em:
  - Texto formatado
  - JSON
- Tratamento robusto de erros
- Logging claro e centralizado
- Testes unitários com **100% de cobertura**

---

## 📂 Estrutura do Projeto

```text
vendas_cli/
├── vendas_cli/
│   ├── __init__.py
│   ├── cli.py          # CLI (argparse)
│   ├── core.py         # Regras de negócio (funções puras)
│   ├── parser.py       # Leitura e validação do CSV
│   ├── output.py       # Formatação de saída
│   ├── models.py       # Dataclasses
│   ├── errors.py       # Exceções customizadas
│   └── config.py       # Configuração de logging
├── tests/
│   ├── test_cli.py
│   ├── test_core.py
│   ├── test_parser.py
│   └── test_output.py
├── pyproject.toml
├── pytest.ini
├── README.md
└── LICENSE
```


# Exemplo CSV

data,produto,quantidade,preco
2025-01-01,Notebook,2,3500.00
2025-01-02,Mouse,5,50.00

# Instalacao

python -m venv venv
source venv/bin/activate  # Linux / macOS
venv\Scripts\activate     # Windows

pip install -e .

# Texto

vendas-cli vendas.csv --format text


# json

vendas-cli vendas.csv --format json


# Filtro com datas

vendas-cli vendas.csv --format json --start 2025-01-01 --end 2025-03-31



# Testes

pytest

