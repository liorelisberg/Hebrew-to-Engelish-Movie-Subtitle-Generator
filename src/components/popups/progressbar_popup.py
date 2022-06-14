from kivy.factory import Factory

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