from threading import Thread
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.clock import Clock

# Builder.load_file('mypopup.kv')

class MyPopUp:
    
    def __init__(self,title_text,msg_text,button_text="Ok"):
        # layout = BoxLayout(orientation='vertical',padding=(10),size_hint_y=None)
        # popupLabel  = Label(text = msg_text,size_hint_y = None,)
        # closeButton = Button(text = button_text,size_hint=(None, None), size=(50, 30),pos_hint ={'x':0.45, 'y':1})

        # layout.add_widget(popupLabel)
        # layout.add_widget(closeButton)      
            
        # # Instantiate the modal popup and display
        # self.popup = Popup(
        #     title_align='center',
        #     auto_dismiss=False,
        #     title=title_text,
        #     content=layout,
        #     size_hint=(None, None),
        #     size=(400, 300))  
        print("title_text: ",title_text)
        print("msg_text: ",msg_text)
        print("button_text: ",button_text)
        print("\n")
        
        self.popup = Factory.MyPopUp()
        self.popup.message.text = msg_text
        self.popup.title = title_text
        self.popup.open()   

        # Attach close button press with popup.dismiss action
        # closeButton.bind(on_press=self.popup.dismiss)
        
class MyProgressBarPopUp:
    def __init__(self,value=0.00):
        print("opening MyProgressBarPopUp")
        self.popup = Factory.MyProgressBarPopUp()
        self.popup.value = value
        # self.popup.message.text = "Downloading ..."
        self.popup.title = "Progress bar"
    
    def open_pb(self):
        self.popup.open()
        
    def update_progressbar(self,value):
        self.popup.ids.my_progress_bar.value = value/100
        print("precent: ",value)