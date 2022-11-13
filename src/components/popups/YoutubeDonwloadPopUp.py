import subprocess
from threading import Thread
from kivy.uix.popup import Popup
from pytube import YouTube as YT
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

class TYDonwloadPopUp(Popup):
    
    video_output_folder = "Video_Downloads"
    audio_output_folder = "Audio_Downloads"
    subtitles_output_folder = "Subtitles_Files"
    
    url_input = StringProperty("")
    progress_value = NumericProperty(0) # To capture the current progress.
    has_started = BooleanProperty(False) 
       
    def __init__(self,url,translator):
        super().__init__()
        self.url_input = url
        self.translator = translator
    
    def start_download(self):
        self.has_started = True
        self.ids.download_button.disabled = True
        self.ids.close_button.disabled = True

        self.ids.progress_label.text = "Saving video file from YouTube URL ..."
        
        filename = self.save_yt_video()
        if filename == "":
            self.ids.close_button.disabled = False
            return
            
        self.process_video(filename)

    def process_video(self,filename):
        # get audio from video
        self.ids.progress_label.text = "Extracting audio from video ..."
        audio_path = self.get_audio_from_video(filename)
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
        translated_subtitles_path = engSrtToHebSrt(sourcePath=eng_subtitles_path,
                                                   destPath=eng_subtitles_path,
                                                   t=self.translator)
        if translated_subtitles_path == "":
            self.ids.progress_label.text = "Exception while tranlating captions to Hebrew"
            self.ids.close_button.disabled = False
            return
        
        
        # embed translated subtitles to video, and save it.
        self.ids.progress_label.text = "Embeding Hebrew captions to video ..."
        try:
            self.embed_subtitles_to_video(filename,translated_subtitles_path)
        except: 
            self.ids.progress_label.text = "Exception while embedding translated captions to video"
            self.ids.close_button.disabled = False
            return
        
        self.ids.progress_label.text = "Done processing video !\nFile is saved in original location."
        self.ids.close_button.disabled = False
         
    def get_audio_from_video(self,video_path):
        try:
            video = mp.VideoFileClip(video_path)
            audio_path = self.audio_output_folder + "\\" + video_path.split("\\")[-1].replace(".mp4",".mp3")
            video.audio.write_audiofile(audio_path)
            return audio_path
        except Exception as e:
            print(e)
            self.ids.progress_label.text = "Exception while saving video as audio :("
            # self.ids.close_button.disabled = False
            return ""
        
    def save_yt_video(self):
        try:
            # url input from user
            yt = YT(self.url_input,on_progress_callback=self.download_progress)
            video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1]
            self.file_size = video.filesize
            # download audio file
            video_file = video.download(output_path=self.video_output_folder)
            return video_file
        except Exception as e:
            print(e)
            self.ids.progress_label.text = "Exception while downloading video from YouTube"
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
            self.ids.progress_label.text = "Exception while writing captions as SRT file :("
            # self.ids.close_button.disabled = False
            return ""
        
        return subtitle_path
    
    def embed_subtitles_to_video(self,video_path,translated_subtitles_path):
        trans_video_path = video_path.replace(".mp4","-translated.mp4")
        translated_subtitles_path = translated_subtitles_path.replace("\\","/")
        command = f"ffmpeg -threads 8  -i \"{video_path}\" -vf subtitles=\"{translated_subtitles_path}\" -y -movflags +faststart -preset ultrafast \"{trans_video_path}\""
        subprocess.call(command,shell=True)
        
    def download_progress(self,stream = None, chunk = None, remaining = None):
        self.progress_value = self.get_download_percent(self.file_size,remaining)
        print(f"{self.progress_value}% downloaded") 

    def download(self):
        # A new thread object will be created each time this method is revoked.
        Thread(target = self.start_download).start()

     # Gets the percentage of the file that has been downloaded.
    def get_download_percent(self,total, left):
        perc = (float(total - left) / float(total)) * float(100)
        return round(perc,2)
        
    def dismiss(self, *_args, **kwargs):
        return super().dismiss(*_args, **kwargs)
       