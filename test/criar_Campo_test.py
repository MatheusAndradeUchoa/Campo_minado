import pytest
from main import CampoMinado  


def test_criar_tabuleiro_facil():
   
    campo_minado = CampoMinado(None, 8, 8, 10)
    
    # Verifica se o tabuleiro foi criado corretamente
    assert len(campo_minado.tabuleiro) == linhas
    assert len(campo_minado.tabuleiro[0]) == colunas

def test_criar_tabuleiro_intermediario():
    root = None
    linhas = 10
    colunas = 16
    num_bombas = 30
    campo_minado = CampoMinado(root, linhas, colunas, num_bombas)
    
    # Verifica se o tabuleiro foi criado corretamente
    assert len(campo_minado.tabuleiro) == linhas
    assert len(campo_minado.tabuleiro[0]) == colunas
    

def test_verificar_bombas_facil():
    root = None
    linhas = 8
    colunas = 8
    num_bombas = 10
    campo_minado = CampoMinado(root, linhas, colunas, num_bombas)

    # Verifica se o número correto de bombas foi adicionado
    bomb_count = sum(row.count(-1) for row in campo_minado.tabuleiro)
    assert bomb_count == num_bombas

def test_verificar_bombas_intermediario():
    root = None
    linhas = 10
    colunas = 16
    num_bombas = 30
    campo_minado = CampoMinado(root, linhas, colunas, num_bombas)

    # Verifica se o número correto de bombas foi adicionado
    bomb_count = sum(row.count(-1) for row in campo_minado.tabuleiro)
    assert bomb_count == num_bombas

def test_verificar_bombas_dificil():
    root = None
    linhas = 24
    colunas = 24
    num_bombas = 100
    campo_minado = CampoMinado(root, linhas, colunas, num_bombas)

    # Verifica se o número correto de bombas foi adicionado
    bomb_count = sum(row.count(-1) for row in campo_minado.tabuleiro)
    assert bomb_count == num_bombas

def test_criar_tabuleiro_tamanho_invalido():
    with pytest.raises(ValueError):
        root = None
        linhas = 7
        colunas = 7
        num_bombas = 10
        CampoMinado(root, linhas, colunas, num_bombas)

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
    
    
    
def test_game_over_no_interface():
    # Criar uma instância de CampoMinado com dimensões 8x8 e 1 bomba
    root = None
    linhas = 8
    colunas = 8
    num_bombas = 1
    campo_minado = CampoMinado(root, linhas, colunas, num_bombas)

    # Colocar uma bomba em uma célula (0, 0)
    campo_minado.tabuleiro[0][0] = -1

    # Chamar a função game_over sem exibir a interface
    campo_minado.game_over(mostrar_interface=False)

    # Verificar se os botões foram desativados e marcados com 'X'
    assert campo_minado.botoes[0][0]['text'] == 'X'
    assert campo_minado.botoes[0][0]['state'] == 'disabled'
    

          
if __name__ == "__main__":
    pytest.main()

