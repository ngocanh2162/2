import os.path
import re
from NLP import NLP
from NLP2 import NLP2

f_ask = open(os.path.join("data","sentences","ask","ask.txt"),encoding="utf8")
f_ask3 = open(os.path.join("data","sentences","ask","ask3.txt"),encoding="utf8")
loca3 = os.path.join("data","location","location3.txt")
f_loca3 = open(loca3, 'w',encoding="utf8")  

dictionary_folder = 'E:\\project2\\data\\dictionary\\'
dictionary_files = []
# r=root, d=directories, f = dictionary_files
for r, d, f in os.walk(dictionary_folder):
    for file in f:
        if '.txt' in file:
            dictionary_files.append(os.path.join(r, file))
for i in range (0, len(dictionary_files)):
    open(dictionary_files[i], 'w',encoding="utf8")

l = []
l.append(['thành_phố', 'tỉnh'])
l.append(['quận', 'thị_trấn', 'huyện', 'phường', 'khối', 'xóm', 'xã', 'thôn', 'làng'])
l.append(['rạp_phim', 'công_viên', 'sở_thú', 'rạp_xiếc', 'quán', 'bảo_tàng','trung_tâm', 'sân'])
l.append(['bến_xe', 'khách_sạn', 'chung_cư','lăng', 'tòa', 'tòa_nhà', 'ga', 'chợ', 'cầu', 'ngân_hàng', 'bệnh_viện', 'nghĩa_trang'])
l.append(['hồ', 'sông','núi', 'đồi'])
l.append(['nhà_hàng', 'quán_cà_phê', 'tiệm', 'quán', 'siêu_thị'])
l.append(['trường','thư_viện', 'học_viện'])
l.append(['đường', 'phố'])
l.append(['đền', 'chùa', 'nhà_thờ', 'am', 'miếu'])

f = []
for i in range (len(l)+1):
    f.append(list())

for line in f_ask3:
    text = NLP(text=line).get_words()
    f = list(NLP2(text, l, f).builDictionary())
for line in f_ask:
    text = NLP(text=line).get_words()
    f = list(NLP2(text, l, f).builDictionary())

def writeListToTextFile(list, file):
    for item in list:
        file.write(str(item) + '\n')

for i in range (0, len(l) + 1):
    writeListToTextFile(f[i], open(dictionary_files[i], 'a',encoding="utf8"))
