import pytest

from src.campo_minado import CampoMinado


def test_game_over_no_interface():
    # Criar uma instância de CampoMinado com dimensões 8x8 e 1 bomba
   
    campo_minado = CampoMinado(None, 8, 8, 1)

    # Colocar uma bomba em uma célula (0, 0)
    campo_minado.tabuleiro[0][0] = -1

    # Chamar a função game_over sem exibir a interface
    campo_minado.game_over(mostrar_interface=False)

    # Verificar se os botões foram desativados e marcados com 'X'
    assert campo_minado.botoes[0][0]['text'] == 'X'
    assert campo_minado.botoes[0][0]['state'] == 'disabled'