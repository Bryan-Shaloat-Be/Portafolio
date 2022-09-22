# Barragan Pulido Bryan Shaloat Be -- Engineer of software
from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as ttk

# ----------------------------   MAIN ------------------------------

window = Tk()
window.title("Eco Calculator")
window.geometry("325x500+800+100")
window.resizable(False, False)
style = ttk.Style("pastel")
window.config(backgroun="gray80")
window.iconbitmap("D:\\Usuario Cat\\Desktop\\PPXP\\GDL Calculator\\calculator.ico")

# Global Variables
list1 = None
numbers = ""
text_pantalla = StringVar()
text_pantalla2 = StringVar()
text_pantalla3 = StringVar()


# ------------------------------ Functions ------------------------------


def calculator(n):
    global numbers
    numbers += str(n)
    text_pantalla.set(numbers)


def results():
    global numbers
    if numbers == "":
        ms = "Its clear"
        text_pantalla.set(ms)
    else:
        try:
            r = str(eval(numbers))
            numbers = r
            text_pantalla.set(r)
        except:
            e = "ERROR"
            text_pantalla.set(e)


def clear():
    global numbers
    numbers = ""
    text_pantalla.set("")
    text_pantalla3.set("")


def clear_space():
    global numbers
    numbers = numbers[:-1]
    text_pantalla.set(numbers)


def grade_converter():
    global list1
    global numbers
    list1 = window.place_slaves()
    for i in list1:
        i.place_forget()
    text_pantalla.set("")
    text_pantalla3.set("")
    numbers = ""
    # ---------------------------- Tv -----------------------------------------
    pantalla2 = Entry(window, font=("arial", 25, "bold"), state="readonly",
                      textvariable=text_pantalla, justify=CENTER)
    pantalla2.place(x=24, y=15, width=280, height=50)
    pantalla3 = Entry(window, font=("arial", 25, "bold"), state="readonly",
                      textvariable=text_pantalla3, justify=CENTER)
    pantalla3.place(x=24, y=75, width=280, height=50)
    grade = StringVar()
    select_grade = ttk.Combobox(window, width=26, textvariable=grade, state="readonly")
    select_grade['values'] = ['Centigrados a Fahrenheit', 'Fahrenheit a Centigrados']
    select_grade.place(x=75, y=140)
    # ------------------ Buttons ---------------------------------------------
    button2_g = ttk.Button(window, text="  1  ", bootstyle=PRIMARY, command=lambda: (calculator(1), converter()))
    button2_g.place(x=28, y=190)
    button2_g.place_configure(width=60, height=60)
    button3_g = ttk.Button(window, text="  2  ", bootstyle=SUCCESS, command=lambda: (calculator(2), converter()))
    button3_g.place(x=98, y=190)
    button3_g.place_configure(width=60, height=60)
    button4_g = ttk.Button(window, text="  3  ", bootstyle=PRIMARY, command=lambda: (calculator(3), converter()))
    button4_g.place(x=168, y=190)
    button4_g.place_configure(width=60, height=60)
    button5_g = ttk.Button(window, text="  CE  ", bootstyle=LIGHT, command=lambda: clear())
    button5_g.place(x=238, y=190)
    button5_g.place_configure(width=60, height=60)
    button6_g = ttk.Button(window, text="  C  ", bootstyle=LIGHT, command=lambda: (clear_space(), converter()))
    button6_g.place(x=238, y=260)
    button6_g.place_configure(width=60, height=60)
    button7_g = ttk.Button(window, text="  4  ", bootstyle=SUCCESS, command=lambda: (calculator(4), converter()))
    button7_g.place(x=28, y=260)
    button7_g.place_configure(width=60, height=60)
    button8_g = ttk.Button(window, text="  5  ", bootstyle=PRIMARY, command=lambda: (calculator(5), converter()))
    button8_g.place(x=98, y=260)
    button8_g.place_configure(width=60, height=60)
    button9_g = ttk.Button(window, text="  6  ", bootstyle=SUCCESS, command=lambda: (calculator(6), converter()))
    button9_g.place(x=168, y=260)
    button9_g.place_configure(width=60, height=60)
    button10_g = ttk.Button(window, text="  7  ", bootstyle=PRIMARY, command=lambda: (calculator(7), converter()))
    button10_g.place(x=28, y=330)
    button10_g.place_configure(width=60, height=60)
    button11_g = ttk.Button(window, text="  8  ", bootstyle=SUCCESS, command=lambda: (calculator(8), converter()))
    button11_g.place(x=98, y=330)
    button11_g.place_configure(width=60, height=60)
    button12_g = ttk.Button(window, text="  9  ", bootstyle=PRIMARY, command=lambda: (calculator(9), converter()))
    button12_g.place(x=168, y=330)
    button12_g.place_configure(width=60, height=60)
    button13_g = ttk.Button(window, text="  0  ", bootstyle=INFO, command=lambda: (calculator(0), converter()))
    button13_g.place(x=28, y=400)
    button13_g.place_configure(width=60, height=60)
    button14_g = ttk.Button(window, text=" :) ", bootstyle=INFO, command=lambda: text_pantalla3.set("I LOVE YOU"))
    button14_g.place(x=168, y=400)
    button14_g.place_configure(height=60, width=130)
    button15_g = ttk.Button(window, text="  .  ", bootstyle=INFO, command=lambda: (calculator("."), converter()))
    button15_g.place(x=98, y=400)
    button15_g.place_configure(width=60, height=60)

    # ----------------------------- Results -------------------------------

    def converter():
        values = select_grade.get()
        if values == 'Centigrados a Fahrenheit':
            if numbers == "":
                result = "(0*9/5)+32"
                r = str(eval(result))
                text_pantalla3.set(r)
            else:
                try:
                    result = "(" + numbers + "*9/5)+32"
                    r = str(eval(result))
                    text_pantalla3.set(r)
                except:
                    ms = "ERROR"
                    text_pantalla.set(ms)
                    text_pantalla3.set(ms)
        elif values == 'Fahrenheit a Centigrados':
            if numbers == "":
                result = "(0-32)*5/9"
                r = str(eval(result))
                c = len(r)
                if c >= 7:
                    io = 0
                    while io < 11:
                        io += 1
                        r = r[:-1]
                    text_pantalla3.set(r)
                else:
                    text_pantalla3.set(r)
                text_pantalla3.set(r)
            else:
                try:
                    result = "(" + numbers + "-32)*5/9"
                    r = str(eval(result))
                    c = len(r)
                    if c >= 7:
                        io = 0
                        while io < 11:
                            io += 1
                            r = r[:-1]
                        text_pantalla3.set(r)
                    else:
                        text_pantalla3.set(r)
                except:
                    ms = "ERROR"
                    text_pantalla.set(ms)
                    text_pantalla3.set(ms)


