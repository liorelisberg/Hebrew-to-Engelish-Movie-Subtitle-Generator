import os

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen

from pytube import YouTube as YT
from pytube.cli import on_progress

from  src.components.validators.validate_url import UrlValidator
from  src.components.validators.validate_internet_connection import InternetConnectionValidator
from src.components.popups.popup import MyPopUp


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
    
    def download_complete(self,stream,file_path):
        file_name = os.path.basename(file_path).split('.')[0]
        MyPopUp("Success","Successfuly Downloaded\n"+file_name)
        print("Done !")
        
        
    def download_video(self, url):
        
        
        
        yt = YT(url,on_progress_callback=on_progress,on_complete_callback=self.download_complete)
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
        print("downloading ...")

        try:
            yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(self._video_output_path)
            
        except Error:
            print(Error)
            
   