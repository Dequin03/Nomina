import flet as ft

class AnimatedApp(ft.UserControl):
    def __init__(self):
        super().__init__()

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
            content=ft.Text("Periodo", color=ft.colors.BLACK),  # Texto dentro del contenedor
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
                                            ft.Dropdown(
                                                width=150,  # Ancho interno del Dropdown
                                                height=40,
                                                bgcolor=ft.colors.GREY_300,  # Fondo del Dropdown
                                                color=ft.colors.BLACK,  # Color del texto del Dropdown
                                                hint_text="Seleccione...",  # Texto dentro del Dropdown cuando no hay opción seleccionada
                                                options=[
                                                    ft.dropdown.Option("Sindicato"),
                                                    ft.dropdown.Option("Confianza")
                                                ],
                                                padding=ft.padding.only(left=10, right=10)  # Padding horizontal para separar del borde
                                            ),
                                            ft.Container(
                                                width=20  # Espacio entre los Dropdowns
                                            ),
                                            ft.Text("Seleccione un Departamento:", size=20, color="BLACK"),  # Texto descriptivo
                                            ft.Dropdown(
                                                width=150,  # Ancho interno del Dropdown
                                                height=40,
                                                bgcolor=ft.colors.GREY_300,  # Fondo del Dropdown
                                                color=ft.colors.BLACK,  # Color del texto del Dropdown
                                                hint_text="Seleccione...",  # Texto dentro del Dropdown cuando no hay opción seleccionada
                                                options=[
                                                    ft.dropdown.Option("1111"),
                                                    ft.dropdown.Option("2222")
                                                ],
                                                padding=ft.padding.only(left=10, right=10)  # Padding horizontal para separar del borde
                                            )
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

    def logout(self, e):
        # Acción a realizar al hacer clic en "Cerrar sesión"
        print("Cierre de sesión realizado.")  # Puedes cambiar esta línea por la lógica de cierre de sesión que desees.

    def send_data(self, e):
        # Acción a realizar al hacer clic en "Enviar"
        print("Datos enviados.")  # Puedes reemplazar esto con la lógica que necesites para enviar los datos

    def bar_icons(self, e):
        # Acción para el icono del botón de inicio (sin uso en este caso)
        pass

# Función para inicializar la aplicación
def main(page: ft.Page):
    page.bgcolor = ft.colors.BLACK
    app = AnimatedApp()
    page.add(app)

# Ejecutar la aplicación
ft.app(target=main)
