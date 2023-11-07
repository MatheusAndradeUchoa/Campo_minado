import tkinter as tk
from unittest import mock
import pytest
from src.campo_minado import CampoMinado


@pytest.mark.parametrize("posicao", [
    (0, 0),  
    (0, 7),
    (3, 3),
    (7, 7),
    (5, 3),
    (6, 6),
    (7, 4),
    (4, 5),
    
    
])
def test_game_over_facil(posicao):
    campo_minado = CampoMinado(None, 8, 8, 10)

    campo_minado.tabuleiro[posicao[0]][posicao[1]] = -1
    campo_minado.game_over(mostrar_interface=False)

    
    assert campo_minado.botoes[posicao[0]][posicao[1]]['text'] == 'X'



@pytest.mark.parametrize("posicao", [
    (0, 0),  
    (9, 15),
    (0, 15), 
    (5, 8),
    (9, 5),
    (8, 2),
    (9, 15),
    (2,5),
    (1, 5),
    
])
def test_game_over_intermediario(posicao):
    campo_minado = CampoMinado(None, 10, 16, 40)

   
    campo_minado.tabuleiro[posicao[0]][posicao[1]] = -1
    campo_minado.game_over(mostrar_interface=False)

   
    assert campo_minado.botoes[posicao[0]][posicao[1]]['text'] == 'X'



@pytest.mark.parametrize("posicao", [
    (0, 0),  
    (23, 23),  
    (0, 23),
    (12, 12),
    (23, 23),
    (22, 22), 
    (5, 10), 
    (15, 15),
    (19,17),
    (1, 5),
    (9,23),
])
def test_game_over_dificil(posicao):
    campo_minado = CampoMinado(None, 24, 24, 0)

    
    campo_minado.tabuleiro[posicao[0]][posicao[1]] = -1
    campo_minado.game_over(mostrar_interface=False)

    
    assert campo_minado.botoes[posicao[0]][posicao[1]]['text'] == 'X'


def test_mostrar_bombas_apos_derrota():
    root = tk.Tk()
    campo_minado = CampoMinado(None, 8, 8, 10)

   
    bomb_positions = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (0, 7), (7, 0)]
    campo_minado.criar_tabuleiro(bomb_positions=bomb_positions)

   
    campo_minado.game_over(mostrar_interface=False)

    for x in range(8):
        for y in range(8):
            assert campo_minado.botoes[x][y]['state'] == 'disabled'

    root.destroy()

