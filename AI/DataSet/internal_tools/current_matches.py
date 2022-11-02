import os

path ="C:\\Users\\lior\\Desktop\\STUDY\\final_project\\AI\\DataSet\\Tables"

#we shall store all the file names in this list
matches_count = 0


print("starting matches count")

for _, _, files in os.walk(path):
    for file in files:
        if "csv" in file and "Avg" in file:
            full_path = path + '\\' + file
            
            try:
                f = open(full_path,"r",encoding='utf-8')
                Content = f.read()
            except Exception as e:
                print(f'### Error ### - {e.with_traceback}')
                
            CoList = Content.split("\n")
            
            for i in CoList:
                if i:
                    matches_count += 1
            
            # print(f'{matches_count} lines so far..')

print(f'in total {matches_count} lines')
            
                    
                    

