import os

path = "Subtitles_Files\\Dummies University Beekeeping 101 (Beekeeping for Dummies).srt"

f = open(path, "r")

lines = f.read()
f.close()

print(lines)

lines = lines.split("\n\n")

print(lines)
new_lines = list()

for line in lines:
    try:
        index, timestamp, _ = line.split("\n")
        new_line = (index,timestamp,"אם אתה אלרגי לדבורים")
        new_line = "\n".join(new_line)
        new_lines.append(new_line)
    except:
        print("here")
        continue
    
new_sub = "\n\n".join(new_lines)



path = "Subtitles_Files\\Dummies University Beekeeping 101 (Beekeeping for Dummies) - with Hebrew subtitles.txt"

f = open(path,"+r",encoding="utf8")
f.write(new_sub)
f.close()
