import sys
from PyQt5.QtWidgets import QApplication
from UI_MainInterface import MainInterface

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainInterface()
    sys.exit(app.exec_())
