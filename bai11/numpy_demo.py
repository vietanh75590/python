import numpy as np

diem_list = [8.5, 7.0, 9.2, 5.5, 6.5]
diem_array = np.array(diem_list)

print(type(diem_array),type(diem_array))

diem_cong_them = diem_array + 0.5
print(diem_cong_them)
diem_cong_them_list = [diem + 0.5 for diem in diem_list]
print(diem_cong_them_list)

print("trung binh:",np.mean(diem_array))
print("lon nhat:", np.max(diem_array))
print("nho nhat:", np.min(diem_array))
print("do lech chuan:", round(np.max(diem_array) - np.min(diem_array), 2))

ma_tran = np.array([[1, 2, 3], [4, 5, 6]])
print("ma_tran:\n", ma_tran)
print("Kich thuoc (shape):", ma_tran.shape)
print("Ma tran nhan 2:\n", ma_tran * 2)
