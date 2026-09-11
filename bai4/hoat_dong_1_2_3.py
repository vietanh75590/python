#hoat dong 1
#baitap1.1
sinh_vien  = {
    "ho_ten" :  "Nguyen Viet Anh",
    "nam_sinh" :  "2006",
    "diem_tb" : "8"
}
print(sinh_vien["ho_ten"])
print(sinh_vien.get("diem_tb"))
print(sinh_vien.get("lop" , "chua co"))


#baitap1.2
sinh_vien["lop"] = "cntt01" #them
sinh_vien["diem_tb"] = 9.0  #sua gia tri khoa
print(sinh_vien)
diem_cu = sinh_vien["diem_tb"]
print (sinh_vien , "diem da xoa " , diem_cu)
sinh_vien.update({"nam_sinh" : 2006 ,"email" :"vietanh75590@gmail.com" })
print(sinh_vien)

#Hoạt động 2
diem_mon_hoc = {"Toan " : 7.0 , "ly" : 7.0 , "Hoa" :7.0 , "Van" :7.0 }
for mon in diem_mon_hoc.keys():
    print(mon)
for diem in diem_mon_hoc.values():
    print(diem)
for mon , diem in diem_mon_hoc.items():
    print(mon , diem)
tong_diem = 0
for diem in diem_mon_hoc.values():
    tong_diem = diem + tong_diem
print ("diem trung binh :" , round (tong_diem / len(diem_mon_hoc),2))

#Hoạt động 3
mon_hoc_ky1 = {"toan","ly","hoa","van"}
mon_hoc_ky2 = {"toan","anh","tin","van"}
print(mon_hoc_ky1 & mon_hoc_ky2)
print(mon_hoc_ky1|mon_hoc_ky2)
print(mon_hoc_ky1 - mon_hoc_ky2)
