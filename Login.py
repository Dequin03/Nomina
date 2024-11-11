import flet as ft
from flet import (
    AppBar,
    ElevatedButton,
    Page,
    Text,
    View,
    colors,
    Column,
    Container,
    LinearGradient,
    alignment,
    border_radius,
    padding,
    Image,
    UserControl,
    Row,
    IconButton,
    margin,
    Card,
    TextField,
    FilledButton,
    SnackBar
)
import requests
import pyodbc
from tkinter import messagebox, ttk  # Agregar ttk para el combobox
import socket
import base64
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import pikepdf
import win32com.client as win32
import os
from datetime import datetime, timedelta,date
KEY_ENCRYPT_DECRYPT = "r3c6rs0sm4t3r14l3sj6m4p4mm4z4tl4ns1n4l04l4p13ld3lm4rr3c6rs0sm4t3r14l3sj6m4p4mm4z4tl4ns1n4l04l4p13ld3lm4r"
periodos=""
def conectar_bd_periodos():
    conexion = pyodbc.connect(
        'DRIVER={SQL Server};'
        f'SERVER={host}\SQLEXPRESS;'
        'DATABASE=BdTrabajadTemporal;'  # Base de datos de usuarios
        'Trusted_Connection=yes;'
    )
    cursor = conexion.cursor()
    return conexion, cursor
def obtener_periodo(x):
    hoy=date.today()
    if x==1:
        conexion, cursor = conectar_bd_periodos()
        cursor.execute("SELECT CLAVE_PERIODO, CLAVE_TIPO_NOMINA, DESCRIPCION FROM PERIODO WHERE CLAVE_TIPO_NOMINA=1 AND ? BETWEEN FECHA_I AND FECHA_F",str(hoy))
        periodo = cursor.fetchall()
        conexion.close()
        return periodo
    else:
        conexion, cursor = conectar_bd_periodos()
        cursor.execute("SELECT CLAVE_PERIODO, CLAVE_TIPO_NOMINA, DESCRIPCION FROM PERIODO WHERE CLAVE_TIPO_NOMINA=2 AND ? BETWEEN FECHA_I AND FECHA_F",str(hoy))
        periodo = cursor.fetchall()
        conexion.close()
        return periodo
def excel_to_pdf(excel_file, pdf_file):
    # Initialize Excel application (headless)
    excel = win32.gencache.EnsureDispatch("Excel.Application")
    excel.Visible = False  # Keep Excel hidden

    # Open the workbook
    workbook = excel.Workbooks.Open(excel_file)

    # Save as PDF
    workbook.ExportAsFixedFormat(0, pdf_file)

    # Close the workbook and Excel application
    workbook.Close(SaveChanges=False)
    

    # Clean up resources
    del excel
    def encrypt_pdf(input_pdf, output_pdf, user_password, owner_password):
        print("hoila")
        # Encrypt the PDF using pikepdf
        with pikepdf.open(input_pdf) as pdf:
            pdf.save(
                output_pdf,
                encryption=pikepdf.Encryption(
                    user=user_password,
                    owner=owner_password,
                    allow=pikepdf.Permissions(extract=False, print_lowres=False, modify_annotation=False,modify_assembly=False,modify_form=False,modify_other=False)
                )
            )

    # Set file paths and passwords
    original_pdf = r"C:\Users\usuario\Downloads\Nomina\output\output.pdf"
    encrypted_pdf = "protected_document.pdf"
    user_password = "userpass123"
    owner_password = "ownerpass456"

    # Create the PDF and then encrypt it
    encrypt_pdf(original_pdf, encrypted_pdf, user_password, owner_password)

