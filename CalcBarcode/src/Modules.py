import flet as ft


class ConBtn(ft.Container):
    def __init__(
        self, page: ft.Page, func_on_click=None, text_value=None, cont_data=None
    ):
        super().__init__()
        self.page = page
        self.func_on_click = func_on_click
        self.data = cont_data
        self.bgcolor = "#C0C0C0"
        self.border_radius = 5
        self.padding = 5
        self.on_hover = self.on_ho
        self.on_click = self.func_on_click
        self.content = ft.Row(
            controls=[
                ft.Icon(name=ft.icons.MENU_OPEN, color="#17202A"),
                ft.Text(value=text_value, size=20, color="#283747"),
            ],
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )

    def on_ho(self, event):
        self.bgcolor = "#B83EB8FF" if self.bgcolor == "#C0C0C0" else "#C0C0C0"
        self.update()


class MenuBok(ft.NavigationDrawer):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.bgcolor = "#C0C0C0"
        self.border_radius = 0
        self.controls = [
            ft.Column(
                controls=[
                    ft.Container(height=20),
                    ConBtn(
                        page=page,
                        text_value="Закрыть",
                        func_on_click=lambda e: self.page.close(self),
                    ),
                    ft.Divider(),
                    ConBtn(
                        page=page,
                        text_value="Скачать справочник",
                        func_on_click=lambda e: print("Скачать справочник"),
                    ),
                    ft.Divider(),
                    ConBtn(
                        page=page,
                        text_value="Отправить собранные",
                        func_on_click=lambda e: print("Отправить собранные"),
                    ),
                    ft.Divider(),
                    ConBtn(
                        page=page,
                        text_value="Скачать документы",
                        func_on_click=lambda e: print("Скачать документы"),
                    ),
                    ft.Divider(),
                ]
            )
        ]
