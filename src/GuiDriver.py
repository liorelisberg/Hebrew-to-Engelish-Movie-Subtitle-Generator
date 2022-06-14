import logging

from logs.LoggerFactory import Logger
logger = Logger().get_logger(__name__)
logger.info("initiliaizing project")

from kivy.logger import Logger
logging.Logger.manager.root = Logger

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from kivy.core.window import Window
from kivy.lang import Builder

from src.windows.MainWindow import MainWindow
from windows.YouTube import YouTube 
from windows.MyPC import MyPC
from windows.AboutUs import AboutUs

Window.clearcolor = (1,1,1,1)
Builder.load_file('app.kv')
            
sm = ScreenManager()
sm.add_widget(MainWindow(name='main'))
sm.add_widget(YouTube(name='YouTube'))
sm.add_widget(MyPC(name='MyPC'))
sm.add_widget(AboutUs(name='AbutUs'))

class MyApp(App):
    def build(self):
        logger.info("initializing window")
        self.title = 'Hebrew Subtitles Maker'
        sm.current = 'main'
        return sm

if __name__ == "__main__":
    logger.info("MyApp is running")    
    MyApp().run()