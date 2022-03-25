from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import  TextInput
from kivy.core.window import Window
from kivy.uix.button import Button

Window.size = (600,400)
Window.clearcolor = (140/255, 163/255, 113/255, 1)
Window.title = "Alkena"

class Myapp(App):

    def __init__(self):
        super().__init__()
        self.knopka = Button(text='Нажмите для подсчёта ИМТ')
        self.imt = Label(text='Ваш показатель ИМТ')
        self.vvod_rosta = TextInput(hint_text='Введите ваш рост (см)\nПример 1.80', multiline=False, padding=20)
        self.vvod_vesa = TextInput(hint_text='Введите ваш вес (кг)', multiline=False, padding=20)

    def knopka_pressed(self,*args):
        rost = self.vvod_rosta.text
        ves = self.vvod_vesa.text
        self.imt.text = 'Ваш показатель ИМТ: ' + str(float(ves) //((float(rost))*float(rost)))

    def build(self):
        box = BoxLayout(orientation='vertical')
        box.add_widget(self.vvod_rosta)
        box.add_widget(self.vvod_vesa)
        box.add_widget(self.knopka)
        self.knopka.bind(on_press=self.knopka_pressed)
        box.add_widget(self.imt)

        return box

if __name__ == "__main__":
    Myapp().run()