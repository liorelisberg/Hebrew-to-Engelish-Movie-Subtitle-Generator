lines_per_file = 1500
smallfile = None

files_path ="C:\\Users\\lior\\Desktop\\STUDY\\final_project\\AI\\DataSet\\OpenSubtitles.en-he.he"


print("start")
with open(files_path, encoding="utf8") as bigfile:
    for lineno, line in enumerate(bigfile):
        if lineno % lines_per_file == 0:
            if smallfile:
                smallfile.close()
            small_filename = 'HebrewSentence/hebrew_small_file_{}'.format(lineno + lines_per_file)
            smallfile = open(small_filename, "w", encoding="utf8")
        smallfile.write(line)
    if smallfile:
        smallfile.close()


print("end")