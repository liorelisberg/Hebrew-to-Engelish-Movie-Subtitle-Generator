from concurrent.futures import thread
import os
from threading import Thread
from kivy.uix.popup import Popup
from pytube import YouTube as YT
from kivy.properties import BooleanProperty,NumericProperty,StringProperty

class UrlPopup(Popup):
    
    video_output_folder = ".\\Video_Downloads"
    subtitles_output_folder = "Subtitles_Files"
    invalid_chars = set(['#','%','&','{','}','<','>','*','/','$','!','\'','\"',':','@','+','`','|','=','?'])
    
    url_input = StringProperty("")
    progress_value = NumericProperty(0) # To capture the current progress.
    has_started = BooleanProperty(False) 
    has_ended = BooleanProperty(False)

    def __init__(self,url):
        super().__init__()
        self.url_input = url
        

    def start_download(self):
        self.has_started = True
        self.has_ended = False
        
        try:
            yt = YT(self.url_input,on_progress_callback=self.download_progress,on_complete_callback=self.download_complete)
        except Exception as e:
            print(e)
            
        title = yt.title   
             
        print('Captions Available: ', yt.captions)
       
        caption_code = ''
        try:
            captions = yt.captions['en']
            caption_code = 'en'
        except:
            try:
                captions = yt.captions['a.en']
                caption_code = 'a.en'
            except Exception as e:
                raise e
        
        # xml_captions = captions.xml_captions
        
        # print(xml_captions)
        
        # srt_format = captions.xml_caption_to_srt(captions.xml_captions)

        captions = yt.captions.get_by_language_code(caption_code)
        
        print(captions.generate_srt_captions())
        self.test_captions(captions)
        
        subtitles = captions.generate_srt_captions()        
        
        completeName = os.path.join(self.subtitles_output_folder, title + '.srt')
        completeName = self.remove_invalid_chars(completeName)
        try:
            open(completeName, 'w').write(subtitles)
        except Exception as e:
            raise e
        
        self.srt_file_path = completeName
        
        video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1]
        self.file_size = video.filesize
            
        try:
            video.download(self.video_output_folder)
        except Exception as e:
            print(e) 
            
        self.video_file_path = self.video_output_folder.replace(".\\",'') +"\\" +video.default_filename
        print("Here")
    
    def test_captions(self,captions):
        caption_list = []
        index = 0
        for line in str(captions.generate_srt_captions()).split('\n'):
            if index == 0:
                caption_list.append({})
            if index in (1, 2):
                caption_list[len(caption_list)-1][('time', 'caption')[index-1]] = line
            index += 1
            if line == '':
                index = 0
        for dic in caption_list:
            print('{} : {}'.format(dic['time'], dic['caption']))
        
    def download_progress(self,stream = None, chunk = None, remaining = None):
        self.progress_value = self.get_download_percent(self.file_size,remaining)
        print(f"{self.progress_value}% downloaded")
       

    def download(self):
        """A new thread object will be created each time this method is revoked. But be careful about the threads already created."""
        Thread(target = self.start_download).start()

    # def on_dismiss(self):
    #     self.url_input = ""
    #     self.has_started = False
        
     # Gets the percentage of the file that has been downloaded.
    def get_download_percent(self,total, left):
        perc = (float(total - left) / float(total)) * float(100)
        return round(perc,2)
    
    def remove_invalid_chars(self,string:str):
        return ''.join([c for c in string if c not in self.invalid_chars])
    
    def download_complete(self,stream,file_path:str):
        self.has_ended = True
        self.ids.progress_label.text = "Download completed." # A confirmation message.
        
    def dismiss(self, *_args, **kwargs):
        return super().dismiss(*_args, **kwargs)
       