# Specify the Excel and PDF file paths
excel_file = os.path.abspath("C:\\Users\\usuario\\Downloads\\Nomina\\Formatollenado.xlsx")
pdf_file = os.path.abspath("C:\\Users\\usuario\\Downloads\\Nomina\\output\\output.pdf")
class AnimatedApp(ft.UserControl):
    def __init__(self):
        super().__init__()
         # Crear el Dropdown de departamentos vacío inicialmente
        self.dropdown_departamentos = ft.Dropdown(
            width=150,
            height=40,
            bgcolor=ft.colors.GREY_300,
            color=ft.colors.BLACK,
            hint_text="Seleccione...",
            padding=ft.padding.only(left=10, right=10)
        )
        self.dropdown_tipo_empleado = ft.Dropdown(
            width=150,
            height=40,
            bgcolor=ft.colors.GREY_300,
            color=ft.colors.BLACK,
            hint_text="Seleccione...",
            value="Sindicato",  # Establecer "Sindicato" como valor predeterminado
            options=[
                ft.dropdown.Option("Sindicato"),
                ft.dropdown.Option("Confianza")
            ],
            padding=ft.padding.only(left=10, right=10),
            on_change=self.tipo_empleado_cambiado  # Llama a la función cuando cambia el valor
        )
        # Llenar el Dropdown de departamentos
        self.llenar_departamentos()
        periodos=self.tipo_empleado_cambiado()
        # Variables de color de ejemplo; reemplázalas según sea necesario
        self.color_title = ft.colors.BLUE_ACCENT_700
        self.color_container = ft.colors.LIGHT_BLUE_100
        self.title_color = ft.colors.BLACK  # Color del título

        # Crear el contenedor de la imagen con un pequeño padding a la izquierda
        self.image = ft.Container(
            content=ft.Image(
                src="https://jumapam.gob.mx/images/JPG/jumapam.jpg",
                width=40,
                height=40,
                fit=ft.ImageFit.CONTAIN
            ),
            padding=ft.padding.only(left=10)  # Espacio a la izquierda
        )

        # Configuración del título
        self.title_text = ft.Text("Jumapam", size=30, color=self.title_color, weight=ft.FontWeight.BOLD)

        # Contenedor vacío para crear un espacio adicional
        self.spacing_container = ft.Container(
            width=200  # Ancho del espacio a la derecha del título
        )
        # Contenedor donde va el periodo, con padding a la izquierda
        self.white_container = ft.Container(
            bgcolor=ft.colors.WHITE,  # Color de fondo blanco
            width=400,  # Ancho del contenedor
            height=30,  # Altura del contenedor
            alignment=ft.alignment.center,  # Alinear contenido al centro
            content=ft.Text(periodos, color=ft.colors.BLACK),  # Texto dentro del contenedor
            border_radius=5,
        )

        # Botón de cerrar sesión
        self.logout_button = ft.ElevatedButton(
            text="Cerrar sesión",
            bgcolor=ft.colors.RED_400,
            color=ft.colors.WHITE,
            width=140,
            height=40,
            on_click=self.logout  # Función para manejar el evento de clic
        )

        # Contenedor con imagen, título y botón en una fila
        self.frame_title = ft.Container(
            expand=False,
            height=60,
            bgcolor=self.color_title,
            border_radius=10,
            alignment=ft.alignment.center_left,
            content=ft.Row(
                controls=[
                    self.image,
                    self.title_text,
                    self.spacing_container,  # Espacio antes del contenedor blanco
                    self.white_container,
                    ft.Container(
                        content=self.logout_button,
                        alignment=ft.alignment.center_right,
                        expand=True,
                        padding=ft.padding.only(top=5, right=10)  # Espacio en la parte superior y derecha
                    )
                ],
                vertical_alignment=ft.CrossAxisAlignment.CENTER
            )
        )

        # Contenedor que contiene los Dropdowns, la tabla y el nuevo botón
        self.remaining_container = ft.Container(
            expand=True,
            content=ft.Column(
                controls=[
                    ft.Container(
                        height=560,  # Mantiene el tamaño del contenedor adicional
                        bgcolor=self.color_container,
                        border_radius=10,
                        alignment=ft.alignment.center_left,
                        content=ft.Column(
                            controls=[
                                ft.Container(  # Contenedor para los Dropdowns
                                    padding=ft.padding.only(top=20),  # Espacio superior para los Dropdowns
                                    content=ft.Row(  # Usar Row para alinear horizontalmente
                                        controls=[
                                            self.dropdown_tipo_empleado,
                                            ft.Container(
                                                width=20  # Espacio entre los Dropdowns
                                            ),
                                            ft.Text("Seleccione un Departamento:", size=20, color="BLACK"),  # Texto descriptivo
                                            self.dropdown_departamentos
                                        ]
                                    )
                                ),
                                # Tabla de ID, nombre, número y días
                                ft.Container(
                                    padding=ft.padding.only(top=20),
                                    content=ft.Column(
                                        controls=[
                                            ft.Row(
                                                controls=[
                                                    ft.Text("ID", size=16, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                                                    ft.Text("Nombre", size=16, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                                                    ft.Text("Número", size=16, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                                                    ft.Text("Lunes", size=16, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                                                    ft.Text("Martes", size=16, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                                                    ft.Text("Miércoles", size=16, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                                                    ft.Text("Jueves", size=16, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                                                    ft.Text("Viernes", size=16, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                                                    ft.Text("Sábado", size=16, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                                                    ft.Text("Domingo", size=16, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                                                ],
                                                alignment=ft.MainAxisAlignment.SPACE_EVENLY
                                            ),
                                            ft.Container(
                                                bgcolor=ft.colors.BLUE_600,  # Fondo azul claro para la fila
                                                padding=ft.padding.all(2),  # Espaciado dentro de la fila
                                                content=ft.Row(
                                                    controls=[
                                                        ft.Text("1", color=ft.colors.BLACK),
                                                        ft.Text("Ejemplo 1", color=ft.colors.BLACK),
                                                        ft.Text("001", color=ft.colors.BLACK),
                                                        *[ft.Checkbox(value=False) for _ in range(7)]  # Checkbox para cada día
                                                    ],
                                                    alignment=ft.MainAxisAlignment.SPACE_EVENLY
                                                )
                                            ),
                                            ft.Container(
                                                bgcolor=ft.colors.BLUE_300,  # Fondo azul claro para la fila
                                                padding=ft.padding.all(5),  # Espaciado dentro de la fila
                                                content=ft.Row(
                                                    controls=[
                                                        ft.Text("2", color=ft.colors.BLACK),
                                                        ft.Text("Ejemplo 2", color=ft.colors.BLACK),
                                                        ft.Text("002", color=ft.colors.BLACK),
                                                        *[ft.Checkbox(value=False) for _ in range(7)]  # Checkbox para cada día
                                                    ],
                                                    alignment=ft.MainAxisAlignment.SPACE_EVENLY
                                                )
                                            ),
                                        ]
                                    )
                                ),
                                # Botón adicional debajo de la tabla
                                ft.Container(
                                    alignment=ft.alignment.top_left,
                                    padding=ft.padding.only(top=20, left=10),
                                    content=ft.ElevatedButton(
                                        text="Generar Reporte",
                                        bgcolor=ft.colors.BLUE_800,
                                        color=ft.colors.WHITE,
                                        on_click=self.send_data  # Función que manejará el evento del botón
                                    )
                                )

                            ],
                            spacing=10
                        )
                    )
                ]
            )
        )
        # Agregar los contenedores a la página
        self.controls = [
            ft.Column(
                expand=True,
                controls=[
                    self.frame_title,
                    self.remaining_container
                ]
            )
        ]
    def llenar_departamentos(self):
        # Crear las opciones para el Dropdown de departamentos
        opciones_departamentos = [ft.dropdown.Option(depto) for depto in departamentos]

        # Asignar las opciones generadas al Dropdown de departamentos
        self.dropdown_departamentos.options = opciones_departamentos
    def tipo_empleado_cambiado(self, e=None):
        # Obtiene el valor seleccionado en el primer Dropdown
        tipo_empleado = self.dropdown_tipo_empleado.value

        # Actualiza el Dropdown de departamentos basado en el valor seleccionado
        if tipo_empleado == "Sindicato" or tipo_empleado=="":
            periodos = obtener_periodo(2)
        elif tipo_empleado == "Confianza":
            periodos = obtener_periodo(1)
        for i, periodo in enumerate(periodos):
            periodos=periodo[2]
        return periodos
    def logout(self, e):
        # Acción a realizar al hacer clic en "Cerrar sesión"
        print("Cierre de sesión realizado.")  # Puedes cambiar esta línea por la lógica de cierre de sesión que desees.

    def send_data(self, e):
        excel_to_pdf(excel_file, pdf_file)
        print("Datos enviados.")  # Puedes reemplazar esto con la lógica que necesites para enviar los datos

    def bar_icons(self, e):
        # Acción para el icono del botón de inicio (sin uso en este caso)
        pass

def encrypt(plain_text):
    str_out = ""
    outx_ = bytearray(len(plain_text))
    idx_ = plain_text.encode('utf-16le')  # Encoding in UTF-16LE (Little Endian) similar to Encoding.Unicode
    key_idx_ = KEY_ENCRYPT_DECRYPT.encode('utf-16le')  # Same encoding for the key
    nbyte = 0
    for n_pos in range(0, len(idx_), 2):
        # Perform XOR between the byte of the plain text and the key
        c = chr(idx_[n_pos] ^ key_idx_[n_pos])
        str_out += c
        outx_[nbyte] = idx_[n_pos] ^ key_idx_[n_pos]
        nbyte += 1
    # Convert the resulting byte array to a base64 string
    return base64.b64encode(outx_).decode('utf-8')
host=socket.gethostname()
departamentos=[]
def obtener_departamentos(user):
        conexion, cursor = conectar_bd_usuarios()
        cursor.execute("SELECT ID_USUARIO FROM MAE_SISTEMAS_USUARIOS WHERE NOMBRE_USUARIO=?",user)
        r=cursor.fetchone()
        id= str(r[0])
        cursor.execute("SELECT CLAVE_DEPARTAMENTO FROM HIS_SISTEMAS_DEPUSER WHERE ID_USUARIO=?",id)
        for i in cursor:
            departamentos.append(str(i[0]))
        conexion.close()
        return departamentos
def conectar_bd_usuarios():
        conexion = pyodbc.connect(
            'DRIVER={SQL Server};'
            f'SERVER={host}\SQLEXPRESS;'
            'DATABASE=JumapamSistemas;'  # Base de datos de usuarios
            'Trusted_Connection=yes;'
        )
        cursor = conexion.cursor()
        return conexion, cursor
def main(page: ft.Page):
    page.title = "Fife's app"
    page.add(Text("Welcome"))
    snack = SnackBar(
        Text("Registration successful")
    )
    def verificar_acceso(username, password):
        try:
            conexion, cursor = conectar_bd_usuarios()
            usuario = username
            password = password
            version = '1.0'
            id_sistema = 12
            host_name = 'DESKTOP'
            cursor.execute("{CALL spAccesoSistemas (?, ?, ?, ?, ?, ?, ?)}", 
                    usuario, password, "mac", "ip", version, id_sistema, host_name)
            # Obtener los resultados
            rows = cursor.fetchmany()
            conexion.commit()
            if "Acceso Correcto|" in str(rows[0]):
                return True
            return False

        except Exception as e:
            messagebox.showerror("Error", f"Error al ejecutar el Proceso Almacenado: {e}")
        # Cerrar la conexión
        if conexion:
            conexion.close()
        # Función que maneja el inicio de sesión
    def iniciar_sesion(e, username, password):
        username = username
        password = encrypt(password)    
        if verificar_acceso(username, password):
            obtener_departamentos(username)
            page.views.append(
                ft.View(
                "/home",
                [
                    ft.AppBar(title=ft.Text("Home Page"), bgcolor=ft.colors.AMBER_ACCENT_700),
                    ft.Text(f"Welcome, {username}!!"),
                    AnimatedApp()
                ]
                )        
            )
            page.update()
            
        else:
            snack.content.value = "Invalid username" # type: ignore
            snack.open = True
            page.update()
    def req_register(e, username, password):
        data = {
            "username": username,
            "password": password,
        }
        response = requests.post("http://127.0.0.1:8000/register", json=data)

        if response.status_code == 201:
            snack.open = True
            page.update()
        elif response.status_code == 400:
            snack.content.value = "User already exists!" # type: ignore
            snack.open = True
            page.update()
        else:
            snack.content.value = "You were not registered" # type: ignore
            snack.open = True
            page.update()

    def req_login(e, username, password):
        data = {
            "username": username,
            "password": password,
        }
        response = requests.post("http://127.0.0.1:8000/login", json=data)

        if response.status_code == 200:

            page.views.append(
                ft.View(
                "/home",
                [
                    ft.AppBar(title=ft.Text("Home Page"), bgcolor=ft.colors.AMBER_ACCENT_700),
                    ft.Text(f"Bienvenido, {username}!!"),
                ]
                )
            )
            page.update()
        if response.status_code == 404:
            snack.content.value = "Usuario Invalido" # type: ignore
            snack.open = True
            page.update()
        if response.status_code == 401:
            snack.content.value = "Contraseña Invalida" # type: ignore
            snack.open = True
            page.update()
    
    def route_change(route):
        username = TextField(
            label="Usuario",
            border="underline", # type: ignore
            width=320,
            text_size=14,
        )

        password = TextField(
            label="Contraseña",
            border="underline", # type: ignore
            width=320,
            text_size=14,
            password=True,
            can_reveal_password=True
        )

        page.views.clear()
        page.views.append(
            ft.View(
                "/register",
                [
                    ft.AppBar(title=ft.Text("Register here"), bgcolor=ft.colors.SURFACE_VARIANT),
                    username,
                    password,
                    ft.Row([
                        ft.ElevatedButton("Register", on_click=lambda e: iniciar_sesion(e, username.value, password.value)),
                        ft.FilledButton("Already registered?", on_click=lambda e: page.go("/login"))
                    ]),
                    
                    snack,
                ],
            )
        )
        if page.route == "/login":
            page.views.append(
                ft.View(
                    "/login",
                    [
                        ft.AppBar(title=ft.Text("Inicio de sesion"), bgcolor=ft.colors.SURFACE_VARIANT),
                        username,
                        password,
                        ft.FilledButton("Ingreso", on_click=lambda e: iniciar_sesion(e, username.value, password.value)),
                        # ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/home")),
                    ],
                )
            )

        page.update()


    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

ft.app(target=main)