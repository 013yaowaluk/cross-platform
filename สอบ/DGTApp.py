from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class Screen1(Screen):
    pass

class Screen2(Screen):
    def check_data(self):
        id_card = self.ids.id_card_input.text
        phone_number = self.ids.phone_number_input.text

        if len(id_card) != 13 or len(phone_number) != 10:
            self.ids.btn_regis.text = "ไม่พร้อมบันทึกข้อมูล"
        else:
            self.ids.btn_regis.text = "พร้อมบันทึกข้อมูล"

class SecondScreen(Screen):
    pass

class DGTApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Screen1(name='home'))
        sm.add_widget(Screen2(name='register'))
        sm.add_widget(SecondScreen(name='second'))
        return sm

if __name__ == '__main__':
    DGTApp().run()
