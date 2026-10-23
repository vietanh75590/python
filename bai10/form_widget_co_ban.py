# hoat dong 2
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QLineEdit, QComboBox, QVBoxLayout)
class formthongtin(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("vi du widget co ban")
        self.resize(400, 300)
        self.o_nhap_ten = QLineEdit()
        self.o_nhap_ten.setPlaceholderText("nhap ho ten :")
        self.chon_thanh_pho = QComboBox()
        self.chon_thanh_pho.addItems(["Ha Noi", "Da Nang", "TP.HCM", "Hue"])
        nut_xac_nhan = QPushButton("xac nhan")
        self.nhan_ket_qua = QLabel("")
        layout = QVBoxLayout()
        layout.addWidget(QLabel("nhap ho ten :"))
        layout.addWidget(self.o_nhap_ten)
        layout.addWidget(QLabel("thanh pho :"))
        layout.addWidget(self.chon_thanh_pho)
        layout.addWidget(nut_xac_nhan)
        layout.addWidget(self.nhan_ket_qua)
        self.setLayout(layout)

        nut_xac_nhan.clicked.connect(self.xy_ly_xac_nhan)
    def xy_ly_xac_nhan(self):
        ten = self.o_nhap_ten.text()
        thanh_pho = self.chon_thanh_pho.currentText()
        self.nhan_ket_qua.setText(f"Xin chao {ten}, den tu {thanh_pho}!")
app = QApplication(sys.argv)
cua_so = formthongtin()
cua_so.show()
sys.exit(app.exec_())