import pytest

from src.campo_minado import CampoMinado
 

def test_verificar_vitoria():
    campo_minado = CampoMinado(None, 8, 8, 4)

    campo_minado.tabuleiro[0][0] = -1
    campo_minado.tabuleiro[1][1] = -1
    campo_minado.tabuleiro[2][2] = -1
    campo_minado.tabuleiro[3][3] = -1

    for i in range(8):
        for j in range(8):
            if campo_minado.tabuleiro[i][j] != -1:
                campo_minado.botoes[i][j]['state'] = 'disabled'

    assert campo_minado.verificar_vitoria() == True