
import pytest
from unittest.mock import MagicMock, patch
import tkinter as tk
from src.campo_minado import CampoMinado


def test_revelar_celula_sem_bombas_adjacentes():
    root = tk.Tk()
    root.withdraw()
    campo_minado = CampoMinado(root, 8, 8, 10)

    
    campo_minado.revelar_adjacentes = MagicMock()

    for i in range(campo_minado.linhas):
        for j in range(campo_minado.colunas):
            if (i, j) != (1, 1):
                campo_minado.tabuleiro[i][j] = 0

    campo_minado.revelar_celula(1, 1)
    campo_minado.revelar_adjacentes.assert_called_with(1, 1)

def test_revelar_celula_sem_bomba_com_vizinhos():
    root = tk.Tk()
    root.withdraw()
    campo_minado = CampoMinado(root, 8, 8, 10)
    campo_minado.revelar_adjacentes = MagicMock()

    for i in range(campo_minado.linhas):
        for j in range(campo_minado.colunas):
            if (i, j) != (1, 1):
                campo_minado.tabuleiro[i][j] = 0

    campo_minado.revelar_celula(1, 1)

    assert campo_minado.botoes[1][1]['text'] == '0'

def test_revelar_celula_sem_bomba_com_vizinhos_intermediario():
    root = tk.Tk()
    root.withdraw()
    campo_minado = CampoMinado(root, 10, 16, 30)
    campo_minado.revelar_adjacentes = MagicMock()

    for i in range(campo_minado.linhas):
        for j in range(campo_minado.colunas):
            if (i, j) != (1, 1):
                campo_minado.tabuleiro[i][j] = 0

    campo_minado.revelar_celula(1, 1)

    assert campo_minado.botoes[1][1]['text'] == '0'

    
@pytest.mark.parametrize(" coordenada", [
    ((0, 0)),  
    ((0, 7)),   
    ((7, 0)),
    ((7, 7)),
    ((4, 4)),
    ((7 , 5)),
])
 
def test_revelar_celula_chama_game_over(coordenada):
    root = tk.Tk()
    root.withdraw()
    campo_minado = CampoMinado(root, 8, 8, 0)
    x,y = coordenada
    campo_minado.tabuleiro[x][y] = -1
    
    with patch.object(campo_minado, 'game_over') as mock_game_over:
        campo_minado.revelar_celula(x, y)

        mock_game_over.assert_called_once()

@pytest.mark.parametrize(" coordenada", [
    ((0, 0)),  
    ((0, 15)),   
    ((9, 0)),
    ((9, 15)),
    ((5, 7)),
    ((7 , 5)),
])
 
def test_revelar_celula_chama_game_over_intermediario(coordenada):
    root = tk.Tk()
    root.withdraw()
    campo_minado = CampoMinado(root, 10, 16, 0)
    x,y = coordenada
    campo_minado.tabuleiro[x][y] = -1
    
    with patch.object(campo_minado, 'game_over') as mock_game_over:
        campo_minado.revelar_celula(x, y)

        mock_game_over.assert_called_once()

@pytest.mark.parametrize(" coordenada", [
    ((0, 0)),  
    ((0, 23)),   
    ((23, 0)),
    ((23, 23)),
    ((12, 12)),
    ((7 , 5)),
])
 
def test_revelar_celula_chama_game_over_dificl(coordenada):
    root = tk.Tk()
    root.withdraw()
    campo_minado = CampoMinado(root, 24, 24, 0)
    x,y = coordenada
    campo_minado.tabuleiro[x][y] = -1
    
    with patch.object(campo_minado, 'game_over') as mock_game_over:
        campo_minado.revelar_celula(x, y)

        mock_game_over.assert_called_once()






   