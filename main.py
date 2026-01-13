import dearpygui.dearpygui as gui
import converter as cnv
import tkinter as tk
from tkinter import filedialog


class viewport:
    def __init__(self):
        self.window = gui.window(tag ="mainwindow",pos=[0,0],width=800,height=600,no_collapse=True,no_move=True,no_title_bar=True)


    def app(self):
        '''главная функция с gui'''
        gui.create_context()

        self.bind_font()
        gui.create_viewport(title='MC skin to base64 converter',width=800,height=600)
        gui.show_viewport()
        with self.window:
            gui.add_text("конвертер скинов в base64")
            gui.add_spacer(height=20)
            gui.add_button(label="Выбрать файл скина",width=200,height=45, callback=self.file_selected)

            gui.add_input_text(
                default_value="",
                tag="b64_text",
                width=750,
                height=350,
                multiline=True,
                readonly=True,
            )
            gui.add_spacer(height=20)
            gui.add_text("",tag="clipboard")
        gui.setup_dearpygui()
        gui.start_dearpygui()
        gui.destroy_context()

    @staticmethod
    def bind_font():
        with gui.font_registry():
            with gui.font("fonts/pixel.ttf", 12, default_font=True, tag="Default font") as f:
                gui.add_font_range_hint(gui.mvFontRangeHint_Cyrillic)

        gui.bind_font("Default font")

    def file_selected(self,sender):
        file_path = filedialog.askopenfilename(
            title="Выберите файл",
            filetypes=[
                ("Все файлы", "*.*"),
                ("изображение скина", "*.png")
            ]
        )
        response = cnv.convert_skin(file_path)
        gui.configure_item("b64_text",default_value=response)
        gui.configure_item("clipboard", default_value="текст автоматически скопирован!")



    def file_canceled(self):
        pass









if __name__ == "__main__":
    mainwindow = viewport()
    viewport.app(mainwindow)
