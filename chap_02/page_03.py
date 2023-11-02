from nltk.stem import WordNetLemmatizer, PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.tokenize import word_tokenize


def chapter(string: str) -> str:
    print("-" * 15, string, "-" * 15)


def big_chapter(string: str) -> str:
    print("=" * 45)
    print(" " * 15, string, " " * 15)
    print("=" * 45)


def lemmatize():
    lemmatizer = WordNetLemmatizer()
    words = [
        "policy",
        "doing",
        "organization",
        "have",
        "going",
        "love",
        "lives",
        "fly",
        "dies",
        "watched",
        "has",
        "starting",
    ]
    print("표제어 추출 전: {}".format(words))
    print("표제어 추출 후: {}".format([lemmatizer.lemmatize(word) for word in words]))
    pos = ["n", "v", "n", "v", "v", "v", "v", "v", "v", "v", "v", "v"]
    print(
        "표제어 개선 후: {}".format(
            [lemmatizer.lemmatize(words[i], pos[i]) for i in range(len(words))]
        )
    )


sentence = "This was not the map we found in Billy Bones's chest, but an accurate copy, complete in all things--names and heights and soundings--with the single exception of the red crosses and the written notes."
tokenized_sentence = word_tokenize(sentence)


def porter_stemmer():
    porter = PorterStemmer()
    print(
        "Porter Stemmer 사용: {}".format(
            [porter.stem(word) for word in tokenized_sentence]
        )
    )


def lencaster_stemmer():
    lencaster = LancasterStemmer()
    print(
        "Lencaster Stemmer 사용: {}".format(
            [lencaster.stem(word) for word in tokenized_sentence]
        )
    )


if __name__ == "__main__":
    big_chapter("Stemming and Lemmatization")
    chapter("2-1")
    lemmatize()
    chapter("2-2")
    porter_stemmer()
    chapter("2-3")
    lencaster_stemmer()
