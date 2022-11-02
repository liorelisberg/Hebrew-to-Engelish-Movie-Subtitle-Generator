from kivy.factory import Factory
class MyPopUp:
    
    def __init__(self,title_text,msg_text,button_text="Ok"):

        print("title_text: ",title_text)
        print("msg_text: ",msg_text)
        print("button_text: ",button_text)
        print("\n")
        
        self.popup = Factory.MyPopUp()
        self.popup.message.text = msg_text
        self.popup.title = title_text
        self.popup.open()
        
