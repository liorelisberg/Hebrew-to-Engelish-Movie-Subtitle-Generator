
import os

input_path = "C:\\Users\\lior\\Desktop\\final_project\\AI\\DataSet\\CompleteDataSet\\clean_eng_to_heb_dataset.csv"
f = open(input_path,"r",encoding="utf-8")

# print(f.read(100))

lines = f.read().split('\n')
f.close()
print(len(lines))


new_lines = list()

invalid_count = 12

count_1 = list()
count_2 = list()
count_3 = list()
for line in lines:
    
    try:
        heb, eng = line.split(',')
        heb = heb.replace("-"," ")
    except:
        print("1 ",heb[::-1])
        count_1.append(heb)
        continue
    
    if(heb =="hebrewFromSub"): continue
    
    splitted_heb = heb.split(' ')
    # if(len(splitted_heb) == 0 and len(heb)!= 0):
    #     # print("1 ",heb[::-1])
    #     count_1.append(heb)
    #     continue
    
    if(len(splitted_heb) == 1 and len(heb)>invalid_count):
        # print("2 ",heb[::-1])
        count_2.append(heb)
        continue
    
    for word in splitted_heb:
        if(len(word))>invalid_count:
            # print(f"3 {heb[::-1]}, bad word: {word[::-1]}")
            count_3.append((heb,word))
            
    new_line = heb+","+eng
    new_lines.append(new_line)
        
print()
print(f"count_1 : {len(count_1)}")
print(f"count_1 example : {count_1[0]}")
print()
print(f"count_2 : {len(count_2)}")
print(f"count_2 example : {count_2[0]}")
print(f"count_2 example : {count_2[10]}")
print(f"count_2 example : {count_2[100]}")
print(f"count_2 example : {count_2[1000]}")
print(f"count_2 example : {count_2[2000]}")
print()
print(f"count_3 : {len(count_3)}")
print(f"count_3 example : {count_3[0]}")
print(f"count_3 example : {count_3[10]}")
print(f"count_3 example : {count_3[100]}")
print(f"count_3 example : {count_3[1000]}")
print(f"count_3 example : {count_3[10000]}")
print()
print(f"before delete: {len(lines)}")
print(f"lines for delete: {len(count_1)+len(count_2)+len(count_3)}")
print(f"before delete: {len(new_lines)}")

ratio = 100-((len(new_lines)/len(lines))*100)
print(f"ratio: {ratio} %")
print()

output_path = "C:\\Users\lior\Desktop\\final_project\\AI\\DataSet\\CompleteDataSet\\super_clean_eng_to_heb_dataset.csv"
f = open(output_path,"w",encoding="utf-8")

lines_to_write = "\n".join(new_lines)
f.write(lines_to_write)
f.close()
print(f"wrote {len(new_lines)} to file")