# ==========================================
# HOẠT ĐỘNG 3: Áp dụng PEP8
# ==========================================
print("--- KẾT QUẢ HOẠT ĐỘNG 3 ---")
ten = "Nguyen Van A" 
diem_toan = 8.5 
diem_van = 7.0 
so_luong_mon_hoc = 2 
MUC_LUONG_TOI_THIEU = 5000000 

print(f"Học sinh: {ten}, Toán: {diem_toan}, Văn: {diem_van}")
print(f"Số môn: {so_luong_mon_hoc}, Lương tối thiểu: {MUC_LUONG_TOI_THIEU}\n")

# ==========================================
# HOẠT ĐỘNG 5: Toán tử
# ==========================================
print("--- KẾT QUẢ HOẠT ĐỘNG 5 ---")
a = 17
b = 5
print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"a * b = {a * b}")
print(f"a / b = {a / b}")
print(f"a // b = {a // b}")
print(f"a % b = {a % b}")
print(f"a ** b = {a ** b}\n")

diem = 6.5 
tuoi = 20
print("Kha (6.5 <= diem < 8.0)?", 6.5 <= diem < 8.0)
print("Chua du 18 hoac tren 60?", tuoi < 18 or tuoi > 60)
print("Phu dinh lai:", not (tuoi < 18 or tuoi > 60))

# Toán tử gán
x = 10 
x += 5; print("x += 5:", x)
x -= 2; print("x -= 2:", x)
x *= 2; print("x *= 2:", x)
x /= 2; print("x /= 2:", x)
x //= 3; print("x //= 3:", x)
x **= 2; print("x **= 2:", x)

# Toán tử đặc biệt
danh_sach = [1, 2, 3, "python"] 
print("3 co trong danh sach?", 3 in danh_sach)

# ==========================================
# HOẠT ĐỘNG 6: Biến & Dynamic typing
# ==========================================
print("\n--- KẾT QUẢ HOẠT ĐỘNG 6 ---")
ho_ten = "Nguyen Van A" 
diem_toan = 8.0 
diem_ly = 7.5 
diem_hoa = 9.0 

dtb = (diem_toan + diem_ly + diem_hoa) / 3 
la_gioi = dtb >= 8.0 
la_kha = dtb >= 6.5 and dtb < 8.0 
la_trung_binh = dtb >= 5.0 and dtb < 6.5 
la_yeu = dtb < 5.0 

print(ho_ten, "- DTB:", round(dtb, 2)) 
print("Dat loai Gioi?", la_gioi) 
print("Dat loai Kha?", la_kha) 
print("Dat loai Trung binh?", la_trung_binh) 
print("Dat loai Yeu?", la_yeu) 
print("Kieu du lieu cua la_gioi:", type(la_gioi))