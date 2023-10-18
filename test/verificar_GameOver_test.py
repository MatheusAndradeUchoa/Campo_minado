import pytest
from src.campo_minado import CampoMinado


@pytest.mark.parametrize("posicao", [
    (0, 0),  
    (0, 7),
    (3, 3),
    (7, 7)
])
def test_game_over_facil(posicao):
    campo_minado = CampoMinado(None, 8, 8, 10)

    campo_minado.tabuleiro[posicao[0]][posicao[1]] = -1
    campo_minado.game_over(mostrar_interface=False)

    
    assert campo_minado.botoes[posicao[0]][posicao[1]]['text'] == 'X'
    assert campo_minado.botoes[posicao[0]][posicao[1]]['state'] == 'disabled'



@pytest.mark.parametrize("posicao", [
    (0, 0),  
    (9, 15),
    (0, 15), 
    (5, 8),
    (9, 15) 
])
def test_game_over_intermediario(posicao):
    campo_minado = CampoMinado(None, 10, 16, 40)

   
    campo_minado.tabuleiro[posicao[0]][posicao[1]] = -1
    campo_minado.game_over(mostrar_interface=False)

   
    assert campo_minado.botoes[posicao[0]][posicao[1]]['text'] == 'X'
    assert campo_minado.botoes[posicao[0]][posicao[1]]['state'] == 'disabled'



@pytest.mark.parametrize("posicao", [
    (0, 0),  # Canto Superior
    (23, 23),  # Canto Inferior
    (0, 23),
    (12, 12),
    (23, 23) 
])
def test_game_over_dificil(posicao):
    campo_minado = CampoMinado(None, 24, 24, 99)

    
    campo_minado.tabuleiro[posicao[0]][posicao[1]] = -1
    campo_minado.game_over(mostrar_interface=False)

    
    assert campo_minado.botoes[posicao[0]][posicao[1]]['text'] == 'X'
    assert campo_minado.botoes[posicao[0]][posicao[1]]['state'] == 'disabled'
