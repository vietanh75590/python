#baitap1.1
diem_so = [8.5, 7.0, 9.2, 6.5, 5.5 ]
print(diem_so[0])
print(diem_so[-1])
print(diem_so[1:4])
print(diem_so[::2])
print(diem_so[-1])




#baitap1.2
ten_sv = ["an" , "binh" , "chi"]
ten_sv.append("dung")
ten_sv.insert(1,"em")
print(ten_sv)
ten_sv.remove("chi")
pop_ra = ten_sv.pop()
print(ten_sv , "-da xoa : ", pop_ra)
ten_sv.sort()
print(ten_sv)
ten_sv.reverse()
print(ten_sv)
ten_sv.extend(["giang","hoa"])
print(ten_sv)




#baitap2.1
diem_so = [8.5, 7.0, 9.2, 6.5, 5.5 ]
tong = 0
for diem in diem_so:
    print(diem)
    tong = tong + diem
    print("tong diem la :" , tong)
    print("diem trung binh la : " , round(tong/len(diem_so), 2))



#baitap2.2
ma_tran = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
#in ra theo tung hang
for hang in ma_tran:
    print(hang)
    #in ra mang phan tu , duyet theo hang roi theo cot
    for hang in ma_tran:
        for phan_tu in hang:
            print(phan_tu, end="")
        print()
print("\n----- Tinh tong cac phan tu -----")
tong = 0
for hang in ma_tran:
    for phan_tu in hang:
        tong += phan_tu
        print("tong tat ca cac phan tu :" , tong)



#baitap3.1
day_so = list(range(1, 21))
so_chan = [x for x in day_so if x % 2 == 0]
so_le = [x for x in day_so if x % 2 != 0]
print("So chan:", so_chan)
print("So le:", so_le)



#baitap3.2
diem_so = [8.5, 7.0, 9.2, 6.5, 5.5 ]
diem_cong = [round(diem+0.5, 2) for diem in diem_so]
print(diem_cong)