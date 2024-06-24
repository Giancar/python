from collections import Counter
from IPython.display import clear_output
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from textblob import TextBlob
import io
import math
import numpy as np
import pandas as pd
import string

def read_pdf(path):
    rsrcmgr = PDFResourceManager()
    retstr = io.StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password, caching=caching, check_extractable=True): 
        interpreter.process_page(page)
    text = retstr.getvalue()
    text = " ".join(text.replace(u"\xa0", " ").strip().split())  
    fp.close()
    device.close()
    retstr.close()
    return text

read_pdf('primer.pdf')

def pdf_to_df(path):
    content = read_pdf(path)
    blob = TextBlob(content)
    sentences = blob.sentences
    df = pd.DataFrame({'sentence': sentences, 'label': np.nan})
    df['sentence'] = df.sentence.apply(''.join)
    return df
df = pdf_to_df('primer.pdf')
df.head()

df.to_pickle('weird_sentences.pickle')

def manually_label(pickle_file):
    print('Is this sentence weird? Type 1 if yes. \n')
    df = pd.read_pickle(pickle_file)
    for index, row in df.iterrows():
        if pd.isnull(row.label):
            print(row.sentence)
            label = input()
            if label == '1':
                df.loc[index, 'label'] = 1
            if label == '':
                df.loc[index, 'label'] = 0
            clear_output()
            df.to_pickle('weird_sentences.pickle')
            
    print('No more labels to classify!')
manually_label('weird_sentences.pickle')

def append_pdf(pdf_path, df_pickle):
    new_data = pdf_to_df(pdf_path)
    df = pd.read_pickle(df_pickle)
    df = df.append(new_data)
    df = df.reset_index(drop=True)
    df.to_pickle(df_pickle)
def reset_labels(df_pickle):
    df = pd.read_pickle(df_pickle)
    df['label'] = np.nan
    df.to_pickle(df_pickle)

def undersample(df, target_col, r=1):
    falses = df[target_col].value_counts()[0]
    trues = df[target_col].value_counts()[1]
    relation = float(trues)/float(falses)
    if trues >= r*falses:
        df_drop = df[df[target_col] == True]
        drop_size = int(math.fabs(int((relation - r) * (falses))))
    else: 
        df_drop = df[df[target_col] == False]
        drop_size = int(math.fabs(int((r-relation) * (falses))))
    df_drop = df_drop.sample(drop_size)
    df = df.drop(labels=df_drop.index, axis=0)
    return df

df = pd.read_pickle('weird_sentences.pickle').dropna()
df = undersample(df, 'label')
df.label.value_counts()

def bag_of_chars(df, text_col):
    chars = []
    df['char_list'] = df[text_col].apply(list)
    df['char_counts'] = df.char_list.apply(Counter)
    for index, row in df.iterrows():
        for c in row.char_counts:
            df.loc[index, c] = row.char_counts[c]
    chars = list(set(chars))
    df = df.fillna(0).drop(['sentence', 'char_list', 'char_counts'], 1)
    return df
data = bag_of_chars(df, 'sentence')
data.head()

data = data.sample(len(data)).reset_index(drop=True)
train_data = data.iloc[:400]
test_data = data.iloc[400:]
x_train = train_data.drop('label', 1)
y_train = train_data['label']
x_test = test_data.drop('label', 1)
y_test = test_data['label']

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
lr = LogisticRegression()
lr.fit(x_train, y_train)
accuracy_score(y_test, lr.predict(x_test))

def predict_sentence(sentence):
    sample_test = pd.DataFrame({'label': np.nan, 'sentence': sentence}, [0])
    for col in x_train.columns:
        sample_test[str(col)] = 0
    sample_test = bag_of_chars(sample_test, 'sentence')
    sample_test = sample_test.drop('label', 1)
    pred = lr.predict(sample_test)[0]
    if pred == 1:
        return 'WEIRD'
    else:
        return 'NORMAL'

normal_sentence = 'We just built a cool machine learning model'
predict_sentence(normal_sentence)

weird_sentence = 'jdaij oadao //// fiajoaa32 32 5555'
predict_sentence(weird_sentence)