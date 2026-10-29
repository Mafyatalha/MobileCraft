from kivy.app import
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.uix.label import Label
class MobileCraftApp(App):
    def build(self):
        self.root_layout = BoxLayout(orientation="vertical")
        self.label = Label(text="MobileCraft'a Hoş Geldin!")
        self.root_layout.add_widget(self.label)
        btn_layout = BoxLayout(size_hint_y=0.2)
        left_btn = Button(text="<")
        jump_btn = Button(text="Zıpla")
        down_btn = Button(text="Aşağı")
        right_btn = Button(text=">")
        action_btn = Button(text="Aksiyon")
        btn_layout.add_widget(left_btn)
        btn_layout.add_widget(jump_btn)
        btn_layout.add_widget(down_btn)
        btn_layout.add_widget(right_btn)
        btn_layout.add_widget(action_btn)
        self.root_layout.add_widget(btn_layout)
        return self.root_layout
if __name__ == "__main__":
    MobileCraftApp().run() 
