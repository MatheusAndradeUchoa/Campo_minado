import pytest
from src.main import CampoMinado  

def test_verificar_vitoria():
    # Crie uma instância de CampoMinado com dimensões 4x4 e 4 bombas
    campo_minado = CampoMinado(None, 8, 8, 4)

    # Defina manualmente as posições das bombas para facilitar os testes
    # Neste exemplo, colocamos bombas nas células (0, 0), (1, 1), (2, 2) e (3, 3)
    campo_minado.tabuleiro[0][0] = -1
    campo_minado.tabuleiro[1][1] = -1
    campo_minado.tabuleiro[2][2] = -1
    campo_minado.tabuleiro[3][3] = -1

    # Simule a revelação de todas as células não bombas
    for i in range(8):
        for j in range(8):
            if campo_minado.tabuleiro[i][j] != -1:
                campo_minado.botoes[i][j]['state'] = 'disabled'

    # Verifique se a função retorna True, indicando que o jogador venceu
    assert campo_minado.verificar_vitoria() == True