import re

class TextProcessor:
    def __init__(self, text):
        self.text = text

    def remove_punctuation(self):
        self.text = re.sub(r'[^\w\s]', '', self.text)

    def remove_stopwords(self, stopwords):
        self.text = ' '.join([word for word in self.text.split() if word.lower() not in stopwords])
