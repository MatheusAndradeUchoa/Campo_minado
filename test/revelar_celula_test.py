
import pytest
from src.main import CampoMinado
from unittest.mock import MagicMock, patch

def test_revelar_celula():
    campo_minado = CampoMinado(None, 8, 8, 10)
    
   # botoes = [['disabled'] * campo_minado.colunas for _ in range(campo_minado.linhas)]
    
    campo_minado.revelar_celula(0, 2)  
    
    vizinhos_esperados = campo_minado.calcular_vizinhos(0, 2)  
    assert campo_minado.botoes[0][2]['text'] == str(vizinhos_esperados) 



   