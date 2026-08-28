#Hoạt động 1

#baitap1.1
ho_ten = input("nhap ho ten : ")
nam_sinh = int(input("nhap nam sinh : ")) # Thêm int() để chuyển sang số nguyên
diem_tb = float(input("nhap diem tb : "))

#baitap1.2
print("python", "la", "ngon", "ngu", "lap trinh", sep="-")
print("dong1", end=" | ")
print("dong 2")

#baitap1.3
# f-string (Đã thêm dấu chấm . vào .2f)
print(f"ho ten : {ho_ten} - nam sinh : {nam_sinh} - diem tb : {diem_tb} - dtb :{diem_tb:.2f}")

#str.format() (Đã thêm {} cho diem tb)
print("ho ten :{} - nam_sinh:{} - diem tb: {}".format(ho_ten, nam_sinh, diem_tb))

#toantu % (Đã thêm dấu chấm . vào .2f)
print("ho ten : %s nam sinh : %d diem tb :%.2f" % (ho_ten, nam_sinh, diem_tb))


#hoatdong2

#baitap2.1
#chu thich mot dong : khai bao thogn tin sinh vien
"""
Chu thich/docstring nhieu dong :
Chuong trinh quan ly diem sinh vien  - buoi 2
"""
ho_ten = "nguyen viet anh " #bien luu ho ten

#baitap2.2

s1 = 'xin chao '
s2 = "ban co khoe khong ? "
s3 = '''
mot chuoi 
nhieu dong
'''
s4 = "duong dan : C:\\Python\\data"
s5 = r"Duong dan raw : C:\Python\data"
s6 = "Toi ten la \"nam\" , con ban ten la gi ?"
print(s1); print(s2);print(s3);print(s4);print(s5);print(s6)
