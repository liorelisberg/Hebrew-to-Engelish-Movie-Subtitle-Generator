import subprocess
from threading import Thread
from kivy.uix.popup import Popup
from components.popups.popup import MyPopUp
from kivy.properties import BooleanProperty, NumericProperty, StringProperty

import moviepy.editor as mp
from components.generators.SrtGenerator import to_srt
from scripts.engSrtTanslate import engSrtToHebSrt
import pvleopard

#TODO - delete the key because it is private
access_key = "j2HYl+0AhFWnswwxXtdkpQjXND8NchN0d4nELfi8WNbOlDvCrGMDRQ=="

try:
    leopard = pvleopard.create(access_key=access_key)
except Exception:
    MyPopUp(f"unable to connect to leopard using access key: {access_key}")

class PCDownloadPopUp(Popup):
    
    video_output_folder = "Video_Downloads"
    audio_output_folder = "Audio_Downloads"
    subtitles_output_folder = "Subtitles_Files"
        
    filename_input = StringProperty("")
    progress_value = NumericProperty(0) # To capture the current progress.
    has_started = BooleanProperty(False) 
        
    def __init__(self, filename):
        super().__init__()
        print(f"filename: {filename}")
        self.filename_input = filename.split("\\")[-1]
        self.filename = filename
        
    def download(self,):
        Thread(target = self.start_download).start()
    
    def start_download(self):
        # self.has_started = True
        self.ids.download_button.disabled = True
        self.ids.close_button.disabled = True
        
        self.process_video()
        
    def process_video(self):     
        # get audio from video
        self.ids.progress_label.text = "Extracting audio from video ..."
        audio_path = self.get_audio_from_video(self.filename)
        if audio_path == "":
            self.ids.close_button.disabled = False
            return
        
        # get subtitles from audio file using speech-to-text
        self.ids.progress_label.text = "Creating English captions from audio ..."
        eng_subtitles_path = self.get_subtitles(audio_path)
        if eng_subtitles_path == "":
            self.ids.close_button.disabled = False
            return
        
        # translate subtitles using NMT tranlator
        self.ids.progress_label.text = "Translating English captions to Hebrew ..."
        translated_subtitles_path = engSrtToHebSrt(sourcePath=eng_subtitles_path,destPath=eng_subtitles_path)
        if translated_subtitles_path == "":
            self.ids.progress_label.text = "Exception while tranlating captions to Hebrew"
            self.ids.close_button.disabled = False
            return
        
        # embed translated subtitles to video, and save it.
        self.ids.progress_label.text = "Embeding Hebrew captions to video ..."
        try:
            self.embed_subtitles_to_video(self.filename,translated_subtitles_path)
        except Exception as e:
            print(e) 
            self.ids.progress_label.text = "Exception while embedding translated captions to video"
            self.ids.close_button.disabled = False
            return
        
        self.ids.progress_label.text = "Done processing video !\nFile is saved in original location."
        self.ids.close_button.disabled = False
        self.has_started = False  
    
    def get_audio_from_video(self,video_path):
        try:
            video = mp.VideoFileClip(video_path)
            audio_path = self.audio_output_folder +"\\"+ video_path.split("\\")[-1].replace(".mp4",".mp3")
            video.audio.write_audiofile(audio_path)
            return audio_path
        except Exception as e:
            print(e)
            self.ids.progress_label.text = "Exception while saving video as audio :("
            # self.ids.close_button.disabled = False
            return ""
    
    def get_subtitles(self,audio_path):
        print(f"here, {audio_path}")
        try:
            _, words = leopard.process_file(audio_path)
        except Exception as e:
            self.ids.progress_label.text = "Exception while creating captions from video :("
            # self.ids.close_button.disabled = False
            return ""
            
        subtitle_path = self.subtitles_output_folder + "\\" + audio_path.split("\\")[-1].replace(".mp3",".srt")

        try:
            with open(subtitle_path, 'w+') as f:
                f.write(to_srt(words))
        except Exception as e:
            print(e)
            return ""
        
        return subtitle_path 
    
    def embed_subtitles_to_video(self,video_path,translated_subtitles_path):
        trans_video_path = video_path.replace(".mp4","-translated.mp4")
        translated_subtitles_path = translated_subtitles_path.replace("\\","/")
        command = f"ffmpeg -threads 8  -i \"{video_path}\" -vf subtitles=\"{translated_subtitles_path}\" -y -movflags +faststart -preset ultrafast \"{trans_video_path}\""
        subprocess.call(command,shell=True)
    
    def dismiss(self, *_args, **kwargs):
        return super().dismiss(*_args, **kwargs)