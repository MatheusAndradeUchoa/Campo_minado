import pytest

from src.campo_minado import CampoMinado


campo_minado = CampoMinado(None,8,8,0)
intermediario = CampoMinado(None,10,16,0)
dificil = CampoMinado(None,10,16,0)

def posicionar_bombas(campo_minado, bomb_positions):
    for x, y in bomb_positions:
        campo_minado.tabuleiro[x][y] = -1
        
#Test que verifica a relação de vizinhança sem bombas nos cantos do tabuleiro e no centro

#Modo Facil
@pytest.mark.parametrize("posicao , expected_vizinhos", [
    ((0, 0), 0),  # Canto superior esquerdo
    ((0, 7), 0),  # Canto superior direito
    ((7, 0), 0),  # Canto inferior esquerdo
    ((7, 7), 0),  # Canto inferior direito
    ((4, 4), 0)  # algum lugar no centro
])
def test_calcular_vizinhos_sem_bomba(posicao, expected_vizinhos):  
    vizinhos = campo_minado.calcular_vizinhos(*posicao)
    assert vizinhos == expected_vizinhos
    
# #intermediario
@pytest.mark.parametrize("posicao, vizinhos_esperados", [
    ((0, 0),0),  # Canto superior esquerdo
    ((0, 15),0),  # Canto superior direito
    ((9, 0),0),  # Canto inferior esquerdo
    ((9, 15),0),  # Canto inferior direito
    ((5, 7),0) #não tenho ideia de onde ta mas deve ta perto do centro(muito grande)
])
def test_calcular_vizinhos_sem_bomba_intermediario(posicao, vizinhos_esperados):  
    vizinhos = intermediario.calcular_vizinhos(*posicao)
    assert vizinhos == vizinhos_esperados
    
# #dificil   
@pytest.mark.parametrize("posicao, vizinhos_esperados", [
    ((0, 0), 0),  
    ((0, 23),0),  
    ((23, 0),0), 
    ((23, 23),0),  
    ((12, 12),0)  #não tenho ideia de onde ta mas deve ta perto do centro(muito grande)
])
def test_calcular_vizinhos_sem_bomba_dificil(posicao, vizinhos_esperados):  
    vizinhos = dificil.calcular_vizinhos(*posicao)
    assert vizinhos == vizinhos_esperados

   
#Test para calcular vizinhos nos cantos e no centro do tabuleiro
#Modo Facil
@pytest.mark.parametrize("posicao, posicao_bomba, vizinhos_esperados", [
    # Canto superior esquerdo
    ((0, 0), [(0, 1), (1, 0), (1, 1)], 3),
    ((0, 0), [(0, 1), (1, 0)], 2),
    ((0, 0), [(0, 1)], 1),
    
    # Canto superior direito
    ((0, 7), [(0, 6), (1, 6), (1, 7)], 3), 
    ((0, 7), [(0, 6), (1, 6)], 2), 
    ((0, 7), [(0, 6)], 1), 
     
     # Canto inferior esquerdo
    ((7, 0), [(6, 0), (6, 1), (7, 1)], 3),
    ((7, 0), [(6, 0), (6, 1)], 2), 
    ((7, 0), [(6, 0)], 1), 
    
    # Canto inferior direito
    ((7, 7), [(6, 6), (6, 7), (7, 6)], 3),
    ((7, 7), [(6, 6), (6, 7)], 2), 
    ((7, 7), [(6, 6)], 1),  
    
    #Centro
    ((4, 4), [(3, 3), (3, 4), (3, 5), (4, 3), (4, 5), (5, 3), (5, 4), (5, 5)], 8),
    ((4, 4), [(3, 3), (3, 4), (3, 5), (4, 3), (4, 5), (5, 3), (5, 4)], 7), 
    ((4, 4), [(3, 3), (3, 4), (3, 5), (4, 3), (4, 5), (5, 3)], 6),   
    ((4, 4), [(3, 3), (3, 4), (3, 5), (4, 3), (4, 5)], 5), 
    ((4, 4), [(3, 3), (3, 4), (3, 5), (4, 3)], 4), 
    ((4, 4), [(3, 3), (3, 4), (3, 5)], 3), 
    ((4, 4), [(3, 3), (3, 4),], 2), 
    ((4, 4), [(3, 3)], 1), 

])
def test_calcular_vizinhos_facil_com_bombas(posicao, posicao_bomba, vizinhos_esperados):
    campo_minado = CampoMinado(None,8,8,0) 
    posicionar_bombas(campo_minado, posicao_bomba)
    vizinhos = campo_minado.calcular_vizinhos(*posicao)
    assert vizinhos == vizinhos_esperados

