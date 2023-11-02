from nltk.tokenize import word_tokenize
from nltk.tokenize import WordPunctTokenizer
import keras

sentence = "Don't be fooled by the dark sounding name, Mr. Jone's Orphanage is as cheery as cheery goes for a pastry shop."
print("word_tokenize: {}\n".format(word_tokenize(sentence)))
print("WordPunctTokenizer: {}\n".format(WordPunctTokenizer().tokenize(sentence)))
print(
    "text_to_word_sequence: {}\n".format(
        keras.preprocessing.text.text_to_word_sequence(sentence)
    )
)


from nltk.tokenize import TreebankWordTokenizer

tokenizer = TreebankWordTokenizer()
text = "Starting a home-based restaurant may be an ideal. it doesn't have a food chain or restaurant of their own."
print("TreebankWordTokenizer: {}\n".format(tokenizer.tokenize(text)))


from nltk.tokenize import sent_tokenize

sentences = "His barber kept his word. But keeping such a huge secret to himself was driving him crazy. Finally, the barber went up a mountain and almost to the edge of a cliff. He dug a hole in the midst of some reeds. He looked about, to make sure no one was near."
print("sent_tokenize: {}\n".format(sent_tokenize(sentences)))

sentences2 = "I am actively looking for Ph.D. students. and you are a Ph.D student."
print("sent_tokenize(2): {}\n".format(sent_tokenize(sentences2)))


import kss

text = "딥 러닝 자연어 처리가 재미있기는 합니다. 그런데 문제는 영어보다 한국어로 할 때 너무 어렵습니다. 이제 해보면 알걸요?"
print("kss.split_sentences: {}\n".format(kss.split_sentences(text)))


from nltk.tag import pos_tag

text = "I am actively looking for Ph.D. students. and you are a Ph.D. student."
tokenized_sentence = word_tokenize(text)
print("Word Tokenization: {}".format(tokenized_sentence))
print("Parts of Speech: {}".format(pos_tag(tokenized_sentence)))


from konlpy.tag import Okt
from konlpy.tag import Kkma

okt = Okt()
kkma = Kkma()

text = "열심히 코딩한 당신, 연휴에는 여행을 가봐요"
print("OKT 형태소 분석", okt.morphs(text))
print("OKT 품사 태깅", okt.pos(text))
print("OKT 명사 추출", okt.nouns(text))

print("Kkma 형태소 분석", kkma.morphs(text))
print("Kkma 품사 태깅", kkma.pos(text))
print("Kkma 명사 추출", kkma.nouns(text))
