import os
from kivy.uix.screenmanager import Screen

from pytube import YouTube as YT

from  src.components.validators.validate_url import UrlValidator
from  src.components.validators.validate_internet_connection import InternetConnectionValidator
from src.components.popups.popup import MyPopUp,MyProgressBarPopUp


class YouTube(Screen):
    urlValidator = UrlValidator()
    icv = InternetConnectionValidator()
    _video_output_path = "//Video_Downloads"
    _subtitle_output_path = "Subtitles_Files"
    invalid_chars = set(['#','%','&','{','}','<','>','*','/','$','!','\'','\"',':','@','+','`','|','='])
    
    def __init__(self, **kw):
        super().__init__(**kw)
        self.mpbpp = MyProgressBarPopUp()
        
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
    
    def download_progress(self,stream = None, chunk = None, remaining = None):
        # Gets the percentage of the file that has been downloaded.
        percent = (100*(file_size-remaining))/file_size
        print("{}".format(round(percent,3)) + "%" +" downloaded")
        
        self.mpbpp.update_progressbar(value=percent)          
        
    
    def download_complete(self,stream,file_path:str):
        file_name = os.path.basename(file_path).split('.')[0]
        MyPopUp("Success","Successfuly Downloaded\n"+file_name)
        print("Done !")
        
    def remove_invalid_chars(self,string:str):
        return ''.join([c for c in string if c not in self.invalid_chars])
    
    def download_video(self, url):
        print("downloading ...")
        
        try:
            yt = YT(url,on_progress_callback=self.download_progress,on_complete_callback=self.download_complete)
        except:
           print("Connection Error")
           
        title = yt.title
        if len(yt.captions) != 0 :
            caption = yt.captions['a.en']
            subtitle = caption.generate_srt_captions()
            completeName = os.path.join(self._subtitle_output_path, title + '.srt')
            completeName = self.remove_invalid_chars(completeName)
            
            try:
                open(completeName, 'w').write(subtitle)
            except Exception as e:
                print(e)
        
        video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1]
        
        global file_size
        file_size = video.filesize

        try:
            video.download(".\\Video_Downloads")
            self.mpbpp.open_pb()    
        
        except Exception as e:
            print(e)