from kivy.uix.screenmanager import Screen
from components.popups.popup import MyPopUp
from components.popups.urlPopup import UrlPopup
from components.validators.validate_url import UrlValidator
from components.validators.validate_internet_connection import InternetConnectionValidator

from googletrans import Translator as google_trans

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
            
        # internet connection is valid and url is valid
        elif(self.internet_coonction_validator.is_cnx_active() and self.urlValidator.is_valid_url(url)):
            self.open_downloader(url)
            
        # error popup
        else:
            MyPopUp("Invalid Url","URL is invalid:\n {}".format(url))    
        
        self.url.text = ""

    def open_downloader(self,url):
        self.UrlPopup = UrlPopup(url)
        self.UrlPopup.bind(on_dismiss=self.on_popup_dismiss)
        self.UrlPopup.open()
        
    def submit_url(self):
        url = self.url.text
        self.create_popup(url)
        
        # if self.UrlPopup.has_ended:
        #     sleep(2)
        #     print(f"download has ended for {url}")
        #     self.UrlPopup.dismiss()
        
    def on_popup_dismiss(self, mypopup):

        print(mypopup.has_ended)
        print(mypopup.has_started)
        print(mypopup.url_input)
        
        if(not mypopup.has_started and not mypopup.has_ended):
            print("here")
            # mypopup.dismiss()
        

        
        if mypopup.has_ended and mypopup.has_started:
            # open the srt file,    V
            # extract all text,     V
            # translate english to hebrew, V
            # insert translation to new srt, V
            # insert to video
            # create save
            print("should create srt")

            srt_path = mypopup.srt_file_path
            vid_path = mypopup.video_file_path

            srt_file = open(srt_path, "r")
            srt_lines = srt_file.read()
            print(srt_lines)
            srt_lines = srt_lines.split("\n\n")
            print(srt_lines)
            
            self.eng_srt_tuple_list = list()
            for line in srt_lines:
                tupleLine = tuple(line.split("\n"))
                self.eng_srt_tuple_list.append(tupleLine)
                
            print(self.eng_srt_tuple_list)
            
            # https://www.youtube.com/watch?v=ZFGAz6vZx1E
            
            self.heb_srt_text = ""
            # self.trans_srt_text
            for index,timestamp,text in self.eng_srt_tuple_list:
                # translate the text
                trans_text = google_trans.translate(text, dest='he', src='en').text
                # add the translated tuple
                # self.heb_srt_tuple_list.append(tuple(index,timestamp,trans_text))
                trans_srt_line = [index,timestamp,trans_text]
                
                self.heb_srt_text += "\n".join(trans_srt_line)
                
                # calculating the end of the list  - ((my_list[i]+1)/2)-1 != len(my_list)
                if int((int(index)+1)/2) != len(self.eng_srt_tuple_list):
                    self.heb_srt_text += "\n\n"
                else:
                    print("end of list")
            
            
            # https://www.youtube.com/watch?v=ZFGAz6vZx1E
            print("self.heb_srt_text")
            

            
            
            
                
                
            
                
            
            
            
            