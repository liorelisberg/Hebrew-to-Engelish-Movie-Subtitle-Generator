import os
import pandas as pd
import num2words as nw
from fuzzywuzzy import fuzz
from googletrans import Translator
from langdetect import detect
import re

lines_per_file = 1500

translator = Translator()
def TranslateLanguages(sentence,sent_src='he',sent_dest='en'):
    try:
        translated = translator.translate(sentence.strip(), src=sent_src, dest=sent_dest).text
        return translated
    except Exception as e:
        print(f"An exception occurred google-translating {e}")
        return "### Error ###"

def clean_subtitled(sub):
    list_of_sentence = list()
    for sentence in sub:
        list_of_sentence.append((sentence)
                                .replace("<i>", " ").replace("</i>", " ")
                                .replace(".", " ").replace(",", " ")
                                .replace("?", " ").replace("  ", " ")
                                .lstrip())

    text = ''.join(list_of_sentence)
    re.sub(r'[\(\[].*?[\)\]]', "", text).replace("  "," ")
    return text.split("\n")

def turn_number_to_words(number):
    if number.isnumeric():
        return nw.num2words(number)
    return number

def average(lst):
    return sum(lst) / len(lst)

def matching_subtitle(englishWords, hebrewSentence, movieName):
    hebrew_subtitles, english_subtitles, english_google_translation, ratio_scale = [],[],[],[]
    high_ratio_sentence_big,not_first_time,heb_sen_length = '',False,len(hebrewSentence)

    for j in range(25, len(englishWords)):
        for z in range(0, len(hebrewSentence)):
            heb_sen_length -= 1
            
            if heb_sen_length <= 1:
                break
            
            heb_sen_length -= 1
            
            if(hebrewSentence[i].isnumeric()):
                print(f"line was numeric - {hebrewSentence[i]}")
                i+=1
                continue
            
            try:
                if(detect(hebrewSentence[z]) != 'he'):
                    print(f"invalind line - {hebrewSentence[z]}")
                    translate_matching = hebrewSentence[z]
                    hebrewSentence[z] = TranslateLanguages(hebrewSentence[z],sent_src='en',sent_dest='he')
                else:
                    translate_matching = TranslateLanguages(hebrewSentence[z])
            except:
                print(f"line {hebrewSentence[i]} throws error")
            
            if not_first_time and high_ratio_big > 60:
                print(prev_heb_sentence)
                print(high_ratio_big)
                print(high_ratio_sentence_big)
                print(prev_translation_sentence)
                print("**************")
                ratio_scale.append(high_ratio_big)
                hebrew_subtitles.append(prev_heb_sentence)
                english_subtitles.append(high_ratio_sentence_big)
                english_google_translation.append(prev_translation_sentence)
                print(average(ratio_scale))
                print("**************")
                
            english_sen,high_ratio_sentence ,high_ratio_big, high_ratio = '', '', 0, 0

            for i in range(j-10, j+25):
                prev_heb_sentence = hebrewSentence[z]
                prev_translation_sentence = translate_matching
                not_first_time = True
                
                if high_ratio > high_ratio_big:
                    high_ratio_sentence_big = high_ratio_sentence
                    high_ratio_big = high_ratio
                    j = i
                    
                english_sen,ratio, high_ratio, prev_ratio = '', 0, 0, 0 

                for k in range(i-15, i+25):
                    english_sen += englishWords[k] + " "
                    ratio = fuzz.token_sort_ratio(translate_matching, english_sen)
                    if ratio >= prev_ratio and ratio != 0:
                        if ratio >= high_ratio:
                            high_ratio = ratio
                            high_ratio_sentence = english_sen
                            i = k
    df = pd.DataFrame({
        'hebrewFromSub': hebrew_subtitles,
        'englishFromSub': english_subtitles,
        'englishFromTranslation': english_google_translation,
        'ratio': ratio_scale
    })
    df.to_pickle(f'{movieName}Dataframe.pkl')
    df.to_csv(f'{movieName}Table.csv')