#Modo Intermediario
@pytest.mark.parametrize("posicao, posicao_bomba, vizinhos_esperados", [
    # Canto superior esquerdo
    ((0, 0), [(0, 1), (1, 0), (1, 1)], 3), 
    ((0, 0), [(0, 1), (1, 0)], 2),  
    ((0, 0), [(0, 1)], 1),  
    # Canto superior direito
    ((0, 15), [(0, 14), (1, 14), (1, 15)], 3),
    ((0, 15), [(0, 14), (1, 14)], 2), 
    ((0, 15), [(0, 14)], 1), 
    
    # Canto inferior esquerdo
    ((9, 0), [(8, 0), (8, 1), (9, 1)], 3), 
    ((9, 0), [(8, 0), (8, 1)], 2),  
    ((9, 0), [(8, 0)], 1), 
    # Canto inferior direito
    ((9, 15), [(8, 14), (8, 15), (9, 14)], 3),
    ((9, 15), [(8, 14), (8, 15)], 2), 
    ((9, 15), [(8, 14)], 1), 
    
    #Centro
    ((5, 7), [(4, 6), (4, 7), (4, 8), (5, 6), (5, 8), (6, 6), (6, 7), (6, 8)], 8),
    ((5, 7), [(4, 6), (4, 7), (4, 8), (5, 6), (5, 8), (6, 6), (6, 7)], 7),
    ((5, 7), [(4, 6), (4, 7), (4, 8), (5, 6), (5, 8), (6, 6)], 6),
    ((5, 7), [(4, 6), (4, 7), (4, 8), (5, 6), (5, 8)], 5),
    ((5, 7), [(4, 6), (4, 7), (4, 8), (5, 6)], 4),
    ((5, 7), [(4, 6), (4, 7), (4, 8)], 3),
    ((5, 7), [(4, 6), (4, 7)], 2),
    ((5, 7), [(4, 6)], 1),
])
def test_calcular_vizinhos_intermediario_com_bombas(posicao, posicao_bomba, vizinhos_esperados):
    campo_minado = CampoMinado(None, 10, 16, 0)
    posicionar_bombas(campo_minado, posicao_bomba)
    vizinhos = campo_minado.calcular_vizinhos(*posicao)
    assert vizinhos == vizinhos_esperados
    
#modo Dificil
@pytest.mark.parametrize("posicao, posicao_bomba, vizinhos_esperados", [
    
    ((0, 0), [(0, 1), (1, 0), (1, 1)], 3),
    ((0, 0), [(0, 1), (1, 0)], 2),
    ((0, 0), [(0, 1)], 1),
    
    
    ((0, 23), [(0, 22), (1, 22), (1, 23)], 3),
    ((0, 23), [(0, 22), (1, 22)], 2), 
    ((0, 23), [(0, 22)], 1), 
  
     
    ((23, 0), [(22, 0), (22, 1), (23, 1)], 3), 
    ((23, 0), [(22, 0), (22, 1)], 2),
    ((23, 0), [(22, 0)], 1),
    
    
    ((23, 23), [(22, 22), (22, 23), (23, 22)], 3),
    ((23, 23), [(22, 22), (22, 23)], 2),
    ((23, 23), [(22, 22)], 1),
    
    
    ((12, 12), [(11, 11), (11, 12), (11, 13), (12, 11), (12, 13), (13, 11), (13, 12), (13, 13)], 8),
    ((12, 12), [(11, 11), (11, 12), (11, 13), (12, 11), (12, 13), (13, 11), (13, 12)], 7),
    ((12, 12), [(11, 11), (11, 12), (11, 13), (12, 11), (12, 13), (13, 11)], 6),
    ((12, 12), [(11, 11), (11, 12), (11, 13), (12, 11), (12, 13)], 5),
    ((12, 12), [(11, 11), (11, 12), (11, 13), (12, 11)], 4),
    ((12, 12), [(11, 11), (11, 12), (11, 13)], 3),
    ((12, 12), [(11, 11), (11, 12)], 2),
    ((12, 12), [(11, 11)], 1),
    
       
])
def test_calcular_vizinhos_dificil_com_bombas(posicao, posicao_bomba, vizinhos_esperados):
    campo_minado = CampoMinado(None, 24, 24, 0)
    posicionar_bombas(campo_minado, posicao_bomba)
    vizinhos = campo_minado.calcular_vizinhos(*posicao)
    assert vizinhos == vizinhos_esperados



    

    

