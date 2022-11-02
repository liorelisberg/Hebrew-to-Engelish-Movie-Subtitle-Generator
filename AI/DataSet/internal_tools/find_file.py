import os

path ="C:\\Users\\lior\\Desktop\\STUDY\\final_project\\AI\\DataSet\\Tables"
#we shall store all the file names in this list
filelist = []

start = 1540500
end = 2970000

avg = str(int((start + end)/2))

is_there = False
for root, dirs, files in os.walk(path):
    for file in files:
        if str(avg) in file: 
            print(file)
            is_there = True
            
print(f"index file - {avg}")
print(f"is it there? - {is_there}")
    
            


