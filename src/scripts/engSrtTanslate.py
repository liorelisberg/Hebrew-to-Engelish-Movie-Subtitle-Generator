import pysrt
import pandas as pd
from googletrans import Translator

# read table
# print("start")
# tablePath = 'CompleteDataSet/eng_to_heb_dataset.csv'
# data = pd.read_csv(tablePath, low_memory=False)
# print("readTable")

translator = Translator()


def engSrtToHebSrt(sourcePath, destPath):
    try:
        subs = pysrt.open(sourcePath, encoding='iso-8859-1')
        counter = 1
        
        print("processing tranlation ...")
        for sentence in subs:
            sentence.text = translate(sentence.text)
            counter = counter +1
        destPath = destPath.replace(".srt"," - translated.srt")
        subs.save(destPath, encoding='utf-8')
        print("Done processing.")
        return destPath
    except:
        return ""


def translate(sen):
    translateSen = translator.translate(text=sen, dest="iw", src="en")
    return translateSen.text