def back_calculator():
    global list1
    global numbers
    list1 = window.place_slaves()
    for i in list1:
        i.place_forget()
    text_pantalla.set("")
    numbers = ""
    pantalla.place(x=24, y=35, width=280, height=50)
    button1_c.place(x=28, y=120)
    button1_c.place_configure(width=60, height=60)
    button2_c.place(x=98, y=120)
    button2_c.place_configure(width=60, height=60)
    button3_c.place(x=168, y=120)
    button3_c.place_configure(width=60, height=60)
    button4_c.place(x=238, y=120)
    button4_c.place_configure(width=60, height=60)
    button1.place(x=28, y=190)
    button1.place_configure(width=60, height=60)
    button2.place(x=98, y=190)
    button2.place_configure(width=60, height=60)
    button3.place(x=168, y=190)
    button3.place_configure(width=60, height=60)
    button4.place(x=28, y=260)
    button4.place_configure(width=60, height=60)
    button5.place(x=98, y=260)
    button5.place_configure(width=60, height=60)
    button7.place(x=168, y=260)
    button7.place_configure(width=60, height=60)
    button8.place(x=28, y=330)
    button8.place_configure(width=60, height=60)
    button9.place(x=98, y=330)
    button9.place_configure(width=60, height=60)
    button10.place(x=168, y=330)
    button10.place_configure(width=60, height=60)
    button11.place(x=28, y=400)
    button11.place_configure(width=60, height=60)
    button12.place(x=238, y=190)
    button12.place_configure(width=60, height=60)
    button13.place(x=238, y=260)
    button13.place_configure(width=60, height=60)
    button14.place(x=168, y=400)
    button14.place_configure(height=60, width=130)
    button5_c.place(x=238, y=330)
    button5_c.place_configure(width=60, height=60)
    button6_c.place(x=98, y=400)
    button6_c.place_configure(width=60, height=60)

    # ---- The best solution of this problem is use a matriz to change the value of x an y  ----
    # for i in list1:
    # i.place_configure(width=60, height=60)
    # i.place()
    # print(i)


