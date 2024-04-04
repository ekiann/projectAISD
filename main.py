import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.widget import Widget

lblKVLang = Builder.load_file("main.kv")


class NewClass(Widget):
    pass


class MyApp(App):
    def build(self):
        Window.clearcolor = (2/255, 49/255, 93/255, 1)
        Window.size = (360, 600)
        return NewClass()


if __name__ == "__main__":
    MyApp().run()
