import os

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.core.window import Window

from components.popups.popup import PopUp

class MyPC(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        
        Window.bind(on_drop_file=MyPC.handlesDrop)
        
    def select(self, *args):
        try: self.label.text = args[1][0]
        except: pass
        
    def handlesDrop(self,filename,x,y):
        self.file_name = filename.decode("utf-8") 
        PopUp(title_text="Success",msg_text=f'this is my dropped file:\n{self.file_name}')