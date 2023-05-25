import re
from psycopg2 import *
import psycopg2
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import SlideTransition, FadeTransition
from kivy.uix.actionbar import ActionItem
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.screen import MDScreen
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.scrollview import ScrollView 
from kivymd.uix.swiper import MDSwiper, MDSwiperItem
from kivy.factory import Factory
from kivy.lang import Builder
from time import *
from kivymd.uix.card import MDCard
from kivy.graphics import Color, Rectangle, Line
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDIconButton
from kivymd.uix.fitimage import FitImage
from kivymd.uix.chip import MDChip
from kivymd.uix.button import MDFloatingActionButton
from kivymd.uix.list import TwoLineIconListItem,MDList, OneLineIconListItem,  IconLeftWidget
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.textfield import MDTextField
from kivy.utils import get_color_from_hex
from kivy.uix.image import Image, CoreImage
import random
from kivymd.uix.filemanager import MDFileManager
import os
import io
import base64
from kivymd.toast import toast


Window.size=(350,580)
control_creacion = False
class Login(Screen): #Pantalla de login
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        # Etiqueta de salida de correo y contraseña
        self.output_label = Label(text="", size_hint=(1, 0.3), pos_hint={'x': 0, 'y': 0.1})
        self.add_widget(self.output_label)
        # Boton de ingreso
        btn = Button(text='Ingresar', size_hint=(0.3, 0.06), pos_hint={'x': 0.35, 'y': 0.30},background_color = (0.2196078431372549,0.6823529411764706, 0.8, 0.45))
        btn.bind(on_press=self.change_screen)
        #boton de registro 
        btn2 = Button(text='Registro', size_hint=(0.3, 0.06), pos_hint={'x': 0.35, 'y': 0.23},background_color = (0.2196078431372549,0.6823529411764706, 0.8, 0.45))
        btn2.bind(on_press=self.change_screen_register)
        # Cambio de contrasena
        btn3 = Button(text='Olvidaste tu contrasena', size_hint=(0.48, 0.06), pos_hint={'x': 0.25, 'y': 0.09},background_color = (0,0.5647058823529412, 0.7568627450980392), background_normal='')
        btn3.bind(on_press=self.change_screen_recover)
        self.add_widget(btn)
        self.add_widget(btn2)
        self.add_widget(btn3)

        # Funcion de cambio de pantalla de home
    def change_screen(self, *args):
        global id_user, correo_verify
        correo_verify = ''
        contra_verify = ''
        id_user = ''
        self.ids.alertas.clear_widgets()
        correo = self.ids.A.text
        contrasena = self.ids.B.text
        conection = psycopg2.connect(dbname="postgresql", user="postgres", password="216472557",
                                                     host="localhost",
                                                     port="5432")
        cursor_points = conection.cursor()
        query_pub = '''SELECT nombre,contrasena,id FROM usuario WHERE nombre = %s OR contrasena = %s'''
        cursor_points.execute(query_pub,(correo, contrasena,))
        datos_login = cursor_points.fetchone()
        conection.commit()
        conection.close()
        verifity = False
        label0 = MDLabel(text='Contrasena incorrecta',pos_hint={'x': 0.15, 'y': 0.12})
        label2 = MDLabel(text='El usuario no existe',pos_hint={'x': 0.15, 'y': 0.12})
        if datos_login is not None:
            for i, valor in enumerate(datos_login):
                if i == 0:
                    correo_verify = valor
                if i == 1:
                    contra_verify = valor
                if i == 2:
                    id_user = valor
        if correo_verify == correo:
            if contra_verify == contrasena:
                if id_user != '':
                    print("Ingreso con exito")
                    verifity = True
            else:
                self.ids.alertas.add_widget(label0)
                print("Contrasena invalida")
        else:
            self.ids.alertas.add_widget(label2)
            print("Usuario invalido")
        if verifity == True:
            self.manager.current = 'home'
        else:
            print("Datos incorrectos")

                                        # BUSCAR MANERA DE LIMPIAR LOS TEXTFIELD CUANDO SE INGRESA
        print((datos_login))
        print(type(datos_login))
        print(correo_verify)
        print(contra_verify)
        print(id_user)

        # ====================== Validaciones =============================
        """\* (?=.*[A-Z]): indica que debe haber al menos una mayuscula en la cadena
            (?=.*[0-9\W]): indica que debe haber al menos un numero o simbolo en la cadena. 
            \W representa cualquier caracter que no sea una letra o un numero.
            .+: indica que la cadena debe contener al menos un caracter"""
        pattern = r"^(?=.*[A-Z])(?=.*[0-9\W]).+$" #Ejemplo de contraseña valida: Abcdef123!
        match = re.search(pattern, contrasena)
        # Validacion para cambiar de pantalla solo si se ingresan los datos
        """if correo.endswith('@alumnos.udg.mx'):
            if match:
                self.output_label.text = "\n\n\n\nCorreo y contraseña valida"
                self.manager.current = 'principal'
        else:
            self.output_label.text = "\n\n\n\nCorreo y\o contraseña invalido"""
        
        clean_text = self.ids.A
        clean_text.text=''
        clean_text_contra = self.ids.B
        clean_text_contra.text=''
# =====================================================================

        # Funcion de cambio de pantalla de registro
    def change_screen_register(self, *args):
        self.manager.current = 'register'

        # Funcion de cambio de pantalla a recuperar contrasena
    def change_screen_recover(self, *args):
        self.manager.current = 'recover'



class Register(Screen): # Pantalla de registro
   
    codigo = str(random.randint(100000, 999999))
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        self.output_label = Label(text="", size_hint=(1, 0.3), pos_hint={'x': 0, 'y': 0.1})
        self.add_widget(self.output_label)
        
        # Boton
        btn = Button(text='Enviar código', size_hint=(0.3, 0.06), pos_hint={'x': 0.2, 'y': 0.07},background_color = (0.2196078431372549,0.6823529411764706, 0.8, 0.45))
        btn.bind(on_press=self.send_code)
        self.add_widget(btn)

        btn2 = Button(text='Registrarse', size_hint=(0.3, 0.06), pos_hint={'x': 0.5, 'y': 0.07},background_color = (0.2196078431372549,0.6823529411764706, 0.8, 0.45))
        btn2.bind(on_press=self.save)
        self.add_widget(btn2)

        btn3 = Button(text='Login', size_hint=(0.3, 0.06), pos_hint={'x': 0.35, 'y': 0.01},background_color = (0.2196078431372549,0.6823529411764706, 0.8, 0.45))
        btn3.bind(on_press=self.change_screen)
        self.add_widget(btn3)

    def save(self, *args):
        if self.ids.cod.text != self.codigo:
            lbel_error = MDLabel(pos_hint={'x': .11, 'y': 0.1}, text='Ingresa codigo de verificacion correcto')
            self.ids.reg.add_widget(lbel_error)
            print("Error de codigo")
        
        else:
            nombre = self.ids.A1.text
            correo = self.ids.B1.text
            codigo = self.ids.C1.text
            contrasena = self.ids.D1.text
            conection = psycopg2.connect(dbname="postgresql", user="postgres", password="216472557",
                                                        host="localhost",
                                                        port="5432")
            cursor_points = conection.cursor()
            query_pub = ''' INSERT INTO usuario VALUES ( DEFAULT, %s, %s, %s, %s);'''
            cursor_points.execute(query_pub,(nombre,codigo,correo,contrasena,))
            conection.commit()
            conection.close()

            clean1 = self.ids.A1
            clean1.text=''
            clean2 = self.ids.B1
            clean2.text=''
            clean3 = self.ids.C1
            clean3.text=''
            clean4 = self.ids.D1
            clean4.text=''
            clean5 = self.ids.cod
            clean5.text=''

    def send_code(self, *args):
        correo = self.ids.B1.text
        print(self.codigo)

        """contrasenaC = '' #contraseno de prueba
        from_email = ('') #correos de pruba

        yag = yagmail.SMTP(user=from_email, password=contrasenaC)

        destinatario= ['ricardofructuosomorales@gmail.com'] #cambiar al correo que lo deseas enviar o modificar variable para tomarlo de los campos
        asunto= 'Prueba de envio correo'
        mensaje= codigo

        yag.send(destinatario, asunto, mensaje)"""

    def change_screen(self, *args):
        self.manager.current = 'login'


