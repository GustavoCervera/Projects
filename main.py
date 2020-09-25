# -*- coding: utf-8 -*-
"""
Codigo para calculadora simples
utilizado para treinamento de 
interface TKinter com Python

Autor: Gustavo Zacarias Cervera

Data: 25-09-2020
"""
from funcoes_calculadora import *

def main():
    janela = criar_janela()
    titulo = criar_titulo(janela)
    display = criar_display(janela)
    r = 2
    c = 0
    botoes = ["7","8","9","/",
              "4","5","6","*",
              "1","2","3","+",
              ".","0","00","-"]
    for botao in botoes:
        criar_botoes(janela, botao, r, c, display)
        c += 1
        if c == 4:
            c = 0
            r += 1
    criar_botoes_controle(janela,display)
        
    
    janela.mainloop()
    
    
main()
