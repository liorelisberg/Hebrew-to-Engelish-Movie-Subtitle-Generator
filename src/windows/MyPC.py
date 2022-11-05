import os
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from components.popups.popup import MyPopUp
from components.validators.mediaFormatsValidator import MediaFormatValidaor

import moviepy.editor as mp
from components.generators.SrtGenerator import to_srt

import pvleopard
#TODO - delete the key because it is private
access_key = "j2HYl+0AhFWnswwxXtdkpQjXND8NchN0d4nELfi8WNbOlDvCrGMDRQ=="

try:
    leopard = pvleopard.create(access_key=access_key)
except Exception as e:
    print(f"unable to connect to leopard using access key: {access_key}",e)
    
audio_files_destionation_path = "src\\Audio_Files\\"
subtitle_files_destionation_path = "src\\Subtitles_Files\\"

class MyPC(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        # self.translator = translator
    
    mfv = MediaFormatValidaor()
    
    def __init__(self, **kw):
        super().__init__(**kw)
        Window.bind(on_drop_file=self.handlesDrop)
        Window.bind(on_request_close=self.handle_chosen_file)
        
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
        
    def handle_chosen_file(self, video_path:str, filename:list=[]):
        if filename != []:
            if self.mfv.is_valid_format(file=filename[0]):
                print("Valid path recieved: {}\nfull file path: {}".format(video_path,filename[0]))
            else:
                MyPopUp("Invalid Format","video format should be mp4")
        else:
            print("Recieved Empty File path")

        audio_path = self.get_audio_from_video(filename[0])
        eng_subtitles = self.get_subtitles(audio_path)
        translated_subtitles = self.translate_subs(eng_subtitles)
        print(translated_subtitles) 

        self._popup.dismiss()
        
    
    def get_audio_from_video(self,video_path):
        video = mp.VideoFileClip(video_path)
        audio_path = audio_files_destionation_path + video_path.split("\\")[-1].replace(".mp4",".mp3")
        video.audio.write_audiofile(audio_path)
        return audio_path
    
    
    def get_subtitles(self,audio_path):
        print(f"here, {audio_path}")
        transcript, words = leopard.process_file(audio_path)
        print(words)
        srt = to_srt(words)
        print(srt)
        ############ TODO FIX HERE
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, subtitle_files_destionation_path)
        subtitle_path = subtitle_files_destionation_path + audio_path.split("\\")[-1].replace(".mp3",".srt")
        ############ TODO FIX HERE
        try:
            with open(subtitle_path, 'w+') as f:
                f.write(to_srt(words))
        except Exception as e:
            print(e)
            return ""
        
        return subtitle_path
       
    def dismiss_popup(self):
        self._popup.dismiss()        


class LoadFileChooser(Screen):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)