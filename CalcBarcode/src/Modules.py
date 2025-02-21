import flet as ft


class Assembling(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__(expand=True, adaptive=True)
        self.page = page
        self.content = ft.Container(
            expand=True,
            content=ft.Column(
                controls=[
                    Header(page=self.page, func=None, text="Заказ"),
                ]
            )
        )
        

class Header(ft.Container):
    def __init__(self, page: ft.Page, func, text="TSD"):
        super().__init__()
        self.page = page
        self.text = text
        self.func = func
        self.padding = ft.padding.only(left=10, right=10)
        self.height = 50
        self.margin = 0
        self.bgcolor = "#17202A"
        self.content = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    content=ft.Text(value=self.text, color="white"),
                ),
                ft.Container(
                    content=ft.Icon(name=ft.icons.MENU, color="white"),
                    on_click=self.func,
                ),
            ],
        )


class Main(ft.Container):
    def __init__(self, page: ft.Page, func=None):
        super().__init__(expand=True)
        # self.bgcolor = "black"
        self.page = page
        self.func = func
        self.content = ft.Column(
            [
                ConBtn(page=page, func_on_click=self.func, text_value="Заказ"),
                ConBtn(page=page, func_on_click=self.func, text_value="Инвентаризация"),
                ConBtn(page=page, func_on_click=self.func, text_value="Поступление"),
            ]
        )


class ConBtn(ft.Container):
    def __init__(
        self, page: ft.Page, func_on_click=None, text_value=None, cont_data=None
    ):
        super().__init__()
        self.page = page
        self.func_on_click = func_on_click
        self.data = cont_data
        self.bgcolor = "#17202A"
        self.border_radius = 5
        self.padding = 2
        self.on_click = self.func_on_click
        self.on_hover = self.on_ho
        self.cursor = "pointer"
        self.text = ft.Text(value=text_value, size=20, color="#C0C0C0")
        self.content = ft.Row(
            controls=[
                ft.Icon(name=ft.icons.MENU_OPEN, color="white"),
                self.text,
            ],
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )

    def on_ho(self, e):
        self.bgcolor = "#17202A" if self.bgcolor == "#C0C0C0" else "#C0C0C0"
        self.text.color = "#283747" if self.text.color == "#C0C0C0" else "#C0C0C0"
        self.update()


class MenuBok(ft.NavigationDrawer):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.position = ft.NavigationDrawerPosition.END
        self.bgcolor = "#C0C0C0"
        self.border_radius = 0
        self.surface_tint_color = "#17202A"
        self.controls = [
            ft.Column(
                alignment=ft.MainAxisAlignment.START,
                controls=[
                    ft.Column(
                        controls=[
                            ft.Container(height=20),
                            ConBtn(
                                page=page,
                                text_value="Закрыть",
                                func_on_click=self.on_click_cont_btn,
                            ),
                            ft.Container(height=self.page.window.height / 5),
                            ConBtn(
                                page=page,
                                text_value="Скачать справочник",
                                func_on_click=lambda e: print("Скачать справочник"),
                            ),
                            # ft.Divider(),
                            ConBtn(
                                page=page,
                                text_value="Отправить собранные",
                                func_on_click=lambda e: print("Отправить собранные"),
                            ),
                            # ft.Divider(),
                            ConBtn(
                                page=page,
                                text_value="Скачать документы",
                                func_on_click=lambda e: print("Скачать документы"),
                            ),
                            # ft.Divider(),
                        ]
                    ),
                    ft.Container(height=self.page.window.height / 3.8),
                    ft.Column(
                        controls=[
                            ConBtn(
                                page=page,
                                text_value="Настройка",
                                func_on_click=lambda e: print("Настройка"),
                            ),
                        ],
                    ),
                ],
            ),
        ]

    def on_click_cont_btn(self, e):
        e.control.bgcolor = "#17202A" if e.control.bgcolor == "#C0C0C0" else "#C0C0C0"
        e.control.text.color = (
            "#283747" if e.control.text.color == "#C0C0C0" else "#C0C0C0"
        )
        e.control.update()
        self.page.close(self)
