from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from components.popups.PCDownloadPopUp import PCDownloadPopUp
from components.popups.popup import MyPopUp
from components.validators.mediaFormatsValidator import MediaFormatValidaor

import pvleopard
#TODO - delete the key because it is private
access_key = "j2HYl+0AhFWnswwxXtdkpQjXND8NchN0d4nELfi8WNbOlDvCrGMDRQ=="


try:
    leopard = pvleopard.create(access_key=access_key)
except Exception:
    MyPopUp(f"unable to connect to leopard using access key: {access_key}")
    
audio_files_destionation_path = "src\\Audio_Files\\"

class MyPC(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        # self.translator = translator
    
    mfv = MediaFormatValidaor()
    
    def __init__(self,translator, **kw):
        super().__init__(**kw)
        Window.bind(on_drop_file=self.handlesDrop)
        Window.bind(on_request_close=self.handle_chosen_file)
        self.translator =  translator
        
    def select(self, *args):
        try: self.label.text = args[1][0]
        except: pass
        
    def handlesDrop(self,filename:str,x,y):
        self.file_name = filename.decode("utf-8") 
        print("global path: {}, local path: {}".format(filename,self.file_name))
        MyPopUp(title_text="Success",msg_text=f'this is my dropped file:\n{self.file_name}')
        
    def show_load_list(self):
        content = LoadFileChooser(load=self.handle_chosen_file, cancel=self.dismiss_popup)
        self._popup = Popup(title="Choose your file", content=content, size_hint=(1, 1))
        self._popup.open()
        
    def handle_chosen_file(self, path:str, filename:list=[]):
        if filename != []:
            filename = filename[0]
            if not self.mfv.is_valid_format(file=filename):
                MyPopUp("Invalid Format","video format should be mp4")
                return
        else:
            MyPopUp("Empty path","Recieved Empty File path")
            return
        
        self.open_downloader(filename)

    def open_downloader(self,filename):
        self.UrlPopup = PCDownloadPopUp(filename,self.translator)
        self.UrlPopup.open() 
       
    def dismiss_popup(self):
        self._popup.dismiss()        

class LoadFileChooser(Screen):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)