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
    contador_de_bomba = sum(row.count(-1) for row in campo_minado.tabuleiro)
    assert contador_de_bomba == num_bombas

def test_verificar_bombas_dificil():
    root = None
    linhas = 24
    colunas = 24
    num_bombas = 100
    campo_minado = CampoMinado(root, linhas, colunas, num_bombas)

    # Verifica se o número correto de bombas foi adicionado
    contador_de_bomba = sum(row.count(-1) for row in campo_minado.tabuleiro)
    assert contador_de_bomba == num_bombas

#modo FAcil    
@pytest.mark.parametrize("posicao_bombas", [
    [(0, 0), (1, 1), (2, 2), (3, 3)],
    [(2, 3), (4, 5), (6, 7), (1, 7)],
    [(0, 1), (2, 4), (5, 3), (6, 6)],
    [(1, 2), (3, 5), (7, 7), (0, 5)],
    [(4, 6), (6, 2), (3, 1), (2, 7)],
    [(5, 1), (0, 2), (4, 3), (6, 4)]
    ])
def test_posicoes_bombas(posicao_bombas):
    campo_minado = CampoMinado(None, 8, 8, 4)

    for x, y in posicao_bombas:
        campo_minado.tabuleiro[x][y] = -1
    
    for x, y in posicao_bombas:
        assert campo_minado.tabuleiro[x][y] == -1
        
#modo Intermediario
@pytest.mark.parametrize("posicao_bomba", [
    [(0, 0), (1, 1), (2, 2), (3, 3)],
    [(2, 3), (4, 5), (6, 7), (1, 7)],
    [(0, 1), (2, 4), (5, 3), (6, 6)],
    [(1, 2), (3, 5), (7, 7), (0, 5)],
    [(4, 6), (6, 2), (3, 1), (2, 7)],
    [(5, 1), (0, 2), (4, 3), (6, 4)]
    ])      
def test_posicoes_bombas__modo_intermediario(posicao_bomba):
    campo_minado = CampoMinado(None, 10, 16, 4)

    for x, y in posicao_bomba:
        campo_minado.tabuleiro[x][y] = -1
    
    for x, y in posicao_bomba:
        assert campo_minado.tabuleiro[x][y] == -1
        
#Modo Dificil
@pytest.mark.parametrize("posicao_bombas", [
    [(0, 0), (1, 1), (2, 2), (3, 3)],
    [(2, 3), (4, 5), (6, 7), (1, 7)],
    [(0, 1), (2, 4), (5, 3), (6, 6)],
    [(1, 2), (3, 5), (7, 7), (0, 5)],
    [(4, 6), (6, 2), (3, 1), (2, 7)],
    [(5, 1), (0, 2), (4, 3), (6, 4)]
    ])      
def test_posicoes_bombas__modo_dificil(posicao_bombas):
    campo_minado = CampoMinado(None, 24, 24, 4)

    for x, y in posicao_bombas:
        campo_minado.tabuleiro[x][y] = -1
    
    for x, y in posicao_bombas:
        assert campo_minado.tabuleiro[x][y] == -1


# Teste para posições inválidas
@pytest.mark.parametrize("posicao_invalida", [
    [(-1, 0),], 
    [(0, -1),], 
    [(8, 0),], 
    [(0, 8)], 
    [(5, 10)], [(15, 3)], [(10, -5)], [(13, 20)],[(-1,-1)],[(8,8)]]
)
def test_posicionar_bombas_posicao_invalida_modo_facil(posicao_invalida):
    with pytest.raises(ValueError):
        campo_minado = CampoMinado(None, 8, 8, 10)
        campo_minado.posicionar_bombas_em_posicoes(posicao_invalida)


@pytest.mark.parametrize("posicao_invalida", [
    [(-1, 0),], 
    [(0, -1),], 
    [(11, 0),], 
    [(10, 17)], 
    [(31, 10)], [(31, 3)], [(10, -5)], [(13, 20)],[(-1,-1)],[(11,17)]]
)
def test_posicionar_bombas_posicao_invalida_modo_intermediario(posicao_invalida):
    with pytest.raises(ValueError):
        campo_minado = CampoMinado(None, 10, 16, 10)
        campo_minado.posicionar_bombas_em_posicoes(posicao_invalida)

@pytest.mark.parametrize("posicao_invalida", [
    [(-1, 0)], 
    [(0, -1)], 
    [(11, -1)], 
    [(-1, 25)], 
    [(31, 10)], [(31, 3)], [(10, -5)], [(25, 20)], [(-1,-1)],[(25,25)]]
)
def test_posicionar_bombas_posicao_invalida_modo_dificil(posicao_invalida):
    with pytest.raises(ValueError):
        campo_minado = CampoMinado(None, 24,24, 10)
        campo_minado.posicionar_bombas_em_posicoes(posicao_invalida)








    

    

