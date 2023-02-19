import flet as ft

from . import core


def main(page: ft.Page):
    page.title = "High-tech computation"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    x_display = ft.Text()
    y_display = ft.Text()

    def x_slider_changed(e):
        x_display.value = e.control.value
        page.update()

    def y_slider_changed(e):
        y_display.value = e.control.value
        page.update()

    # x_field = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)
    x_field = ft.Slider(min=-5, max=20, label="{value}%", on_change=x_slider_changed)
    y_field = ft.Slider(min=-5, max=20, label="{value}%", on_change=y_slider_changed)
    result_field = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    def update(math_function):
        result = math_function(x_field.value, y_field.value)
        result_field.value = result
        page.update()

    def minus_click(e):
        update(core.subtract)

    def plus_click(e):
        update(core.add)

    page.add(
        ft.Row(
            [
                x_display,
                y_display,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            [
                x_field,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                y_field,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            [result_field],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )


def run():
    ft.app(target=main)


def web():
    ft.app(target=main, view=ft.WEB_BROWSER)
