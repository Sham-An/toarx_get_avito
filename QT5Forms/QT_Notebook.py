import sys
from PyQt5.QtWidgets import *

class UiApp(QMainWindow):

    def __init__(self):
        super().__init__()

        self.title = 'QMainWindow'
        self.setWindowTitle(self.title)
        self.setFixedSize(200, 270)
        self.table_widget = TabsWidget()
        self.setCentralWidget(self.table_widget)


class TabsWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)

        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab_user = QWidget()
        self.tab_sid = QWidget()

        # Add tabs
        self.tabs.addTab(self.tab_user, "User")
        self.tabs.addTab(self.tab_sid, "Sid")

        # Add tab_user ui_user
        self.btm = QPushButton("User")
        self.tab_user.layout = QVBoxLayout()
        self.tab_user.layout.addWidget(self.btm)
        #self.btm.clicked.connect(UiApp.close) # закрываю окно Методы должны вызываться на объектах, а не классах.<--------------------------------------------
        self.btm.clicked.connect(self.window().close)
        self.tab_user.setLayout(self.tab_user.layout)

        # Add tab_sid ui_sid
        self.lbl = QLabel('Sid')
        self.tab_sid.layout = QVBoxLayout()
        self.tab_sid.layout.addWidget(self.lbl)
        self.tab_sid.setLayout(self.tab_sid.layout)

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = UiApp()
    ex.show()
    sys.exit(app.exec_())
