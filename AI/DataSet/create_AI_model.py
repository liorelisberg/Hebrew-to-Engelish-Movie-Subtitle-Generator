import pandas as pd

# from ast import Index
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score

def dataframes_to_big_csv(start,end,delta=1500):
    i = start
    listOfDataframes = []
    missingFiles = []
    while end > i:
        try:
            a = pd.read_pickle('DataFrames/{}Dataframe.pkl'.format(i))
            tempDf = pd.DataFrame(a)
            listOfDataframes.append(tempDf)
            i = i + delta
        except:
            missingFiles.append(i)
            i = i + delta

    df = pd.concat(listOfDataframes, ignore_index=True)
    print(df.columns)
    df.to_csv(r'bigFile.csv', encoding='utf-8-sig')
    return missingFiles


# def test_func():
#     dataframes_to_big_csv(1500,36000,delta=1500)
#     sentence = pd.read_csv('bigFile.csv')
    
#     X = sentence['englishFromSub']
#     y = sentence['hebrewFromSub']
    
#     X_train, X_test , y_train, y_test = train_test_split(X,y, test_size=0.2)

#     model = DecisionTreeClassifier()
#     model.fit(X_train,y_train)
#     predictions = model.predict(X_test)

#     print(accuracy_score(y_test,predictions))

#     Index(['hebrewFromSub', 'englishFromSub', 'englishTranslation', 'ratio'], dtype='object')
    
    
# if __name__ == '__main__':
#     test_func()