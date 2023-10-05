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
                 
    def verificar_dimensoes(self):
        if self.linhas < 8 or self.colunas < 8 or self.linhas > 64 or self.colunas > 64:
            raise ValueError("As dimensões do tabuleiro estao incorretas")
   
    def criar_interface(self):
        for x in range(self.linhas):
            for y in range(self.colunas):
                self.botoes[x][y] = tk.Button(self.root, width=3, height=1, command=lambda x=x, y=y: self.revelar_celula(x, y))
                self.botoes[x][y].grid(row=x, column=y)
                
    def revelar_celula(self, x, y):
        if self.tabuleiro[x][y] == -1:
            self.game_over()
        else:
            vizinhos = self.calcular_vizinhos(x, y)
            self.botoes[x][y]['text'] = str(vizinhos)
            self.botoes[x][y]['state'] = 'disabled'
            # Após revelar uma célula, verificamos se o jogador venceu
            if self.verificar_vitoria():
                self.vitoria()
                
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
        messagebox.showinfo("Parabéns!", "Você venceu o jogo!")
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
                self.root.destroy()  # Fecha a janela atual e voltará para a tela de escolha de níveis
            else:
                self.root.destroy()  # Fecha a janela e encerra o jogo

   
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

        self.jogo = CampoMinado(self.root, linhas, colunas, bombas)
        self.root.geometry(f"{colunas*30}x{linhas*30}")
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        user_choice = messagebox.askquestion("Sair", "Deseja sair do jogo?")
        if user_choice == 'yes':
            self.root.destroy()
        else:
            self.mostrar_tela_inicial()

    def ver_historico(self):
        messagebox.showinfo("Histórico de Resultados", "Aqui está o histórico de resultados:\n\n"
                                                        "Data e Hora: {}\n"
                                                        "Nível: {}\n"
                                                        "Resultado: {}".format(datetime.datetime.now(), "Nível do Jogo", "Resultado do Jogo"))

if __name__ == "__main__":
    root = tk.Tk()
    jogo = Jogo(root)
    root.mainloop()
