import pytest
import tkinter as tk

from src.campo_minado import CampoMinado


@pytest.fixture
def root():
    return tk.Tk()



def obter_combinacoes_dimensoes():
    # Defina as combinações de linhas e colunas para diferentes níveis
    dimensoes = {
        'facil': (8, 8),
        'intermediario': (10, 16),
        'dificil': (24, 24)
    }
    return dimensoes.items()

@pytest.mark.parametrize("nivel, dimensoes", obter_combinacoes_dimensoes())
def test_criar_linhas_tabuleiro(nivel, dimensoes,root):
    linhas, colunas = dimensoes
    campo_minado = CampoMinado(None, linhas, colunas, 10)  

    assert len(campo_minado.tabuleiro) == linhas

@pytest.mark.parametrize("nivel, dimensoes", obter_combinacoes_dimensoes())
def test_criar_colunas_tabuleiro(nivel, dimensoes):
    linhas, colunas = dimensoes
    campo_minado = CampoMinado(None, linhas, colunas, 10)  

    assert len(campo_minado.tabuleiro[0]) == colunas


@pytest.mark.parametrize("linhas, colunas",[(8,7),(7,8),(10,7),(7,16),(25,24),(24,25)])
def test_criar_tabuleiro_tamanho_invalido_facil(linhas,colunas):
    with pytest.raises(ValueError):   
        CampoMinado(None, linhas, colunas, 10)




#teste criar interface no modo dificil
# def test_criar_interface_nivel_dificil():
#     root = tk.Tk()
#     jogo = Jogo(root)
#     jogo.iniciar_jogo(24, 24, 100)
    
#     assert jogo.jogo.linhas == 24
#     assert jogo.jogo.colunas == 24
#     assert jogo.jogo.num_bombas == 100

#     root.destroy()


            
if __name__ == "__main__":
    pytest.main()

