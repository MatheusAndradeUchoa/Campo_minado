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
        self.contador_bandeiras = 0
        self.verificar_dimensoes()
        self.tabuleiro = [[0] * colunas for _ in range(linhas)]
        self.botoes = [[None] * colunas for _ in range(linhas)]
        self.criar_tabuleiro()
        self.criar_interface()

    def criar_tabuleiro(self, bomb_positions=None):
        self.tabuleiro = [[0] * self.colunas for _ in range(self.linhas)]
        if bomb_positions is None:
            bomb_positions = self.gerar_posicoes_bombas_aleatorias()

        self.posicionar_bombas_em_posicoes(bomb_positions)

    def gerar_posicoes_bombas_aleatorias(self):
        bomb_positions = set()
        while len(bomb_positions) < self.num_bombas:
            x = random.randint(0, self.linhas - 1)
            y = random.randint(0, self.colunas - 1)
            bomb_positions.add((x, y))
        return list(bomb_positions)

    def posicionar_bombas_em_posicoes(self, positions):
        for x, y in positions:
            if not (0 <= x < self.linhas and 0 <= y < self.colunas):
                raise ValueError("Posição inválida para posicionar a bomba")
            self.tabuleiro[x][y] = -1

                 
    def verificar_dimensoes(self):
        if self.linhas < 8 or self.colunas < 8 or self.linhas > 24 or self.colunas > 24:
            raise ValueError("As dimensões do tabuleiro estao incorretas")
   
    def criar_interface(self):
        global tempo
        tempo = 0
        timer_label = tk.Label(self.root, text='Tempo: 0')
        timer_label.grid(row=0, column=0, columnspan=self.colunas // 2, sticky="nsew")
        self.atualizar_tempo(timer_label) 
        
        bandeiras_label = tk.Label(self.root, text=f'Bandeiras: {self.contador_bandeiras}')
        bandeiras_label.grid(row=0, column=self.colunas // 2, columnspan=self.colunas // 2)
        
        frame_tabuleiro = tk.Frame(self.root)
        frame_tabuleiro.grid(row=1, column=0, columnspan=self.colunas)
        
        for x in range(self.linhas):
            for y in range(self.colunas):
                self.botoes[x][y] = tk.Button(frame_tabuleiro, width=3, height=1, command=lambda x=x, y=y: self.revelar_celula(x, y))
                self.botoes[x][y].grid(row=x, column=y)
                self.botoes[x][y].bind('<Button-1>', lambda event, x=x, y=y: self.on_left_click(x, y))
                self.botoes[x][y].bind('<Button-3>', lambda event, x=x, y=y: self.on_right_click(x, y))
        restart_button = tk.Button(self.root, text="Reiniciar Jogo",command=self.reiniciar_jogo)
        
        restart_button.grid(row=self.linhas, column=0, columnspan=self.colunas // 2, sticky="nsew")
        if self.root:
            exit_button = tk.Button(self.root, text="Sair", command=self.root.quit)
            exit_button.grid(row=self.linhas, column=self.colunas // 2, columnspan=self.colunas // 2, sticky="nsew")
        
      
    def reiniciar_jogo(self):
        for widget in self.root.winfo_children():
            widget.destroy() 
             
        self.criar_tabuleiro()
        self.criar_interface()
    
    def alternar_bandeira(self, x, y):
        if self.botoes[x][y]['text'] == '':
            self.botoes[x][y]['text'] = '🏴'
            self.contador_bandeiras += 1
        else:
            self.botoes[x][y]['text'] = ''
            self.contador_bandeiras -= 1

    def revelar_adjacentes(self, x, y):
        for i in range(-1, 2):
            for j in range(-1, 2):
                novo_x, novo_y = x + i, y + j
                if 0 <= novo_x < self.linhas and 0 <= novo_y < self.colunas:
                    if self.botoes[novo_x][novo_y]['state'] != 'disabled':
                        self.revelar_celula(novo_x, novo_y)

    def atualizar_tempo(self,timer_label):
        global tempo
        tempo += 1
        timer_label.config(text=f'Tempo: {tempo}')
        timer_label.after(1000, lambda: self.atualizar_tempo(timer_label)) 

    def on_left_click(self, x, y):
        if self.root.state() == 'normal':
            self.revelar_celula(x, y)

    def on_right_click(self, x, y):
        if self.root.state() == 'normal':
            self.adicionar_bandeira(x, y)
                
    def on_button_click(self, x, y):
        if self.root.state() == 'normal':
            self.revelar_celula(x, y)

    def revelar_celula(self, x, y):
        if self.tabuleiro[x][y] == -1:
            self.game_over()
        else:
            vizinhos = self.calcular_vizinhos(x, y)
            self.botoes[x][y]['text'] = str(vizinhos)
            self.botoes[x][y]['state'] = 'disabled'

            if vizinhos == 0:
                self.revelar_adjacentes(x, y)

            if self.verificar_vitoria():
                self.vitoria()

    def adicionar_bandeira(self, x, y):
        if self.botoes[x][y]['text'] == '':
            self.botoes[x][y]['text'] = '🏴'
        elif self.botoes[x][y]['text'] == ' 🏴':
            self.botoes[x][y]['text'] = ''
                
    def calcular_vizinhos(self, x, y):
        bomb_count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= x + i < self.linhas and 0 <= y + j < self.colunas:
                    if self.tabuleiro[x + i][y + j] == -1:
                        bomb_count += 1
        return bomb_count
    
    def verificar_vitoria(self):
        # Verifica se todas as células que não são bombas foram reveladas
        for x in range(self.linhas):
            for y in range(self.colunas):
                if self.tabuleiro[x][y] != -1 and self.botoes[x][y]['state'] != 'disabled':
                    return False
        return True

    def vitoria(self):
        user_choice = messagebox.askquestion("Parabéns!", "Você venceu o jogo! Quer jogar novamente?")
        if user_choice == 'yes':
            self.reiniciar_jogo()
        else:
            self.root.destroy()
        
    def game_over(self, mostrar_interface=True):
        for x in range(self.linhas):
            for y in range(self.colunas):
                if self.tabuleiro[x][y] == -1:
                    self.botoes[x][y]['text'] = 'X'
                self.botoes[x][y]['state'] = 'disabled'
                
        if mostrar_interface:
            user_choice = messagebox.askquestion("Fim de Jogo", "Você perdeu!\nDeseja jogar novamente ou sair?")
            if user_choice == 'yes':
                self.reiniciar_jogo()
            else:
                self.root.destroy()