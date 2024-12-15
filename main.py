

from PySide6 import QtCore, QtWidgets, QtGui
import sys
from gui import MyWidget




if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    app.setApplicationName("BD Realization")
    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
