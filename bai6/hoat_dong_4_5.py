#Hoạt động 4:
so_luot_truy_cap = 0 #   bien global
def tang_luot_truy_cap():
    global so_luot_truy_cap
    so_luot_truy_cap += 2
def vi_du_bien_local():
    so_luot_truy_cap = 100 #khac voi bien global o tren
    print("ben trong ham bien local = " , so_luot_truy_cap)
tang_luot_truy_cap()
tang_luot_truy_cap()
tang_luot_truy_cap()
print("so_luot_truy_cap (global)" , so_luot_truy_cap)
vi_du_bien_local()
print("sau khi goi ham , bien global van la : " , so_luot_truy_cap)

#hoat dong 5 :
#Bài tập 5.1
danh_sach_so = [1,2,3,4,5]
binh_phuong = list(map(lambda x: x**2, danh_sach_so))
print(binh_phuong)

#bài tập 5.2
so_chan = list(filter(lambda x: x%2==0, danh_sach_so))
print(so_chan)

#bai tap 5.3
danh_sach_sv = [
    {"ten" :"viet anh ", "diem" : 7 },
    {"ten" :"chinh ", "diem" : 9 },
    {"ten" :"hoang ", "diem" : 8 },
    ]
sap_xep_theo_diem = sorted(danh_sach_sv, key=lambda sv: sv["diem"])
sap_xep_giam_dan = sorted(danh_sach_sv, key=lambda sv: sv["diem"] , reverse= True)
for sv in sap_xep_theo_diem:
    print(sv["ten"] , "-" , sv["diem"])
print("-----điểm giảm dần-----")
for sv in sap_xep_giam_dan:
    print(sv["ten"] , "-" , sv["diem"])