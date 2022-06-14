import time
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from threading import Thread

# Designate Our .kv design file 
Builder.load_file('progress.kv')

class MyLayout(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def progress_bar(self):
        for i in range(10):
            time.sleep(1.5)
            # Grab the current progress bar value
            current = self.ids.my_progress_bar.value
            # If statement to start over after 100
            if current == 1:
                current = 0

            # Increment value by .25
            current += .25
            # Update the progress bar
            self.ids.my_progress_bar.value = current
            # Update the label
            self.ids.my_label.text = f'{int(current*100)}% Progress'
            print(f'{int(current*100)}% Progress')
            
        print("Done !")


    def button_press(self):
        # create the thread to invoke other_func with arguments (2, 5)
        t = Thread(target=self.progress_bar,args=())
        # set daemon to true so the thread dies when app is closed
        t.daemon = True
        # start the thread
        t.start()
        
        
class AwesomeApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
	AwesomeApp().run()