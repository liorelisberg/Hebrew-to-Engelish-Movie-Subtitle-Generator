from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from kivy.core.window import Window
from kivy.lang import Builder

from windows import YouTube 
from windows import MyPC
from windows import MainWindow
from windows import AboutUs

from logs.LoggerFactory import Logger

import webbrowser

Builder.load_file("myapp.kv")
Window.clearcolor = (1,1,1,1)
Logger = Logger()
            
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
    logger = Logger.get_logger()
    logger.info("Initializing Application")
    MyApp().run()