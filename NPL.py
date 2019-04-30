from pyvi import ViTokenizer, ViPosTagger
import settings
import os
class NLP(object):
    def __init__(self, text = None):
        self.text = text
        self.__set_stopwords()

    def segmentation(self):
        return ViTokenizer.tokenize(self.text)

    def __set_stopwords(self):
        f_stopwords = open(os.path.join("data","vietnamese-stopwords-dash.txt"),encoding="utf8")
        self.stopwords = f_stopwords.read()

    def split_words(self):
        text = self.segmentation()
        try:
            return [x.strip(settings.SPECIAL_CHARACTER).lower() for x in text.split()]
        except TypeError:
            return []
            
    def get_words(self):
        split_words = self.split_words()
        # return [word for word in split_words if word not in self.stopwords]
        list1 = [] 
        # atuple = [['V'], ['A']]
        for word in split_words:
            if word not in self.stopwords:
                # if ViPosTagger.postagging(word)[1] not in atuple:
                    list1.append(word)
        return list1
    
    def get_words2(self):
        split_words = self.split_words()
        str = ''
        for word in split_words:
            # if word not in self.stopwords:
                str += word + ' '
        return str
    
    