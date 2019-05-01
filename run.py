import os.path
import re
from pyvi import ViTokenizer, ViPosTagger
import settings

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

class NLP2(object):
    def __init__(self, list1 = [], list2 = [], list3 =[]):
        self.list1 = list1
        self.list2 = list2
        self.list3 = list3


    def builDictionary(self):
        list = self.list1
        l = self.list2
        f = self.list3
        i = 0
        l_leng = len(l)
        while i <= len(list) - 2:
            flag = True
            for j in range (l_leng):
                for k in range (len(l[j])):
                    if list[i] in l[j][k]:
                        flag = False
                        if j in (0,1,7):  # tên city, district, street thì ko thêm tiền tố từ
                            str1 = ''.join(list[i+1]) 
                        else:    
                            str1 = ''
                            str1 += list[i] + '_' + list[i+1]        
                        if str1 not in f[j]:
                            f[j].append(str1)
                        if list[i+1] in f[l_leng]:
                            f[l_leng].remove(list[i+1])
                        break
            if flag == False:
                i += 2
            else:
                for k in range (l_leng):
                    if list[i] in f[k]:
                        flag = False
                        break
                if flag == True:
                    if list[i] not in f[l_leng]:
                        f[l_leng].append(list[i])
                flag = True
                i += 1
                if i == len(list)-1:
                    for k in range (len(f)):
                        if list[i] in f[k]:
                            flag = False
                            break
                    if flag == True:
                        f[l_leng].append(list[i])
        return f
    


def writeListToTextFile(list, file):
    for item in list:
        file.write(str(item) + '\n')
            
f_ask = open(os.path.join("data","ask","ask.txt"),encoding="utf8")
f_ask3 = open(os.path.join("data","ask","ask3.txt"),encoding="utf8")
ask_file = [f_ask,f_ask3]
dictionary_folder = 'E:\\2\\data\\dictionary' 
dictionary_files = []
# r=root, d=directories, f = dictionary_files
for r, d, f in os.walk(dictionary_folder):
    for file in f:
        if '.txt' in file:
            dictionary_files.append(os.path.join(r, file))
for i in range (0, len(dictionary_files)):
    open(dictionary_files[i], 'w',encoding="utf8")

l = []
l.append([['thành_phố'], ['tỉnh']])
l.append([['quận'], ['thị_trấn'], ['huyện'], ['phường'], ['khối'], ['xóm'], ['xã'], ['thôn'], ['làng']])
l.append([['rạp_phim'], ['công_viên'], ['sở_thú'], ['rạp_xiếc'], ['quán'], ['bảo_tàng'], ['trung_tâm'], ['sân']])
l.append([['bến_xe'], ['khách_sạn'], ['nhà_nghỉ'], ['chung_cư'], ['lăng'], ['tòa'], ['tòa_nhà'], ['ga'], ['chợ'], ['cầu'], ['ngân_hàng'], ['bệnh_viện'], ['nghĩa_trang']])
l.append([['hồ'], ['sông'], ['núi'], ['đồi']])
l.append([['nhà_hàng'], ['quán_cà_phê'], ['tiệm'], ['quán'], ['siêu_thị']])
l.append([['trường'], ['thư_viện'], ['học_viện']])
l.append([['đường'], ['phố']])
l.append([['đền'], ['chùa'], ['nhà_thờ'], ['am'], ['miếu']])

f = []
for i in range (len(l)+1):
    f.append(list())

for i in range (len(ask_file)):
    for line in ask_file[i]:
        text = NLP(text=line).get_words()
        f = list(NLP2(text, l, f).builDictionary())

for i in range (0, len(l) + 1):
    writeListToTextFile(f[i], open(dictionary_files[i], 'a',encoding="utf8"))
