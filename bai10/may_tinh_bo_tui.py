import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QLineEdit, QPushButton


class MayTinhBoTui(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Máy tính bỏ túi - PyQt5")
        self.resize(320, 450)
        layout_chinh = QVBoxLayout()
        self.man_hinh = QLineEdit()
        self.man_hinh.setReadOnly(True)  # Chỉ hiển thị, không cho phép gõ phím trực tiếp
        self.man_hinh.setStyleSheet("font-size: 30px; padding: 10px; text-align: right;")
        layout_chinh.addWidget(self.man_hinh)
        layout_ban_phim = QGridLayout()
        danh_sach_phim = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        hang = 0
        cot = 0
        for text in danh_sach_phim:
            nut = QPushButton(text)
            nut.setFixedSize(70, 70)
            nut.setStyleSheet("font-size: 20px; font-weight: bold;")
            nut.clicked.connect(lambda chked, t=text: self.xu_ly_bam_nut(t))

            layout_ban_phim.addWidget(nut, hang, cot)
            cot += 1
            if cot > 3:
                cot = 0
                hang += 1

        layout_chinh.addLayout(layout_ban_phim)
        self.setLayout(layout_chinh)
    def xu_ly_bam_nut(self, gia_tri):
        if gia_tri == 'C':
            self.man_hinh.clear()
        elif gia_tri == '=':
            try:
                bieu_thuc = self.man_hinh.text()

                if "=" in bieu_thuc:
                    return
                ket_qua = str(eval(bieu_thuc))
                self.man_hinh.setText(f"{bieu_thuc}={ket_qua}")
            except Exception:
                self.man_hinh.setText("Lỗi")
        else:
            noi_dung_hien_tai = self.man_hinh.text()
            if noi_dung_hien_tai == "Lỗi" or "=" in noi_dung_hien_tai:
                noi_dung_hien_tai = ""
                self.man_hinh.clear()
            self.man_hinh.setText(noi_dung_hien_tai + gia_tri)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    cua_so = MayTinhBoTui()
    cua_so.show()
    sys.exit(app.exec_())