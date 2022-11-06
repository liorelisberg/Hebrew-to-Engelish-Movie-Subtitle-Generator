# import os

# path = "Subtitles_Files\\Dummies University Beekeeping 101 (Beekeeping for Dummies).srt"

# f = open(path, "r")

# lines = f.read()
# f.close()

# print(lines)

# lines = lines.split("\n\n")

# print(lines)
# new_lines = list()

# for line in lines:
#     try:
#         index, timestamp, _ = line.split("\n")
#         new_line = (index,timestamp,"אם אתה אלרגי לדבורים")
#         new_line = "\n".join(new_line)
#         new_lines.append(new_line)
#     except:
#         print("here")
#         continue
    
# new_sub = "\n\n".join(new_lines)
import subprocess

# path = "Subtitles_Files\\Dummies University Beekeeping 101 (Beekeeping for Dummies) - with Hebrew subtitles.txt"

# f = open(path,"+r",encoding="utf8")
# f.write(new_sub)
# f.close()

def embed_subtitles_to_video(video_path,translated_subtitles_path):

    trans_video_path = video_path.split("\\")[-1]
    translated_subtitles_path = translated_subtitles_path.replace("\\","/")
    command = f"ffmpeg -threads 8 -i \"{video_path}\" -vf subtitles=\"{translated_subtitles_path}\" -acodec copy -movflags +faststart \"{trans_video_path}\""
    subprocess.call(command,shell=True)
    return video_path

video_path = "Video_Downloads\God of War Ragnarok - Official Trailer (Ben Stiller LeBron James John Travolta).mp4"
translated_subtitles_path = "Subtitles_Files\God of War Ragnarok - Official Trailer (Ben Stiller LeBron James John Travolta) - translated.srt"

embed_subtitles_to_video(video_path,translated_subtitles_path)