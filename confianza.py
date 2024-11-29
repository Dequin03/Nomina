import flet as ft

class AnimatedApp(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.color_title = ft.colors.BLUE_600
        self.color_container = ft.colors.LIGHT_BLUE_100
        self.title_color = ft.colors.BLACK
        self.image = ft.Container(
            content=ft.Image(
                src="https://jumapam.gob.mx/images/JPG/jumapam.jpg",
                width=40,
                height=40,
                fit=ft.ImageFit.CONTAIN
            ),
            padding=ft.padding.only(left=10)
        )
        self.title_text = ft.Text("Jumapam", size=30, color=self.title_color, weight=ft.FontWeight.BOLD)
        self.spacing_container = ft.Container(width=200)
        self.white_container = ft.Container(
            bgcolor=ft.colors.WHITE,
            width=400,
            height=30,
            alignment=ft.alignment.center,
            content=ft.Text("Periodo", color=ft.colors.BLACK),
            border_radius=5,
        )
        self.logout_button = ft.ElevatedButton(
            text="Cerrar sesión",
            bgcolor=ft.colors.RED_400,
            color=ft.colors.WHITE,
            width=140,
            height=40,
            on_click=self.logout
        )
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
                    self.spacing_container,
                    self.white_container,
                    ft.Container(
                        content=self.logout_button,
                        alignment=ft.alignment.center_right,
                        expand=True,
                        padding=ft.padding.only(top=5, right=10)
                    )
                ],
                vertical_alignment=ft.CrossAxisAlignment.CENTER
            )
        )
        
        # Encabezados de la tabla (definidos correctamente)
        self.table_headers = ft.Row(
            
            controls=[
                ft.Text("ID", size=16, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK, text_align="center", width=70),
                ft.Text("Nombre", size=16, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK, text_align="center", width=200),
                ft.Text("Proyecto", size=16, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK, text_align="center", width=70),
                
                    ft.Text("Lunes", size=16, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK, text_align="center", width=80),
                   ft.Text("Martes", size=16, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK, text_align="center", width=100),
                   ft.Text("Miercoles", size=16, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK, text_align="center", width=80),
                   ft.Text("Jueves", size=16, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK, text_align="center", width=90),
                   ft.Text("Viernes", size=16, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK, text_align="center", width=90),
                   ft.Text("Sabado", size=16, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK, text_align="center", width=90),
                   ft.Text("Domingo", size=16, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK, text_align="center", width=90),
                   
                ft.Text("Comentarios", size=16, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK, text_align="center", width=160),
                ft.Text("Añadir", size=16, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK, text_align="center", width=60),
            ]
        )
        
        # Dropdowns
        self.dropdown_sindicato_confianza = ft.Dropdown(                                                
            width=150,
            height=40,
            bgcolor=ft.colors.GREY_100,
            color=ft.colors.BLACK,
            hint_text="Seleccione...",
            options=[
                ft.dropdown.Option("Sindicato"),
                ft.dropdown.Option("Confianza")
            ],
            padding=ft.padding.only(left=10, right=10),
            on_change=self.update_departamento_state
        )
        self.dropdown_departamento = ft.Dropdown(
            width=150,
            height=40,
            bgcolor=ft.colors.GREY_100,
            color=ft.colors.BLACK,
            hint_text="Seleccione...",
            options=[
                ft.dropdown.Option("1111"),
                ft.dropdown.Option("2222")
            ],
            padding=ft.padding.only(left=10, right=10),
            disabled=True  # Inicialmente deshabilitado
        )
        
        # Tabla con scroll
        self.remaining_container = ft.Container(
            expand=True,
            content=ft.Column(
                controls=[
                    ft.Container(
                        height=560,
                        bgcolor=self.color_container,
                        border_radius=10,
                        alignment=ft.alignment.center_left,
                        content=ft.Column(
                            controls=[
                                ft.Container(
                                    padding=ft.padding.only(top=20),
                                    content=ft.Row(
                                        controls=[
                                            self.dropdown_sindicato_confianza,
                                            ft.Container(width=20),
                                            ft.Text("Seleccione un Departamento:", size=20, color="BLACK"),
                                            self.dropdown_departamento,
                                            ft.Container(width=100),
                                            ft.TextField("",  color="black",bgcolor="white",hint_text="Buscar", height=40,),
                                            ft.Container(width=1),
                                            ft.ElevatedButton(text="Buscar",bgcolor=ft.colors.BLUE_800,color=ft.colors.WHITE, on_click=self.send_data,height=40 ),
                                        ]
                                    )
                                ),
                                # Aquí agregas los datos de la tabla en las filas
                                ft.Container(
                                    height=400,
                                    bgcolor=ft.colors.BLUE_300,
                                    border_radius=10,
                                    padding=ft.padding.all(5),
                                    content=ft.Row(
                                        scroll=ft.ScrollMode.ALWAYS,
                                        controls=[
                                            ft.Column(
                                                scroll=ft.ScrollMode.ALWAYS,
                                                controls=[
                                                    self.table_headers,  # Encabezados
                                                    *[  # Aquí agregas las filas de datos
                                                        ft.Row(
                                                            controls=[
                                                                ft.TextField(value="1111", height=60, width=70, color="black", bgcolor=ft.colors.BLUE_300, disabled=True, multiline=True, min_lines=1, max_lines=2, text_size=13, border="none", text_align="center"),
                                                                ft.TextField(value="Kevin Alan Quintero Barragan", height=60, width=200, bgcolor=ft.colors.BLUE_300, disabled=True, multiline=True, min_lines=1, max_lines=2, text_size=13, border="none", color="black", text_align="center"),
                                                                ft.TextField(value="0002", height=60, width=70, color="black", bgcolor=ft.colors.BLUE_300, disabled=True, multiline=True, min_lines=1, max_lines=2, text_size=13, border="none", text_align="center"),
                                                                *[ft.Column(
                                                                    controls=[
                                                                        ft.Row(
                                                                            controls=[
                                                                                ft.TextField(height=35, width=40, color="black", hint_text="HE", bgcolor="white", text_align="center", text_size=10, tooltip="Horas Extras"),
                                                                                ft.Checkbox(value=True, check_color="black", fill_color="white", tooltip="Asistencia"),
                                                                            ]
                                                                        ),
                                                                        ft.Row(
                                                                            controls=[
                                                                                ft.TextField(height=35, width=40, color="black", hint_text="DT", bgcolor="white", text_align="center", text_size=10, tooltip="Descanzos Trabajados"),
                                                                                ft.TextField(height=35, width=40, color="black", hint_text="TE", bgcolor="white", text_align="center", text_size=10, tooltip="Turnos Extras"),
                                                                            ]
                                                                        ),
                                                                    ]
                                                                ) for _ in range(7)],  # Generar 7 columnas
                                                                ft.TextField(height=50, width=150, color="black", hint_text="Comentarios", bgcolor="white", multiline=True, min_lines=1, max_lines=2, text_size=13),
                                                                ft.ElevatedButton(text="Añadir", icon=ft.icons.ADD, width=60, height=50, bgcolor=ft.colors.BLUE_900, color=ft.colors.WHITE, on_click=self.send_data),
                                                            ]
                                                        ) for _ in range(20)  # Generar 20 filas
                                                    ]
                                                ]
                                            )
                                        ]
                                    )
                                ),
                                 ft.Container(
                                        padding=ft.padding.only(top=0, left=20),
                                            content=ft.Row(
                                                controls=[
                                                    ft.ElevatedButton(
                                                        text="Añadir Proyectos",
                                                        bgcolor=ft.colors.BLUE_800,
                                                        color=ft.colors.WHITE,
                                                        on_click=self.send_data
                                                    ),
                                                    ft.ElevatedButton(
                                                        text="Generar Reporte",
                                                        bgcolor=ft.colors.BLUE_800,
                                                        color=ft.colors.WHITE,
                                                        on_click=self.send_data
                                                    ),
                                                    ft.ElevatedButton(
                                                        text="Añadir a Todos",
                                                        bgcolor=ft.colors.BLUE_800,
                                                        color=ft.colors.WHITE,
                                                        on_click=self.send_data
                                                    ),
                                                ],
                                                spacing=25,  # Espaciado entre botones
                                                alignment=ft.MainAxisAlignment.START,  # Alinear los botones al inicio
                                            )
                                        )
                            ],
                            spacing=10
                        )
                    )
                ]
            )
        )

        self.controls = [
            ft.Column(
                expand=True,
                controls=[self.frame_title, self.remaining_container]
            )
        ]

    def logout(self, e):
        print("Cierre de sesión realizado.")

    def send_data(self, e):
        print("Datos enviados.")

    def update_departamento_state(self, e):
        """
        Método para habilitar o deshabilitar el dropdown de departamento
        según la selección del primer dropdown.
        """
        if self.dropdown_sindicato_confianza.value:  # Si hay una selección
            self.dropdown_departamento.disabled = False
        else:  # Si no hay selección
            self.dropdown_departamento.disabled = True
        self.update()  # Refrescar la interfaz para reflejar los cambios

def main(page: ft.Page):
    page.bgcolor = ft.colors.BLACK
    app = AnimatedApp()
    page.add(app)

ft.app(target=main)
