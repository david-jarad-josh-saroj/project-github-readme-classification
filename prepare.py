

# unicode, regex, json for text digestion
import unicodedata
import re
import json

# nltk: natural language toolkit -> tokenization, stopwords (more on this soon)
import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords

# pandas dataframe manipulation, acquire script, time formatting
import pandas as pd
import acquire





def basic_clean(text):
    '''
    This function returns a normalized lowercase version of input text.
    '''
    text = text.lower()

    text = unicodedata.normalize('NFKD', text)\
             .encode('ascii', 'ignore')\
             .decode('utf-8', 'ignore')
    text = re.sub(r'[^\w\s]', '', text).lower()
    text = re.sub(r'\w*\n\w*', '', text)
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    return text


def tokenize(text):
    '''
    This function returns a tokenized version of the input text.
    '''
    tokenizer = nltk.tokenize.ToktokTokenizer()
    text = tokenizer.tokenize(text, return_str=True)
    return text


def stem(text):
    '''
    This function returns a stemmed text.
    '''
    ps = nltk.porter.PorterStemmer()
    stems = [ps.stem(word) for word in text.split()]
    text = ' '.join(stems)    
    return text


def lemmatize(text):
    '''
    This function returns a lemmatized version of the input text.
    '''
    wnl = nltk.stem.WordNetLemmatizer()
    lemmas = [wnl.lemmatize(word) for word in text.split()]
    text = ' '.join(lemmas)    
    return text


def remove_stopwords(text, extra_words = [], exclude_words = []):
    '''
    This function limits the output of words with parameters set in place to exclude words 
    and add extra words ontop of the stopwords .
    '''
    stopword_list = stopwords.words('english')
    stopword_list = set(stopword_list) - set(exclude_words)
    stopword_list = stopword_list.union(set(extra_words))
    words = text.split()
    filtered_words = [word for word in words if word not in stopword_list]
    text_without_stopwords = ' '.join(filtered_words)    
    return text_without_stopwords


