import re
from TextProcessor import TextProcessor

class MildInappropriateLanguageDetector(TextProcessor):
    def __init__(self, text):
        super().__init__(text)
        self.stopwords = set(['the', 'a', 'an', 'is', 'and', 'in', 'of', 'to', 'that', 'it', 'with', 'for'])
        self.threshold = 3

    def count_bad_words(self):
        bad_words = ['damn', 'hell', 'crap', 'sucks']
        count = 0
        for word in self.text.split():
            if word.lower() in bad_words:
                count += 1
        return count

    def classify(self):
        self.remove_punctuation()
        self.remove_stopwords(self.stopwords)
        count = self.count_bad_words()
        if count >= self.threshold:
            return "Mild Inappropriate Language"
        else:
            return "Not Inappropriate"
