from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from function import *
from collections import Counter

raw_text = "A barber is a person. a barber is good person. a barber is huge person. he Knew A Secret! The Secret He Kept is huge secret. Huge secret. His barber kept his word. a barber kept his word. His barber kept his secret. But keeping and keeping such a huge secret to himself was driving the barber crazy. the barber went up a huge mountain."


def use_dictionary():
    sentences = sent_tokenize(raw_text)
    vocab = {}
    preprocessed_sentences = []
    stop_words = set(stopwords.words("english"))

    for sentence in sentences:
        words = word_tokenize(sentence)
        result = []

        for word in words:
            word = word.lower()
            if word not in stop_words:
                if len(word) > 2:
                    result.append(word)
                    if word not in vocab:
                        vocab[word] = 0
                    vocab[word] += 1
        preprocessed_sentences.append(result)
    print("단어 집합: {}".format(vocab))

    # vocab 빈도 순대로 정렬
    vocab_sorted = sorted(vocab.items(), key=lambda x: x[1], reverse=True)

    word_to_index = {}
    i = 0
    for word, freq in vocab_sorted:
        if freq > 3:
            i += 1
            word_to_index[word] = i
    word_to_index["OOV"] = len(word_to_index) + 1

    print("빈도가 3 이상인 단어들의 인코딩: {}".format(word_to_index))

    encoded_sentences = []
    for sentence in preprocessed_sentences:
        encoded_sentence = []
        for word in sentence:
            try:
                encoded_sentence.append(word_to_index[word])
            except KeyError:
                encoded_sentence.append(word_to_index["OOV"])
        encoded_sentences.append(encoded_sentence)

    print("정수 인코딩 결과: \n{}".format(encoded_sentences))


if __name__ == "__main__":
    big_chapter("Integer Encoding")
    chapter("6-1")
    use_dictionary()
