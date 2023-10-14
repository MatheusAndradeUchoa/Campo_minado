
import pytest
from src.main import CampoMinado
from unittest.mock import MagicMock, patch

def test_revelar_celula():
    campo_minado = CampoMinado(None, 8, 8, 10)
    
   # botoes = [['disabled'] * campo_minado.colunas for _ in range(campo_minado.linhas)]
    
    campo_minado.revelar_celula(0, 2)  
    
    vizinhos_esperados = campo_minado.calcular_vizinhos(0, 2)  
    assert campo_minado.botoes[0][2]['text'] == str(vizinhos_esperados) 
def test_revelar_celula_sem_bombas_adjacentes():
    #root = tkinter.Tk()
    campo_minado = CampoMinado(None, 8, 8, 10)

    
    campo_minado.revelar_adjacentes = MagicMock()

    for i in range(campo_minado.linhas):
        for j in range(campo_minado.colunas):
            if (i, j) != (1, 1):
                campo_minado.tabuleiro[i][j] = 0

    campo_minado.revelar_celula(1, 1)
    campo_minado.revelar_adjacentes.assert_called_with(1, 1)
    
       



   