import re
from validate_docbr import CPF


def cpf_invalido(numero_cpf):
    cpf_valido = CPF().validate(numero_cpf)
    return not cpf_valido

def nome_invalido (nome):
    return not nome.isalpha()

def celular_invalido(celular):
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    re.findall(modelo,celular)        