class home(Screen): # Pantalla principal
    direccion = ""
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.manager_open = False
        self.file_manager = MDFileManager(
                exit_manager=self.exit_manager,  # function called when the user reaches directory tree root
                select_path=self.select_path,  # function called when selecting a file/directory
            )
        self.direccion = ""
    
    def filtros(self, button):

        menu_items = [
                {
                    "text": "Comida",
                    "viewclass": "OneLineListItem",
                    "on_release": lambda: self.busqueda_filtros(filtro=1),
                },
                {
                    "text": "Electronicos",
                    "viewclass": "OneLineListItem",
                    "on_release": lambda: self.busqueda_filtros(filtro=2),
                },
                {
                    "text": "Libros",
                    "viewclass": "OneLineListItem",
                    "on_release": lambda: self.busqueda_filtros(filtro=3),
                },
                {
                    "text": "Accesorios",
                    "viewclass": "OneLineListItem",
                    "on_release": lambda: self.busqueda_filtros(filtro=4),
                },
                {
                    "text": "Papeleria",
                    "viewclass": "OneLineListItem",
                    "on_release": lambda: self.busqueda_filtros(filtro=5),
                },
                                {
                    "text": "Todas",
                    "viewclass": "OneLineListItem",
                    "on_release": lambda: self.busqueda_filtros(filtro=6),
                },
            ]
        menu = MDDropdownMenu(
            caller=button,
            size_hint=(1, 0.1),
            items=menu_items,
            width_mult=2
            )
        menu.open()

    def guardar_categoria(self):
        
        menu_items = [
                {
                    "text": "Comida",
                    "viewclass": "OneLineListItem",
                    "on_release": lambda: self.seleccionar_categoria(filtro=1),
                },
                {
                    "text": "Electronicos",
                    "viewclass": "OneLineListItem",
                    "on_release": lambda: self.seleccionar_categoria(filtro=2),
                },
                {
                    "text": "Libros",
                    "viewclass": "OneLineListItem",
                    "on_release": lambda: self.seleccionar_categoria(filtro=3),
                },
                {
                    "text": "Accesorios",
                    "viewclass": "OneLineListItem",
                    "on_release": lambda: self.seleccionar_categoria(filtro=4),
                },
                 {
                    "text": "Papeleria",
                    "viewclass": "OneLineListItem",
                    "on_release": lambda: self.seleccionar_categoria(filtro=5),
                },
            ]
        menu = MDDropdownMenu(
            caller=self.ids.AC5,
            size_hint=(1, 0.1),
            items=menu_items,
            width_mult=2
            )
        menu.open()

    def seleccionar_categoria(self, filtro):
        global cat_comida, cat_electrico, cat_accesorios, cat_libro, cat_papeleria
        cat_comida = False
        cat_electrico = False
        cat_libro = False
        cat_accesorios = False
        cat_papeleria = False 

        if filtro == 1:
            textfield = self.ids.AC5
            textfield.text='Comida'
            cat_comida = True
        elif filtro == 2:
            textfield = self.ids.AC5
            textfield.text='Electronicos'
            cat_electrico = True
        elif filtro == 3:
            textfield = self.ids.AC5
            textfield.text='Libros'
            cat_libro = True
        elif filtro == 4:
            textfield = self.ids.AC5
            textfield.text='Accesorios'
            cat_accesorios = True
        elif filtro == 5:
            textfield = self.ids.AC5
            textfield.text='Papeleria'
            cat_papeleria = True
    
    def busqueda_filtros(self, filtro):
        global cat_comida, cat_electrico, cat_accesorios, cat_libro, cat_papeleria,boxA,card1
        self.ids.container.clear_widgets()
        cat_comida = False
        cat_electrico = False
        cat_libro = False
        cat_accesorios = False
        cat_papeleria = False
        controlador_idices = 7

        def eliminar_pub(controlador_idices):
            #idices = self.ids.container.children.index(self.ids.container.children[])
            if controlador_idices == 7:
                self.ids.container.remove_widget(self.ids.container.children[0])
                controlador_idices = 6
                print("removido")
            elif controlador_idices == 6:
                self.ids.container.remove_widget(self.ids.container.children[6])
                print("removido")

        
        def open_menu(instance):
            menu_items = [
                {
                    "text": "Editar",
                    "viewclass": "OneLineListItem",
                    "on_release": lambda: print("Opción 1 seleccionada"),
                },
                {
                    "text": "Eliminar",
                    "viewclass": "OneLineListItem",
                    "on_release": lambda: eliminar_pub(controlador_idices),
                },
            ]
            menu = MDDropdownMenu(
                caller=instance,
                items=menu_items,
                width_mult=4,
            )
            menu.open()
        def show_report_dialog(self, *args):
                dialog = MDDialog(
                    title="Reportar publicación\n\n",
                    type="custom",
                    content_cls=BoxLayout(orientation="vertical", spacing="12dp"),
                    buttons=[
                        MDFlatButton(text="CANCELAR", on_release=lambda x: dialog.dismiss()),
                        MDFlatButton(text="ENVIAR", on_release=send_report)
                    ],
                )
                dialog.content_cls.add_widget(MDTextField(
                    hint_text="Motivo del reporte",
                    helper_text="Por favor, proporcione una breve descripción.",
                    helper_text_mode="persistent"
                ))
                dialog.open()
        def send_report(self, *args):
            # insert - comentario_reporte
            # select con join titulo, reporte, id where id
            # Gmail ---> titulo, report , id 
            # Lógica para enviar el reporte de la publicación
            # lista[1223,323,323,22332,2]
            # lista 
            print("Reporte enviado")

        def change_heart_color(instance):
            if instance.theme_text_color == "Custom" and instance.text_color == (1, 0, 0, 1):
                # Cambiar a color original
                instance.theme_text_color = "Primary"
            else:
                # Cambiar a color rojo
                instance.theme_text_color = "Custom"
                instance.text_color = (1, 0, 0, 1)
            # instance.theme_text_color = "Custom"
            # instance.text_color = (1, 0, 0, 1)  # Cambiar a color rojo   
        
        if filtro == 1:
            cat_comida = True
            
            nombre_user = ''
            id_user_pub = ''
            titulo_pub = ''
            descripcion_pub = ''
            precio_pub = ''
            disponibilidad_pub = True
            
            conection_titulo = psycopg2.connect(dbname="postgresql", user="postgres", password="216472557",
                                                        host="localhost",
                                                        port="5432")
            cursor_points = conection_titulo.cursor()
            query_pub = '''SELECT p.idus,p.titulo,p.imagen,p.descrip,p.dispo,p.precio,u.nombre FROM publicacion p JOIN usuario u ON p.idus = u.id WHERE p.comida = True'''
            cursor_points.execute(query_pub,())
            datos_publica = cursor_points.fetchall()
            conection_titulo.commit()
            conection_titulo.close()
    
            
            #print(datos_publica)
            #print(titulo_pub)
            #print(imagen_pub)         ==================================================
            #print(precio_pub) 
            #print(descripcion_pub)

            # Construccion de las publicaciones
            for x in datos_publica:
                for i, valor in enumerate(x):
                    if i == 0: 
                        id_user_pub = valor
                    if i == 1:
                        titulo_pub = valor
                    if i == 2:
                        image_bytes = base64.b64decode(valor)
                        image_data = io.BytesIO(image_bytes)
                        core_image = CoreImage(image_data, ext = 'jpg')
                        image1 = Image()
                        image1.texture = core_image.texture
                    if i == 3: 
                        descripcion_pub = valor
                    if i == 4:
                        disponibilidad_pub = valor
                    if i == 5:
                        precio_pub = valor
                    if i == 6:
                        nombre_user = valor
                boxA = FloatLayout(size_hint=(1, 1))
                self.ids.container.add_widget(boxA)
                card1 = MDCard(
                    orientation='vertical', 
                    size_hint=(.95,.95),
                    pos_hint={'center_x': 0.5, 'center_y': 0.5},
                    radius = 16)
                boxA.add_widget(card1)
                floatb = FloatLayout(size_hint=(1, 0.09))
                with floatb.canvas:
                    Color(0.8, 0.8, 0.8, 1)
                    floatb.Line = Line(points=(floatb.x, floatb.y, floatb.right, floatb.y), width=1)
                card1.add_widget(floatb)
                label_titulo = MDLabel(text=titulo_pub,
                                    pos_hint={"center_x": 0.8, "center_y": 0.5})
                floatb.add_widget(label_titulo)
                iconbu = MDIconButton(icon="dots-vertical",pos_hint={"right": 1,"top": 1})
                iconbu.bind(on_release=open_menu)
                floatb.add_widget(iconbu)
                boxC = BoxLayout(size_hint=(1, 0.50), padding=(5,5,5,5))
                card1.add_widget(boxC)
                mdswiper = MDSwiper(size_hint=(1, 1), width_mult = 0.1)
                mdswiper_item1 = MDSwiperItem(size_hint=(1, 1),
                                            padding=(3,8,10,3))
                # MAS ITEMS MINIMO 3
                mdswiper_item1.add_widget(image1)
                mdswiper.add_widget(mdswiper_item1)
                boxC.add_widget(mdswiper)
                floatd = FloatLayout(size_hint=(0.95, 0.30),
                                    pos_hint={'x':0 , 'y':0 },
                                    )
                card1.add_widget(floatd)
                label_description = MDLabel(text=descripcion_pub, 
                                            pos_hint={'x': 0.05, 'y': 0.03},
                                            size_hint=(0.95, None))
                chip_usuario = MDChip(text=nombre_user,
                                    icon_left = "account",
                                    pos_hint={'x': 0.03, 'y': 0.75})
                chip_precio = MDChip(text=(precio_pub + '$'),
                                    icon_left = "cash",
                                    pos_hint={'x': 0.75, 'y': 0.75})
                floatd.add_widget(label_description)
                floatd.add_widget(chip_precio)
                floatd.add_widget(chip_usuario)
                floate = FloatLayout(size_hint=(1, 0.11), 
                                    )
                card1.add_widget(floate)
                faction_b = MDFloatingActionButton(icon='comment',
                                                size_hint=(0.55, 0.85),
                                                pos_hint={"center_x": 0.5,"center_y": 0.5})
                icon_heart =MDIconButton(icon='cards-heart-outline',
                                        pos_hint={'x': 0.04, 'y': 0},
                                        icon_size="25sp")
                icon_alert =MDIconButton(icon='alert-box',
                                        pos_hint={'x': 0.82, 'y': 0},
                                        icon_size="25sp")
                floate.add_widget(faction_b)
                floate.add_widget(icon_heart)
                floate.add_widget(icon_alert)
                icon_alert.bind(on_release=show_report_dialog)
                icon_heart.bind(on_release=change_heart_color)
    
                
        elif filtro == 2:
            cat_electrico = True

            nombre_user = ''
            id_user_pub = ''
            titulo_pub = ''
            descripcion_pub = ''
            precio_pub = ''
            disponibilidad_pub = True
            
            conection_titulo = psycopg2.connect(dbname="postgresql", user="postgres", password="216472557",
                                                        host="localhost",
                                                        port="5432")
            cursor_points = conection_titulo.cursor()
            query_pub = '''SELECT p.idus,p.titulo,p.imagen,p.descrip,p.dispo,p.precio,u.nombre FROM publicacion p JOIN usuario u ON p.idus = u.id WHERE p.electronico = True'''
            cursor_points.execute(query_pub,())
            datos_publica = cursor_points.fetchall()
            conection_titulo.commit()
            conection_titulo.close()
    
            
            print(datos_publica)
            print(titulo_pub)
            print(precio_pub)
            print(descripcion_pub)

            # Construccion de las publicaciones
            for x in datos_publica:
                for i, valor in enumerate(x):
                    if i == 0: 
                        id_user_pub = valor
                    if i == 1:
                        titulo_pub = valor
                    if i == 2:
                        image_bytes = base64.b64decode(valor)
                        image_data = io.BytesIO(image_bytes)
                        core_image = CoreImage(image_data, ext = 'jpg')
                        image1 = Image()
                        image1.texture = core_image.texture
                    if i == 3: 
                        descripcion_pub = valor
                    if i == 4:
                        disponibilidad_pub = valor
                    if i == 5:
                        precio_pub = valor
                    if i == 6:
                        nombre_user = valor
                boxA = FloatLayout(size_hint=(1, 1))
                self.ids.container.add_widget(boxA)
                card1 = MDCard(
                    orientation='vertical', 
                    size_hint=(.95,.95),
                    pos_hint={'center_x': 0.5, 'center_y': 0.5},
                    radius = 16)
                boxA.add_widget(card1)
                floatb = FloatLayout(size_hint=(1, 0.09))
                with floatb.canvas:
                    Color(0.8, 0.8, 0.8, 1)
                    floatb.Line = Line(points=(floatb.x, floatb.y, floatb.right, floatb.y), width=1)
                card1.add_widget(floatb)
                label_titulo = MDLabel(text=titulo_pub,
                                    pos_hint={"center_x": 0.8, "center_y": 0.5})
                floatb.add_widget(label_titulo)
                iconbu = MDIconButton(icon="dots-vertical",pos_hint={"right": 1,"top": 1})
                iconbu.bind(on_release=open_menu)
                floatb.add_widget(iconbu)
                boxC = BoxLayout(size_hint=(1, 0.50), padding=(5,5,5,5))
                card1.add_widget(boxC)
                mdswiper = MDSwiper(size_hint=(1, 1), width_mult = 0.1)
                mdswiper_item1 = MDSwiperItem(size_hint=(1, 1),
                                            padding=(3,8,10,3))
                # MAS ITEMS MINIMO 3
                mdswiper_item1.add_widget(image1)
                mdswiper.add_widget(mdswiper_item1)
                boxC.add_widget(mdswiper)
                floatd = FloatLayout(size_hint=(0.95, 0.30),
                                    pos_hint={'x':0 , 'y':0 },
                                    )
                card1.add_widget(floatd)
                label_description = MDLabel(text=descripcion_pub, 
                                            pos_hint={'x': 0.05, 'y': 0.03},
                                            size_hint=(0.95, None))
                chip_usuario = MDChip(text=nombre_user,
                                    icon_left = "account",
                                    pos_hint={'x': 0.03, 'y': 0.75})
                chip_precio = MDChip(text=(precio_pub + '$'),
                                    icon_left = "cash",
                                    pos_hint={'x': 0.75, 'y': 0.75})
                floatd.add_widget(label_description)
                floatd.add_widget(chip_precio)
                floatd.add_widget(chip_usuario)
                floate = FloatLayout(size_hint=(1, 0.11), 
                                    )
                card1.add_widget(floate)
                faction_b = MDFloatingActionButton(icon='comment',
                                                size_hint=(0.55, 0.85),
                                                pos_hint={"center_x": 0.5,"center_y": 0.5})
                icon_heart =MDIconButton(icon='cards-heart-outline',
                                        pos_hint={'x': 0.04, 'y': 0},
                                        icon_size="25sp")
                icon_alert =MDIconButton(icon='alert-box',
                                        pos_hint={'x': 0.82, 'y': 0},
                                        icon_size="25sp")
                floate.add_widget(faction_b)
                floate.add_widget(icon_heart)
                floate.add_widget(icon_alert)
                icon_alert.bind(on_release=show_report_dialog)
                icon_heart.bind(on_release=change_heart_color)
        elif filtro == 3:
            cat_libro = True

            nombre_user = ''
            id_user_pub = ''
            titulo_pub = ''
            descripcion_pub = ''
            precio_pub = ''
            disponibilidad_pub = True
            
            conection_titulo = psycopg2.connect(dbname="postgresql", user="postgres", password="216472557",
                                                        host="localhost",
                                                        port="5432")
            cursor_points = conection_titulo.cursor()
            query_pub = '''SELECT p.idus,p.titulo,p.imagen,p.descrip,p.dispo,p.precio,u.nombre FROM publicacion p JOIN usuario u ON p.idus = u.id WHERE p.libro = True'''
            cursor_points.execute(query_pub,())
            datos_publica = cursor_points.fetchall()
            conection_titulo.commit()
            conection_titulo.close()
    
            
            print(datos_publica)
            print(titulo_pub)
            print(precio_pub)
            print(descripcion_pub)

            # Construccion de las publicaciones
            for x in datos_publica:
                for i, valor in enumerate(x):
                    if i == 0: 
                        id_user_pub = valor
                    if i == 1:
                        titulo_pub = valor
                    if i == 2:
                        image_bytes = base64.b64decode(valor)
                        image_data = io.BytesIO(image_bytes)
                        core_image = CoreImage(image_data, ext = 'jpg')
                        image1 = Image()
                        image1.texture = core_image.texture
                    if i == 3: 
                        descripcion_pub = valor
                    if i == 4:
                        disponibilidad_pub = valor
                    if i == 5:
                        precio_pub = valor
                    if i == 6:
                        nombre_user = valor
                boxA = FloatLayout(size_hint=(1, 1))
                self.ids.container.add_widget(boxA)
                card1 = MDCard(
                    orientation='vertical', 
                    size_hint=(.95,.95),
                    pos_hint={'center_x': 0.5, 'center_y': 0.5},
                    radius = 16)
                boxA.add_widget(card1)
                floatb = FloatLayout(size_hint=(1, 0.09))
                with floatb.canvas:
                    Color(0.8, 0.8, 0.8, 1)
                    floatb.Line = Line(points=(floatb.x, floatb.y, floatb.right, floatb.y), width=1)
                card1.add_widget(floatb)
                label_titulo = MDLabel(text=titulo_pub,
                                    pos_hint={"center_x": 0.8, "center_y": 0.5})
                floatb.add_widget(label_titulo)
                iconbu = MDIconButton(icon="dots-vertical",pos_hint={"right": 1,"top": 1})
                iconbu.bind(on_release=open_menu)
                floatb.add_widget(iconbu)
                boxC = BoxLayout(size_hint=(1, 0.50), padding=(5,5,5,5))
                card1.add_widget(boxC)
                mdswiper = MDSwiper(size_hint=(1, 1), width_mult = 0.1)
                mdswiper_item1 = MDSwiperItem(size_hint=(1, 1),
                                            padding=(3,8,10,3))
                # MAS ITEMS MINIMO 3
                mdswiper_item1.add_widget(image1)
                mdswiper.add_widget(mdswiper_item1)
                boxC.add_widget(mdswiper)
                floatd = FloatLayout(size_hint=(0.95, 0.30),
                                    pos_hint={'x':0 , 'y':0 },
                                    )
                card1.add_widget(floatd)
                label_description = MDLabel(text=descripcion_pub, 
                                            pos_hint={'x': 0.05, 'y': 0.03},
                                            size_hint=(0.95, None))
                chip_usuario = MDChip(text=nombre_user,
                                    icon_left = "account",
                                    pos_hint={'x': 0.03, 'y': 0.75})
                chip_precio = MDChip(text=(precio_pub + '$'),
                                    icon_left = "cash",
                                    pos_hint={'x': 0.75, 'y': 0.75})
                floatd.add_widget(label_description)
                floatd.add_widget(chip_precio)
                floatd.add_widget(chip_usuario)
                floate = FloatLayout(size_hint=(1, 0.11), 
                                    )
                card1.add_widget(floate)
                faction_b = MDFloatingActionButton(icon='comment',
                                                size_hint=(0.55, 0.85),
                                                pos_hint={"center_x": 0.5,"center_y": 0.5})
                icon_heart =MDIconButton(icon='cards-heart-outline',
                                        pos_hint={'x': 0.04, 'y': 0},
                                        icon_size="25sp")
                icon_alert =MDIconButton(icon='alert-box',
                                        pos_hint={'x': 0.82, 'y': 0},
                                        icon_size="25sp")
                floate.add_widget(faction_b)
                floate.add_widget(icon_heart)
                floate.add_widget(icon_alert)
                icon_alert.bind(on_release=show_report_dialog)
                icon_heart.bind(on_release=change_heart_color)
        elif filtro == 4:
            cat_accesorios = True

            nombre_user = ''
            id_user_pub = ''
            titulo_pub = ''
            descripcion_pub = ''
            precio_pub = ''
            disponibilidad_pub = True
            
            conection_titulo = psycopg2.connect(dbname="postgresql", user="postgres", password="216472557",
                                                        host="localhost",
                                                        port="5432")
            cursor_points = conection_titulo.cursor()
            query_pub = '''SELECT p.idus,p.titulo,p.imagen,p.descrip,p.dispo,p.precio,u.nombre FROM publicacion p JOIN usuario u ON p.idus = u.id WHERE p.accesorios = True'''
            cursor_points.execute(query_pub,())
            datos_publica = cursor_points.fetchall()
            conection_titulo.commit()
            conection_titulo.close()
    
            
            print(datos_publica)
            print(titulo_pub)
            print(precio_pub)
            print(descripcion_pub)

            # Construccion de las publicaciones
            for x in datos_publica:
                for i, valor in enumerate(x):
                    if i == 0: 
                        id_user_pub = valor
                    if i == 1:
                        titulo_pub = valor
                    if i == 2:
                        image_bytes = base64.b64decode(valor)
                        image_data = io.BytesIO(image_bytes)
                        core_image = CoreImage(image_data, ext = 'jpg')
                        image1 = Image()
                        image1.texture = core_image.texture
                    if i == 3: 
                        descripcion_pub = valor
                    if i == 4:
                        disponibilidad_pub = valor
                    if i == 5:
                        precio_pub = valor
                    if i == 6:
                        nombre_user = valor
                boxA = FloatLayout(size_hint=(1, 1))
                self.ids.container.add_widget(boxA)
                card1 = MDCard(
                    orientation='vertical', 
                    size_hint=(.95,.95),
                    pos_hint={'center_x': 0.5, 'center_y': 0.5},
                    radius = 16)
                boxA.add_widget(card1)
                floatb = FloatLayout(size_hint=(1, 0.09))
                with floatb.canvas:
                    Color(0.8, 0.8, 0.8, 1)
                    floatb.Line = Line(points=(floatb.x, floatb.y, floatb.right, floatb.y), width=1)
                card1.add_widget(floatb)
                label_titulo = MDLabel(text=titulo_pub,
                                    pos_hint={"center_x": 0.8, "center_y": 0.5})
                floatb.add_widget(label_titulo)
                iconbu = MDIconButton(icon="dots-vertical",pos_hint={"right": 1,"top": 1})
                iconbu.bind(on_release=open_menu)
                floatb.add_widget(iconbu)
                boxC = BoxLayout(size_hint=(1, 0.50), padding=(5,5,5,5))
                card1.add_widget(boxC)
                mdswiper = MDSwiper(size_hint=(1, 1), width_mult = 0.1)
                mdswiper_item1 = MDSwiperItem(size_hint=(1, 1),
                                            padding=(3,8,10,3))
                # MAS ITEMS MINIMO 3
                mdswiper_item1.add_widget(image1)
                mdswiper.add_widget(mdswiper_item1)
                boxC.add_widget(mdswiper)
                floatd = FloatLayout(size_hint=(0.95, 0.30),
                                    pos_hint={'x':0 , 'y':0 },
                                    )
                card1.add_widget(floatd)
                label_description = MDLabel(text=descripcion_pub, 
                                            pos_hint={'x': 0.05, 'y': 0.03},
                                            size_hint=(0.95, None))
                chip_usuario = MDChip(text=nombre_user,
                                    icon_left = "account",
                                    pos_hint={'x': 0.03, 'y': 0.75})
                chip_precio = MDChip(text=(precio_pub + '$'),
                                    icon_left = "cash",
                                    pos_hint={'x': 0.7, 'y': 0.75})
                floatd.add_widget(label_description)
                floatd.add_widget(chip_precio)
                floatd.add_widget(chip_usuario)
                floate = FloatLayout(size_hint=(1, 0.11), 
                                    )
                card1.add_widget(floate)
                faction_b = MDFloatingActionButton(icon='comment',
                                                size_hint=(0.55, 0.85),
                                                pos_hint={"center_x": 0.5,"center_y": 0.5})
                icon_heart =MDIconButton(icon='cards-heart-outline',
                                        pos_hint={'x': 0.04, 'y': 0},
                                        icon_size="25sp")
                icon_alert =MDIconButton(icon='alert-box',
                                        pos_hint={'x': 0.82, 'y': 0},
                                        icon_size="25sp")
                floate.add_widget(faction_b)
                floate.add_widget(icon_heart)
                floate.add_widget(icon_alert)
                icon_alert.bind(on_release=show_report_dialog)
                icon_heart.bind(on_release=change_heart_color)
        elif filtro == 5:
            cat_papeleria = True
            nombre_user = ''
            id_user_pub = ''
            titulo_pub = ''
            descripcion_pub = ''
            precio_pub = ''
            disponibilidad_pub = True
            
            conection_titulo = psycopg2.connect(dbname="postgresql", user="postgres", password="216472557",
                                                        host="localhost",
                                                        port="5432")
            cursor_points = conection_titulo.cursor()
            query_pub = '''SELECT p.idus,p.titulo,p.imagen,p.descrip,p.dispo,p.precio,u.nombre FROM publicacion p JOIN usuario u ON p.idus = u.id WHERE p.papeleria = True'''
            cursor_points.execute(query_pub,())
            datos_publica = cursor_points.fetchall()
            conection_titulo.commit()
            conection_titulo.close()
    
            
            print(datos_publica)
            print(titulo_pub)
            print(precio_pub)
            print(descripcion_pub)

            # Construccion de las publicaciones
            for x in datos_publica:
                for i, valor in enumerate(x):
                    if i == 0: 
                        id_user_pub = valor
                    if i == 1:
                        titulo_pub = valor
                    if i == 2:
                        image_bytes = base64.b64decode(valor)
                        image_data = io.BytesIO(image_bytes)
                        core_image = CoreImage(image_data, ext = 'jpg')
                        image1 = Image()
                        image1.texture = core_image.texture
                    if i == 3: 
                        descripcion_pub = valor
                    if i == 4:
                        disponibilidad_pub = valor
                    if i == 5:
                        precio_pub = valor
                    if i == 6:
                        nombre_user = valor
                boxA = FloatLayout(size_hint=(1, 1))
                self.ids.container.add_widget(boxA)
                card1 = MDCard(
                    orientation='vertical', 
                    size_hint=(.95,.95),
                    pos_hint={'center_x': 0.5, 'center_y': 0.5},
                    radius = 16)
                boxA.add_widget(card1)
                floatb = FloatLayout(size_hint=(1, 0.09))
                with floatb.canvas:
                    Color(0.8, 0.8, 0.8, 1)
                    floatb.Line = Line(points=(floatb.x, floatb.y, floatb.right, floatb.y), width=1)
                card1.add_widget(floatb)
                label_titulo = MDLabel(text=titulo_pub,
                                    pos_hint={"center_x": 0.8, "center_y": 0.5})
                floatb.add_widget(label_titulo)
                iconbu = MDIconButton(icon="dots-vertical",pos_hint={"right": 1,"top": 1})
                iconbu.bind(on_release=open_menu)
                floatb.add_widget(iconbu)
                boxC = BoxLayout(size_hint=(1, 0.50), padding=(5,5,5,5))
                card1.add_widget(boxC)
                mdswiper = MDSwiper(size_hint=(1, 1), width_mult = 0.1)
                mdswiper_item1 = MDSwiperItem(size_hint=(1, 1),
                                            padding=(3,8,10,3))
                
                # MAS ITEMS MINIMO 3
                mdswiper_item1.add_widget(image1)
                mdswiper.add_widget(mdswiper_item1)
                boxC.add_widget(mdswiper)
                floatd = FloatLayout(size_hint=(0.95, 0.30),
                                    pos_hint={'x':0 , 'y':0 },
                                    )
                card1.add_widget(floatd)
                label_description = MDLabel(text=descripcion_pub, 
                                            pos_hint={'x': 0.05, 'y': 0.03},
                                            size_hint=(0.95, None))
                chip_usuario = MDChip(text=nombre_user,
                                    icon_left = "account",
                                    pos_hint={'x': 0.03, 'y': 0.75})
                chip_precio = MDChip(text=(precio_pub + '$'),
                                    icon_left = "cash",
                                    pos_hint={'x': 0.7, 'y': 0.75})
                floatd.add_widget(label_description)
                floatd.add_widget(chip_precio)
                floatd.add_widget(chip_usuario)
                floate = FloatLayout(size_hint=(1, 0.11), 
                                    )
                card1.add_widget(floate)
                faction_b = MDFloatingActionButton(icon='comment',
                                                size_hint=(0.55, 0.85),
                                                pos_hint={"center_x": 0.5,"center_y": 0.5})
                icon_heart =MDIconButton(icon='cards-heart-outline',
                                        pos_hint={'x': 0.04, 'y': 0},
                                        icon_size="25sp")
                icon_alert =MDIconButton(icon='alert-box',
                                        pos_hint={'x': 0.82, 'y': 0},
                                        icon_size="25sp")
                floate.add_widget(faction_b)
                floate.add_widget(icon_heart)
                floate.add_widget(icon_alert)
                icon_alert.bind(on_release=show_report_dialog)
                icon_heart.bind(on_release=change_heart_color) 
        elif filtro == 6:
            
            nombre_user = ''
            id_user_pub = ''
            titulo_pub = ''
            descripcion_pub = ''
            precio_pub = ''
            disponibilidad_pub = True
            
            conection_titulo = psycopg2.connect(dbname="postgresql", user="postgres", password="216472557",
                                                        host="localhost",
                                                        port="5432")
            cursor_points = conection_titulo.cursor()
            query_pub = '''SELECT p.idus,p.titulo,p.imagen,p.descrip,p.dispo,p.precio,u.nombre FROM publicacion p JOIN usuario u ON p.idus = u.id WHERE p.dispo = True'''
            cursor_points.execute(query_pub,())
            datos_publica = cursor_points.fetchall()
            conection_titulo.commit()
            conection_titulo.close()
    
            
            print(datos_publica)
            print(titulo_pub)
            print(precio_pub)
            print(descripcion_pub)

            # Construccion de las publicaciones
            for x in datos_publica:
                for i, valor in enumerate(x):
                    if i == 0: 
                        id_user_pub = valor
                    if i == 1:
                        titulo_pub = valor
                    if i == 2:
                        image_bytes = base64.b64decode(valor)
                        image_data = io.BytesIO(image_bytes)
                        core_image = CoreImage(image_data, ext = 'jpg')
                        image1 = Image()
                        image1.texture = core_image.texture
                    if i == 3: 
                        descripcion_pub = valor
                    if i == 4:
                        disponibilidad_pub = valor
                    if i == 5:
                        precio_pub = valor
                    if i == 6:
                        nombre_user = valor
                boxA = FloatLayout(size_hint=(1, 1))
                self.ids.container.add_widget(boxA)
                card1 = MDCard(
                    orientation='vertical', 
                    size_hint=(.95,.95),
                    pos_hint={'center_x': 0.5, 'center_y': 0.5},
                    radius = 16)
                boxA.add_widget(card1)
                floatb = FloatLayout(size_hint=(1, 0.09))
                with floatb.canvas:
                    Color(0.8, 0.8, 0.8, 1)
                    floatb.Line = Line(points=(floatb.x, floatb.y, floatb.right, floatb.y), width=1)
                card1.add_widget(floatb)
                label_titulo = MDLabel(text=titulo_pub,
                                    pos_hint={"center_x": 0.8, "center_y": 0.5})
                floatb.add_widget(label_titulo)
                iconbu = MDIconButton(icon="dots-vertical",pos_hint={"right": 1,"top": 1})
                iconbu.bind(on_release=open_menu)
                floatb.add_widget(iconbu)
                boxC = BoxLayout(size_hint=(1, 0.50), padding=(5,5,5,5))
                card1.add_widget(boxC)
                mdswiper = MDSwiper(size_hint=(1, 1), width_mult = 0.1)
                mdswiper_item1 = MDSwiperItem(size_hint=(1, 1),
                                            padding=(3,8,10,3))
                # MAS ITEMS MINIMO 3
                mdswiper_item1.add_widget(image1)
                mdswiper.add_widget(mdswiper_item1)
                boxC.add_widget(mdswiper)
                floatd = FloatLayout(size_hint=(0.95, 0.30),
                                    pos_hint={'x':0 , 'y':0 },
                                    )
                card1.add_widget(floatd)
                label_description = MDLabel(text=descripcion_pub, 
                                            pos_hint={'x': 0.05, 'y': 0.03},
                                            size_hint=(0.95, None))
                chip_usuario = MDChip(text=nombre_user,
                                    icon_left = "account",
                                    pos_hint={'x': 0.03, 'y': 0.75})
                chip_precio = MDChip(text=(precio_pub + '$'),
                                    icon_left = "cash",
                                    pos_hint={'x': 0.7, 'y': 0.75})
                floatd.add_widget(label_description)
                floatd.add_widget(chip_precio)
                floatd.add_widget(chip_usuario)
                floate = FloatLayout(size_hint=(1, 0.11), 
                                    )
                card1.add_widget(floate)
                faction_b = MDFloatingActionButton(icon='comment',
                                                size_hint=(0.55, 0.85),
                                                pos_hint={"center_x": 0.5,"center_y": 0.5})
                icon_heart =MDIconButton(icon='cards-heart-outline',
                                        pos_hint={'x': 0.04, 'y': 0},
                                        icon_size="25sp")
                icon_alert =MDIconButton(icon='alert-box',
                                        pos_hint={'x': 0.82, 'y': 0},
                                        icon_size="25sp")
                floate.add_widget(faction_b)
                floate.add_widget(icon_heart)
                floate.add_widget(icon_alert)
                icon_alert.bind(on_release=show_report_dialog)
                icon_heart.bind(on_release=change_heart_color) 
    

        # Funcion de cambio de pantallas
    def change_screen(self, *args):
        self.manager.current = 'login'

    def on_enter2(self, *args):
        btn_f = self.ids.btn_f    # Funcion que permite interactuar a fondo con las screens
        btn_f.bind(on_press=self.change_screen)
    
    def exit_manager(self, *args):
        self.manager_open = False
        self.file_manager.close()

    def select_path(self, path: str):
        self.exit_manager()
        self.direccion = path
        print(self.direccion)
        return self.direccion
        
    def up_image(self):
            path = os.path.expanduser("~")
              # path to the directory that will be opened in the file manager
            self.file_manager.show(path)
            self.manager_open == True
            print(path)
            print(self.direccion)
            
    def agregar_publicaciones(self,*args):  #Funcion que permite agregar un box loyaut dentro del grid.
        titulo_pub = ''
        imagen_pub =''
        descripcion_pub = ''
        precio_pub = ''
        disponibilidad_pub = True
        
        titulo_pub = self.ids.AC.text
        precio_pub = self.ids.AC3.text
        descripcion_pub = self.ids.AC4.text
        imagen_pub = self.direccion

        print(titulo_pub)
        print(imagen_pub)
        print(precio_pub)
        print(descripcion_pub)

        with open(imagen_pub, "rb") as image2string:
            converted_string = base64.b64encode(image2string.read())
            
        def change_heart_color(instance):
            if instance.theme_text_color == "Custom" and instance.text_color == (1, 0, 0, 1):
                # Cambiar a color original
                instance.theme_text_color = "Primary"
            else:
                # Cambiar a color rojo
                instance.theme_text_color = "Custom"
                instance.text_color = (1, 0, 0, 1)
            # instance.theme_text_color = "Custom"
            # instance.text_color = (1, 0, 0, 1)  # Cambiar a color rojo

        def show_report_dialog(self, *args):
            dialog = MDDialog(
                title="Reportar publicación\n\n",
                type="custom",
                content_cls=BoxLayout(orientation="vertical", spacing="12dp"),
                buttons=[
                    MDFlatButton(text="CANCELAR", on_release=lambda x: dialog.dismiss()),
                    MDFlatButton(text="ENVIAR", on_release=send_report)
                ],
            )

            dialog.content_cls.add_widget(MDTextField(
                hint_text="Motivo del reporte",
                helper_text="Por favor, proporcione una breve descripción.",
                helper_text_mode="persistent"
            ))

            dialog.open()

        def send_report(self, *args):
            # Lógica para enviar el reporte de la publicación
            print("Reporte enviado")

        # ================== Conexion total para guardar ================
        conection_titulo = psycopg2.connect(dbname="postgresql", user="postgres", password="216472557",
                                                     host="localhost",
                                                     port="5432")
        cursor_points = conection_titulo.cursor()
        query_pub = '''INSERT INTO publicacion(idus,titulo,imagen,descrip,comida,electronico,libro,accesorios,papeleria,dispo,precio) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'''
        cursor_points.execute(query_pub,(id_user,titulo_pub,converted_string.decode('utf-8'),descripcion_pub,cat_comida,cat_electrico,cat_libro,cat_accesorios,cat_papeleria,disponibilidad_pub,precio_pub,))
        conection_titulo.commit()
        conection_titulo.close()

        # ===========================================================
        boxA = FloatLayout(size_hint=(1, 1))
        self.ids.container.add_widget(boxA)
        card1 = MDCard(
            orientation='vertical', 
            size_hint=(.95,.95),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            radius = 16)
        boxA.add_widget(card1)
        floatb = FloatLayout(size_hint=(1, 0.09))
        with floatb.canvas:
            Color(0.8, 0.8, 0.8, 1)
            floatb.Line = Line(points=(floatb.x, floatb.y, floatb.right, floatb.y), width=1)
        card1.add_widget(floatb)
        label_titulo = MDLabel(text=titulo_pub,
                               pos_hint={"center_x": 0.8, "center_y": 0.5})
        floatb.add_widget(label_titulo)
        def open_menu(instance):
            menu_items = [
                {
                    "text": "Editar",
                    "viewclass": "OneLineListItem",
                    "on_release": lambda: print("Opción 1 seleccionada"),
                },
                {
                    "text": "Eliminar",
                    "viewclass": "OneLineListItem",
                    "on_release": lambda: print("Opción 2 seleccionada"),
                },
            ]
            menu = MDDropdownMenu(
                caller=instance,
                items=menu_items,
                width_mult=4,
            )
            menu.open()
        iconbu = MDIconButton(icon="dots-vertical",pos_hint={"right": 1,"top": 1})
        iconbu.bind(on_release=open_menu)
        floatb.add_widget(iconbu)
        boxC = BoxLayout(size_hint=(1, 0.50), padding=(5,5,5,5))
        card1.add_widget(boxC)
        mdswiper = MDSwiper(size_hint=(1, 1), width_mult = 0.1)
        mdswiper_item1 = MDSwiperItem(size_hint=(1, 1),
                                      padding=(3,8,10,3))
        image1 = FitImage(source=imagen_pub,
                           size_hint=(1, 1))
        # MAS ITEMS MINIMO 3
        mdswiper_item1.add_widget(image1)
        mdswiper.add_widget(mdswiper_item1)
        boxC.add_widget(mdswiper)
        floatd = FloatLayout(size_hint=(0.95, 0.30),
                             pos_hint={'x':0 , 'y':0 },
                             )
        card1.add_widget(floatd)
        label_description = MDLabel(text=descripcion_pub, 
                                    pos_hint={'x': 0.05, 'y': 0.03},
                                    size_hint=(0.95, None))
        chip_usuario = MDChip(text=correo_verify,
                              icon_left = "account",
                              pos_hint={'x': 0.03, 'y': 0.75})
        chip_precio = MDChip(text=(precio_pub + '$'),
                              icon_left = "cash",
                              pos_hint={'x': 0.7, 'y': 0.75})
        floatd.add_widget(label_description)
        floatd.add_widget(chip_precio)
        floatd.add_widget(chip_usuario)
        floate = FloatLayout(size_hint=(1, 0.11), 
                             )
        card1.add_widget(floate)
        faction_b = MDFloatingActionButton(icon='comment',
                                           size_hint=(0.55, 0.85),
                                           pos_hint={"center_x": 0.5,"center_y": 0.5})
        #faction_b.self.ids.current = "comentarios"
        icon_heart =MDIconButton(icon='cards-heart-outline',
                                 pos_hint={'x': 0.04, 'y': 0},
                                 icon_size="25sp")
        icon_alert =MDIconButton(icon='alert-box',
                                 pos_hint={'x': 0.82, 'y': 0},
                                 icon_size="25sp")
        icon_alert.bind(on_release=show_report_dialog)
        floate.add_widget(faction_b)
        floate.add_widget(icon_heart)
        icon_heart.bind(on_press=change_heart_color)
        floate.add_widget(icon_alert)
        
        
        # Limpieza de datos ingresados
        clean_titulo = self.ids.AC
        clean_titulo.text=''
        clean_precio = self.ids.AC3
        clean_precio.text=''
        clean_descrip = self.ids.AC4
        clean_descrip.text=''
        clean_cat = self.ids.AC5
        clean_cat.text=''

    


    def on_enter(self, *args): #Buscar una alternativa ya que solo funciona con on_enter
        box = self.ids.box
        box.bind(on_press=self.agregar_publicaciones)

    def reinicio(self, *args):
        if control_creacion == True:
            self.ids.perfil_card.clear_widgets()
           
            print("Eliminacion completa")
        else:
            print("Aun no hay creacion")


    def perfil(self, *args):
        global control_creacion, esconder
        x = 0
        esconder = True
        variable_titulo = ''
        variable_precio = ''
        usuario_perfil = ''
        correo_perfil = ''
        
        def private(self, *args):
            float_control_list.clear_widgets()

        # ========================= PERFIL ==================
        conection = psycopg2.connect(dbname="postgresql", user="postgres", password="216472557",
                                                     host="localhost",
                                                     port="5432")
        cursor_points = conection.cursor()
        query_pub = '''SELECT nombre,correo FROM usuario WHERE id = %s'''
        cursor_points.execute(query_pub,(id_user,))
        datos_perfil = cursor_points.fetchone()
        conection.commit()
        conection.close()
        for x, valor in enumerate(datos_perfil):
            if x == 0:
                usuario_perfil = valor
                print(usuario_perfil)
            if x == 1:
                correo_perfil = valor
                print(correo_perfil)
        print(datos_perfil)

        card_perfil = MDCard(size_hint=(0.95, 0.30), 
                             pos_hint={'x':0.025 , 'y': 0.57})
        self.ids.perfil_card.add_widget(card_perfil)
        control_float = FloatLayout(size_hint=(1, 1))
        card_perfil.add_widget(control_float)
        icon_perfil = MDIconButton(icon_size="90sp", icon='C:\\Users\\PC BRYAN\\.virtualenvs\\mercadillo\\descarga.jpg',
                                   pos_hint={'x': 0, 'y': 0.35})
        control_float.add_widget(icon_perfil)
        nombre_user = MDLabel(size_hint=(1, 1),
                              pos_hint={'x': 0.35, 'y': 0.35},
                              text=usuario_perfil)
        control_float.add_widget(nombre_user)
        correo_user =  MDLabel(size_hint=(1, 1),
                              pos_hint={'x': 0.35, 'y': 0.15},
                              text=correo_perfil)
        control_float.add_widget(correo_user)
        Boton_privado = MDIconButton(icon="account-cancel", pos_hint={'x': 0.79, 'y': 0.05},
                               size_hint=(0.2, 0.3), md_bg_color=(0,0.5647058823529412, 0.7568627450980392,.6))
        control_float.add_widget(Boton_privado)
        Boton_privado.bind(on_release=private)

        # ===================== HISTORIAL ==========================
        conection = psycopg2.connect(dbname="postgresql", user="postgres", password="216472557",
                                                     host="localhost",
                                                     port="5432")
        cursor_points = conection.cursor()
        query_pub = '''SELECT titulo,precio FROM publicacion p INNER JOIN usuario u ON p.idUS = u.id WHERE u.id = %s'''
        cursor_points.execute(query_pub,(id_user,))
        datos_login = cursor_points.fetchall()
        conection.commit()
        conection.close()
        print(datos_login)

        float_control_list = FloatLayout(size_hint=(1, 0.5),pos_hint={'x': 0, 'y': 0})
        self.ids.perfil_card.add_widget(float_control_list)
        scroll = MDScrollView(pos_hint={'x':0.025 , 'y': 0.02})
        float_control_list.add_widget(scroll)
        label_historial = MDLabel(size_hint=(1, 1),
                                  pos_hint={'x': 0.24, 'y': 0.57},
                                  text='HISTORIAL-PUBLICACIONES')
        float_control_list.add_widget(label_historial)
        lista_historial = MDList(pos_hint={'x': 0.025, 'y': 1}, size_hint=(0.955,1 ), spacing=10)
        scroll.add_widget(lista_historial)
        for x in datos_login:
            for i, valor in enumerate(x):
                if i == 0:
                    variable_titulo = valor
                    print(variable_titulo)
                if i == 1:
                    variable_precio = valor
                    print(variable_precio)
                list1 = TwoLineIconListItem(text=variable_titulo,secondary_text=(variable_precio + '$'),radius=16,bg_color=(1,1,1,1))
                icon_historial =  IconLeftWidget(icon="text-box")
            list1.add_widget(icon_historial)
            lista_historial.add_widget(list1)
            control_creacion = True
        

