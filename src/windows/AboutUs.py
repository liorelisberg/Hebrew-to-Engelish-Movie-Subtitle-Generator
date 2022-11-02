from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.properties import StringProperty

class AboutUs(Screen):
    aboutUsText = StringProperty()
    
    def __init__(self,**kw):
        super().__init__(**kw)
        self.aboutUsText = self.getAboutUsText()
        
    def getAboutUsText(self):
        text = "“Hi there,\nWe are Guy Dahan & Lior Elisberg.\n\n sotware engineering students.\n"
        text += "We are both Tech & movies enthusiasts.\n\n"
        text += "Often we've searched for a sultion to be able to \nwatch movies with Herbrew subtitles,"
        text += "So we decided to \ncreate this desktop application - Hebrew Subtitle Maker.\n\n"
        text += "To use our app, simply paste your Youtube URL or\nchoose a video/audio file from you PC,"
        text += "let the magic happen, \nsave the file locally on your PC and enjoy your hebrew-subtitled content.”"
        return text
    