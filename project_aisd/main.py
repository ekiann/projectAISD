# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication

#import res_rc
from authorization import Authorization


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Authorization()
    widget.show()
    sys.exit(app.exec())