def match_sentence_to_sentence(englishSentence, hebrewSentence, fileName):
    tries,delta, i, prev_ratio, best_ratio = 10, 5 , 0, 0, 0
    hebrew, english, ratio_scale, english_translation = [] , [] , [], []
    best_match, hebrew_sen, translation_sen, first_time = '' , '', '', False
    
    try:
        while True:
            if first_time:
                
                if best_ratio >= 60:
                    hebrew.append(hebrew_sen.strip())
                    english.append(best_match.strip())
                    ratio_scale.append(best_ratio)
                    english_translation.append(translation_sen.strip())
                    
                    if best_ratio > 85 and tries < 12 and delta > 10:
                        tries += 1
                        delta -= 3
                        
                elif best_ratio < 40:
                    tries -= 1
                    delta += 3
                    
                if tries == 0:
                    break
                    
                # print("***********")
                # print(delta)
                print(i)
                # print(best_ratio)
                # print(hebrew_sen)
                # print(best_match)
                # print(average(ratio_scale))
                # print(translation_sen)
                # print("***********")
                
                best_match, translation_sen = '', ''
                best_ratio, ratio, prev_ratio = 0, 0 ,0
                
            if(hebrewSentence[i].isnumeric()):
                print(f"line was numeric - {hebrewSentence[i]}")
                i+=1
                continue
                
            try:
                if(detect(hebrewSentence[i]) != 'he'):
                    translate_matching = hebrewSentence[i]
                    hebrewSentence[i] = TranslateLanguages(hebrewSentence[i],sent_src='en',sent_dest='he')
                else:
                    translate_matching = TranslateLanguages(hebrewSentence[i])
            except:
                print(f"line {hebrewSentence[i]} throws error")
                i+=1
                continue
                            
            if translate_matching == "### Error ###":
                while translate_matching == "### Error ###":
                    print(i)
                    translate_matching = TranslateLanguages(hebrewSentence[i])
                    
            hebrew_sen = hebrewSentence[i]
            first_time = True
            for z in range(i-delta, i+delta):
                if z < 0:
                    z = 0
                    
                ratio = fuzz.token_sort_ratio(translate_matching, englishSentence[z])
                if ratio > prev_ratio:
                    if ratio > best_ratio:
                        best_match = englishSentence[z]
                        best_ratio = ratio
                        translation_sen = translate_matching
                prev_ratio = ratio
                
            i += 1
            if i+delta+2 > len(hebrewSentence) or i+delta+2 > len(englishSentence):
                break
        
        corrupted = False
        
        if hebrew == [] or english == [] or english_translation == []:
            corrupted =  True
            print(f"all lists are empty -  check if file {fileName} is corrupted ")
        else:   
            df = pd.DataFrame({'hebrewFromSub': hebrew,'englishFromSub': english,'englishTranslation': english_translation,'ratio': ratio_scale})
        
    except Exception as e:
        print(f"in loop crash - {e}")
        
    if not corrupted:
        pickle_file  = f'Pickles/{fileName}Dataframe.pkl'
        csv_file = f'Tables/{average(ratio_scale)}Avg{fileName}Table.csv'
        
        try:
            df.to_pickle(pickle_file, encoding='utf-8-sig')
            df.to_csv(csv_file, encoding='utf-8-sig')
            
        except TypeError as e:
            print(f"invalid param 'encoding=' - {e}")
        except Exception as e:
            print(f"out of loop crash - {e}")
        finally:
            df.to_pickle(pickle_file)
            df.to_csv(csv_file)
            print(f'######## end of file index {fileName} #########')

def main():

    path ="C:\\Users\\lior\\Desktop\\STUDY\\final_project\\AI\\DataSet\\Tables"
    
    fileName = 1797000
    end_file_index = 2970000
    
    while fileName < end_file_index:

       # TODO remove this ! # 
        exists,currentFile = False,""
        
        for file in os.listdir(path):
            if file.endswith(f"Avg{fileName}Table.csv") :
                exists = True
                currentFile = str(file)
                break
            
        if exists == True:
            print(f'File {currentFile} already exists.')
            fileName += lines_per_file
            continue

        # TODO remove this ! # 
        
        try:
            print(f'###### starting file {fileName} ######')
            EnglishFile = open('EnglishSentence/english_small_file_{}'.format(fileName), 'r', encoding='utf-8-sig')
            HebrewFile = open('HebrewSentence/hebrew_small_file_{}'.format(fileName), 'r', encoding="utf8")
            English = clean_subtitled(EnglishFile.readlines())
            Hebrew = clean_subtitled(HebrewFile.readlines())
            print("start main function loop")
            match_sentence_to_sentence(English, Hebrew, fileName)
        except Exception as e:
            print(f"missing folders or failed matching - {e}")
        finally:
            fileName += lines_per_file
            print(f'###### End of file {fileName} ######')

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
    finally:
        print("######### End of Program #########")