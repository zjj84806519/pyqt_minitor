import cv2

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import pyqtSignal, QDateTime, QTimer
from PyQt5.QtWidgets import QWidget


class SmallScreen(QWidget):
    double_clicked_item = pyqtSignal(str)  # 双击信号

    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi()

    def setupUi(self):
        self.resize(305, 178)
        self.setMinimumSize(QtCore.QSize(305, 178))
        # self.setMaximumSize(QtCore.QSize(931, 524))
        self.setStyleSheet("QLabel{\n"
        "    font: 12px;\n"
        "    color: white;\n"
        "}\n"
        "QLabel#text{\n"
        "    background-color: rgb(83,83,83);\n"
        "    font: 18px;\n"
        "    font-weight: bold;\n"
        "}")

        self.text = QtWidgets.QLabel(self)
        self.text.setGeometry(QtCore.QRect(0, 0, 317, 178))
        self.text.setAlignment(QtCore.Qt.AlignCenter)
        self.text.setObjectName("text")

        self.time = QtWidgets.QLabel(self)
        self.time.setGeometry(QtCore.QRect(150, 0, 160, 21))
        self.time.setObjectName("time")
        self.time.setText("年-月-日 小时：分：秒")
        self.text.setText("无信号")

        self.camera = QtWidgets.QLabel(self)
        self.camera.setGeometry(QtCore.QRect(0, 160, 51, 20))
        self.camera.setObjectName("camera")
        self.camera.setText("camera1")

        self.timer = QTimer()
        self.timer.timeout.connect(self.showTime)  # 这个通过调用槽函数来刷新时间
        self.timer.start(1000)  # 每隔一秒刷新一次，这里设置为1000ms

        QtCore.QMetaObject.connectSlotsByName(self)

    def setCameraName(self, name):
        self.camera.setText(name)

    def showTime(self):
        time = QDateTime.currentDateTime()  # 获取当前时间
        timedisplay = time.toString("yyyy-MM-dd hh:mm:ss dddd")  # 格式化一下时间
        # print(timedisplay)
        self.time.setText(timedisplay)

    def mouseDoubleClickEvent(self, QMouseEvent):
        self.double_clicked_item.emit(self.camera.text())


class BigScreen(SmallScreen):
    double_clicked_item = pyqtSignal(str)  # 双击信号

    def __init__(self, parent):
        super().__init__(parent)
        # self.openCamera()

    def setupUi(self):
        super().setupUi()
        self.resize(931, 524)
        self.setStyleSheet("QLabel{\n"
                            "    font: 20px;\n"
                            "    color: white;\n"
                            "}\n"
                            "QLabel#text{\n"
                            "    background-color: rgb(83,83,83);\n"
                            "    font: 30px;\n"
                            "    font-weight: bold;\n"
                            "}")
        self.text.setGeometry(QtCore.QRect(0, 0, 931, 524))
        self.time.setGeometry(QtCore.QRect(660, 10, 271, 20))
        self.camera.setGeometry(QtCore.QRect(10, 490, 101, 20))

    def setCameraName(self, name):
        super().setCameraName(name)

    def showTime(self):
        super().showTime()

    def mouseDoubleClickEvent(self, QMouseEvent):
        self.double_clicked_item.emit(self.camera.text())