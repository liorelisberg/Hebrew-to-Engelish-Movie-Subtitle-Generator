# from kivy.app import App
# from kivy.uix.popup import Popup
# from kivy.uix.floatlayout import FloatLayout
# from kivy.properties import ObjectProperty
# from kivy.core.window import Window

# class Root(FloatLayout):
#     load = ObjectProperty(None)
#     cancel = ObjectProperty(None)
    
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         Window.bind(on_request_close=self.load_list)
        

#     def show_load_list(self):
#         content = LoadDialog(load=self.load_list, cancel=self.dismiss_popup)
#         self._popup = Popup(title="Load a file list", content=content, size_hint=(1, 1))
#         self._popup.open()

#     def load_list(self, path, filename):
#         if filename != []:
#             print("path: ",path)
#             print("filename: ",filename)
#             Window.close()
            
#     def dismiss_popup(self):
#         self._popup.dismiss()
#         Window.close()  

# class LoadDialogApp(App):
#     pass

# class LoadDialog(FloatLayout):
#     load = ObjectProperty(None)
#     cancel = ObjectProperty(None)

# if __name__ == '__main__':
#     LoadDialogApp().run()