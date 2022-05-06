from asyncio.windows_events import NULL
import os
from queue import Empty

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen

from pytube import YouTube as YT
from pytube.cli import on_progress

from  src.components.validators.validate_url import UrlValidator
from  src.components.validators.validate_internet_connection import InternetConnectionValidator
from src.components.popups.popup import MyPopUp,MyProgressBarPopUp


class YouTube(Screen):
    urlValidator = UrlValidator()
    icv = InternetConnectionValidator()
    _video_output_path = "/Video_Downloads"
    _subtitle_output_path = "/Subtitles_Files"
        
    def create_popup(self,url):
        if(self.urlValidator.is_empty_url(url)):
            MyPopUp("Invalid URL","Received Empty URL")
        elif(self.icv.is_cnx_active() and self.urlValidator.is_valid_url(url)):
            self.download_video(url)
        else:
            MyPopUp("Invalid Url","URL is invalid:\n {}".format(url))    
        
        self.url.text = ""

    def submit_url(self):
        url = self.url.text
        self.create_popup(url)
    
    def percent(self, tem, total):
        perc = (float(tem) / float(total)) * float(100)
        return perc
    
    def download_progress(stream = None, chunk = None, file_handle = None, remaining = None):
        # Gets the percentage of the file that has been downloaded.
        percent = (100*(file_size-remaining))/file_size
        print("{}".format(percent,3) + "%" +" downloaded")
        # print("stream.filesize: ",stream.filesize)
        # total_size = stream.filesize
        # bytes_downloaded = total_size - bytes_remaining 
        # percentage_of_completion = round((bytes_downloaded / total_size * 100),3)
        
        # print("precentage completed: ",percentage_of_completion)         
        MyProgressBarPopUp()
        
        
    
    def download_complete(self,stream,file_path):
        file_name = os.path.basename(file_path).split('.')[0]
        MyPopUp("Success","Successfuly Downloaded\n"+file_name)
        print("Done !")
        
        
    def download_video(self, url):
        print("downloading ...")
        
        # yt = YT(url,on_progress_callback=on_progress,on_complete_callback=self.download_complete)
        try:
            yt = YT(url,on_progress_callback=self.download_progress,on_complete_callback=self.download_complete)
        except:
           print("Connection Error") #to handle exception  
           
        # print(yt.captions)
        title = yt.title
        # print("captions: ",yt.captions)
        if len(yt.captions) != 0 :
            caption = yt.captions['a.en']
            # print("caption: ",caption)
            subtitle = caption.generate_srt_captions()
            # print("subtitle: ",subtitle)
            completeName = os.path.join("Subtitles_Files", title + '.srt')
            open(completeName, 'w').write(subtitle)
        
        # print("title: ",title,"caption size: ", caption)
        video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1]
        
        global file_size
        file_size = video.filesize

        try:
            video.download(self._video_output_path)
            # video = yt.order_by(mp4files[-1].extension,mp4files[-1].resolution)      
        except Exception as e:
            print(e)
            
   