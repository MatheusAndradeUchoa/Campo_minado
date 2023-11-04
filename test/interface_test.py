import tkinter as tk
import pytest
from unittest.mock import Mock, patch
from src.campo_minado import CampoMinado  


def test_vitoria_yes():
    root = tk.Tk()
    campo_minado = CampoMinado(root, 8, 8, 10)
    campo_minado.reiniciar_jogo = Mock()
    with patch("tkinter.messagebox.askquestion", return_value="yes")as mock_askquestion:
        campo_minado.vitoria()
    
    mock_askquestion.assert_called_once_with("Parabéns!", "Você venceu o jogo! Quer jogar novamente?")
    assert campo_minado.reiniciar_jogo.called

def test_vitoria_no():
    root = tk.Tk()
    campo_minado = CampoMinado(root, 8, 8, 10)
    campo_minado.root.destroy = Mock()
    with patch("tkinter.messagebox.askquestion", return_value="no")as mock_askquestion:
        campo_minado.vitoria()
    
    mock_askquestion.assert_called_once_with("Parabéns!", "Você venceu o jogo! Quer jogar novamente?")
    assert campo_minado.root.destroy.called

def test_game_over_yes():
    root = tk.Tk()
    campo_minado = CampoMinado(root, 8, 8, 10)
    campo_minado.reiniciar_jogo = Mock()
    with patch("tkinter.messagebox.askquestion", return_value="yes")as mock_askquestion:
       
        campo_minado.game_over()
    
    
    mock_askquestion.assert_called_once_with("Fim de Jogo", "Você perdeu!\nDeseja jogar novamente ou sair?")
    
   
    campo_minado.reiniciar_jogo.assert_called_once()

def test_game_over_no():
    root = tk.Tk()
    campo_minado = CampoMinado(root, 8, 8, 10)
    campo_minado.root.destroy = Mock()
    with patch("tkinter.messagebox.askquestion", return_value="no")as mock_askquestion:
       
        campo_minado.game_over()
    
    
    mock_askquestion.assert_called_once_with("Fim de Jogo", "Você perdeu!\nDeseja jogar novamente ou sair?")
    
   
    campo_minado.root.destroy.assert_called_once()

