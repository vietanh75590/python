#baitap 1.2

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QGridLayout
class vidugridlayout(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vi du QGridLayout")
        self.resize(500, 400)
        layout = QGridLayout()
        layout.addWidget(QLabel("Ho ten:"), 0, 0)
        layout.addWidget(QLabel("Tuoi:"), 1, 0)
        layout.addWidget(QPushButton("Dong y"), 2,0)
        layout.addWidget(QPushButton("huy "), 2,1)
        self.setLayout(layout)
app = QApplication(sys.argv)
cua_so = vidugridlayout()
cua_so.show()
sys.exit(app.exec_())