import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

from widget import *

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """기본적인 레이아웃 제작"""
        #상단 메뉴바 및 기본 단축키---------------------------------
        self.statusBar()
        menubar = self.menuBar()

        #file
        filemenu = menubar.addMenu('&File')

        #나가기
        exitAction = QAction(QIcon(''), 'Exit', self)
        exitAction.setShortcut('Alt+F4')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)
        filemenu.addAction(exitAction)

        #help-----------------------------------------------------
        helpmenu = menubar.addMenu('&Help')
        #---------------------------------------------------------

        #Q위젯 삽입------------------------------------------------
        widget = sort_widget()
        self.setCentralWidget(widget)
        #---------------------------------------------------------

        # 창 이름, 아이콘, 위치 설정--------------------------------
        self.setWindowTitle('My First Application')
        # self.setWindowIcon(QIcon('web.png'))
        self.resize(1080, 720)
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        self.setWindowTitle('QSplitter')
        self.show()
        #---------------------------------------------------------


        


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())