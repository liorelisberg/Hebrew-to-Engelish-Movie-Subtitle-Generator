import os
import threading
from tkinter import E
from src.components.popups.popup import MyPopUp
from src.components.popups.progressbar_popup import MyProgressBarPopUp
from pytube import YouTube as YT


video_output_path = ".\\Video_Downloads"
subtitle_output_path = "Subtitles_Files"
invalid_chars = set(['#','%','&','{','}','<','>','*','/','$','!','\'','\"',':','@','+','`','|','=','?'])

class YouTubeDownloadManager:
    def __init__(self):
        self.mpbpp = MyProgressBarPopUp()  
    
    # Gets the percentage of the file that has been downloaded.
    def get_download_percent(self,total, left):
        perc = (float(total - left) / float(total)) * float(100)
        return round(perc,2)
       
    def remove_invalid_chars(self,string:str):
        return ''.join([c for c in string if c not in invalid_chars])
    
    def download_progress(self,stream = None, chunk = None, remaining = None):
        percent = self.get_download_percent(file_size,remaining)
        print(f"{percent}% downloaded") 
        threading.Thread(target=self.mpbpp.update_progressbar,args=(percent))
        
    def download_complete(self,stream,file_path:str):
        file_name = os.path.basename(file_path).split('.')[0]
        self.mpbpp.dismiss()
        MyPopUp(title_text="Success",msg_text="Successfuly Downloaded\n"+file_name)
        print("Done !")
        
    def download_video(self, url):
        print("downloading ...")
        
        try:
            yt = YT(url,on_progress_callback=self.download_progress,on_complete_callback=self.download_complete)
        except e:
           print("Connection Error - ",e)
           
        title = yt.title
        if len(yt.captions) != 0 :
            caption = yt.captions['a.en']
            subtitle = caption.generate_srt_captions()
            completeName = os.path.join(subtitle_output_path, title + '.srt')
            completeName = self.remove_invalid_chars(completeName)
            
            try:
                open(completeName, 'w').write(subtitle)
            except Exception as e:
                print(e)
        
        video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1]
        
        global file_size
        file_size = video.filesize

        try:
            self.mpbpp.open_pb()
            video.download(video_output_path)
        
        except Exception as e:
            print(e)

    