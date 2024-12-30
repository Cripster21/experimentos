import flet as ft

def main(page):
    def button_clicked(e):
        if not text_name.value:
            text_name.error_text = "Por favor, introduce tu nombre"
            page.update()
        else:
            name = text_name.value
            page.clean()
            page.add(ft.Text(f"Hola, {name}"))
        
    text_name = ft.TextField(label="Introduce tu nombre")

    page.add(text_name, ft.ElevatedButton("Hola", on_click=button_clicked))

ft.app(target=main)