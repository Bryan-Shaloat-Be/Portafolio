from tkinter import *
from tkinter import messagebox as mBox
from ttkbootstrap.constants import *
import ttkbootstrap as ttk
import tkinter as tk
from psycopg2 import *
import psycopg2
import time
from tkinter.messagebox import _show


def function_box_message():
    mBox.showinfo("Message of MECANOGAME",
                  'This Game was created with educational intention. '
                  'You can find us in www.MecanoGame.com for more information')


def function_exit():
    window.quit()
    window.destroy()
    exit()


def show_points_top():
    def function_back():
        window6.destroy()

    window6 = Toplevel(window)
    window6.title('POINTS')
    window6.geometry("700x495+600+200")
    window6.iconbitmap("D:\\Usuario Cat\\Desktop\\PPXP\\Mecano\\Escritura_meca.ico")
    back_button2 = ttk.Button(window6, text="         EXIT        ", bootstyle=(OUTLINE, DANGER),
                              command=function_back)
    back_button2.place(x=560, y=430)
    

def function_help():
    def function_back():
        window2.destroy()

    window2 = Toplevel(window)
    window2.title('HELP GAME')
    window2.geometry("700x495+600+200")
    control_tab = ttk.Notebook(window2)
    window2.iconbitmap("D:\\Usuario Cat\\Desktop\\PPXP\\Mecano\\Escritura_meca.ico")
    tab1 = ttk.Frame(control_tab)
    tab2 = ttk.Frame(control_tab)
    control_tab.add(tab2, text='Game')
    control_tab.add(tab1, text='Questions')
    control_tab.pack(expand=1, fill="both")
    back_button = ttk.Button(window2, text="         EXIT        ", bootstyle=(OUTLINE, DANGER), command=function_back)
    back_button.place(x=580, y=430)
    latest = Label(tab2, text="""
    Bienvenidos a Mecano Game!
    El juego fue realizado con fines educacionales para la practica de programacion como tambien
    una herramienta para la mejora mecanografica como mental.
    
     """)
    latest.place(x=100, y=10)
    latest = Label(tab2, text="""
    ¿COMO JUGAR?
    El Juego consta de 3 niveles cada uno con su dificultad eeeee
    como sus tipos de palabras y oraciones, estas se arrojan de
    manera automatica y aleatoria cuando usted pulsta el boton
    de comenzar(despues de colar su usuario y seleccionar el nivel)
    el tiempo comenzara a correr y tendra que memorizar la palabra
    para asi rescribirla en la barra, una vez terminado debera pulsar
    'finish' para verificar su puntuacion y registrarla :) puede volver a
    jugar presionando 'try again' y asi hasta que finalmente alcance
    su objetivo en puntos o  habilidad :).

     """, )
    latest.place(x=315, y=130)
    image_label = Label(tab2, image=imaginal)
    image_label.place(x=20, y=100)


def new_user():
    def function_back():
        window3.destroy()

    def register_user_data(name):
        label_valid = Label(window3, text='Successful registration')
        label_valid.place(x=295, y=410)
        connection = psycopg2.connect(dbname="MecanoGame", user="postgres", password="216472557", host="localhost",
                                      port="5432")
        cursor = connection.cursor()
        query = '''INSERT INTO users(name_user) VALUES (%s)'''
        cursor.execute(query, (name,))

        cursor = connection.cursor()
        query = '''INSERT INTO points(name_user_points, points) VALUES (%s,0)'''
        cursor.execute(query, (name,))
        connection.commit()
        connection.close()

    window3 = Toplevel(window)
    window3.title('NEW USER')
    window3.geometry("700x495+600+200")
    back_button = ttk.Button(window3, text="         EXIT        ", bootstyle=(OUTLINE, DANGER), command=function_back)
    back_button.place(x=580, y=430)
    window3.iconbitmap("D:\\Usuario Cat\\Desktop\\PPXP\\Mecano\\Escritura_meca.ico")
    labelled = Label(window3, text="REGISTER NEW USER", font=("Times", 30), bg="white")
    labelled.place(x=155, y=30)
    imaginable2 = Label(window3, image=image_user)
    imaginable2.place(x=260, y=100)
    user = tk.StringVar()
    register = ttk.Entry(window3, width=20, textvariable=user)
    register.place(x=287, y=310)
    register.get()
    register_button = ttk.Button(window3, text='     REGISTER     ', command=lambda: register_user_data(register.get()),
                                 bootstyle=(INFO, OUTLINE))
    register_button.place(x=303, y=360)