def binary_converter():
    global list1
    global numbers
    list1 = window.place_slaves()
    for i in list1:
        i.place_forget()
    text_pantalla.set("")
    text_pantalla3.set("")
    numbers = ""
    # ----------------------------------------- TV ------------------------------------
    pantalla2 = Entry(window, font=("arial", 25, "bold"), state="readonly",
                      textvariable=text_pantalla, justify=CENTER)
    pantalla2.place(x=24, y=15, width=280, height=50)
    pantalla3 = Entry(window, font=("arial", 25, "bold"), state="readonly",
                      textvariable=text_pantalla3, justify=CENTER)
    pantalla3.place(x=24, y=75, width=280, height=50)
    binary = StringVar()
    select_binary = ttk.Combobox(window, width=26, textvariable=binary, state="readonly")
    select_binary['values'] = ['Binario a Decimal', 'Decimal a Binario']
    select_binary.place(x=75, y=140)

    # ----------------------------------  Buttons -----------------------
    button1_b = ttk.Button(window, text="  A  ", bootstyle=LIGHT, command=lambda: calculator("A"))
    button1_b.place(x=28, y=350)
    button1_b.place_configure(width=60, height=40)

    button2_b = ttk.Button(window, text="  B  ", bootstyle=LIGHT, command=lambda: calculator("B"))
    button2_b.place(x=98, y=350)
    button2_b.place_configure(width=60, height=40)

    button3_b = ttk.Button(window, text="  C  ", bootstyle=LIGHT, command=lambda: calculator("C"))
    button3_b.place(x=168, y=350)
    button3_b.place_configure(width=60, height=40)

    button4_b = ttk.Button(window, text="  D  ", bootstyle=LIGHT, command=lambda: calculator("D"))
    button4_b.place(x=238, y=350)
    button4_b.place_configure(width=60, height=40)

    button1b = ttk.Button(window, text="  1  ", bootstyle=PRIMARY, command=lambda: (calculator(1), converter()))
    button1b.place(x=28, y=200)
    button1b.place_configure(width=60, height=40)

    button2b = ttk.Button(window, text="  2  ", bootstyle=SUCCESS, command=lambda: (calculator(2), converter()))
    button2b.place(x=98, y=200)
    button2b.place_configure(width=60, height=40)

    button3b = ttk.Button(window, text="  3  ", bootstyle=PRIMARY, command=lambda: (calculator(3), converter()))
    button3b.place(x=168, y=200)
    button3b.place_configure(width=60, height=40)

    button4b = ttk.Button(window, text="  4  ", bootstyle=SUCCESS, command=lambda: (calculator(4), converter()))
    button4b.place(x=28, y=250)
    button4b.place_configure(width=60, height=40)

    button5b = ttk.Button(window, text="  5  ", bootstyle=PRIMARY, command=lambda: (calculator(5), converter()))
    button5b.place(x=98, y=250)
    button5b.place_configure(width=60, height=40)

    button7b = ttk.Button(window, text="  6  ", bootstyle=SUCCESS, command=lambda: (calculator(6), converter()))
    button7b.place(x=168, y=250)
    button7b.place_configure(width=60, height=40)

    button8b = ttk.Button(window, text="  7  ", bootstyle=PRIMARY, command=lambda: (calculator(7), converter()))
    button8b.place(x=28, y=300)
    button8b.place_configure(width=60, height=40)

    button9b = ttk.Button(window, text="  8  ", bootstyle=SUCCESS, command=lambda: (calculator(8), converter()))
    button9b.place(x=98, y=300)
    button9b.place_configure(width=60, height=40)

    button10b = ttk.Button(window, text="  9  ", bootstyle=PRIMARY, command=lambda: (calculator(9), converter()))
    button10b.place(x=168, y=300)
    button10b.place_configure(width=60, height=40)

    button11b = ttk.Button(window, text="  0  ", bootstyle=SUCCESS, command=lambda: (calculator(0), converter()))
    button11b.place(x=238, y=300)
    button11b.place_configure(width=60, height=40)

    button12b = ttk.Button(window, text=" CE ", bootstyle=LIGHT, command=lambda: (clear(), converter()))
    button12b.place(x=238, y=200)
    button12b.place_configure(width=60, height=40)

    button13b = ttk.Button(window, text="  C  ", bootstyle=LIGHT, command=lambda: (clear_space(), converter()))
    button13b.place(x=238, y=250)
    button13b.place_configure(width=60, height=40)

    button14b = ttk.Button(window, text="  E  ", bootstyle=LIGHT, command=lambda: calculator("E"))
    button14b.place(x=28, y=400)
    button14b.place_configure(width=60, height=40)

    button15_b = ttk.Button(window, text="  F  ", bootstyle=LIGHT, command=lambda: calculator("F"))
    button15_b.place(x=98, y=400)
    button15_b.place_configure(width=60, height=40)

    button16_b = ttk.Button(window, text="  0  ", bootstyle=INFO, command=lambda: (calculator(0), converter()))
    button16_b.place(x=168, y=400)
    button16_b.place_configure(width=60, height=40)

    button17_b = ttk.Button(window, text="  1  ", bootstyle=INFO, command=lambda: (calculator(1), converter()))
    button17_b.place(x=238, y=400)
    button17_b.place_configure(width=60, height=40)

    def converter():
        global numbers
        values = select_binary.get()
        if values == 'Decimal a Binario':
            button1b.configure(state=NORMAL)
            button2b.configure(state=NORMAL)
            button3b.configure(state=NORMAL)
            button4b.configure(state=NORMAL)
            button5b.configure(state=NORMAL)
            button7b.configure(state=NORMAL)
            button8b.configure(state=NORMAL)
            button9b.configure(state=NORMAL)
            button10b.configure(state=NORMAL)
            button11b.configure(state=NORMAL)
            button14b.configure(state=NORMAL)
            button15_b.configure(state=NORMAL)
            button1_b.configure(state=NORMAL)
            button2_b.configure(state=NORMAL)
            button3_b.configure(state=NORMAL)
            button4_b.configure(state=NORMAL)
            if numbers == "":
                text_pantalla3.set("0")
            else:
                aux = ''
                aux2 = numbers
                try:
                    while aux2 != "1":
                        r = str(eval(aux2 + "%2"))
                        aux2 = str(eval(aux2 + "//2"))
                        aux += r
                    aux += "1"
                    result = "".join(reversed(aux))
                    text_pantalla3.set(result)
                except:
                    ms = "ERROR"
                    text_pantalla3.set(ms)
        if values == 'Binario a Decimal':
            button1b.configure(state=DISABLED)
            button2b.configure(state=DISABLED)
            button3b.configure(state=DISABLED)
            button4b.configure(state=DISABLED)
            button5b.configure(state=DISABLED)
            button7b.configure(state=DISABLED)
            button8b.configure(state=DISABLED)
            button9b.configure(state=DISABLED)
            button10b.configure(state=DISABLED)
            button11b.configure(state=DISABLED)
            button14b.configure(state=DISABLED)
            button15_b.configure(state=DISABLED)
            button1_b.configure(state=DISABLED)
            button2_b.configure(state=DISABLED)
            button3_b.configure(state=DISABLED)
            button4_b.configure(state=DISABLED)
            if numbers == "":
                text_pantalla3.set("0")
            else:
                aux3 = ""
                j = "0"
                aux4 = numbers
                result2 = "".join(reversed(aux4))
                for i in result2:
                    result = str(eval(i + "*2**" + j))
                    j = str(eval(j + "+1"))
                    aux3 += result + "+"
                aux3 += "0"
                r = str(eval(aux3))
                text_pantalla3.set(r)


