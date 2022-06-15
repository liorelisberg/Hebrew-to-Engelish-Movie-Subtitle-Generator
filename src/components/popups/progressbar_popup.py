from kivy.factory import Factory
from kivy.uix.progressbar import ProgressBar
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup

import time
import threading
from threading import Thread

class MyProgressBarPopUp:
    # def __init__(self):
    #     self.bp = ProgressBar()
    #     self.popup = Popup(title="Progress Bar",content=self.bp,size_hint=(0.5,0.2))
    
    
    # def progressbar(self,value=0.0):
    #     if not self.popup._is_open:
    #         self.popup.open()
    #     threading.Thread(target=self.update_progressbar,args=(value)).start()

    # def update_progressbar(self,update_value):
    #     self.bp.value = round(update_value/100,2)
    #     print("precent: ",self.bp.value)
        
    # def dismiss(self):
    #     time.sleep(2)
    #     self.popup.dismiss
        
    def __init__(self,value=0.00):
        print("opening MyProgressBarPopUp")
        
        self.bp = ProgressBar()
        self.popup = Popup(title="Progress Bar",content=self.bp,size_hint=(0.8,0.5))
    
    def open_pb(self):
        self.popup.open()
        
    def update_progressbar(self,value):
        self.bp.value = round(value/100,2)
        print("precent: ",self.bp.value)
        
    def dismiss(self):
        time.sleep(5)
        self.popup.dismiss