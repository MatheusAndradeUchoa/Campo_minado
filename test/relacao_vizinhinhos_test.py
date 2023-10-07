import pytest
from src.main import CampoMinado

campo_minado = CampoMinado(None,8,8,0)
def posicionar_bombas(campo_minado, bomb_positions):
    for x, y in bomb_positions:
        campo_minado.tabuleiro[x][y] = -1
        
def test_calcular_vizinhos_canto_superior_esquerdo_sem_bombas():
    
    vizinhos = campo_minado.calcular_vizinhos(0,0)  
    assert vizinhos == 0
    
def test_calcular_vizinhos_canto_superior_direito_sem_bombas():

    vizinhos = campo_minado.calcular_vizinhos(0, 7)  
    assert vizinhos == 0

def test_calcular_vizinhos_canto_inferior__esquerdo_sem_bombas():
    
    vizinhos = campo_minado.calcular_vizinhos(7,0)  
    assert vizinhos == 0

def test_calcular_vizinhos_canto_inferior_direito_sem_bombas():
    
    vizinhos = campo_minado.calcular_vizinhos(7,0)  
    assert vizinhos == 0

def test_calcular_vizinhos_centro_sem_bombas():
    
    vizinhos = campo_minado.calcular_vizinhos(4, 4)
    assert vizinhos == 0



def test_calcular_vizinhos_canto_superior_esquerdo_com_bombas():
    bomb_positions = [(0, 1), (1, 0), (1, 1)] 
    posicionar_bombas(campo_minado, bomb_positions)
    vizinhos = campo_minado.calcular_vizinhos(0, 0)
    assert vizinhos == 3 

def test_calcular_vizinhos_canto_superior_direito_com_bombas():
   
    bomb_positions = [(0, 7), (1, 7)] 
    posicionar_bombas(campo_minado, bomb_positions)
    vizinhos = campo_minado.calcular_vizinhos(0, 7)  
    assert vizinhos == 2

def test_calcular_vizinhos_canto_inferior__esquerdo_com_bombas():
    bomb_positions = [(7, 1), (6, 0)]  
    posicionar_bombas(campo_minado, bomb_positions)
    vizinhos = campo_minado.calcular_vizinhos(7,0)  
    assert vizinhos == 2
    
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
    vizinhos = campo_minado.calcular_vizinhos(7,0)  
    assert vizinhos == 2

def test_calcular_vizinhos_centro_com_bombas():
    bomb_positions = [(3, 3), (3, 4), (3, 5), (4, 3), (4, 5), (5, 3), (5, 4), (5, 5)]  
    posicionar_bombas(campo_minado, bomb_positions)
    vizinhos = campo_minado.calcular_vizinhos(4, 4)
    assert vizinhos == 8




    

    

