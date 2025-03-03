from PyQt5.QtCore import Qt, QSize, QEvent
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *

from model.FrameConfig import FrameConfig
from view.QTransparentButtonView import TransparentButton
from view.QDevelopView import QDevelopView


class QSmartFrameView(QMainWindow):

    def __init__(self):
        super().__init__()

        self.fc = FrameConfig()

        self.setWindowTitle("SmartPicFrame")
        self.setObjectName("main")
        self.setStyleSheet("QMainWindow#main {background-color:'BLACK';}")

        self.blurEffect = QGraphicsBlurEffect()
        self.blurEffect.setBlurRadius(18)

        self.bgImage = QLabel(self)
        self.bgImage.setGraphicsEffect(self.blurEffect)

        self.darkBg = QLabel(self)
        self.darkBg.setStyleSheet("background-color: rgba(0, 0, 0, 25%)")

        self.image = QLabel(self)
        self.image.setAlignment(Qt.AlignCenter)

        self.pixmap = QPixmap("")
        self.image.setPixmap(self.pixmap)
        self.bgImage.setPixmap(self.pixmap)

        '''
        Message Box
        '''
        self.msg = QLabel(self)
        self.msg.setStyleSheet("color:'WHITE'; "
                               "background-color: rgba(0, 0, 0, 60%); "
                               "font: 'Helvetica'; "
                               "font-size: 50px;"
                               "border-width: 3px;"
                               "border-style: solid;"
                               "border-color: rgba(0, 0, 0, 60%);"
                               "border-radius: 10px;")
        self.msg.setAlignment(Qt.AlignLeft)
        self.msg.setWordWrap(True)
        self.msg.setContentsMargins(20, 10, 10, 10)

        '''
        Semino
        '''
        self.seminoImage = QLabel(self)
        self.seminoPixmap = QPixmap('defaultImage/seminoImg2.png')
        self.seminoImage.setPixmap(self.seminoPixmap)
        self.seminoImage.adjustSize()
        self.seminoImage.hide()

        '''
        Last Update Display
        '''
        self.lastDate = QLabel(self)
        self.lastDate.setStyleSheet("color:'WHITE'; "
                                    "background-color: rgba(0, 0, 0, 60%); "
                                    "font: 'Helvetica'; "
                                    "font-size: 35px;"
                                    "border-width: 3px;"
                                    "border-style: solid;"
                                    "border-color: rgba(0, 0, 0, 60%);"
                                    "border-radius: 10px;")
        self.lastDate.setAlignment(Qt.AlignCenter)
        self.lastDate.setFixedWidth(480)
        self.lastDate.setFixedHeight(self.lastDate.height() + 10)

        '''
        Current Image Counter Display
        '''
        self.imgCount = QLabel(self)
        self.imgCount.setStyleSheet("color:'WHITE'; "
                                    "background-color: rgba(0, 0, 0, 60%); "
                                    "font: 'Helvetica'; "
                                    "font-size: 35px;"
                                    "border-width: 3px;"
                                    "border-style: solid;"
                                    "border-color: rgba(0, 0, 0, 60%);"
                                    "border-radius: 10px;")
        self.imgCount.setAlignment(Qt.AlignCenter)
        self.imgCount.setWordWrap(True)
        self.imgCount.setFixedHeight(self.imgCount.height() + 10)

        '''
        Touch Layer / Frame
        '''
        self.touchFrame = QLabel(self)

        '''
        Buttons
        '''
        self.pauseBtn = TransparentButton(self, 'graphics/pauseBtn.png')
        self.playBtn = TransparentButton(self, 'graphics/playBtn.png')
        self.playBtn.btn.hide()
        self.arrowBtn = TransparentButton(self, 'graphics/arrowButtonTmp.png')
        self.arrowBtnL = TransparentButton(self, 'graphics/arrowButtonTmpL.png')
        self.messageBtn = TransparentButton(self, 'graphics/messageBtn.png')
        self.messageOpen = TransparentButton(self, 'graphics/messageOpen.png')
        self.messageOpen.btn.setIconSize(QSize(200, 200))
        self.messageBtn.btn.hide()
        self.seminoBtn = TransparentButton(self, 'graphics/seminoBtn.png')

        '''
        QDevelopView
        '''
        self.dev = QDevelopView(self)
        self.dev.frame.hide()

        self.setPosition()

        self.show()

    def setPosition(self):
        self.setGeometry(0, 0, self.fc.width, self.fc.height)

        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)

        self.arrowBtn.btn.move(self.fc.width - 200, int(self.fc.height / 2) - 100)
        self.arrowBtnL.btn.move(50, int(self.fc.height / 2) - 100)
        self.pauseBtn.btn.move(int(self.fc.width / 2) - int(self.pauseBtn.btn.width() / 2), int(self.fc.height / 2) - 100)
        self.playBtn.btn.move(int(self.fc.width / 2) - int(self.playBtn.btn.width() / 2) + 10, int(self.fc.height / 2) - 100)
        self.messageBtn.btn.move(self.fc.width - 200, self.fc.height - 175)
        self.messageOpen.btn.move(self.fc.width - 200, self.fc.height - 200)
        self.lastDate.move(self.fc.width - 500, 20)
        self.imgCount.move(int(self.fc.width / 2) - int(self.imgCount.width() / 2), 20)
        self.msg.setFixedWidth(int(self.fc.width * 0.65))
        self.move(qtRectangle.topLeft())

        self.touchFrame.resize(self.fc.width, self.fc.height)
        self.image.resize(self.fc.width, self.fc.height)
        self.bgImage.resize(self.fc.width, self.fc.height)
        self.darkBg.resize(self.fc.width, self.fc.height)

    def showDevMode(self):
        self.dev.setValues()
        self.dev.frame.show()

    def hideDevMode(self):
        self.dev.frame.hide()

    def hideSemino(self):
        self.seminoImage.hide()

    def showSemino(self):
        self.seminoImage.show()

    def touchVisibility(self):
        if not self.fc.isTouch:
            self.arrowBtn.btn.hide()
            self.arrowBtnL.btn.hide()
            self.pauseBtn.btn.hide()
            self.playBtn.btn.hide()
            self.imgCount.hide()
            self.lastDate.hide()
        else:
            self.arrowBtn.btn.show()
            self.arrowBtnL.btn.show()
            self.imgCount.show()
            self.lastDate.show()
            if self.fc.pause:
                self.playBtn.btn.show()
            else:
                self.pauseBtn.btn.show()

    def messageVisibility(self):
        if self.fc.showMessage:
            self.messageBtn.btn.hide()
            self.messageOpen.btn.show()
            self.msg.show()
            self.seminoBtn.btn.show()
            if self.fc.isSemino:
                self.seminoImage.show()
        else:
            self.messageBtn.btn.show()
            self.messageOpen.btn.hide()
            self.msg.hide()
            self.seminoBtn.btn.hide()
            self.seminoImage.hide()

    def messageMove(self):
        self.msg.move(int(self.fc.width / 2 - self.msg.width() / 2), int(self.fc.height - self.fc.msgHeight - 50))
        self.seminoImage.move(self.msg.x() - self.seminoPixmap.width() + 75, self.fc.height - self.seminoPixmap.height())
        self.seminoBtn.btn.move(self.msg.x() - self.seminoBtn.btn.width() + 65, self.fc.height - 145)

    def keyPressEvent(self, event):
        if event.type() == QEvent.KeyPress and event.key() == Qt.Key_Escape:
            self.showDevMode()
