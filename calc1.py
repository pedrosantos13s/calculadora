from tkinter import *

# Funções


def btnNumClick(number):
    main_input.insert(len(main_input.get()), str(number))
    return

## select_present()
## If there is a selection, returns true, else returns false.


madjust = 1
dadjust = 1
muadjust = 1
j = 0
m = ";"
def btnActionClick(action):
    global j 
    global m
    global madjust
    global dadjust
    global muadjust
    if action == "C":
        main_input.delete(0, len(main_input.get()))
        j=0
## SOMA ###############
    if action == "+":
        if m == "=":
            j = float(main_input.get())
            main_input.delete(0, len(main_input.get()))
            m = "+"
            return
        j = j + float(main_input.get())
        main_input.delete(0, len(main_input.get()))
        m = "+"
        #print("+")
        #print(j)
## SUBTRAÇÃO ###############
    if action == "-":
        if madjust == 1:
            j = 2 * float(main_input.get())
            madjust = 0
        #print(j)
        j = j - float(main_input.get())
        main_input.delete(0, len(main_input.get()))
        m = "-"
        #print("-")
        #print(j)
## DIVISÃO ######################
    if action == "/":
        if dadjust == 1:
            j = float(main_input.get()) * float(main_input.get())
            dadjust = 0
        j = j / float(main_input.get())
        main_input.delete(0, len(main_input.get()))
        m = "/"
        #print("/")
        #print(j)
## MULTIPLICAÇÃO #################
    if action == "*":
        if muadjust == 1:
            j = 1
            muadjust = 0
        j = j * float(main_input.get())
        main_input.delete(0, len(main_input.get()))
        m = "*"
        #print("*")
        #print(j)
    if action == "clear":
        main_input.delete(len(main_input.get())-1, )
## IGUALDADE ################
    if action == "=":
        madjust=1
        dadjust=1
        muadjust=1
        if m == "+":
            j = j + float(main_input.get())
            main_input.delete(0, len(main_input.get()))
        if m == "-":
            #print(j)
            j = j - float(main_input.get())
            main_input.delete(0, len(main_input.get()))
        if m == "/":
            #print(j)
            j = j / float(main_input.get())
            main_input.delete(0, len(main_input.get()))
        if m == "*":
            #print(j)
            j = j * float(main_input.get())
            main_input.delete(0, len(main_input.get()))
        main_input.insert(len(main_input.get()), str(j))
        m = "="
        #print("=")
        #print(j)
    return


# Criar uma janela
window = Tk()

# Título para janela
window.title("Calculadora")

# Input Area
main_input = Entry(window)

# Butões Numéricos
i = 0
while i < 10:
    btn = Button(window,
                 text=str(i),
                 padx=21,
                 pady=7,
                 command=lambda k=i: btnNumClick(k))

    if (i == 0):
        btn.grid(row=5, column=1)
    elif (i <= 3):
        btn.grid(row=4, column=i-1)
    elif (i <= 6):
        btn.grid(row=3, column=i-4)
    else:
        btn.grid(row=2, column=i-7)

    i += 1

# Botões de Ação
btn_c = Button(window, text="C", padx=21, pady=7,
               command=lambda: btnActionClick("C"))

btn_plus = Button(window, text="+", padx=21, pady=7,
               command=lambda: btnActionClick("+"))

btn_equal = Button(window, text="=", padx=21, pady=7,
               command=lambda: btnActionClick("="))

btn_minus = Button(window, text="-", padx=21, pady=7,
               command=lambda: btnActionClick("-"))

btn_multiplication = Button(window, text="*", padx=21, pady=7,
               command=lambda: btnActionClick("*"))

btn_division = Button(window, text="/", padx=21, pady=7,
               command=lambda: btnActionClick("/"))

btn_co = Button(window, text="<", padx=21, pady=7,
               command=lambda: btnActionClick("clear"))

btn_dot = Button(window, text=".", padx=21, pady=7,
               command=lambda: btnActionClick("dot"))


# Construir tela
main_input.grid(row=0, column=0, columnspan=4)
btn_c.grid(row=1, column=1)
btn_equal.grid(row=5, column=3)
btn_plus.grid(row=4, column=3)
btn_minus.grid(row=3, column=3)
btn_multiplication.grid(row=2, column=3)
btn_division.grid(row=1, column=3)
btn_co.grid(row=1, column=2)
btn_dot.grid(row=5, column=2)

# Rodar Tela
window.mainloop()