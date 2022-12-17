from tkinter import *
from tkinter import ttk


root = Tk()
root.title("ЧМФ")
root.geometry("300x300")

label = ttk.Label(text="Программка")
label.pack()
def y():
    window = Toplevel()
    window.title("Статистика Команд")
    window.geometry("250x200")
    label = ttk.Label(window,text="Статистика Команд")
    label.pack()
    close_button = ttk.Button(window, text="Закрыть окно", command=lambda: dismiss(window))
    close_button.pack(expand=True, ipadx=10, ipady=10)
    window.grab_set()


btn = ttk.Button(text="Статистика Команд", command=y)
btn.pack(expand=True, ipadx=10, ipady=10)

def dismiss(window):
    window.grab_release()
    window.destroy()


brazil = [["Сербия",0,2],["Швейцария",0,1],["Камерун",1,0]]
def click():
    window = Toplevel()
    window.title("Результаты Матчей Команд")
    window.geometry("300x300")

    Label = ttk.Label(window,text="Результаты Матчей Команд")
    Label.pack()

    def selected(event, ):
        selection = a.get()


        match selection:
            case "Бразилия":
                editor = Text(window, height=50)
                editor.pack()
                brazil1 =  "Сербия 0:2 Бразилия - Победа\nШвейцария 0:1 Бразилия - Победа\nКамерун 1:0 Бразилия - Поражение"
                editor.insert("1.0", f"{brazil1}")
            case "Сербия":
                serbia = "Баризилия 2:0 Сербия - Поражение\nКамерун, 3:3 Сербия - Ничья\nШвецария 3:2 Сербия - Поражение"
                label = ttk.Label(window,text=f"{serbia}", font=("Arial", 14))
                label.pack()
            #case "Швейцария":

            #case "Камерун":

            #case "Гана":

            #case "Уругвай":

            #case "Южная Корея":

            #case "Португалия":

            #case  "Сенегал":

            #case "Эквадор":

            #case "Катар":

            #case "Нидерланды":

            #case "Иран":

            #case "США":

            #case "Уэльс":

            #case "Англия":

            #case "Саудовская Аравия":

            #case "Мексика":

            #case "Польша":

            #case "Аргентина":

            #case 'Австралия':

            #case 'Дания':

            #case 'Тунис':

            #case 'Франция':

            #case 'Германия':

           # case 'Коста-рика':









    fotball = ["Сербия","Швейцария","Камерун","Бразилия","Гана","Уругвай","Южная Корея","Португалия",
               "Сенегал","Эквадор","Катар","Нидерланды","Иран","США","Уэльс","Англия","Саудовская Аравия",
               "Мексика","Польша","Аргентина",'Австралия','Дания','Тунис','Франция','Германия','Коста-рика',
               'Испания','Япония','Хорватия','Бельгия','Канада','Морокко',]
    a = ttk.Combobox(window,values=fotball,state="readonly")
    a.pack(anchor=NW, fill=X, padx=5, pady=5)
    a.bind("<<ComboboxSelected>>", selected)

    close_button = ttk.Button(window, text="Закрыть окно", command=lambda: dismiss(window))
    close_button.pack(expand=True, ipadx=1, ipady=1)
    window.grab_set()
    return 0




btn = ttk.Button(text="Результаты Матчей Команд", command=click)
btn.pack(expand=True, ipadx=10, ipady=10)
btn.pack()



def z():
    editor = Text()
    editor.pack(fill=BOTH, expand=1)
    editor.insert("1.0", "")
btn = ttk.Button(text="Рейтинг по пропущенным и забитым", command=z)
btn.pack(expand=True, ipadx=10, ipady=10)
root.mainloop()


#группа G
brazil = [["Сербия",0,2.],["Швейцария",0,1.],["Камерун",1,0.]]
switzerlan = [["Камерун", 0, 1], ["Бразилия", 1, 0], ["Сербия", 2, 3]]
cameroon = [["Швейцария", 1, 0], ["Сербия", 3, 3], ["Бразилия", 0, 1]]
serbia = "Баризилия 2:0 Сербия - поражение\nКамерун, 3:3 Сербия - Ничья\nШвецария 3:2 Сербия - Поражение"



