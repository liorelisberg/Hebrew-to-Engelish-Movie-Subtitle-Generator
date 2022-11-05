
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from components.popups.popup import MyPopUp
from components.validators.mediaFormatsValidator import MediaFormatValidaor

class MyPC(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        # self.translator = translator
    
    mfv = MediaFormatValidaor()
    
    def __init__(self, **kw):
        super().__init__(**kw)
        Window.bind(on_drop_file=self.handlesDrop)
        Window.bind(on_request_close=self.load_list)
        
    def select(self, *args):
        try: self.label.text = args[1][0]
        except: pass
        
    def handlesDrop(self,filename:str,x,y):
        self.file_name = filename.decode("utf-8") 
        print("global path: {}, local path: {}".format(filename,self.file_name))
        MyPopUp(title_text="Success",msg_text=f'this is my dropped file:\n{self.file_name}')
        
    def show_load_list(self):
        content = LoadFileChooser(load=self.load_list, cancel=self.dismiss_popup)
        self._popup = Popup(title="Choose your file", content=content, size_hint=(1, 1))
        self._popup.open()
        
    def load_list(self, video_path:str, filename:list=[]):
        if filename != []:
            if self.mfv.is_valid_format(file=filename[0]):
                print("Valid path recieved: {}\nfull file path: {}".format(video_path,filename[0]))
            else:
                MyPopUp("Invalid Format","video format should be mp4")
        else:
            print("Recieved Empty File path")

        self.get_subtitles(video_path)

        self._popup.dismiss()
        
    
    def get_subtitles(self,video_path):
        print(f"here, {video_path}")
       
    def dismiss_popup(self):
        self._popup.dismiss()        


class LoadFileChooser(Screen):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)