class recover(Screen): # Pantalla de recuperacion de contrasena
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        #Boton
        btn2 = Button(text='regresar', size_hint=(0.3, 0.06), pos_hint={'x': 0.35, 'y': 0.10},background_color = (0.2196078431372549,0.6823529411764706, 0.8, 0.45))
        btn2.bind(on_press=self.back)
        self.add_widget(btn2)
        
        btn = Button(text='Recuperacion', size_hint=(0.3, 0.06), pos_hint={'x': 0.35, 'y': 0.20},background_color = (0.2196078431372549,0.6823529411764706, 0.8, 0.45))
        btn.bind(on_press=self.recuperar_contra)
        self.add_widget(btn)

    def recuperar_contra(self, *args):
        correo_rec = self.ids.z.text
        nueva_contra = self.ids.w.text

        conection = psycopg2.connect(dbname="postgresql", user="postgres", password="216472557",
                                                     host="localhost",
                                                     port="5432")
        cursor_points = conection.cursor()
        query_pub = '''UPDATE usuario SET contrasena = %s WHERE correo = %s'''
        cursor_points.execute(query_pub,(nueva_contra,correo_rec,))
        conection.commit()
        conection.close()
        self.manager.current = 'login'
        clean_text = self.ids.z
        clean_text.text=''
        clean_text_contra = self.ids.w
        clean_text_contra.text=''
    
    def back(self, *args):
        self.manager.current = 'login'
    

class ScreenManagerApp1(ScreenManager):
	pass

class cont(FloatLayout):
    pass

class MainApp(MDApp):
    title = 'Merca Cucei'
    def build(self):
        sm = ScreenManagerApp1(transition=FadeTransition())
        sm.add_widget(Login(name="login"))
        sm.add_widget(Register(name="register"))
        sm.add_widget(home(name="home"))
        sm.add_widget(recover(name="recover"))
        
        
        return sm

if __name__ == '__main__':
	MainApp().run()