import nltk

# nltk.download('punkt')

from nltk.tokenize import word_tokenize

text = 'Hello, My name is Kim. Nice to meet you.'

print(word_tokenize(text))
