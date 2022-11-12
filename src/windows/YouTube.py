from kivy.uix.screenmanager import Screen
from components.popups.popup import MyPopUp
from components.popups.YoutubeDonwloadPopUp import TYDonwloadPopUp
from components.validators.validate_url import UrlValidator
from components.validators.validate_internet_connection import InternetConnectionValidator

class YouTube(Screen):
    
    def __init__(self ,**kw):
        super().__init__(**kw)
        self.urlValidator = UrlValidator()
        self.internet_coonction_validator = InternetConnectionValidator()
        # self.translator =  translator

    def create_popup(self,url):
        # empty url
        if(self.urlValidator.is_empty_url(url)):
            MyPopUp("Invalid URL","Received Empty URL")
            
        if(not self.urlValidator.is_valid_url(url)):
            MyPopUp("Invalid URL","Received Invalid URL format")
            
        elif not self.internet_coonction_validator.is_cnx_active():
            MyPopUp("Error","No Internet Connection available")
            
        # internet connection is valid and url is valid
        else:
            self.open_downloader(url)
        
        self.url.text = ""

    def open_downloader(self,url):
        self.UrlPopup = TYDonwloadPopUp(url)
        self.UrlPopup.open()
        
    def submit_url(self):
        url = self.url.text
        self.create_popup(url)

            

            
            
            
                
                
            
                
            
            
            
            