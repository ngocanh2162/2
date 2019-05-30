import os.path
import re
from pyvi import ViTokenizer, ViPosTagger
import settings
import json

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
            if word not in self.stopwords:
                list1.insert(len(list1), word)
        return list1

class NLP2(object):
    def __init__(self, list1 = []):
        self.list1 = list1

    # def countWord(self):
    #     v1 = settings.v
    #     k1 = settings.k
    #     text = self.list1
    #     for j in range(len(text)):
    #         if text[j] in v1:
    #             k1[v1.index(text[j])] += 1
    #         else:
    #             v1.insert(len(v1), text[j])
    #             k1.insert(len(k1), 1)

    def builDictionary(self):
        list = self.list1
        i = 0
        l = settings.l
        f = settings.f
        l_leng = len(l)
        while i < len(list) - 1:
            flag = True
            for j in range(l_leng):
                for k in range (len(l[j])):
                    if list[i] in l[j][k]:
                        flag = False
                        if j in (0,1,7):  
                            str1 = ''.join(list[i+1])
                            k = 2
                        elif ((j == 6) and (i < len(list) - 2)):
                            if (list[i+1 ]== 'trung_học') and (i < len(list) - 3):
                                if list[i+2] == 'phổ': 
                                    str1 = list[i] + '_' + list[i+1] + '_' + list[i+2] + '_' + list[i+3] + '_' + list[i+4]
                                    k = 5
                                else:
                                    str1 = list[i] + '_' + list[i+1] + '_' + list[i+2] + '_' + list[i+3]
                                    k = 4
                            else:
                                str1 = list[i] + '_' + list[i+1] + '_' + list[i+2] 
                                k = 3
                        else:
                            str1 = list[i] + '_' + list[i+1]
                            k=2
                        if str1 not in f[j][0]:
                            f[j][0].insert(len(f[j][0]), str1)
                            f[j][1].insert(len(f[j][0]), 1)
                            # f[j][2].insert(len(f[j][0]), list[i])
                        else:
                            f[j][1][f[j][0].index(str1)] += 1
                        if list[i+1] in f[l_leng]:
                            index1 = f[l_leng][0].index(list[i+1])
                            v1 = f[l_leng][1][index1]
                            f[j][1][f[l_leng][0].index(list[i+1])] += v1
                            f[l_leng][0].remove(list[i+1])
                            f[l_leng][1].pop(index1)
                        break
                if flag == False:
                    break
            if flag == False:
                    i += k
            else:
                for k in range (l_leng):
                    if list[i] in f[k][0]:
                        f[k][1][f[k][0].index(list[i])] += 1
                        flag = False 
                        if list[i] in f[l_leng][0]:
                            index1 = f[l_leng][0].index(list[i])
                            v1 = f[l_leng][1][index1]
                            f[k][1][len(f[k][0])-1] += v1
                            f[l_leng][0].remove(list[i])
                            f[l_leng][1].pop(index1)
                        break
                if flag == True:
                    if list[i] not in f[l_leng][0]:
                        f[l_leng][0].insert(len(f[l_leng][0]), list[i])
                        f[l_leng][1].insert(len(f[l_leng][0]), 1)
                    else:
                        f[l_leng][1][f[l_leng][0].index(list[i])] += 1
                flag = True
                i += 1
                if i == len(list)-1:
                    for k in range (len(f)):
                        if list[i] in f[k][0]:
                            f[k][1][f[k][0].index(list[i])] += 1
                            flag = False
                            break
                    if flag == True:
                        f[l_leng][0].insert(len(f[l_leng][0]), list[i])
                        f[l_leng][1].insert(len(f[l_leng][0]), 1)
        return f

def writeListToTextFile(list, file):
    sum = 0
    for i in range(len(list[0])):
        if list[1][i] != 0:
            file.write(str(list[0][i]).replace("_"," ")+ ' ' + str(list[1][i]) +'\n')
            sum += list[1][i]
    file.write(str(sum))
            
def fileInFolder(folderPath, fileList):
    # r=root, d=directories, f = dictionary_files
    for r, d, f in os.walk(folderPath):
        for file in f:
            if '.txt' in file:
                fileList.append(os.path.join(r, file))

def hauXuLy(f, h):
    f.insert(len(f), 'abcxyzghf')
    h.insert(len(f), 0)
    j = 0
    k = 1
    while j < len(f):
        flag = False
        while k < len(f):
            flag = False
            if ((str(f[j]) in str(f[k])) & (h[k]>h[j]))or((str(f[k]) in str(f[j])) & (h[j]<h[k])):
                flag = True
                h[k] += h[j]
                f.remove(f[j])
                h.pop(j)
            if ((str(f[j]) in str(f[k])) & (h[k]<h[j]))or((str(f[k]) in str(f[j])) & (h[j]>h[k])):
                flag = True
                h[j] += h[k]
                f.remove(f[k])
                h.pop(k)
            if flag == True:
                continue
            else:
                k += 1
        if flag == True:
            continue  
        else: 
            j +=1
            k = j+1

# setting
l1 = settings.l
f1 = settings.f

# open files
f_ask = open(os.path.join("data","ask","ask.txt"), encoding="utf8")
f_ask3 = open(os.path.join("data","ask","ask3.txt"), encoding="utf8")
ask_files = [f_ask,f_ask3]

dictionary_folder = os.path.join("data","dictionary") 
dictionary_files = []
fileInFolder(dictionary_folder, dictionary_files)
for i in range (0, len(f1)):
    open(dictionary_files[i], 'w', encoding="utf8")

# main
for j in range (len(ask_files)):
    for line in ask_files[j]:
        text = NLP(text=line).get_words()
        f1 = list(NLP2(text).builDictionary())
  
for i in range (0, len(f1)):
    hauXuLy(f1[i][0], f1[i][1])
    writeListToTextFile(f1[i], open(dictionary_files[i], 'a',encoding="utf8"))