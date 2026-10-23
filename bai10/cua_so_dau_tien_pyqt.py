# baitap 1.1
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QMainWindow, QVBoxLayout, QLabel


class CuaSoDauTien(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CuaSoDauTien")
        self.resize(700, 500)

        layout = QVBoxLayout()
        nhan = QLabel("xin chao pyqt")

        layout.addWidget(nhan)
        self.setLayout(layout)

app = QApplication(sys.argv)
cua_so = CuaSoDauTien()
cua_so.show()
sys.exit(app.exec_())
