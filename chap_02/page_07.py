import numpy as np
from function import *
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences


preprocessed_sentences = [
    ["barber", "person"],
    ["barber", "good", "person"],
    ["barber", "huge", "person"],
    ["knew", "secret"],
    ["secret", "kept", "huge", "secret"],
    ["huge", "secret"],
    ["barber", "kept", "word"],
    ["barber", "kept", "word"],
    ["barber", "kept", "secret"],
    ["keeping", "keeping", "huge", "secret", "driving", "barber", "crazy"],
    ["barber", "went", "huge", "mountain"],
]

tokenizer = Tokenizer()


def padding_with_numpy():
    tokenizer.fit_on_texts(preprocessed_sentences)
    encoded = tokenizer.texts_to_sequences(preprocessed_sentences)

    # padding
    max_len = max(len(item) for item in encoded)
    for sentence in encoded:
        while len(sentence) < max_len:
            sentence.append(0)

    padded_np = np.array(encoded)
    print(padded_np)


def padding_with_keras():
    encoded = tokenizer.texts_to_sequences(preprocessed_sentences)
    padded = pad_sequences(encoded)
    print(padded)


if __name__ == "__main__":
    big_chapter("Padding")
    chapter("7-1")
    padding_with_numpy()
    chapter("7-2")
    padding_with_keras()
