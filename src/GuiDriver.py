import os
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.lang import Builder
from components.popups.popup import PopUp
from components.validators.validate_url import UrlValidator
import webbrowser
from pytube import YouTube as YT
from pytube.cli import on_progress

Builder.load_file("myapp.kv")
Window.clearcolor = (1,1,1,1)
class MainWindow(Screen):
    pass

class YouTube(Screen):
    urlValidator = UrlValidator()
    _video_output_path = "venv/Video_Downloads"
    _subtitle_output_path = "venv/Video_Downloads"
        
    def create_popup(self,url):
        if(self.urlValidator.is_empty_url(url)):
            PopUp("Invalid URL","Received Empty URL")
            
        elif(self.urlValidator.is_valid_url(url)):
            self.download_video(url)

            self.url.text = "" 
              
        else:
            PopUp("Invalid Url","URL is invalid")    
            self.url.text = ""

    def submit_url(self):
        url = self.url.text
        self.create_popup(url)
    
    def download_complete(self,stream,file_path):
        file_name = os.path.basename(file_path).split('.')[0]
        PopUp("Success","Successfuly Downloaded\n"+file_name)
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

        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(self._video_output_path)
        
    
class MyPC(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        Window.bind(on_drop_file=MyPC.handlesDrop)
        
    def select(self, *args):
        try: self.label.text = args[1][0]
        except: pass
        
    def handlesDrop(self,filename,x,y):
        self.file_name = filename.decode("utf-8") 
        PopUp(title_text="Success",msg_text=f'this is my dropped file:\n{self.file_name}')
        
class AboutUs(Screen):
    pass
            
sm = ScreenManager()
sm.add_widget(MainWindow(name='main'))
sm.add_widget(YouTube(name='YouTube'))
sm.add_widget(MyPC(name='MyPC'))
sm.add_widget(AboutUs(name='AbutUs'))

class MyApp(App):
    def build(self):
        self.title = 'Hebrew Subtitles Maker'
        
        return sm

if __name__ == "__main__":
    MyApp().run()