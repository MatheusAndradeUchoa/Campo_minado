import pytest
from src.main import CampoMinado  

def test_verificar_bombas_facil():
    root = None
    linhas = 8
    colunas = 8
    num_bombas = 10
    campo_minado = CampoMinado(root, linhas, colunas, num_bombas)

    # Verifica se o número correto de bombas foi adicionado
    bomb_count = sum(row.count(-1) for row in campo_minado.tabuleiro)
    assert bomb_count == num_bombas

def test_verificar_bombas_intermediario():
    root = None
    linhas = 10
    colunas = 16
    num_bombas = 30
    campo_minado = CampoMinado(root, linhas, colunas, num_bombas)

    # Verifica se o número correto de bombas foi adicionado
    bomb_count = sum(row.count(-1) for row in campo_minado.tabuleiro)
    assert bomb_count == num_bombas

def test_verificar_bombas_dificil():
    root = None
    linhas = 24
    colunas = 24
    num_bombas = 100
    campo_minado = CampoMinado(root, linhas, colunas, num_bombas)

    # Verifica se o número correto de bombas foi adicionado
    bomb_count = sum(row.count(-1) for row in campo_minado.tabuleiro)
    assert bomb_count == num_bombas