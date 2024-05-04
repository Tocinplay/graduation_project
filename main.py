# This Python file uses the following encoding: utf-8
import sys
import os
from faceRecoui import Ui_faceReco

from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader


class faceReco(QMainWindow, Ui_faceReco):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def load_ui(self):
        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), "form.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()

if __name__ == "__main__":
    app = QApplication([])
    widget = faceReco()
    widget.show()
    sys.exit(app.exec_())
