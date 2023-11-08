import tkinter as tk
from tkinter import messagebox
import random
import datetime

from campo_minado import CampoMinado
class Jogo:
    def __init__(self, root):
        self.root = root
        self.root.title('Campo Minado')
        self.mostrar_tela_inicial()

    def mostrar_tela_inicial(self):
        tk.Label(self.root, text="Escolha o nível de dificuldade:").pack(pady=10)

        tk.Button(self.root, text="Fácil", command=lambda: self.iniciar_jogo(8, 8, 10)).pack(pady=5)
        tk.Button(self.root, text="Intermediário", command=lambda: self.iniciar_jogo(10, 16, 30)).pack(pady=5)
        tk.Button(self.root, text="Difícil", command=lambda: self.iniciar_jogo(24, 24, 100)).pack(pady=5)

        tk.Button(self.root, text="Ver Histórico", command=self.ver_historico).pack(pady=10)

    def iniciar_jogo(self, linhas, colunas, bombas):
        for widget in self.root.winfo_children():
            widget.destroy()

        CampoMinado(self.root, linhas, colunas, bombas)
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)


    def on_close(self):
        user_choice = messagebox.askquestion("Sair", "voltar para o menu?")
        if user_choice == 'yes':
          for widget in self.root.winfo_children():
            widget.destroy()
          self.mostrar_tela_inicial()
           
        else:
           self.root.destroy()
            
    def reiniciar_jogo(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        CampoMinado.criar_tabuleiro()
        
        

    def ver_historico(self):
        messagebox.showinfo("Histórico de Resultados", "Aqui está o histórico de resultados:\n\n"
                                                        "Data e Hora: {}\n"
                                                        "Nível: {}\n"
                                                        "Resultado: {}".format(datetime.datetime.now(), "Nível do Jogo", "Resultado do Jogo"))
