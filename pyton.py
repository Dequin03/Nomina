import flet as ft

class AnimatedApp(ft.UserControl):
    def __init__(self):
        super().__init__()

        self.color_title = ft.colors.BLUE_ACCENT_700
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
                                            ft.Dropdown(
                                                width=150,
                                                height=40,
                                                bgcolor=ft.colors.GREY_300,
                                                color=ft.colors.BLACK,
                                                hint_text="Seleccione...",
                                                options=[
                                                    ft.dropdown.Option("Sindicato"),
                                                    ft.dropdown.Option("Confianza")
                                                ],
                                                padding=ft.padding.only(left=10, right=10)
                                            ),
                                            ft.Container(width=20),
                                            ft.Text("Seleccione un Departamento:", size=20, color="BLACK"),
                                            ft.Dropdown(
                                                width=150,
                                                height=40,
                                                bgcolor=ft.colors.GREY_300,
                                                color=ft.colors.BLACK,
                                                hint_text="Seleccione...",
                                                options=[
                                                    ft.dropdown.Option("1111"),
                                                    ft.dropdown.Option("2222")
                                                ],
                                                padding=ft.padding.only(left=10, right=10)
                                            )
                                        ]
                                    )
                                ),
                                ft.Container(
                                    padding=ft.padding.only(top=20),
                                    content=ft.Column(
                                        controls=[
                                            ft.Row(
                                                controls=[
                                                    ft.Container(content=ft.Text("ID", size=16, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK), padding=ft.padding.only(left=20,right=10, top=0, bottom=0)),
                                                    ft.Container(content=ft.Text("Nombre", size=16, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),  padding=ft.padding.only(left=20,right=90, top=0, bottom=0)),
                                                    ft.Container(content=ft.Text("Proyecto", size=16, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK), alignment=ft.alignment.center_left),
                                                    ft.Container(content=ft.Text("Lunes", size=16, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK), padding=ft.padding.only(left=4,right=25, top=0, bottom=0)),
                                                    ft.Container(content=ft.Text("Martes", size=16, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK), padding=ft.padding.only(left=0,right=25, top=0, bottom=0)),
                                                    ft.Container(content=ft.Text("Miércoles", size=16, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK), padding=ft.padding.only(left=0,right=25, top=0, bottom=0)),
                                                    ft.Container(content=ft.Text("Jueves", size=16, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK), padding=ft.padding.only(left=0,right=25, top=0, bottom=0)),
                                                    ft.Container(content=ft.Text("Viernes", size=16, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK), padding=ft.padding.only(left=0,right=25, top=0, bottom=0)),
                                                    ft.Container(content=ft.Text("Sábado", size=16, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK), padding=ft.padding.only(left=0,right=25, top=0, bottom=0)),
                                                    ft.Container(content=ft.Text("Domingo", size=16, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK), padding=ft.padding.only(left=0,right=25, top=0, bottom=0)),
                                                    ft.Container(content=ft.Text("Comentarios", size=16, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK), padding=ft.padding.only(left=0,right=25, top=0, bottom=0)),
                                                    ft.Container(content=ft.Text("Añadir", size=16, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK), padding=ft.padding.only(left=50,right=25, top=0, bottom=0)),
                                                ],
                                               # alignment=ft.MainAxisAlignment.SPACE_EVENLY
                                            ),
                                            ft.Container(
                                                bgcolor=ft.colors.BLUE_500,
                                                padding=ft.padding.all(2),
                                                content=ft.Row(
                                                    controls=[
                                                         ft.TextField(value="1111",height=60, width=70, color="black", bgcolor=ft.colors.BLUE_500, disabled=True, multiline=True,min_lines=1, max_lines=2,text_size=13, border="none", text_align="center"),
                                                        ft.TextField(value="Kevin Alan Quintero Barragan jjjjjjjjjjj",height=60, width=200, bgcolor=ft.colors.BLUE_500, disabled=True, multiline=True,min_lines=1, max_lines=2,text_size=13, border="none",color="black", text_align="center"),
                                                        ft.TextField(value="0002",height=60, width=70, color="black",  bgcolor=ft.colors.BLUE_500, disabled=True, multiline=True,min_lines=1, max_lines=2,text_size=13, border="none", text_align="center"),
                                                        *[ft.Column(
                                                            controls=[
                                                                ft.Row(
                                                                    controls=[
                                                                        ft.TextField(height=35, width=40, color="black", hint_text="HE", bgcolor="white", text_align="center", text_size=10),
                                                                        ft.Checkbox(value=True, check_color="black", fill_color="white"),
                                                                    ],
                                                                    spacing=4
                                                                ),
                                                                ft.Row(
                                                                    controls=[
                                                                        ft.TextField(height=35, width=40, color="black", hint_text="DT", bgcolor="white", text_align="center", text_size=10),
                                                                        ft.TextField(height=35, width=40, color="black", hint_text="TE", bgcolor="white", text_align="center", text_size=10),
                                                                    ],
                                                                    spacing=4
                                                                ),
                                                            ]
                                                        ) for _ in range(7)],
                                                        ft.TextField(height=50, width=150, color="black", hint_text="Comentarios", bgcolor="white", multiline=True,min_lines=1, max_lines=2,text_size=13),
                                                        ft.ElevatedButton(text="Añadir",icon=ft.icons.ADD,width=60 ,height=50,bgcolor=ft.colors.BLUE_900, color=ft.colors.WHITE, on_click=self.send_data),
                                                    ],
                                                  #  alignment=ft.MainAxisAlignment.SPACE_EVENLY
                                                )
                                            ),
                                            ft.Container(
                                                bgcolor=ft.colors.BLUE_300,
                                                padding=ft.padding.all(2),
                                                content=ft.Row(
                                                    controls=[
                                                        ft.TextField(value="1631",height=60, width=70, color="black", bgcolor=ft.colors.BLUE_300, disabled=True, multiline=True,min_lines=1, max_lines=2,text_size=13, border="none", text_align="center"),
                                                        ft.TextField(value="Kevin Alan Quintero ",height=60, width=200, bgcolor=ft.colors.BLUE_300, disabled=True, multiline=True,min_lines=1, max_lines=2,text_size=13, border="none",color="black", text_align="center"),
                                                        ft.TextField(value="00",height=60, width=70, color="black",  bgcolor=ft.colors.BLUE_300, disabled=True, multiline=True,min_lines=1, max_lines=2,text_size=13, border="none", text_align="center"),
                                                        *[ft.Column(
                                                            controls=[
                                                                ft.Row(
                                                                    controls=[
                                                                        ft.TextField(height=35, width=40, color="black", hint_text="HE", bgcolor="white", text_align="center", text_size=10),
                                                                        ft.Checkbox(value=True, check_color="black", fill_color="white"),
                                                                    ],
                                                                    spacing=4
                                                                ),
                                                                ft.Row(
                                                                    controls=[
                                                                        ft.TextField(height=35, width=40, color="black", hint_text="DT", bgcolor="white", text_align="center", text_size=10),
                                                                        ft.TextField(height=35, width=40, color="black", hint_text="TE", bgcolor="white", text_align="center", text_size=10),
                                                                    ],
                                                                    spacing=4
                                                                ),
                                                            ]
                                                        ) for _ in range(7)],
                                                        ft.TextField(height=50, width=150, color="black", hint_text="Comentarios", bgcolor="white", multiline=True,min_lines=1, max_lines=2,text_size=13),
                                                        ft.ElevatedButton(text="Añadir",icon=ft.icons.ADD,width=60 ,height=50,bgcolor=ft.colors.BLUE_900, color=ft.colors.WHITE, on_click=self.send_data),
                                                    ],
                                                   # alignment=ft.MainAxisAlignment.SPACE_EVENLY
                                                )
                                            ),
                                        ]
                                    )
                                ),
                                ft.Container(
                                    alignment=ft.alignment.top_left,
                                    padding=ft.padding.only(top=20, left=10),
                                    content=ft.ElevatedButton(
                                        text="Generar Reporte",
                                        bgcolor=ft.colors.BLUE_800,
                                        color=ft.colors.WHITE,
                                        on_click=self.send_data
                                    ),
                                    
                                    
                                ),
                               
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
                controls=[
                    self.frame_title,
                    self.remaining_container
                ]
            )
        ]

    def logout(self, e):
        print("Cierre de sesión realizado.")

    def send_data(self, e):
        print("Datos enviados.")

def main(page: ft.Page):
    page.bgcolor = ft.colors.BLACK
    app = AnimatedApp()
    page.add(app)

ft.app(target=main)
