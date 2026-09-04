#baitap5
import math
diem_a = (2, 3)
diem_b = (7, 8)
xa, ya = diem_a
xb, yb = diem_b
khoang_cach = math.sqrt((xb - xa) ** 2 + (yb - ya) ** 2)
print(f"Khoang cach giua {diem_a} va {diem_b} la: {round(khoang_cach, 2)}")
cac_diem = [ (0,0),(3,4),(6,8)]
goc_toa_do = (0, 0)
x0, y0 = goc_toa_do
for diem in cac_diem:
    x, y = diem
    kc_toi_goc = math.sqrt((x - x0) ** 2 + (y - y0) ** 2)
print(f"Khoảng cách từ điểm {diem} đến gốc tọa độ (0, 0) là: {kc_toi_goc}")
