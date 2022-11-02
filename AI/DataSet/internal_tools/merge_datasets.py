import os
import re

input_path ="C:\\Users\\lior\\Desktop\\STUDY\\final_project\\AI\\DataSet\\Tables"
complete_dataset_output_path = "C:\\Users\\lior\\Desktop\\STUDY\\final_project\\AI\\DataSet\\CompleteDataSet\\eng_to_heb_dataset.csv"
clean_dataset_output_path = "C:\\Users\\lior\\Desktop\\STUDY\\final_project\\AI\\DataSet\\CompleteDataSet\\clean_eng_to_heb_dataset.csv"
invalid_input_path = "C:\\Users\\lior\\Desktop\\STUDY\\final_project\\AI\\DataSet\\CompleteDataSet\\invalid_lines.txt"

#we shall store all the file names in this list
filelist = []

for root, dirs, files in os.walk(input_path):
    for file in files:
        if "csv" in file and "Avg" in file:
            filelist.append(os.path.join(root,file))
            
            
print(len(filelist))
print(filelist[0])
print(filelist[1])

headers ="index,hebrewFromSub,englishFromSub,englishTranslation,ratio"


def create_clean_complete_dataset():
    with open(clean_dataset_output_path, 'w', encoding="utf8") as outfile:
        
        # take only hebrewFromSub,englishFromSub
        clean_headers = ','.join(headers.split(',')[1:3])
        outfile.write(clean_headers+'\n')
        
        for fname in filelist:
            with open(fname,encoding="utf8") as infile:
                isFirstLine = True
                
                for line in infile:
                    if(isFirstLine == True):
                        isFirstLine = False
                        continue
                    
                    line = line.replace('\"\"','')
                    
                    quotes = re.findall(r'"([^"]*)"', line)
                    
                    for quote in quotes:
                        double_quotes = re.findall(r'"([^"]*)"', quote)
                        
                        if(len(double_quotes)>0):
                            line = line.replace("\""+quote+"\"",quote)
                    
                        line = line.replace("\""+quote+"\"",quote.replace(',',''))
                    
                    splitted_line = line.split(',')
                   
                    if(len(splitted_line) != 5):
                        quotes_strings = re.findall(r'"([^"]*)"', line)
                        
                        if quotes_strings == []:
                            with open(invalid_input_path,'a',encoding="utf8") as invalid_file:
                                invalid_file.write(line)
                                continue
                        
                        new_line = ""
                        for quetes_string in quotes_strings:
                            quetes_string = "\""+quetes_string+"\""
                            new_line = line.replace(quetes_string+',','')
                        
                        splitted_line = new_line.split(',')
                        (index,hebrewFromSub,englishFromSub,ratio) =  splitted_line
                        
                    else:  
                        (index,hebrewFromSub,englishFromSub,englishTranslation,ratio) =  splitted_line
                        
                    clean_line = ",".join((hebrewFromSub.strip(), englishFromSub.strip()))+"\n"
                            
                    outfile.write(clean_line)
                                  
def create_complete_dataset():
    with open(complete_dataset_output_path, 'w', encoding="utf8") as outfile:
        
        outfile.write(headers)
        
        i = 1
        
        for fname in filelist:
            with open(fname,encoding="utf8") as infile:
                isFirstLine = True
                
                for line in infile:
                        
                    if(isFirstLine == True):
                        isFirstLine = False
                        continue
                    outfile.write(line)
                    i += 1
                    

def GetLinesCount(file_path):
    lines_count = sum(1 for line in open(file_path,encoding="utf-8"))
    return lines_count

def main():
    print('#'*20 + " Creating complete dataset ... " + '#'*20 )
    create_complete_dataset()
    print(f"Lines in eng_to_heb_dataset.csv {GetLinesCount(complete_dataset_output_path)}")

    # print('#'*20 + " Creating clean dataset ... " + '#'*20 )
    # create_clean_complete_dataset()
    print(f"Lines in clean_eng_to_heb_dataset.csv {GetLinesCount(clean_dataset_output_path)}")
       
if __name__ == '__main__':
    main()

    