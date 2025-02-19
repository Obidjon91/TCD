import flet as ft


class BtnMenu(ft.IconButton):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        # self.icon = ft.icons.MENU_OPEN
        self.icon = ft.icons.MENU



class Header(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.bgcolor = "#C0C0C0"
        self.border_radius = 5
        self.content = ft.Row(
            controls=[
                BtnMenu(page),
            ]
        )


class ConBtn(ft.Container):
    def __init__(self, page: ft.Page, func_on_click = None, text_value = None):
        super().__init__()
        self.page = page
        self.on_click = func_on_click
        self.bgcolor = "#C0C0C0"
        self.border_radius = 5
        self.padding = 5
        self.on_hover = self.on_hover
        self.content = ft.Row(
            controls=[
                ft.Icon(name=ft.icons.MENU_OPEN),
                ft.Text(value=text_value, size=20),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER
        )

    def on_hover(self, event):
        self.bgcolor = "#B2BABB "
        self.page.update()