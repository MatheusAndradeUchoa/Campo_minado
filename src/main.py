import tkinter as tk
from tkinter import messagebox
import random
import datetime

class CampoMinado:
    def __init__(self, root, linhas, colunas, num_bombas):
        self.root = root
        self.linhas = linhas
        self.colunas = colunas 
        self.num_bombas = num_bombas
        self.verificar_dimensoes()
        self.tabuleiro = [[0] * colunas for _ in range(linhas)]
        self.botoes = [[None] * colunas for _ in range(linhas)]
        self.criar_tabuleiro()
        self.criar_interface()

    def criar_tabuleiro(self):
        bombas_adicionadas = 0
        while bombas_adicionadas < self.num_bombas:
            x = random.randint(0, self.linhas - 1)
            y = random.randint(0, self.colunas - 1)

            if self.tabuleiro[x][y] != -1:
                self.tabuleiro[x][y] = -1
                bombas_adicionadas += 1
   