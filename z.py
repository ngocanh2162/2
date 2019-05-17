f = ['đống','đồng_nhân' ,'dương_văn_bé','phóng','giải_phóng' ,'hàn_thuyên' ,'hàng_chuối' ,'hàng','trường_trinh' ,'đại_cồ','trần_đại_nghĩa','tạ_quang_bửu']
h = [28,8,29,1,52,29,1,3,49,2,33,2]
f.insert(len(f), 'abcxyzghf')
h.insert(len(f), 0)
j = 0
k = 1
while j < len(f):
    flag = False
    while k < len(f):
        print(f[j]+ ' ' + f[k])
        flag = False
        if ((str(f[j]) in str(f[k])) & (h[k]>h[j]))or((str(f[k]) in str(f[j])) & (h[j]<h[k])):
                flag = True
                print("true1" + ' '+str(j)+' '+str(k))
                h[k] += h[j]
                f.remove(f[j])
                h.pop(j)
        if ((str(f[j]) in str(f[k])) & (h[k]<h[j]))or((str(f[k]) in str(f[j])) & (h[j]>h[k])):
                flag = True
                print("true2" + ' '+str(j)+' '+str(k))
                h[j] += h[k]
                f.remove(f[k])
                h.pop(k)
        if flag == True:
            continue
        else:
            k += 1
        print(str(j)+' '+str(k)+' '+str(flag))
    if flag == True:
        continue  
    else: 
        j +=1
        k =j+1
    print(str(j)+' '+str(k)+' '+str(flag))
    
print(f)
print(h)
# str1= 'hà_nộ'
# str2 = 'hà_nội'
# if str1 in str2:
#     print("true")