def start_game():
    def function_back():
        window4.destroy()

    def enter_game(value, name):
        def function_back2():
            window5.destroy()

        window5 = Toplevel(window)
        window5.title('GAME')
        window5.geometry("700x495+600+200")
        window5.iconbitmap("D:\\Usuario Cat\\Desktop\\PPXP\\Mecano\\Escritura_meca.ico")
        back_button2 = ttk.Button(window5, text="         EXIT        ", bootstyle=(OUTLINE, DANGER),
                                  command=function_back2)
        back_button2.place(x=560, y=430)

        def function_points(words_user, words_sis, entry_user, button_finish):
            if value == 'level1':
                points = 0
                result = 0
                print(words_user)
                print(words_sis)
                for j in words_sis:
                    if j == words_user:
                        points = points + 200
                        print(points)
                    else:
                        points = points - 150
                connection_points = psycopg2.connect(dbname="MecanoGame", user="postgres", password="216472557",
                                                     host="localhost",
                                                     port="5432")
                cursor_points = connection_points.cursor()
                query_points = '''SELECT (name_user_points) FROM points WHERE name_user_points = %s'''
                cursor_points.execute(query_points, (name,))
                row_points = cursor_points.fetchall()
                for x in row_points:
                    for y in x:
                        if y == name:
                            cursor_points = connection_points.cursor()
                            query_points = '''SELECT (points) FROM points WHERE name_user_points = %s'''
                            cursor_points.execute(query_points, (name,))
                            row_points = cursor_points.fetchall()
                            for a in row_points:
                                for b in a:
                                    result = b + points
                            cursor_points = connection_points.cursor()
                            query_points = '''UPDATE points SET points = %s WHERE name_user_points = %s'''
                            cursor_points.execute(query_points, (result, name))
                            break
                connection_points.commit()
                connection_points.close()
                entry_user.config(state='disable')
                button_finish.config(state='disable')
                if points < 0:
                    message_points = Label(window5, text='Sorry, you are wrong, try again! (-150)')
                    message_points.place(x=250, y=290)
                    image_label_points = Label(window5, image=image_points)
                    image_label_points.place(x=280, y=320)
                if points > 0:
                    message_points = Label(window5, text='Good Job! You was good (+100)')
                    message_points.place(x=250, y=290)
                    print("es mayor")
                window5.after(2000, lambda: message_points.config(text=''))
                window5.after(2000, lambda: image_label_points.config(image=''))
            elif value == 'level2':
                points = 0
                result = 0
                print(words_user)
                print(words_sis)
                for j in words_sis:
                    if j == words_user:
                        points = points + 300
                        print(points)
                    else:
                        points = points - 400
                connection_points = psycopg2.connect(dbname="MecanoGame", user="postgres", password="216472557",
                                                     host="localhost",
                                                     port="5432")
                cursor_points = connection_points.cursor()
                query_points = '''SELECT (name_user_points) FROM points WHERE name_user_points = %s'''
                cursor_points.execute(query_points, (name,))
                row_points = cursor_points.fetchall()
                for x in row_points:
                    for y in x:
                        if y == name:
                            cursor_points = connection_points.cursor()
                            query_points = '''SELECT (points) FROM points WHERE name_user_points = %s'''
                            cursor_points.execute(query_points, (name,))
                            row_points = cursor_points.fetchall()
                            for a in row_points:
                                for b in a:
                                    result = b + points
                            cursor_points = connection_points.cursor()
                            query_points = '''UPDATE points SET points = %s WHERE name_user_points = %s'''
                            cursor_points.execute(query_points, (result, name))
                            break
                connection_points.commit()
                connection_points.close()
                entry_user.config(state='disable')
                button_finish.config(state='disable')
                if points < 0:
                    message_points = Label(window5, text='Sorry, you are wrong, try again! (-400)')
                    message_points.place(x=250, y=290)
                    image_label_points = Label(window5, image=image_points)
                    image_label_points.place(x=280, y=320)
                if points > 0:
                    message_points = Label(window5, text='Good Job! You was good (+300)')
                    message_points.place(x=250, y=290)
                    print("es mayor")
                window5.after(2000, lambda: message_points.config(text=''))
                window5.after(2000, lambda: image_label_points.config(image=''))
            elif value == 'level3':
                points = 0
                result = 0
                print(words_user)
                print(words_sis)
                for j in words_sis:
                    if j == words_user:
                        points = points + 500
                        print(points)
                    else:
                        points = points - 700
                connection_points = psycopg2.connect(dbname="MecanoGame", user="postgres", password="216472557",
                                                     host="localhost",
                                                     port="5432")
                cursor_points = connection_points.cursor()
                query_points = '''SELECT (name_user_points) FROM points WHERE name_user_points = %s'''
                cursor_points.execute(query_points, (name,))
                row_points = cursor_points.fetchall()
                for x in row_points:
                    for y in x:
                        if y == name:
                            cursor_points = connection_points.cursor()
                            query_points = '''SELECT (points) FROM points WHERE name_user_points = %s'''
                            cursor_points.execute(query_points, (name,))
                            row_points = cursor_points.fetchall()
                            for a in row_points:
                                for b in a:
                                    result = b + points
                            cursor_points = connection_points.cursor()
                            query_points = '''UPDATE points SET points = %s WHERE name_user_points = %s'''
                            cursor_points.execute(query_points, (result, name))
                            break
                connection_points.commit()
                connection_points.close()
                entry_user.config(state='disable')
                button_finish.config(state='disable')
                if points < 0:
                    message_points = Label(window5, text='Sorry, you are wrong, try again! (-700)')
                    message_points.place(x=250, y=290)
                    image_label_points = Label(window5, image=image_points)
                    image_label_points.place(x=280, y=320)
                if points > 0:
                    message_points = Label(window5, text='Good Job! You was good (+500)')
                    message_points.place(x=250, y=290)
                    print("es mayor")
                window5.after(2000, lambda: message_points.config(text=''))
                window5.after(2000, lambda: image_label_points.config(image=''))

        def register_points_words_lvl(row):
            register_words_user = ttk.Entry(window5, width=50, justify=tk.CENTER, font=("Times", 12), state=tk.DISABLED)
            register_words_user.place(x=150, y=190)
            register_words_user.after(1000, register_words_user.config(state=tk.NORMAL))
            button_final = ttk.Button(window5, text="         FINISH        ", bootstyle=(INFO, OUTLINE),
                                      command=lambda: function_points(register_words_user.get(), row,
                                                                      register_words_user, button_final))
            button_final.place(x=295, y=250)
            button_try_again = ttk.Button(window5, text="        TRY AGAIN       ", bootstyle=(INFO, OUTLINE),
                                          command=lambda: playing_game())
            button_try_again.place(x=40, y=430)
            register_words_user.get()

        def playing_game():
            if value == 'level1':
                connection = psycopg2.connect(dbname="MecanoGame", user="postgres", password="216472557",
                                              host="localhost",
                                              port="5432")
                cursor = connection.cursor()
                query = '''select * from level1 order by random() limit 1;  '''
                cursor.execute(query)
                row = cursor.fetchone()
                for i in row:
                    word_show = Listbox(window5, width=64, height=1, font=("Times", 15))
                    word_show.place(x=30, y=50)
                    word_show.insert(END, i)
                window5.after(1000, lambda: word_show.delete(0, 1))
                window5.after(1000, lambda: register_points_words_lvl(row))
                connection.commit()
                connection.close()
            if value == 'level2':  # WARNING WE NEED TO STAR WITH LEVEL 2 and 3
                connection = psycopg2.connect(dbname="MecanoGame", user="postgres", password="216472557",
                                              host="localhost",
                                              port="5432")
                cursor = connection.cursor()
                query = '''select * from level2 order by random() limit 1;  '''
                cursor.execute(query)
                row = cursor.fetchone()
                for i in row:
                    word_show = Listbox(window5, width=64, height=1, font=("Times", 15))
                    word_show.place(x=30, y=50)
                    word_show.insert(END, i)
                window5.after(1000, lambda: word_show.delete(0, 1))
                window5.after(1000, lambda: register_points_words_lvl(row))
                connection.commit()
                connection.close()
            if value == 'level3':
                connection = psycopg2.connect(dbname="MecanoGame", user="postgres", password="216472557",
                                              host="localhost",
                                              port="5432")
                cursor = connection.cursor()
                query = '''select * from level3 order by random() limit 1;  '''
                cursor.execute(query)
                row = cursor.fetchone()
                for i in row:
                    word_show = Listbox(window5, width=64, height=1, font=("Times", 15))
                    word_show.place(x=30, y=50)
                    word_show.insert(END, i)
                window5.after(1000, lambda: word_show.delete(0, 1))
                window5.after(1000, lambda: register_points_words_lvl(row))
                connection.commit()
                connection.close()

        playing_game()

    def confirmation_user(name):
        connection = psycopg2.connect(dbname="MecanoGame", user="postgres", password="216472557", host="localhost",
                                      port="5432")
        cursor = connection.cursor()
        query = '''SELECT * FROM users WHERE name_user = %s '''
        cursor.execute(query, (name,))
        row = cursor.fetchall()
        for i in row:
            for j in i:
                print(j)
                if j == name:
                    value = select_difficult.get()
                    window4.destroy()
                    enter_game(value, name)
        connection.commit()
        connection.close()

    window4 = Toplevel(window)
    window4.title('STAR THE GAME')
    window4.geometry("500x295+700+300")
    window4.iconbitmap("D:\\Usuario Cat\\Desktop\\PPXP\\Mecano\\Escritura_meca.ico")
    labelled = Label(window4, text="START GAME", font=("Times", 24), bg="white")
    labelled.place(x=170, y=30)
    label_text = Label(window4, text='Insert user')
    label_text.place(x=160, y=90)
    label_text_diff = Label(window4, text='Select the difficult')
    label_text_diff.place(x=140, y=145)
    difficult = tk.StringVar()
    select_difficult = ttk.Combobox(window4, width=16, textvariable=difficult, state="readonly")
    select_difficult['values'] = ['level1', 'level2', 'level3']
    select_difficult.place(x=280, y=140)
    select_difficult.current(0)
    user = tk.StringVar()
    user_confirm = ttk.Entry(window4, width=18, textvariable=user)
    user_confirm.place(x=280, y=95)
    user_confirm.get()
    back_button = ttk.Button(window4, text="         EXIT        ", bootstyle=(OUTLINE, DANGER), command=function_back)
    back_button.place(x=390, y=250)
    confirm_button = ttk.Button(window4, text='     START     ', command=lambda: confirmation_user(user_confirm.get()),
                                bootstyle=(INFO, OUTLINE))
    confirm_button.place(x=210, y=200)


