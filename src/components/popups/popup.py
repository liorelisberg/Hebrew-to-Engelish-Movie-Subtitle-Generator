from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class PopUp:
    def __init__(self,title_text,msg_text,button_text="Ok"):
        layout = GridLayout(cols=1, padding=10)
        popupLabel  = Label(text = msg_text,size_hint_y = None,)
        closeButton = Button(text = button_text,size_hint=(None, None), size=(50, 30))

        layout.add_widget(popupLabel)
        layout.add_widget(closeButton)      

        # Instantiate the modal popup and display
        self.popup = Popup(
            title=title_text,
            content=layout,
            size_hint=(None, None),
            size=(400, 300)
            )  

        #content=(Label(text='This is a demo pop-up')))
        self.popup.open()   

        # Attach close button press with popup.dismiss action
        closeButton.bind(on_press=self.popup.dismiss)