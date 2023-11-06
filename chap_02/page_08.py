from konlpy.tag import Okt
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.utils import to_categorical


def one_hot_encoding_python():
    okt = Okt()

    text = "나는 자연어 처리를 배운다"
    tokens = okt.morphs(text)
    word_to_index = {word: index for index, word in enumerate(tokens)}

    def one_hot_encoding(word, word_to_index):
        one_hot_vector = [0] * (len(word_to_index))
        index = word_to_index[word]
        one_hot_vector[index] = 1
        return one_hot_vector

    for word in tokens:
        print(one_hot_encoding(word, word_to_index))


def one_hot_encoding_keras():
    text = "나랑 점심 먹으러 갈래 점심 메뉴는 햄버거 갈래 갈래 햄버거 최고야"

    tokenizer = Tokenizer()
    tokenizer.fit_on_texts([text])
    encoded = tokenizer.texts_to_sequences([text])[0]
    one_hot = to_categorical(encoded)
    print(one_hot)


if __name__ == "__main__":
    one_hot_encoding_python()
    one_hot_encoding_keras()
