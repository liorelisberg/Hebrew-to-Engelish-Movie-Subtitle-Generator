from kivy.uix.screenmanager import Screen

from src.download_managers.YTDownloadManager import YouTubeDownloadManager

from  src.components.validators.validate_url import UrlValidator
from  src.components.validators.validate_internet_connection import InternetConnectionValidator
from src.components.popups.popup import MyPopUp

class YouTube(Screen):
    urlValidator = UrlValidator()
    internet_coonction_validator = InternetConnectionValidator()
    YouTube_donwload_manager = YouTubeDownloadManager()
    
    def __init__(self, **kw):
        super().__init__(**kw)
        
    def create_popup(self,url):
        if(self.urlValidator.is_empty_url(url)):
            MyPopUp("Invalid URL","Received Empty URL")
        elif(self.internet_coonction_validator.is_cnx_active() and self.urlValidator.is_valid_url(url)):
            self.YouTube_donwload_manager.download_video(url)
        else:
            MyPopUp("Invalid Url","URL is invalid:\n {}".format(url))    
        
        self.url.text = ""

    def submit_url(self):
        url = self.url.text
        self.create_popup(url)