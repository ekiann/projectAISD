# # import kivy.uix.textinput
# # import kivy.uix.label
# # import kivy.uix.button
# from kivy.app import App
# from kivy.lang import Builder
# from kivy.uix.widget import Widget
#
# # KV = """
# #
# # Button:
# #     text: 'aboba'
# #     size_hint: None, None
# #     size: 200, 40
# #     pos_hint: {'center_y': .5, 'center_x': .5}
# #     background_normal: 'button_normal.png'
# #     border: 30, 30, 30, 30
# # """
#
# class app(Widget):
#     pass
# class my_app(App):
#     def build(self):
#         self.load_kv('file.kv')
#         return app()
#
# my_app().run()

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.recycleview import RecycleView
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.config import ConfigParser
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.metrics import dp
from datetime import datetime
import os
import ast
import time
from kivy.graphics import RoundedRectangle


class StartScreen(Screen):
    def __init__(self, **kvargs):
        super(StartScreen, self).__init__(**kvargs)
        box = BoxLayout(orientation='vertical')
        # Window.clearcolor = (2 / 255, 49 / 255, 93 / 255, 1)
        self.layout = GridLayout(rows=2, size_hint_y=None)
        layout_bar = GridLayout(cols=2, size_hint=[None, None])
        layout_window = GridLayout(cols=3, size_hint=[None, None])
        menu = Button(background_normal='button_normal', on_press=lambda x:
                      set_screen('menu'))
        layout_bar.add_widget(menu)
        self.layout.add_widget(layout_bar)
        title = Label(text='Новые тесты')
        layout_window.add_widget(title)

        self.layout.add_widget(layout_window)
        box.add_widget(self.layout)
        self.add_widget(box)





class MenuScreen(Screen):
    ...


def set_screen(name_screen):
    sm.current = name_screen

sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))

# if __name__ == '__main__':
#     StartScreen().run()

