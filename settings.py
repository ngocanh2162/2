import os

# SPECIAL_CHARACTER = '%@$.,=+-!;/()*"&^:#|\n\t\''
SPECIAL_CHARACTER = '0123456789%@$.,=+-!;/()*"&^:#|\n\t\''
dict_f = os.path.join("data","dictionary")
l = []
l.append([['thành_phố'], ['tỉnh']])
l.append([['quận'], ['thị_trấn'], ['huyện'], ['phường'], ['khối'], ['xóm'], ['xã'], ['thôn'], ['làng']])
l.append([['rạp_phim'], ['công_viên'], ['sở_thú'], ['rạp_xiếc'], ['quán'], ['bảo_tàng'], ['trung_tâm'], ['sân']])
l.append([['công_ty'], ['nhà_máy'], ['ga'], ['bến_xe'], ['khu_đô_thị'], ['khách_sạn'], ['nhà_nghỉ'], ['chung_cư'], ['lăng'], ['tòa'], ['tòa_nhà'], ['chợ'], ['cầu'], ['ngân_hàng'], ['bệnh_viện'], ['nghĩa_trang']])
l.append([['hồ'], ['sông'], ['núi'], ['đồi'], ['đèo'], ['rừng'], ['suối'], ['biển'], ['vịnh']])
l.append([['nhà_hàng'], ['quán_cà_phê'], ['tiệm'], ['quán'], ['siêu_thị'], ['cửa_hàng']])
l.append([['trường'], ['thư_viện'], ['học_viện']])
l.append([['đường'], ['phố']])
l.append([['đền'], ['chùa'], ['nhà_thờ'], ['am'], ['miếu']])

f = []
for i in range (len(l)+1):
    f.append(list())
for i in range (len(f)):
    f[i].append(list())
    f[i].append(list())
    # f[i].append(list())

v = []
k = []
# , ['trung_học'], ['đại_học'],['tiểu_học']
# 'chùa', 'cầu', 'quán'
d = ['tỉnh', 'quận', 'huyện', 'phường', 'khối', 'xóm', 'xã', 'thôn', 'làng','sân','ga', 'ngõ', 
'lăng', 'tòa',  'sông', 'núi', 'đồi', 'đèo', 'rừng', 'suối', 'biển', 'vịnh', 'miếu', 'tiệm', 'đền',
'nơi', 'chỗ', 'tới', 'đi']