# ---------------------------    Barr  of menu -------------------------------------------------------
menu_bar = Menu(window)
menu_principal = Menu(menu_bar, tearoff=0)
menu_principal.add_command(label="Calculator", command=lambda: back_calculator())
menu_principal.add_command(label="Grade Converter", command=lambda: grade_converter())
menu_bar.add_separator()
menu_principal.add_command(label="Binary Converter", command=lambda: binary_converter())
menu_bar.add_separator()
menu_bar.add_cascade(label="Functions", menu=menu_principal)
menu_bar.add_cascade(label="Options")
window.config(menu=menu_bar)

# -------------------------------------- Entry or TV ------------------------------------------------
pantalla = Entry(window, font=("arial", 20, "bold"), state="readonly",
                 textvariable=text_pantalla, justify=CENTER)
pantalla.place(x=24, y=35, width=280, height=50)

# Buttons
button1_c = ttk.Button(window, text="  x²  ", bootstyle=LIGHT, command=lambda: calculator("**"))
button1_c.place(x=28, y=120)
button1_c.place_configure(width=60, height=60)

button2_c = ttk.Button(window, text="  CE  ", bootstyle=LIGHT, command=lambda: clear())
button2_c.place(x=98, y=120)
button2_c.place_configure(width=60, height=60)

