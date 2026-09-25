#Hoạt động 1 :
#Bài tập 1.1

def uscln(a,b):
    while b != 0:
        a,b = b,a%b
    return a
def bscnn(a,b):
    return a * b  // uscln(a, b)
def kiem_tra_nguyen_to(n):
    if n < 2 :
        return False
    for i in range(2,n):
        if n % i == 0 :
            return False
        return True
def kiem_tra_so_hoan_thien(n):
    tong_uoc = 0
    for i in range(1,n):
        if n % i == 0 :
            tong_uoc = i
        return tong_uoc == n
print(uscln(24,36))
print(bscnn(4,6))
print(kiem_tra_nguyen_to(29))
print(kiem_tra_so_hoan_thien(28)) #28 = 1 + 2 + 4 + 7 + 14

#Bài tập 1.2
def in_loi_chao(ten):
    print(f"xin chao,{ten}!")
    return # hàm trả giá trị về none
def chia_lay_thuong_du(a,b):
    return a // b , a % b #tra gia tri qua tuple
in_loi_chao("vietanh")
thuong,du = chia_lay_thuong_du(17,5)
print(f"thuong:{thuong}, du:{du}")


#Hoạt động 2:
def gioi_thieu(ten, tuoi=18, lop="Chua ro"):
    print(f"Ten: {ten} - Tuoi: {tuoi} - Lop: {lop}")
gioi_thieu("vietanh")
gioi_thieu("emchinh",20)
gioi_thieu("hoang",lop = "cntt")
gioi_thieu("dung",tuoi=17,lop = "cntt01")

#Hoạt động 3:
#baitap3.1
def tinh_tong(*args):
    tong = 0
    for so in args:
        tong += so
    return tong
print(tinh_tong(1, 2, 3))
print(tinh_tong(12, 24, 36, 48))
print(tinh_tong()) # =>tra kq ve 0

#baitap3.2
def in_thong_tin(ho_ten , tuoi  , **kwargs):
    print(f"hoten: {ho_ten} - Tuoi: {tuoi}")
    for khoa , gia_tri in kwargs.items() :
        print(f"{khoa}: {gia_tri}")
in_thong_tin("nguyen viet anh ", 20 , lop = "cnttc1" , que_quan = "nam dinh")
in_thong_tin("nguyen thi chinh " , 21 , gmail = "vietanh75590@gmail.com")