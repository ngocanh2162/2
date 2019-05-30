import os.path
import settings
from pyvi import ViTokenizer, ViPosTagger
from underthesea import ner

class NLP(object):
    def __init__(self, text = None):
        self.text = text
        self.__set_stopwords()

    def segmentation(self):
        return ViTokenizer.tokenize(self.text)

    def __set_stopwords(self):
        f_stopwords = open(os.path.join("data","vietnamese-stopwords-dash.txt"), encoding="utf8")
        self.stopwords = f_stopwords.read()

    def split_words(self):
        text = self.segmentation()
        try:
            return [x.strip(settings.SPECIAL_CHARACTER).lower() for x in text.split()]
        except TypeError:
            return []

    def removeDup(self):
        text = self.split_words()
        x = settings.d
        for i in range(0, len(text)):
            for j in range(len(x)):
                flag = True
                if (x[j] in text[i]):
                    if str("_" + x[j]) in text[i]:
                        flag = False
                        index_cut1 = text[i].index(x[j])
                    if str(x[j] + "_") in text[i]:
                        flag = False
                        index_cut1 = text[i].index(str(x[j] + "_")) + len(str(x[j] + "_"))
                    if flag == False:
                        index_cut2 = len(text[i]) - index_cut1
                        s1 = str(text[i][: -(index_cut2+1)])
                        s2 = str(text[i][-index_cut2:])
                        text.remove(text[i])
                        text.insert(i, s1)
                        text.insert(i+1, s2) 
        return text

    def get_words(self):
        split_words = self.removeDup()
        list1 = []
        for word in split_words:
            # if word not in self.stopwords:
                # list1.insert(len(list1), word)
                list1.insert(len(list1),pos_tag(word))
        return list1

def fileInFolder(folderPath, fileList):
    # r=root, d=directories, f = dictionary_files
    for r, d, f in os.walk(folderPath):
        for file in f:
            if '.txt' in file:
                fileList.append(os.path.join(r, file))

# f_ask = open(os.path.join("data","ask","ask3.txt"), encoding="utf8")
# f = []
# dictionary_folder = os.path.join("data","dictionary") 
# dictionary_files = []
# fileInFolder(dictionary_folder, dictionary_files)
# for i in range (0, len(dictionary_files)):
#     open(dictionary_files[i], 'r+', encoding="utf8")
#     f[i] = dictionary_files[i].readlines()

# for line in f_ask:
#     text = NLP(text=line).get_words()
#     for i in range (0, len(dictionary_files)):
#         for x in f[i]:
#             if x in text:
#                 print(x) 

if ViPosTagger.postagging(list[i])[1] == 'M':
                str1 = str1 = ''.join(list[i+1])
                if str1 not in f[7][0]:
                    f[7][0].insert(len(f[7][0]), str1)
                    f[7][1].insert(len(f[7][0]), 1)
                else:
                    f[7][1][f[7][0].index(str1)] += 1
                if str1 in f[l_leng]:
                    index1 = f[l_leng][0].index(list[i+1])
                    v1 = f[l_leng][1][index1]
                    f[7][1][f[l_leng][0].index(list[i+1])] += v1
                    f[l_leng][0].remove(list[i+1])
                    f[l_leng][1].pop(index1)