button3_c = ttk.Button(window, text="  C  ", bootstyle=LIGHT, command=lambda: clear_space())
button3_c.place(x=168, y=120)
button3_c.place_configure(width=60, height=60)

button4_c = ttk.Button(window, text="  /  ", bootstyle=LIGHT, command=lambda: calculator("/"))
button4_c.place(x=238, y=120)
button4_c.place_configure(width=60, height=60)

button1 = ttk.Button(window, text="  1  ", bootstyle=PRIMARY, command=lambda: calculator(1))
button1.place(x=28, y=190)
button1.place_configure(width=60, height=60)

button2 = ttk.Button(window, text="  2  ", bootstyle=SUCCESS, command=lambda: calculator(2))
button2.place(x=98, y=190)
button2.place_configure(width=60, height=60)

button3 = ttk.Button(window, text="  3  ", bootstyle=PRIMARY, command=lambda: calculator(3))
button3.place(x=168, y=190)
button3.place_configure(width=60, height=60)

button4 = ttk.Button(window, text="  4  ", bootstyle=SUCCESS, command=lambda: calculator(4))
button4.place(x=28, y=260)
button4.place_configure(width=60, height=60)

button5 = ttk.Button(window, text="  5  ", bootstyle=PRIMARY, command=lambda: calculator(5))
button5.place(x=98, y=260)
button5.place_configure(width=60, height=60)

button7 = ttk.Button(window, text="  6  ", bootstyle=SUCCESS, command=lambda: calculator(6))
button7.place(x=168, y=260)
button7.place_configure(width=60, height=60)

button8 = ttk.Button(window, text="  7  ", bootstyle=PRIMARY, command=lambda: calculator(7))
button8.place(x=28, y=330)
button8.place_configure(width=60, height=60)

button9 = ttk.Button(window, text="  8  ", bootstyle=SUCCESS, command=lambda: calculator(8))
button9.place(x=98, y=330)
button9.place_configure(width=60, height=60)

button10 = ttk.Button(window, text="  9  ", bootstyle=PRIMARY, command=lambda: calculator(9))
button10.place(x=168, y=330)
button10.place_configure(width=60, height=60)

button11 = ttk.Button(window, text="  0  ", bootstyle=INFO, command=lambda: calculator(0))
button11.place(x=28, y=400)
button11.place_configure(width=60, height=60)

button12 = ttk.Button(window, text="  x  ", bootstyle=LIGHT, command=lambda: calculator("*"))
button12.place(x=238, y=190)
button12.place_configure(width=60, height=60)

button13 = ttk.Button(window, text="  -  ", bootstyle=LIGHT, command=lambda: calculator("-"))
button13.place(x=238, y=260)
button13.place_configure(width=60, height=60)

button14 = ttk.Button(window, text=" = ", bootstyle=INFO, command=lambda: results())
button14.place(x=168, y=400)
button14.place_configure(height=60, width=130)

button5_c = ttk.Button(window, text="  +  ", bootstyle=LIGHT, command=lambda: calculator("+"))
button5_c.place(x=238, y=330)
button5_c.place_configure(width=60, height=60)

button6_c = ttk.Button(window, text="  .  ", bootstyle=INFO, command=lambda: calculator("."))
button6_c.place(x=98, y=400)
button6_c.place_configure(width=60, height=60)
window.mainloop()

print("Esta la prueba para git and github")