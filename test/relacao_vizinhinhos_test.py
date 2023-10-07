import pytest
from src.main import CampoMinado


def posicionar_bombas(campo_minado, bomb_positions):
    for x, y in bomb_positions:
        campo_minado.tabuleiro[x][y] = -1
        
def test_calcular_vizinhos_canto_superior_esquerdo_sem_bombas():
    campo_minado = CampoMinado(None, 8, 8, 0) 
    vizinhos = campo_minado.calcular_vizinhos(0,0)  
    assert vizinhos == 0


    

    

