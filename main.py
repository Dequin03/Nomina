import flet as ft

def main(page: ft.Page):
    conteiner = ft.Container(
        ft.Column([
            # Contenedor de la imagen
            ft.Container(
                ft.Image(
                    src="https://jumapam.gob.mx/images/JPG/jumapam.jpg",  # Cambia a la URL o ruta de tu imagen
                    width=120,
                    height=120,
                    fit=ft.ImageFit.CONTAIN
                ),
                alignment=ft.alignment.center,  # Centra la imagen dentro de su contenedor
                padding=ft.padding.only(20, 20)
            ),
            ft.Container(
                ft.Text(
                    "Iniciar Sesión",
                    color="black",
                    width=320,
                    size=30,
                    text_align="center",
                    weight="w900"
                ),
                padding=ft.padding.only(20, 20),
                alignment=ft.alignment.center
            ),
            ft.Container(
                ft.TextField(
                    width=280,  # Aumenta el ancho del campo para que quede alineado con el contenedor
                    height=40,
                    hint_text="Correo electrónico",
                    border="underline",
                    color="black",
                    prefix_icon=ft.icons.EMAIL,
                ),
                padding=ft.padding.only(20, 10),
                alignment=ft.alignment.center  # Centra el campo en el contenedor
            ),
            ft.Container(
                ft.TextField(
                    width=280,  # Aumenta el ancho del campo para que quede alineado con el contenedor
                    height=40,
                    hint_text="Contraseña",
                    border="underline",
                    color="black",
                    prefix_icon=ft.icons.LOCK,
                    password=True
                ),
                padding=ft.padding.only(20, 10),
                alignment=ft.alignment.center  # Centra el campo en el contenedor
            ),
            ft.Container(
                ft.ElevatedButton(
                    text="Iniciar",
                    width=280,
                    bgcolor="black",
                    color="white",
                    on_click=lambda e: page.go('/Login/python.py')  # Cambia "pyton" a "python" si es necesario
                ),
                padding=ft.padding.only(20, 20),
                alignment=ft.alignment.center  # Centra el botón en el contenedor
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,  # Centra verticalmente el contenido en la columna
        horizontal_alignment=ft.CrossAxisAlignment.CENTER  # Centra horizontalmente el contenido en la columna
        ),
        border_radius=20,
        width=360,
        height=500,
        gradient=ft.LinearGradient([
            ft.colors.WHITE,
        ])
    )
    
    # Configura la alineación de la página para centrar el contenedor en la mitad de la pantalla
    page.title = 'login'
    page.bgcolor = ft.colors.BLUE_900
    page.padding = 0
    page.vertical_alignment = "center"  # Centra verticalmente el contenedor en la pantalla
    page.horizontal_alignment = "center"  # Centra horizontalmente el contenedor en la pantalla
    page.add(conteiner)

ft.app(target=main)
