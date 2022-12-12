from tkinter import *
from tkinter import ttk
root = Tk()
root.title("ЧМФ")
root.geometry("350x300")
clicks = 0
label = ttk.Label(text="Программка")
label.pack()
def y():
    editor = Text()
    editor.pack(fill=BOTH, expand=1)
    editor.insert("1.0", "Hello World")
btn = ttk.Button(text="Статистика Команд", command=y)
btn.pack()
btn.pack(expand=True, ipadx=10, ipady=10)

def click():
    editor = Text()
    editor.pack(fill=BOTH, expand=1)
    editor.insert("1.0", "Hello World")
btn = ttk.Button(text="Результаты Матчей Команд", command=click )
btn.pack(expand=True, ipadx=10, ipady=10)
btn.pack()
def z():
    editor = Text()
    editor.pack(fill=BOTH, expand=1)
    editor.insert("1.0", "")
btn = ttk.Button(text="Результаты Матчей Команд", command=z)
btn.pack(expand=True, ipadx=10, ipady=10)
root.mainloop()


#группа G
brazil = [["Сербия",0,2],["Швейцария",0,1],["Камерун",1,0]]
switzerlan = [["Камерун", 0, 1], ["Бразилия", 1, 0], ["Сербия", 2, 3]]
cameroon = [["Швейцария", 1, 0], ["Сербия", 3, 3], ["Бразилия", 0, 1]]
serbia = [["Баризилия", 2, 0], ["Камерун", 3, 3], ["Швецария", 3, 2]]
#группа H
portugal= [["Гана", 2, 3], ["Уругвай", 0, 2], ["Южная Корея", 2, 1]]
south_korea = [["Уругвай", 0, 0], ["Гана", 3, 2], ["Португалия", 1, 2]]
uruguay = [["Южная Корея", 0, 0], ["Португалия", 2, 0], ["Гана", 0, 2]]
gana = [["Португалия", 3, 2], ["Южная Корея", 2, 3], ["Уругвай", 2, 0]]
