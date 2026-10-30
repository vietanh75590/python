
def tinh_toan(a, phep_tinh, b):
    if phep_tinh == "+":
        return a + b
    elif phep_tinh == "-":
        return a - b
    elif phep_tinh == "*":
        return a * b
    elif phep_tinh == "/":
        if b == 0:
            return "khong the chia cho 0"
        else:
            return a / b
    else:
        return "phep tinh khong hop le"
def main():
    print("-----may tinh bo tui-----")
    while True:
        bieu_thuc = input(
            "nhap bieu thuc, hoac 'thoat' de dung: "
        ).strip()
        if bieu_thuc.lower() == "thoat":
            print("bye")
            break
        try:
            a_str, phep_tinh, b_str = bieu_thuc.split()
            ket_qua = tinh_toan(
                float(a_str),
                phep_tinh,
                float(b_str)
            )
            print("ket qua:", ket_qua)
        except ValueError:
            print("dinh dang khong hop le")
if __name__ == "__main__":
    main()
