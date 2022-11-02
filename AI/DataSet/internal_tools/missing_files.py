import os
import re
import sys

path ="C:\\Users\\lior\\Desktop\\STUDY\\final_project\\AI\\DataSet"

corrupted_files = ["192000", "696000","390000","2988000"]

filelist = []

for root, dirs, files in os.walk(path):
    for file in files:
        if "csv" in file and "Avg" in file:
            filelist.append(os.path.join(root,file))

if len(filelist) == 0:
    print("no csv files in dir")
    sys.exit()
    
print(f"{len(filelist)} csv files in dir")

file_indexes_list = []
for file in filelist:
    result = re.search('Avg(.*)Table', file)
    file_indexes_list.append(result.group(1))

int_indexes_list = [int(i) for i in file_indexes_list]
int_indexes_list.sort()

missing_files = []
prev_index = int_indexes_list[0]

for index in int_indexes_list:
    if index == prev_index:
        continue
    
    if index-prev_index != 1500:
        missing_files.append((prev_index,index))
        if index - prev_index  == 3000:
            print(f"missing a file {int((index+prev_index)/2)} between {(prev_index,index)}")
        else:
            step = 1500
            files = list(range(prev_index+step,index,step))
            if len(files) > 3:
                print(f"missing {len(files)} between {(prev_index,index)}") 
            else:    
                print(f"missing {len(files)} files: {', '.join(map(str, files))} between {(prev_index,index)}")
    
    prev_index = index

print(f"missing {len(missing_files)} csv files in dir")
print('#'*30)
print(f"{len(corrupted_files)} corrupted files in dir - {', '.join(map(str, corrupted_files))}")
print('#'*30)