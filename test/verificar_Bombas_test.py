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
def test_calcular_vizinhos_sem_bomba(posicao, expected_vizinhos):  
    vizinhos = campo_minado.calcular_vizinhos(*posicao)
    assert vizinhos == expected_vizinhos

@pytest.mark.parametrize("posicao,expected_vizinhos", [
    ((0, 0), 0),  # Canto superior esquerdo
    ((0, 15),0),  # Canto superior direito
    ((9, 0),0),  # Canto inferior esquerdo
    ((9, 15), 0),  # Canto inferior direito
    ((5, 7), 0)    #centro(eu acho, sou burro)
])
def test_calcular_vizinhos_intermediario_sem_bomba(posicao, expected_vizinhos):
    campo_minado_intermediario = CampoMinado(None, 10, 16, 0) 
    vizinhos = campo_minado_intermediario.calcular_vizinhos(*posicao)
    assert vizinhos == expected_vizinhos

#modo Dificil
@pytest.mark.parametrize("posicao, expected_vizinhos",[
    ((0, 0),0),  
    ((0, 23),0),  
    ((23, 0), 0), 
    ((23, 23), 0),  
    ((12, 12),0)  #não tenho ideia de onde ta mas deve ta perto do centro(muito grande)
])
def test_calcular_vizinhos_dificil_sem_bomba(posicao, expected_vizinhos):
    campo_minado = CampoMinado(None, 24, 24, 0)
    vizinhos = campo_minado.calcular_vizinhos(*posicao)
    assert vizinhos == expected_vizinhos

#Test para calcular vizinhos nos cantos e no centro do tabuleiro com BOMBA
#Modo Facil
@pytest.mark.parametrize("posicao, bomb_positions, expected_vizinhos", [
    ((0, 0), [(0, 1), (1, 0), (1, 1)], 3),  # Canto superior esquerdo
    ((0, 7), [(0, 6), (1, 6), (1, 7)], 3),  # Canto superior direito
    ((7, 0), [(6, 0), (6, 1), (7, 1)], 3),  # Canto inferior esquerdo
    ((7, 7), [(6, 6), (6, 7), (7, 6)], 3),  # Canto inferior direito
    ((4, 4), [(3, 3), (3, 4), (3, 5), (4, 3), (4, 5), (5, 3), (5, 4), (5, 5)], 8)  # algum lugar no centro
])
def test_calcular_vizinhos_facil_com_bombas(posicao, bomb_positions, expected_vizinhos): 
    posicionar_bombas(campo_minado, bomb_positions)
    vizinhos = campo_minado.calcular_vizinhos(*posicao)
    assert vizinhos == expected_vizinhos

#Modo Intermediario
@pytest.mark.parametrize("posicao, bomb_positions, expected_vizinhos", [
    ((0, 0), [(0, 1), (1, 0), (1, 1)], 3),  # Canto superior esquerdo
    ((0, 15), [(0, 14), (1, 14), (1, 15)], 3),  # Canto superior direito
    ((9, 0), [(8, 0), (8, 1), (9, 1)], 3),  # Canto inferior esquerdo
    ((9, 15), [(8, 14), (8, 15), (9, 14)], 3),  # Canto inferior direito
    ((5, 7), [(4, 6), (4, 7), (4, 8), (5, 6), (5, 8), (6, 6), (6, 7), (6, 8)], 8) #não tenho ideia de onde ta mas deve ta perto do centro(muito grande)
])
def test_calcular_vizinhos_intermediario_com_bombas(posicao, bomb_positions, expected_vizinhos):
    campo_minado = CampoMinado(None, 10, 16, 0)
    posicionar_bombas(campo_minado, bomb_positions)
    vizinhos = campo_minado.calcular_vizinhos(*posicao)
    assert vizinhos == expected_vizinhos
    
#modo Dificil
@pytest.mark.parametrize("posicao, bomb_positions, expected_vizinhos", [
    ((0, 0), [(0, 1), (1, 0), (1, 1)], 3),  
    ((0, 23), [(0, 22), (1, 22), (1, 23)], 3),  
    ((23, 0), [(22, 0), (22, 1), (23, 1)], 3), 
    ((23, 23), [(22, 22), (22, 23), (23, 22)], 3),  
    ((12, 12), [(11, 11), (11, 12), (11, 13), (12, 11), (12, 13), (13, 11), (13, 12), (13, 13)], 8)  #não tenho ideia de onde ta mas deve ta perto do centro(muito grande)
])
def test_calcular_vizinhos_dificil_com_bombas(posicao, bomb_positions, expected_vizinhos):
    campo_minado = CampoMinado(None, 24, 24, 0)
    posicionar_bombas(campo_minado, bomb_positions)
    vizinhos = campo_minado.calcular_vizinhos(*posicao)
    assert vizinhos == expected_vizinhos





    

    

