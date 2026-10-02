#4.1
from bai4.hoat_dong_4 import ket_qua

danh_sach_sv = [
    {"ma_sv": "SV01", "ten": "Nguyen Viet Anh", "tuoi": 21, "nganh": "CNTT", "diem_tb": 8.5},
    {"ma_sv": "SV02", "ten": "Le Thu Trang", "tuoi": 20, "nganh": "Kinh Te", "diem_tb": 7.0},
    {"ma_sv": "SV03", "ten": "Tran Van Nam", "tuoi": 22, "nganh": "CNTT", "diem_tb": 9.2},
    {"ma_sv": "SV04", "ten": "Pham Thi Mai", "tuoi": 20, "nganh": "Ngon Ngu Anh", "diem_tb": 6.0},
    {"ma_sv": "SV05", "ten": "Vu Van Hoang", "tuoi": 21, "nganh": "Kinh Te", "diem_tb": 4.5}
]

#4.2

def hien_thi_danh_sach_sv():
    print("\n" + "=" * 70)
    print(f"{'Ma SV': <10}{'Ho va Ten': <20}{'Tuoi': <10}{'Nganh': <15}{'Diem TB': <10}")
    print("-" * 70)
    if len(danh_sach_sv) == 0:
        print("Danh sach trong.")
    else:
        for sv in danh_sach_sv:
            print(f"{sv['ma_sv']: <10}{sv['ten']: <20}{sv['tuoi']: <10}{sv['nganh']: <15}{sv['diem_tb']: <10.1f}")
    print("=" * 70)

def xem_phan_loai_hoc_luc():
    gioi, kha, tb, yeu = [], [], [], []
    for sv in danh_sach_sv:
        diem = sv["diem_tb"]
        if diem >= 8.0:
            gioi.append(sv)
        elif diem >= 6.3:
            kha.append(sv)
        elif diem >= 5:
            tb.append(sv)
        else :
            yeu.append(sv)
    print("\n" + "=" * 50)
    print("       PHAN LOAI HOC LUC SINH VIEN")
    print("=" * 50)
    print("\n1. LOAI GIOI (Diem TB >= 8.0):")
    if len(gioi) == 0: print(" -> Khong co sinh vien nao.")
    else:
        for sv in gioi: print(f" - {sv['ma_sv']} | {sv['ten']} | Nganh: {sv['nganh']} | Diem: {sv['diem_tb']}")

    print("\n2. LOAI KHA (6.5 <= Diem TB < 8.0):")
    if len(kha) == 0: print(" -> Khong co sinh vien nao.")
    else:
        for sv in kha: print(f" - {sv['ma_sv']} | {sv['ten']} | Nganh: {sv['nganh']} | Diem: {sv['diem_tb']}")
    print("\n3. LOAI TRUNG BINH (5.0 <= Diem TB < 6.5):")
    if len(tb) == 0: print(" -> Khong co sinh vien nao.")
    else:
           for sv in tb: print(f" - {sv['ma_sv']} | {sv['ten']} | Nganh: {sv['nganh']} | Diem: {sv['diem_tb']}")
    print("\n4. LOAI YEU (Diem TB < 5.0):")
    if len(yeu) == 0: print(" -> Khong co sinh vien nao.")
    else:
         for sv in yeu: print(f" - {sv['ma_sv']} | {sv['ten']} | Nganh: {sv['nganh']} | Diem: {sv['diem_tb']}")

def tim_kiem_sinh_vien(tu_khoa):
    ket_qua = []
    for sv in danh_sach_sv:
        if tu_khoa.lower() in sv["ma_sv"].lower() or tu_khoa.lower() in sv["ten"].lower():
            ket_qua.append(sv)
        if len(ket_qua) == 0:
            print(f"\n khong tim thay sinh vien 'tu_khoa' : ")
        else:
            print(f"\nKET QUA TIM KIEM  '{tu_khoa}'")
            for sv in ket_qua:
                print(f"Ma SV: {sv['ma_sv']} | Ten: {sv['ten']} | Nganh: {sv['nganh']} | Diem: {sv['diem_tb']}")
def tim_sv_theo_ma(ma_sv):
    for sv in danh_sach_sv:
        if sv["ma_sv"] == ma_sv:
            return sv
    return None

