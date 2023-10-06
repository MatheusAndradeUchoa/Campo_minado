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
    
@pytest.mark.parametrize("bomb_positions", [
    [(0, 0), (1, 1), (2, 2), (3, 3)],
    [(2, 3), (4, 5), (6, 7), (1, 7)],
    [(0, 1), (2, 4), (5, 3), (6, 6)],
    [(1, 2), (3, 5), (7, 7), (0, 5)],
    [(4, 6), (6, 2), (3, 1), (2, 7)],
    [(5, 1), (0, 2), (4, 3), (6, 4)]
    ])
def test_posicoes_bombas(bomb_positions):
    campo_minado = CampoMinado(None, 8, 8, 4)

    for x, y in bomb_positions:
        campo_minado.tabuleiro[x][y] = -1
    
    for x, y in bomb_positions:
        assert campo_minado.tabuleiro[x][y] == -1