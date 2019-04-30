import os
import settings

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
                if list[i] in l[j]:
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