#4.3 hàm thêm sửa xóa
def them_sinh_vien(ma_sv, ten, tuoi, nganh, diem_tb):
    if tim_sv_theo_ma(ma_sv) is not None:
        print(f"-> Ma SV {ma_sv} da ton tai, khong the them.")
        return
    # Thêm dict mới vào list
    danh_sach_sv.append({
        "ma_sv": ma_sv, "ten": ten, "tuoi": tuoi,
        "nganh": nganh, "diem_tb": diem_tb
    })
    print(f"-> Da them sinh vien {ten} thanh cong.")

def cap_nhat_diem(ma_sv, diem_moi):
    sv = tim_sv_theo_ma(ma_sv)
    if sv is None:
        print(f"-> Khong tim thay sinh vien {ma_sv}.")
        return
    # Cập nhật giá trị trong dict
    sv["diem_tb"] = diem_moi
    print(f"-> Cap nhat diem cho sinh vien {sv['ten']} thanh cong.")

def xoa_sinh_vien(ma_sv):
    sv = tim_sv_theo_ma(ma_sv)
    if sv is None:
        print(f"-> Khong tim thay sinh vien {ma_sv}.")
        return
    danh_sach_sv.remove(sv)
    print(f"-> Da xoa sinh vien {sv['ten']} khoi he thong.")

#4.4 thống kê và nhập dữ liệu
def thong_ke_theo_nganh():
    if len(danh_sach_sv) == 0:
        print("-> Danh sach trong.")
        return
    thong_ke = {}
    for sv in danh_sach_sv:
        nganh = sv["nganh"]
        thong_ke[nganh] = thong_ke.get(nganh, 0) + 1

    print("\nTHONG KE SINH VIEN THEO NGANH:")
    for nganh, so_luong in thong_ke.items():
        print(f"- Nganh {nganh}: {so_luong} sinh vien")


def nhap_so_an_toan(loi_nhac, kieu_du_lieu):
    # Dùng while và try-except để ép người dùng nhập đúng định dạng
    while True:
        try:
            if kieu_du_lieu == "int":
                so = int(input(loi_nhac))
                if so > 0: return so
                print("-> Vui long nhap so lon hon 0.")
            elif kieu_du_lieu == "float":
                diem = float(input(loi_nhac))
                if 0 <= diem <= 10: return diem
                print("-> điểm trong khoảng từ 0-10.")
        except ValueError:
            print("-> Du lieu khong hop le, vui long nhap lai .")

#menu chính  và vòng lặp
def hien_thi_menu():
    print("\n===== QUAN LY SINH VIEN =====")
    print("1. Hien thi tat ca sinh vien")
    print("2. Xem phan loai hoc luc (Gioi, Kha, TB, Yeu)")
    print("3. Them sinh vien moi")
    print("4. Cap nhat diem")
    print("5. Xoa sinh vien")
    print("6. Thong ke theo nganh")
    print("7. Tim kiem sinh vien (Theo Ten/Ma SV)")
    print("0. Thoat chuong trinh")


def chay_chuong_trinh():
    while True:
        hien_thi_menu()
        lua_chon = input("Nhap lua chon cua ban: ").strip()
        if lua_chon == "1":
            hien_thi_danh_sach_sv()
        elif lua_chon == "2":
            xem_phan_loai_hoc_luc()
        elif lua_chon == "3":
            ma_sv = input("\nNhap ma SV moi: ").strip().upper()
            ten = input("Nhap ten sinh vien: ").strip().title()
            tuoi = nhap_so_an_toan("Nhap tuoi: ", "int")
            nganh = input("Nhap nganh hoc: ").strip().upper()
            diem_tb = nhap_so_an_toan("Nhap diem TB (0-10): ", "float")
            them_sinh_vien(ma_sv, ten, tuoi, nganh, diem_tb)
        elif lua_chon == "4":
            ma_sv = input("\nNhap ma SV can cap nhat: ").strip().upper()
            diem_moi = nhap_so_an_toan("Nhap diem TB moi (0-10): ", "float")
            cap_nhat_diem(ma_sv, diem_moi)
        elif lua_chon == "5":
            ma_sv = input("\nNhap ma SV can xoa: ").strip().upper()
            xoa_sinh_vien(ma_sv)
        elif lua_chon == "6":
            thong_ke_theo_nganh()
        elif lua_chon == "7":
            tu_khoa = input("\nNhap Ma SV hoac Ten sinh vien can tim: ").strip()
            tim_kiem_sinh_vien(tu_khoa)
        elif lua_chon == "0":
            print("Cam on da su dung chuong trinh. Tam biet!")
            break
        else:
            print("-> Lua chon khong hop le, vui long chon lai.")
if __name__ == "__main__":
    chay_chuong_trinh()




