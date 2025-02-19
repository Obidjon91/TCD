import flet as ft

from Modules import Header, ConBtn

def main(page: ft.Page):
    page.title = "CalcBarcode"
    page.horizontal_alignment = "start"
    page.vertical_alignment = "start"
    page.window.min_height = 600
    page.window.min_width = 350
    page.window.max_height = 600
    page.window.max_width = 350
    page.bgcolor = "#F2F3F4"
    page.add(
        Header(page=page),
        ConBtn(page=page, text_value="Заказ"),
        ConBtn(page=page, text_value="Инвентаризация"),
        ConBtn(page=page, text_value="Поступление"),
    )
    page.update()


if __name__ == "__main__":
    ft.app(main)
