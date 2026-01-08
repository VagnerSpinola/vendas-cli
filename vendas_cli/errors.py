class VendasError(Exception):
    """Erro base da aplicação."""


class FileLoadError(VendasError):
    """Erro ao carregar arquivo."""


class FormatoCSVError(VendasError):
    """CSV inválido ou malformado."""


class ValidacaoDataError(VendasError):
    """Erro de validação dos dados."""