window = Tk()
window.title('MECANOGAME')
window.geometry("700x495+600+200")
window.configure(bg='Black')
window.resizable(False, False)
style = ttk.Style("darkly")
window.iconbitmap("D:\\Usuario Cat\\Desktop\\PPXP\\Mecano\\Escritura_meca.ico")

label = Label(window, text="MECANO", font=("Times", 32), bg="white")
label.place(x=190, y=50)

label = Label(window, text="GAME", font=("Times", 32), fg='white', bg='black')
label.place(x=390, y=50)

menu_bar = Menu(window)
window.configure(menu=menu_bar)  # Menu bar fo Menu in the game

menu_help = Menu(menu_bar, tearoff=0)  # Add a menu in the menu bar
menu_help.add_command(label="About us", command=function_box_message)
menu_bar.add_cascade(label="Help", menu=menu_help)

# buttons
register_users = ttk.Button(window, text='     NEW USER     ', command=new_user, bootstyle=(INFO, OUTLINE))
register_users.place(x=300, y=190)

test_button = ttk.Button(window, text="         START        ", bootstyle=(SUCCESS, OUTLINE), command=start_game)
test_button.place(x=300, y=230)

test_button = ttk.Button(window, text="        POINTS       ", bootstyle=(SUCCESS, OUTLINE), command=show_points_top)
test_button.place(x=300, y=270)

test_button = ttk.Button(window, text="          HELP         ", bootstyle=(SUCCESS, OUTLINE), command=function_help)
test_button.place(x=300, y=310)

test_button = ttk.Button(window, text="         EXIT        ", bootstyle=(OUTLINE, DANGER), command=function_exit)
test_button.place(x=580, y=430)

# Images
imaginal = PhotoImage(file="D:\\Usuario Cat\\Desktop\\PPXP\\Mecano\\example.gif")
image_user = PhotoImage(file="D:\\Usuario Cat\\Desktop\\PPXP\\Mecano\\user_.gif")
image_points = PhotoImage(file="D:\\Usuario Cat\\Desktop\\PPXP\\Mecano\\Sad_Face.gif")

window.mainloop()
