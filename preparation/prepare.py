import re
import pandas as pd

def tokenize_sentences_bengali(text):
    pattern = r'।|\?|!'  # Common sentence delimiters in Bengali
    sentences = re.split(pattern, text)
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    return sentences
    
def tokenize_words_bengali(sentence):
    return sentence.split()

stopwords_url = 'https://raw.githubusercontent.com/avisheak/preparation/main/stopwords_bangla.csv'
stopwords_df = pd.read_csv(stopwords_url)
stopwords = set(stopwords_df['words'].tolist())

def remove_stopwords(tokens):
    return [token for token in tokens if token not in stopwords]


def custom_stemmer(word):
    suffixes = ['ের', 'কে', 'দের', 'র', 'তে', 'ও', 'ওয়া']  # Add more suffixes as needed
    for suffix in suffixes:
        if word.endswith(suffix):
            return word[:-len(suffix)]
    return word

def stem_words(tokens):
    return [custom_stemmer(word) for word in tokens]

def prepare(text):
    # text = punctuation_removal(text)
    sentences = tokenize_sentences_bengali(text)
    tokenized_sentences = [tokenize_words_bengali(sentence) for sentence in sentences]
    cleaned_sentences = [remove_stopwords(tokens) for tokens in tokenized_sentences]
    stemmed_sentences = [stem_words(tokens) for tokens in cleaned_sentences]
    return stemmed_sentences
