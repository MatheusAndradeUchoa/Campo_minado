import tkinter as tk
import pytest
from src.campo_minado import CampoMinado
 
@pytest.mark.parametrize("linha,coluna", [
    (8, 8),  
    (10, 16),  
    (24, 24),  
])  
#rmv
def test_adicionar_bandeira_em_diferentes_niveis(linha,coluna):
    campo_minado = CampoMinado(None, linha, coluna, 10)
    campo_minado.botoes[0][0] = {'text': ''}

   
    campo_minado.alternar_bandeira(0, 0)
    assert campo_minado.botoes[0][0]['text'] == '🏴'


@pytest.mark.parametrize("linha, coluna, nivel, coordenada", [
    (8, 8, 10, (2, 3)),  
    (10, 16, 30, (3, 2)),   
    (24, 24, 100, (4, 5)),
    (8, 8 ,10,(7 , 5)),
    (24, 24, 100, (12, 12)),
    (10, 16 ,30,(6 , 8)),
    (8, 8 ,30,(3, 5)),
    (10, 16 ,30,(8 , 5)),
    (24, 24 ,30,(23 , 10)),
])
def test_adicionar_bandeira(linha, coluna, nivel, coordenada):
    campo_minado = CampoMinado(None, linha, coluna, nivel)
    x, y = coordenada
    campo_minado.alternar_bandeira(x, y)
    assert campo_minado.botoes[x][y]['text'] == '🏴'

# Teste para remover bandeira em diferentes posições e níveis
@pytest.mark.parametrize("linha, coluna, nivel, coordenada", [
    (8, 8, 10, (2, 3)),  
    (10, 16, 30, (3, 2)),   
    (24, 24, 100, (4, 5)),
    (8, 8 ,10,(7 , 5)),
    (24, 24, 100, (12, 12)),
    (10, 16 ,30,(6 , 8)),
    (8, 8 ,30,(3, 5)),
    (10, 16 ,30,(8 , 5)),
    (24, 24 ,30,(23 , 10)),
])
def test_remover_bandeira(linha, coluna, nivel, coordenada):
    campo_minado = CampoMinado(None, linha, coluna, nivel)
    x, y = coordenada
    campo_minado.botoes[x][y]['text'] = '🏴'
    campo_minado.alternar_bandeira(x, y)
    assert campo_minado.botoes[x][y]['text'] == ''
    
    


def test_contador_bandeiras_inicial():
   
    campo_minado = CampoMinado(None, 8, 8, 10)

    assert campo_minado.contador_bandeiras == 0


def test_remover_bandeira():
    root = tk.Tk()
    campo_minado = CampoMinado(root, 8, 8, 10)

   
    campo_minado.alternar_bandeira(2, 2)

   
    campo_minado.alternar_bandeira(2, 2)
    
    assert campo_minado.contador_bandeiras == 0

def test_limite_contador_bandeiras():
    root = tk.Tk()
    campo_minado = CampoMinado(root, 8, 8, 10)

    
    for x in range(8):
        for y in range(8):
            campo_minado.alternar_bandeira(x, y)

    
    campo_minado.alternar_bandeira(0, 0)

    
    assert campo_minado.contador_bandeiras == 63

   
def test_adicionar_bandeira():
    
    campo_minado = CampoMinado(None, 8, 8, 10)

    
    campo_minado.alternar_bandeira(2, 2)

   
    assert campo_minado.contador_bandeiras == 1