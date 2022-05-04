import os

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.properties import ObjectProperty

from components.popups.popup import PopUp

class MyPC(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        Window.bind(on_drop_file=MyPC.handlesDrop)
        Window.bind(on_request_close=self.load_list)
        
    def select(self, *args):
        try: self.label.text = args[1][0]
        except: pass
        
    def handlesDrop(self,filename,x,y):
        self.file_name = filename.decode("utf-8") 
        PopUp(title_text="Success",msg_text=f'this is my dropped file:\n{self.file_name}')
        
    def show_load_list(self):
        content = LoadFileChooser(load=self.load_list, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load a file list", content=content, size_hint=(1, 1))
        self._popup.open()
        
    def load_list(self, path, filename):
        if filename != []:
            print("path: ",path)
            print("filename: ",filename)
            Window.close()
            
    def dismiss_popup(self):
        self._popup.dismiss()
        Window.close()
        
class LoadFileChooser(Screen):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)