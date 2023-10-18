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
    (10, 16 ,30,(7 , 5)),
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
    (10, 16 ,30,(7 , 5)),
])
def test_remover_bandeira(linha, coluna, nivel, coordenada):
    campo_minado = CampoMinado(None, linha, coluna, nivel)
    x, y = coordenada
    campo_minado.botoes[x][y]['text'] = '🏴'
    campo_minado.alternar_bandeira(x, y)
    assert campo_minado.botoes[x][y]['text'] == ''




   
