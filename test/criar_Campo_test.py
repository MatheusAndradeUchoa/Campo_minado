import pytest
from main import CampoMinado  


def test_criar_tabuleiro_facil():
   
    campo_minado = CampoMinado(None, 8, 8, 10)
    
    # Verifica se o tabuleiro foi criado corretamente
    assert len(campo_minado.tabuleiro) == 8
    assert len(campo_minado.tabuleiro[0]) == 8

def test_criar_tabuleiro_intermediario():
  
    campo_minado = CampoMinado(None, 10, 16, 30)
    
    # Verifica se o tabuleiro foi criado corretamente
    assert len(campo_minado.tabuleiro) == 10
    assert len(campo_minado.tabuleiro[0]) == 16
    


def test_criar_tabuleiro_tamanho_invalido():
    with pytest.raises(ValueError):
       
        CampoMinado(None, 7, 7, 10)

def test_posicoes_bombas():
    
    campo_minado = CampoMinado(None, 8, 8, 4)

    
    campo_minado.tabuleiro[0][0] = -1
    campo_minado.tabuleiro[1][1] = -1
    campo_minado.tabuleiro[2][2] = -1
    campo_minado.tabuleiro[3][3] = -1
    
    assert campo_minado.tabuleiro[0][0] == -1
    assert campo_minado.tabuleiro[1][1] == -1
    assert campo_minado.tabuleiro[2][2] == -1
    assert campo_minado.tabuleiro[3][3] == -1
            
if __name__ == "__main__":
    pytest.main()

