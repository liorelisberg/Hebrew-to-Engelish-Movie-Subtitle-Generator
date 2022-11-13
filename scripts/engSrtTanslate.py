import pysrt
import re
from AI.Model.Translator import translate

# needed when translation is overly unaccurate 
from googletrans import Translator
translator = Translator()


def isAllUnk(target:str):
    try:
        count_unk = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape("_"), target))
        ratio = (count_unk/len(target.split()))*100
        if ratio >= 50.0: return True
        else: return False
    except Exception as e:
        print (e)
        return False

def isCorruptedLentgh(target, source):
    try:
        return len(target.split()) > len(source.split())*2
    except Exception as e:
        print (e)
        return False
       
def engSrtToHebSrt(sourcePath, destPath,t):
    try:
        subs = pysrt.open(sourcePath, encoding='iso-8859-1')
        counter = 1
        
        # print("processing tranlation ...")
        for sentence in subs:
            try:
                translated = translate(t=t,source=sentence.text)
                if(len(translated) == 0 or len(translated) == 1 or isAllUnk(translated) or isCorruptedLentgh(translated,sentence.text)):
                    other_trans = translator.translate(text=sentence.text,dest='iw')
                    if len(other_trans.text.split()) == 1 or len(other_trans.text.split()) > 6:
                       sentence.text =  translated
                    else:
                        sentence.text  = other_trans.text
                else:    
                    sentence.text =  translated
            except Exception as e:
                print(e)
                sentence.text  = translator.translate(sentence.text)
            finally:
                counter = counter +1
                
        destPath = destPath.replace(".srt"," - translated.srt")
        subs.save(destPath, encoding='utf-8')
        print("Done processing.")
        return destPath
    except:
        return ""