# # test_jogo.py
# import pytest
# import tkinter as tk
# # from ..src.jogo import Jogo

# @pytest.fixture
# def root():
#     return tk.Tk()

# def test_mostrar_tela_inicial(root):
#     jogo = Jogo(root)
#     jogo.mostrar_tela_inicial()
#     # Adicione aqui os asserts para verificar se a tela inicial foi mostrada corretamente
#     assert len(root.winfo_children()) == 4  # Verifica se há 4 widgets

# def test_iniciar_jogo(root):
#     jogo = Jogo(root)
#     jogo.iniciar_jogo(8, 8, 10)
#     # Adicione aqui os asserts para verificar se o jogo foi iniciado corretamente
#     assert len(root.winfo_children()) == 81  # Verifica se há 81 widgets (8x8 + botões de ação)

# def test_on_close(root):
#     jogo = Jogo(root)
#     # Simule o fechamento da janela
#     jogo.on_close()
#     # Adicione aqui os asserts para verificar se o fechamento é tratado corretamente
#     assert root.winfo_children() == []  # Verifica se não há widgets após o fechamento

# def test_reiniciar_jogo(root):
#     jogo = Jogo(root)
#     # Simule o reinício do jogo
#     jogo.reiniciar_jogo()
#     # Adicione aqui os asserts para verificar se o jogo é reiniciado corretamente
#     assert len(root.winfo_children()) == 4  # Verifica se há 4 widgets após o reinício

# def test_ver_historico(root):
#     jogo = Jogo(root)
#     # Simule a visualização do histórico
#     jogo.ver_historico()
#     # Adicione aqui os asserts para verificar se o histórico é exibido corretamente
#     assert len(root.winfo_children()) == 3  # Verifica se há 3 widgets (label, button, messagebox)

import pytest
import tkinter as tk
from src.campo_minado import CampoMinado


@pytest.fixture
def root():
    return tk.Tk()



