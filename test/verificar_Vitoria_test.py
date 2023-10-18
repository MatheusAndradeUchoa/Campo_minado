from unittest.mock import patch
import pytest

from src.campo_minado import CampoMinado
 

def test_verificar_vitoria():
    campo_minado = CampoMinado(None, 8, 8, 4)

    campo_minado.tabuleiro[0][0] = -1
    campo_minado.tabuleiro[1][1] = -1
    campo_minado.tabuleiro[2][2] = -1
    campo_minado.tabuleiro[3][3] = -1

    for i in range(8):
        for j in range(8):
            if campo_minado.tabuleiro[i][j] != -1:
                campo_minado.botoes[i][j]['state'] = 'disabled'

    assert campo_minado.verificar_vitoria() == True

def test_verificar_vitoria_intermediario():
    campo_minado = CampoMinado(None, 10, 16, 30)

  
    for i in range(10):
        for j in range(16):
            if campo_minado.tabuleiro[i][j] != -1:
                campo_minado.botoes[i][j]['state'] = 'disabled'

    assert campo_minado.verificar_vitoria() == True


def test_verificar_vitoria_dificil():
    campo_minado = CampoMinado(None, 24, 24, 100)

  
    for i in range(24):
        for j in range(24):
            if campo_minado.tabuleiro[i][j] != -1:
                campo_minado.botoes[i][j]['state'] = 'disabled'

    assert campo_minado.verificar_vitoria() == True

def test_verificar_vitoria_dificil_sem_bombas_facil():
    campo_minado = CampoMinado(None, 8, 8, 0)

  
    for i in range(8):
        for j in range(8):
            if campo_minado.tabuleiro[i][j] != -1:
                campo_minado.botoes[i][j]['state'] = 'disabled'

    assert campo_minado.verificar_vitoria() == True

def test_verificar_vitoria_dificil_sem_bombas_intermediario():
    campo_minado = CampoMinado(None, 10, 16, 0)

  
    for i in range(10):
        for j in range(16):
            if campo_minado.tabuleiro[i][j] != -1:
                campo_minado.botoes[i][j]['state'] = 'disabled'

    assert campo_minado.verificar_vitoria() == True

def test_verificar_vitoria_dificil_sem_bombas_dificil():
    campo_minado = CampoMinado(None, 24, 24, 0)

  
    for i in range(24):
        for j in range(24):
            if campo_minado.tabuleiro[i][j] != -1:
                campo_minado.botoes[i][j]['state'] = 'disabled'

    assert campo_minado.verificar_vitoria() == True

#somente bomba
def test_verificar_vitoria_dificil_apenas_bombas_facil():
    campo_minado = CampoMinado(None, 8, 8, 64)

  
    for i in range(8):
        for j in range(8):
            if campo_minado.tabuleiro[i][j] != -1:
                campo_minado.botoes[i][j]['state'] = 'disabled'

    assert campo_minado.verificar_vitoria() == True

def test_verificar_vitoria_dificil_apenas_bombas_intermediario():
    campo_minado = CampoMinado(None, 10, 16, 16)

  
    for i in range(10):
        for j in range(16):
            if campo_minado.tabuleiro[i][j] != -1:
                campo_minado.botoes[i][j]['state'] = 'disabled'

    assert campo_minado.verificar_vitoria() == True

def test_verificar_vitoria_dificil_apenas_bombas_dificil():
    campo_minado = CampoMinado(None, 24, 24, 576)

  
    for i in range(24):
        for j in range(24):
            if campo_minado.tabuleiro[i][j] != -1:
                campo_minado.botoes[i][j]['state'] = 'disabled'

    assert campo_minado.verificar_vitoria() == True


 
