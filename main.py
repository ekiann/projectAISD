import kivy
kivy.require('2.0.0')
from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen


class Start(Screen):
    pass

lblKVLang = Builder.load_file("main.kv")

class KVLangTestApp(App):

    def build(self):
        # Window.clearcolor = (2/255,	49/255,	93/255, 1)
        # Window.size = (360, 800)
        return Start()


if __name__ == '__main__':
    KVLangTestApp().run()
