import sys
import cv2
from PyQt5 import QtCore,QtGui, QtWidgets
from Ui_yolodet import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btnopen.clicked.connect(self.Open)

    def Open(self):
        cap = cv2.VideoCapture(0)
        while cap.isOpened():
            ret, frame = cap.read()
            img = QtGui.QImage(frame.data, frame.shape[1], frame.shape[0], QtGui.QImage.Format_BGR888)
            # 重载修复图像显示变形问题
            # img = QtGui.QImage(frame.data, frame.shape[1], frame.shape[0], frame.shape[1] * 3,
            #                    QtGui.QImage.Format_BGR888)  # 设置label高度和宽度
            self.lblimg.setFixedSize(frame.shape[1], frame.shape[0])
            # self.lblimg.setFixedSize(307, 194)
            self.lblimg.setPixmap(QtGui.QPixmap.fromImage(img))
            self.lblimg.setScaledContents(True)  # 自适应大小
            QtWidgets.QApplication.processEvents()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mywin = MainWindow()
    mywin.setObjectName('Yolo3Detect')
    mywin.show()
    sys.exit(app.exec_())