#группа H
portugal= [["Гана", 2, 3], ["Уругвай", 0, 2], ["Южная Корея", 2, 1]]
south_korea = [["Уругвай", 0, 0], ["Гана", 3, 2], ["Португалия", 1, 2]]
uruguay = [["Южная Корея", 0, 0], ["Португалия", 2, 0], ["Гана", 0, 2]]
gana = [["Португалия", 3, 2], ["Южная Корея", 2, 3], ["Уругвай", 2, 0]]


netherlands = [["Сенегал",0,2],["Эквадор", 1, 1],["Катар", 0, 2]]
senegal = [["Нидерланды",2,0],["Катар", 1, 3],["Эквадор", 1, 2]]
ecuador = [["Катар", 0, 2],["Нидерланды", 1, 1],["Сенегал", 1, 2]]
qatar = [["Эквадор", 2, 0],["Сенегал", 3, 1],["Нидерланды", 2, 0]]
england = [["Иран", 2, 6],["США", 0, 0],["Уэльс", 0, 3]]
usa = [["Уэльс", 1, 1],["Англия", 0, 0],["Иран", 0, 1]]
iran = [["Англия", 6, 2],["Уэльс", 0, 2],["США", 1, 0]]
wales = [["США", 1, 1],["Иран", 2, 0],["Англия", 3, 0]]
argentina = [["Саудовская Аравия", 2, 1],["Мексика", 0, 2],["Польша", 0, 2]]
poland = [["Мексика", 0, 0],["Саудовская Аравия", 0, 2],["Аргентина", 2, 0]]
mexico = [["Польша", 0, 0],["Аргентина", 2, 0],["Саудовская Аравия", 1, 2]]
saudi_arabia = [["Аргентина", 1, 2],["Польша", 2, 0],["Мексика", 2, 1]]


# D
france = [['Австралия', 1, 4], ['Дания', 1, 2], ['Тунис', 0, 1]]
australia = [['Франция', 4, 1], ['Тунис', 0, 1], ['Дания', 0, 1]]
tunis = [['Дания', 0, 0], ['Австралия', 1, 0], ['Франция', 0, 1]]
denmark = [['Тунис', 0, 0], ['Франция', 2, 1], ['Австралия', 1, 0]]

# E
japan = [['Германия', 1, 2], ['Коста-рика', 1, 0], ['Испания', 1, 2]]
spain = [['Коста-рика', 0, 7], ['Германия', 1, 1], ['Япония', 2, 1]]
germany = [['Япония', 2, 1], ['Испания', 1, 1], ['Коста-рика', 2, 4]]
kostarika = [['Испания', 7, 0], ['Япония', 0, 1], ['Германия', 4, 2]]

# F


morocco = [['Хорватия', 0, 0], ['Бельгия', 0, 2], ['Канада', 1, 2]]
Croatia = [['Морокко', 0, 0], ['Канада', 1, 4], ['Бельгия', 0, 0]]
Belgium = [['Канада', 0, 1], ['Морокко', 2, 0], ['Хорватия', 0, 0]]
Canada = [['Бельгия', 1, 0], ['Ховатия', 4, 1], ['Марокко', 2, 1]]
#case "Швейцария":

            #case "Камерун":

            #case "Гана":

            #case "Уругвай":

            #case "Южная Корея":

            #case "Португалия":

            #case  "Сенегал":

            #case "Эквадор":

            #case "Катар":

            #case "Нидерланды":

            #case "Иран":

            #case "США":

            #case "Уэльс":

            #case "Англия":

            #case "Саудовская Аравия":

            #case "Мексика":

            #case "Польша":

            #case "Аргентина":

            #case 'Австралия':

            #case 'Дания':

            #case 'Тунис':

            #case 'Франция':

            #case 'Германия':

           # case 'Коста-рика':
                #editor = Text(window, height=50)
                #editor.pack()
                #brazil1 =  "Сербия 0:2 Бразилия - Победа\nШвейцария 0:1 Бразилия - Победа\nКамерун 1:0 Бразилия - Поражение"
                #editor.insert("1.0", f"{brazil1}")

