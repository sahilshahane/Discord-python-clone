import sys
import random
from PySide2 import QtCore, QtWidgets, QtGui

from MainWindow import MainApplication as MyApplication


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyApplication()
    widget.resize(414, 736)
    widget.show()

    sys.exit(app.exec_())