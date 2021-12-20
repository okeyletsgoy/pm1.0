import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from ui import Ui_MainWindow

app = QtWidgets.QApplication(sys.argv)

MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

def chisl():
    dbl = ui.lineEdit.text()
    n = int(dbl, 2)

    Oct = oct(n)
    Oct = Oct[2:]

    Hex = hex(n)
    Hex = Hex[2:]
    Hex = Hex.upper()

    ui.label_6.setText(str(n))
    ui.label_7.setText(str(Oct))
    ui.label_8.setText(str(Hex)) 

ui.pushButton.clicked.connect( chisl )

sys.exit(app.exec_())
