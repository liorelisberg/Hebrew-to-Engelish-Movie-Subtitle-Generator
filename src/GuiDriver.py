from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from kivy.core.window import Window
from kivy.lang import Builder
from AI.Model.Translator import get_translator,translate

from windows.MainWindow import MainWindow
from windows.YouTube import YouTube 
from windows.MyPC import MyPC
from windows.AboutUs import AboutUs

Window.clearcolor = (1,1,1,1)
Builder.load_file('app.kv')
            

class MyApp(App):
    def build(self):
        self.title = 'Hebrew Subtitles Maker'
        t = get_translator()
        translate(t,"Hello world")
        
        sm = ScreenManager()
        sm.add_widget(MainWindow(name='Main'))
        sm.add_widget(YouTube(translator=t,name='YouTube'))
        sm.add_widget(MyPC(translator=t,name='MyPC'))
        sm.add_widget(AboutUs(name='AboutUs'))
        
        sm.current = 'Main'
        return sm

if __name__ == "__main__":
    MyApp().run()