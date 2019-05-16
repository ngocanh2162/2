import os.path
import re
import settings

# f_ask = open(os.path.join("data","ask","ask.txt"), encoding="utf8")
# f_ask3 = open(os.path.join("data","ask","ask3.txt"), encoding="utf8")
# ask_files = [f_ask,f_ask3]

# fo = open(os.path.join("data","dictionary","w1.txt"), 'w', encoding="utf8")
# v1= []
# k1 = []

# for i in range (len(ask_files)):
#     for line in ask_files[i]:
#         text = NLP(text=line).get_words()
#         for j in range(len(text)):
#             if text[j] in v1:
#                 k1[v1.index(text[j])] += 1
#             else:
#                 v1.insert(len(v1), text[j])
#                 k1.insert(len(k1), 1)
# lenv1 = len(v1)
# for i in range(lenv1):
#     fo.write(str(v1[i]) + ' ' + str(k1[i]) + '\n')

f =[]
f.append(list())
f.append(list())
f[0].insert(0, 'hanoi')
f[0].insert(len(f[0]), 'vinh')
f[0].insert(len(f[0]), 'saigon')
f[1].insert(len(f[1]),1)
f[1].insert(len(f[1]),2)
f[1].insert(len(f[1]),3)
# str = 'cantho'
# if str not in f[0][0]:
#     f[0][0].insert(len(f[0][0]), str)
#     f[0][1].insert(len(f[0][1]), 5)
#     f[0][1][len(f[0][1]) -1] -= 1
print(f)
# str1 = 'saigon'
# if str1 in f[0][0]:
#     index1 = f[0][0].index(str1)
#     v1 = f[0][1][index1]
#     f[0][0].remove(str1)
#     f[0][1].pop(index1)
# print(f[0])