quan_ly_diem = {
    "Nguyen Việt Anh": [7.0, 7.5, 8.0],
    "Vương Quốc Chính": [10, 10, 10],
    "Vương Quốc Anh": [6, 6.5, 7.0],
}

# Them sinh vien moi
quan_ly_diem["Pham Thi D"] = [7.0, 8.0, 7.5]

# Sua diem mon dau tien cua mot sinh vien
quan_ly_diem["Vương Quốc Chính"][0] = 7.0

diem_trung_binh = {}
for ho_ten, danh_sach_diem in quan_ly_diem.items():
    diem_trung_binh[ho_ten] = round(sum(danh_sach_diem) / len(danh_sach_diem), 2)

print("BANG DIEM TRUNG BINH:")
for ho_ten, dtb in diem_trung_binh.items():
    dat_loai_gioi = dtb >= 8.0
    # Đã tăng khoảng trống từ 15 lên 20 để tên dài không bị lệch cột
    print(f"{ho_ten:<20} - DTB: {dtb:<5} - Dat loai Gioi? {dat_loai_gioi}")