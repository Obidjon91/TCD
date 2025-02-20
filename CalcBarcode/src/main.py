import flet as ft

from Modules import MenuBok, Main, Header


class App(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__(expand=True, adaptive=True)
        # page
        self.page = page
        self.page.window.min_height = 600
        self.page.window.min_width = 350
        self.page.window.max_height = 600
        self.page.window.max_width = 350
        self.page.padding = 0
        self.page.bgcolor = "#bdc3c7"

        # self container
        self.margin = 0

        # content

        self.content = ft.Container(
            margin=0,
            expand=True,
            content=ft.Column(
                [
                    Header(page=self.page, func=self.open_drawer),
                    Main(page=self.page),
                ],
            ),
        )
        # add
        self.page.add(self)

    # functions
    def open_drawer(self, e):
        self.page.open(MenuBok(self.page))


if __name__ == "__main__":
    ft.app(target=App)
