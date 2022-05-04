
import os


class MediaFormatValidaor:
    
    def __init__(self):
        self.valid_video_formats = ("mp4", "mov", "wmv", "avi")
        self.valid_audio_formats = ("mp3", "wav")
    
        
    def is_valid_format(self,file:str):
        split_tup = os.path.splitext(file)    
        self.file_name = split_tup[0].split('\\')[-1]
        
        # extracting the path using reverting, picking and reverting again 
        self.full_path = split_tup[0][::-1].partition('\\')[-1][::-1]
        
        self.file_extension = split_tup[1].replace('.','')
        
        print("file name: ",self.file_name)
        print("path: ",self.full_path)
        
        return self.file_extension in self.valid_audio_formats  or self.file_extension in self.valid_video_formats
        
           
def test():
    file_path = "C:\\Users\\lior\\Desktop\\STUDY\\final_project\\srtMovieName.srt"
    print("format: ",MediaFormatValidaor().is_valid_format(file=file_path))
    
if __name__ =='__main__':
    test()
    