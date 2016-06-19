# -*- coding: utf-8 -*-
import time
import sys
from tkinter import *
import tkinter.simpledialog
import tkinter.messagebox
import random

def calc():
    calc.a = time.time()
def calcc():
    calcc.b = time.time()

def inserter(c):
    """ Inserts specified value into text widget """
    output.delete("0.0","end")
    output.insert("0.0",c)
def runtime():
    c = calcc.b - calc.a
    print(c)
    c_val = int(c)
    inserter(c_val)

def handler():
        c_val = float(c.get())
        inserter(runtime(c_val))


root = Tk()
root.title("Time calculator")

root.minsize(200,50)
root.resizable(width=False, height=False)
frame = Frame(root)
frame.grid()
but = Button(root, text="Начало работы", width=15,height=2,bg="white",fg="blue", command = calc).grid(row=1, column=7, padx=(10,0) )

butt = Button(root, text="Конец работы", width=15,height=2,bg="white",fg="blue", command = calcc).grid(row=1, column=8, padx=(10,0) )

buttt = Button(root, text="Вывод результата", width=15,height=2,bg="white",fg="blue", command =runtime ).grid(row=1, column=9, padx=(10,0) )
a_lab = Label(frame, text="Результат").grid(row=1,column=2)
output = Text(frame, bg="lightblue", font="Arial 12", width=10, height=1)
output.grid(row=2, columnspan=8)




root.mainloop()