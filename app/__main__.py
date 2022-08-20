import sys
import random
from PySide2 import QtCore, QtWidgets, QtGui

from app.MainWindow import MainApplication as MyApplication
from app.screen2 import screen2

if __name__ == "__main__":
    screen2()
    app = QtWidgets.QApplication([])

    widget = MyApplication()
    widget.resize(414, 736)
    widget.show()

    sys.exit(app.exec_())