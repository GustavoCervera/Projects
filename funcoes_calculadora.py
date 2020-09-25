# -*- coding: utf-8 -*-
"""
Codigo para calculadora simples
utilizado para treinamento de 
interface TKinter com Python

Autor: Gustavo Zacarias Cervera

Data: 25-09-2020
"""

from tkinter import *
#from functools import partial

def criar_janela():
    janela = Tk()
    janela.resizable(False, False)
    janela.title("Calculadora Simples")
    janela.config(bg="gray")
    janela.geometry("400x550+100+100")
    
    return janela

def criar_titulo(janela):
    fonte = 'Verdana 19 bold'
    titulo = Label(janela,
                   text="CALCULADORA SIMPLES",
                   bg="gray",
                   fg="white",
                   font=fonte,
                   anchor = "n",
                   justify = "center")
    titulo.grid(row=0, column=0, columnspan = 5)
    return titulo

def criar_display(janela):
    fonte = 'Verdana 16'
    display = Entry(janela,
                    font = fonte,
                    justify="center",
                    width=31)
    display.grid(row=1, column=0, columnspan = 5)
    return display

def criar_botoes(janela, botao, r, c, display):
    fonte = 'Verdana 16 bold'
    bt = Button(janela,
                text=botao,
                bd = 4,
                font = fonte,
                height = 2,
                width = 5,
                command = lambda: valor_botao(janela,botao,display)
                )
    bt.grid(row=r, column=c)
    return bt

def criar_botoes_controle(janela, display):
    fonte = 'Verdana 16 bold'
    bt_c = Button(janela,
                text = "C",
                bd = 4,
                font = fonte,
                height = 2,
                width = 5,
                command = lambda: valor_botao(janela,"C",display)
                )
    bt_igual = Button(janela,
                text = "=",
                bd = 4,
                font = fonte,
                height = 2,
                width = 5,
                command = lambda: valor_botao(janela,"=",display)
                )
    bt_igual.grid(row=6,column=0,columnspan=4,sticky="w,e")
    bt_c.grid(row=8,column=0,columnspan=4,sticky="w,e")
    
    
def valor_botao(janela, botao, display):
    if botao == "C":
        display.delete(0,END)
    elif botao == "=":
        realizar_calculo(janela, display)
    else:
        display.insert(END, botao)
    
def realizar_calculo(janela, display):
    try:
        resultado = eval(display.get())
        display.delete(0,END)
        display.insert(END,resultado)
    except:
        display.delete(0,END)
        display.insert(END,"VALORES INVALIDOS")