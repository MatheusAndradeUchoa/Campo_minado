import time
import tkinter as tk

from src.campo_minado import CampoMinado


def test_atualizar_tempo():
    root = tk.Tk()
    campo_minado = CampoMinado(root, 8, 8, 10)
    timer_label = tk.Label(root, text='Tempo: 0')
    
    campo_minado.atualizar_tempo(timer_label)
    
    # Aguarde um pouco (por exemplo, 2 segundos) para garantir que o texto tenha sido atualizado
    time.sleep(2)
    
    # Agora, verifique se o texto foi atualizado corretamente
    assert timer_label.cget("text") == 'Tempo: 2' 