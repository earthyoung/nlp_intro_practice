from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from konlpy.tag import Okt
from .function import *


def check_stopwords():
    stopword_list = stopwords.words("english")
    print("불용어 개수: {}".format(len(stopword_list)))
    print("불용어 10개: {}".format(stopword_list[:10]))


def remove_stopwords_english():
    example = "Family is not an important thing. It's everything."
    stopword_list = set(stopwords.words("english"))
    tokenized_words = word_tokenize(example)
    print("불용어 제거 전: {}".format(tokenized_words))
    filtered_words = [word for word in tokenized_words if word not in stopword_list]
    print("불용어 제거 후: {}".format(filtered_words))


if __name__ == "__main__":
    print(__package__)
    big_chapter("Stopwords")
    chapter("4-1")
    check_stopwords()
    chapter("4-2")
    remove_stopwords_english()
