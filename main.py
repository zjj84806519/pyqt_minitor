import sys

from PyQt5.Qt import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *

from Camera import SmallScreen, BigScreen


class MyWindow(QWidget):
    pressing = False
    start = QPoint(0, 0)

    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.show()

    def setup_ui(self):
        self.resize(1201, 875)
        self.setMinimumSize(QtCore.QSize(1201, 875))
        self.setMaximumSize(QtCore.QSize(1920, 1080))
        self.setWindowOpacity(1.0)
        self.main_page = QtWidgets.QTabWidget(self)
        self.main_page.setGeometry(QtCore.QRect(0, 10, 1191, 841))
        self.main_page.setStyleSheet("QTabWidget::pane {\n"
                                     "    background-color: rgba(0, 0, 0, 0);\n"
                                     "}\n"
                                     "QTabBar::tab:first{\n"
                                     "    margin-left: 160px;\n"
                                     "}\n"
                                     "QTabBar::tab {\n"
                                     "    width: 110px;\n"
                                     "    height: 30px;\n"
                                     "    /* 未选择的选项卡样式 */\n"
                                     "    padding-left: 10px;\n"
                                     "    color: white;\n"
                                     "    font: 12px;\n"
                                     "    border: 0px solid;\n"
                                     "}\n"
                                     "QTabBar::tab:selected {\n"
                                     "    /* 被选择的选项卡样式 */\n"
                                     "    width: 110px;\n"
                                     "    height: 30px;\n"
                                     "    border-bottom: 2px solid #225f9a;\n"
                                     "    background-color: #343761;\n"
                                     "}")
        self.main_page.setTabPosition(QtWidgets.QTabWidget.North)
        self.main_page.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.main_page.setIconSize(QtCore.QSize(20, 20))
        self.main_page.setElideMode(QtCore.Qt.ElideNone)
        self.main_page.setUsesScrollButtons(True)
        self.main_page.setDocumentMode(False)
        self.main_page.setTabsClosable(False)
        self.main_page.setMovable(False)
        self.main_page.setTabBarAutoHide(False)
        self.main_page.setObjectName("main_page")
        self.home = QtWidgets.QWidget()
        self.home.setStyleSheet("background-color: #212234;\n")
        self.home.setObjectName("home")
        self.home_page = QtWidgets.QStackedWidget(self.home)
        self.home_page.setEnabled(True)
        self.home_page.setGeometry(QtCore.QRect(229, 0, 971, 811))
        self.home_page.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.home_page.setTabletTracking(False)
        self.home_page.setFocusPolicy(QtCore.Qt.NoFocus)
        self.home_page.setAcceptDrops(False)
        self.home_page.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.home_page.setStyleSheet("")
        self.home_page.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.home_page.setFrameShadow(QtWidgets.QFrame.Plain)
        self.home_page.setLineWidth(1)
        self.home_page.setObjectName("home_page")
        self.all = QtWidgets.QWidget()
        self.all.setMouseTracking(False)
        self.all.setTabletTracking(False)
        self.all.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.all.setAutoFillBackground(False)
        self.all.setInputMethodHints(QtCore.Qt.ImhNone)
        self.all.setObjectName("all")
        self.camera_group = QtWidgets.QGroupBox(self.all)
        self.camera_group.setEnabled(True)
        self.camera_group.setGeometry(QtCore.QRect(10, 0, 951, 811))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.camera_group.sizePolicy().hasHeightForWidth())
        self.camera_group.setSizePolicy(sizePolicy)
        self.camera_group.setMinimumSize(QtCore.QSize(951, 811))
        # self.camera_group.setMaximumSize(QtCore.QSize())
        self.camera_group.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.camera_group.setAutoFillBackground(False)
        self.camera_group.setStyleSheet("QGroupBox{\n"
                                        "    border: 0px solid;\n"
                                        "}\n"
                                        "QLabel{\n"
                                        "    background-color: rgb(0,0,0,0);\n"
                                        "    color: white;\n"
                                        "}")
        self.camera_group.setObjectName("camera_group")
        self.gridLayout = QtWidgets.QGridLayout(self.camera_group)
        self.gridLayout.setObjectName("gridLayout")

        self.camera_1 = SmallScreen(self.camera_group)
        self.camera_1.setObjectName("camera1")
        self.camera_1.setCameraName(self.camera_1.objectName())
        self.camera_1.double_clicked_item.connect(self.videoDoubleClicked)
        self.gridLayout.addWidget(self.camera_1, 0, 1, 1, 1)

        self.camera_2 = SmallScreen(self.camera_group)
        self.camera_2.setObjectName("camera2")
        self.camera_2.setCameraName(self.camera_2.objectName())
        self.camera_2.double_clicked_item.connect(self.videoDoubleClicked)
        self.gridLayout.addWidget(self.camera_2, 0, 2, 1, 1)

        self.camera_3 = SmallScreen(self.camera_group)
        self.camera_3.setObjectName("camera3")
        self.camera_3.setCameraName(self.camera_3.objectName())
        self.camera_3.double_clicked_item.connect(self.videoDoubleClicked)
        self.gridLayout.addWidget(self.camera_3, 0, 3, 1, 1)

        self.camera_4 = SmallScreen(self.camera_group)
        self.camera_4.setObjectName("camera4")
        self.camera_4.setCameraName(self.camera_4.objectName())
        self.camera_4.double_clicked_item.connect(self.videoDoubleClicked)
        self.gridLayout.addWidget(self.camera_4, 1, 1, 1, 1)

        self.camera_5 = SmallScreen(self.camera_group)
        self.camera_5.setObjectName("camera5")
        self.camera_5.setCameraName(self.camera_5.objectName())
        self.camera_5.double_clicked_item.connect(self.videoDoubleClicked)
        self.gridLayout.addWidget(self.camera_5, 1, 2, 1, 1)

        self.camera_6 = SmallScreen(self.camera_group)
        self.camera_6.setObjectName("camera6")
        self.camera_6.setCameraName(self.camera_6.objectName())
        self.camera_6.double_clicked_item.connect(self.videoDoubleClicked)
        self.gridLayout.addWidget(self.camera_6, 1, 3, 1, 1)

        self.camera_7 = SmallScreen(self.camera_group)
        self.camera_7.setObjectName("camera7")
        self.camera_7.setCameraName(self.camera_7.objectName())
        self.camera_7.double_clicked_item.connect(self.videoDoubleClicked)
        self.gridLayout.addWidget(self.camera_7, 2, 1, 1, 1)

        self.camera_8 = SmallScreen(self.camera_group)
        self.camera_8.setObjectName("camera8")
        self.camera_8.setCameraName(self.camera_8.objectName())
        self.camera_8.double_clicked_item.connect(self.videoDoubleClicked)
        self.gridLayout.addWidget(self.camera_8, 2, 2, 1, 1)

        self.camera_9 = SmallScreen(self.camera_group)
        self.camera_9.setObjectName("camera9")
        self.camera_9.setCameraName(self.camera_9.objectName())
        self.camera_9.double_clicked_item.connect(self.videoDoubleClicked)
        self.gridLayout.addWidget(self.camera_9, 2, 3, 1, 1)

        self.camera_10 = SmallScreen(self.camera_group)
        self.camera_10.setObjectName("camera10")
        self.camera_10.setCameraName(self.camera_10.objectName())
        self.camera_10.double_clicked_item.connect(self.videoDoubleClicked)
        self.gridLayout.addWidget(self.camera_10, 3, 1, 1, 1)

        self.camera_11 = SmallScreen(self.camera_group)
        self.camera_11.setObjectName("camera11")
        self.camera_11.setCameraName(self.camera_11.objectName())
        self.camera_11.double_clicked_item.connect(self.videoDoubleClicked)
        self.gridLayout.addWidget(self.camera_11, 3, 2, 1, 1)

        self.camera_12 = SmallScreen(self.camera_group)
        self.camera_12.setObjectName("camera12")
        self.camera_12.setCameraName(self.camera_12.objectName())
        self.camera_12.double_clicked_item.connect(self.videoDoubleClicked)
        self.gridLayout.addWidget(self.camera_12, 3, 3, 1, 1)

        self.home_page.addWidget(self.all)
        self.one = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.one.sizePolicy().hasHeightForWidth())
        self.one.setSizePolicy(sizePolicy)
        self.one.setObjectName("one")
        self.big_camera = QtWidgets.QGroupBox(self.one)
        self.big_camera.setGeometry(QtCore.QRect(10, 0, 951, 811))
        self.big_camera.setStyleSheet("QGroupBox{\n"
                                        "    border: 0px solid;\n"
                                        "}\n"
                                        "QLabel{\n"
                                        "    background-color: rgb(0,0,0,0);\n"
                                        "    color: white;\n"
                                        "}")
        self.big_camera.setObjectName("big_camera")

        self.video = BigScreen(self.big_camera)
        self.video.setGeometry(QtCore.QRect(10, 90, 931, 611))
        self.video.double_clicked_item.connect(self.videoBack)

        self.play_button = QtWidgets.QGroupBox(self.big_camera)
        self.play_button.setGeometry(QtCore.QRect(290, 710, 381, 43))
        self.play_button.setStyleSheet("QPushButton{\n"
                                       "    width: 70px;\n"
                                       "    height: 35px;\n"
                                       "    color: white;\n"
                                       "    background-color: #46485d;\n"
                                       "    border-radius: 5px;\n"
                                       "}\n"
                                       "QPushButton:pressed{\n"
                                       "    background-color: #25273a;\n"
                                       "}")
        self.play_button.setTitle("")
        self.play_button.setObjectName("play_button")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.play_button)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.forward_btn = QtWidgets.QPushButton(self.play_button)
        self.forward_btn.setObjectName("forward_btn")
        self.horizontalLayout_2.addWidget(self.forward_btn)
        self.pause_btn = QtWidgets.QPushButton(self.play_button)
        self.pause_btn.setObjectName("pause_btn")
        self.horizontalLayout_2.addWidget(self.pause_btn)
        self.backward_btn = QtWidgets.QPushButton(self.play_button)
        self.backward_btn.setObjectName("backward_btn")
        self.horizontalLayout_2.addWidget(self.backward_btn)
        self.home_page.addWidget(self.one)
        self.info = QtWidgets.QWidget(self.home)
        self.info.setGeometry(QtCore.QRect(10, 0, 221, 801))
        self.info.setStyleSheet("background-color: #2a2c36;")
        self.info.setObjectName("info")
        self.user_info = QtWidgets.QGroupBox(self.info)
        self.user_info.setGeometry(QtCore.QRect(0, 410, 218, 401))
        self.user_info.setStyleSheet("QGroupBox{\n"
                                     "    background-color: #212234;\n"
                                     "    border-top: 3px solid black;\n"
                                     "}\n"
                                     "QGroupBox QLabel{\n"
                                     "    background-color: rgb(0,0,0,0);\n"
                                     "    color: white;\n"
                                     "}\n"
                                     "")
        self.user_info.setTitle("")
        self.user_info.setObjectName("user_info")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.user_info)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.user_info)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.user_info)
        self.label_3.setMinimumSize(QtCore.QSize(100, 150))
        self.label_3.setMaximumSize(QtCore.QSize(150, 150))
        self.label_3.setStyleSheet("background-color: black;")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("Python.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(False)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.user_info)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.user_info)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/jiankongkongzhiguanli_white.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.main_page.addTab(self.home, icon, "")
        self.manage = QtWidgets.QWidget()
        self.manage.setStyleSheet("QWidget{\n"
                                  "    color: white;\n"
                                  "    background-color: #212234;\n"
                                  "    font-size: 14px;\n"
                                  "}\n"
                                  "QTableWidget{\n"
                                  "    border: 0px solid;\n"
                                  "}")
        self.manage.setObjectName("manage")
        self.tableWidget = QtWidgets.QTableWidget(self.manage)
        self.tableWidget.setGeometry(QtCore.QRect(10, 60, 1171, 741))
        self.tableWidget.setStyleSheet("QTableWidget{\n"
                                       "    background-color: #212234;\n"
                                       "}\n"
                                       "QTableWidget::item{\n"
                                       "    padding: 5px;\n"
                                       "    background-color: #212234;\n"
                                       "    border-bottom: 1px solid #5b7b9a;\n"
                                       "    border-right: 1px solid #5b7b9a;\n"
                                       "}\n"
                                       "QTableWidget::item:selected {\n"
                                       "    background-color: #99CCFF;\n"
                                       "}\n"
                                       "QHeaderView::section {\n"
                                       "    background-color: #212234;\n"
                                       "    border:    1px solid #5b7b9a;\n"
                                       "    border-left: 0px solid;\n"
                                       "    color: white;\n"
                                       "}")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setRowCount(4)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.tableWidget.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 3, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.horizontalWidget = QtWidgets.QWidget(self.manage)
        self.horizontalWidget.setGeometry(QtCore.QRect(0, 0, 1191, 41))
        self.horizontalWidget.setStyleSheet("QWidget{\n"
                                            "    background-color: #2a2c36;\n"
                                            "}\n"
                                            "QPushButton{\n"
                                            "    width: 70px;\n"
                                            "    height: 35px;\n"
                                            "    margin-left: 5px;\n"
                                            "    background-color: #46485d;\n"
                                            "    border-radius: 5px;\n"
                                            "}\n"
                                            "QPushButton:pressed{\n"
                                            "    background-color: #25273a;\n"
                                            "}")
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.horizontalWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon/shipinjiankong_white.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.main_page.addTab(self.manage, icon1, "")
        self.diary = QtWidgets.QWidget()
        self.diary.setObjectName("diary")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icon/rizhi_white.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.main_page.addTab(self.diary, icon2, "")
        self.setting = QtWidgets.QWidget()
        self.setting.setObjectName("setting")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icon/shezhi_white.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.main_page.addTab(self.setting, icon3, "")
        self.title = QtWidgets.QGroupBox(self)
        self.title.setGeometry(QtCore.QRect(0, 0, 161, 51))
        self.title.setStyleSheet("QGroupBox{\n"
                                 "    border: 0px solid;\n"
                                 "}\n"
                                 "QGroupBox QLabel {\n"
                                 "    /* QLabel样式设置 */\n"
                                 "    color:white;\n"
                                 "    font: 18px;\n"
                                 "}")
        self.title.setTitle("")
        self.title.setObjectName("title")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.title)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.title_icon = QtWidgets.QLabel(self.title)
        self.title_icon.setMaximumSize(QtCore.QSize(22, 22))
        self.title_icon.setText("")
        self.title_icon.setPixmap(QtGui.QPixmap("Python.png"))
        self.title_icon.setScaledContents(True)
        self.title_icon.setObjectName("title_icon")
        self.horizontalLayout.addWidget(self.title_icon)
        self.title_text = QtWidgets.QLabel(self.title)
        self.title_text.setObjectName("title_text")
        self.horizontalLayout.addWidget(self.title_text)
        self.tool_btn = QtWidgets.QGroupBox(self)
        self.tool_btn.setGeometry(QtCore.QRect(1110, 0, 90, 40))
        self.tool_btn.setMinimumSize(QtCore.QSize(90, 40))
        self.tool_btn.setMaximumSize(QtCore.QSize(90, 40))
        self.tool_btn.setStyleSheet("QGroupBox{\n"
                                    "    border: 0px solid;\n"
                                    "}\n"
                                    "QPushButton{\n"
                                    "    border-radius: 2px;\n"
                                    "}\n"
                                    "QPushButton:hover{\n"
                                    "    background-color: #242531;\n"
                                    "}\n"
                                    "QPushButton:pressed{\n"
                                    "    background-color: #1d1f31;\n"
                                    "}")
        self.tool_btn.setTitle("")
        self.tool_btn.setObjectName("tool_btn")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tool_btn)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.min_btn = QtWidgets.QPushButton(self.tool_btn)
        self.min_btn.setMinimumSize(QtCore.QSize(20, 20))
        self.min_btn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icon/Minimize-2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.min_btn.setIcon(icon4)
        self.min_btn.setFlat(True)
        self.min_btn.setObjectName("min_btn")
        self.horizontalLayout_4.addWidget(self.min_btn)
        self.max_btn = QtWidgets.QPushButton(self.tool_btn)
        self.max_btn.setMinimumSize(QtCore.QSize(20, 20))
        self.max_btn.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icon/Maximize-4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.max_btn.setIcon(icon5)
        self.max_btn.setFlat(True)
        self.max_btn.setObjectName("max_btn")
        self.horizontalLayout_4.addWidget(self.max_btn)
        self.close_btn = QtWidgets.QPushButton(self.tool_btn)
        self.close_btn.setMinimumSize(QtCore.QSize(20, 20))
        self.close_btn.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icon/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_btn.setIcon(icon6)
        self.close_btn.setFlat(True)
        self.close_btn.setObjectName("close_btn")
        self.horizontalLayout_4.addWidget(self.close_btn)
        self.background = QtWidgets.QLabel(self)
        self.background.setGeometry(QtCore.QRect(0, 0, 1201, 875))
        self.background.setStyleSheet("background-color: #212234;border-radius: 10px;")
        self.background.setText("")
        self.background.setObjectName("background")
        self.background.raise_()
        self.main_page.raise_()
        self.title.raise_()
        self.tool_btn.raise_()

        self.retranslateUi()
        self.main_page.setCurrentIndex(0)
        self.home_page.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.Title_Button()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))
        self.forward_btn.setText(_translate("self", "前进"))
        self.pause_btn.setText(_translate("self", "暂停"))
        self.backward_btn.setText(_translate("self", "后退"))
        self.label_2.setText(_translate("self", "姓名：XXX"))
        self.label_4.setText(_translate("self", "sssss"))
        self.label_5.setText(_translate("self", "xxxxx"))
        self.main_page.setTabText(self.main_page.indexOf(self.home), _translate("self", "监控大屏"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("self", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("self", "2"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("self", "名称"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("self", "url"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("self", "启动AI监测"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("self", "监测类型"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("self", "A-1"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("self", "111111"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("self", "人脸识别"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("self", "A-2"))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("self", "222222"))
        item = self.tableWidget.item(1, 3)
        item.setText(_translate("self", "目标追踪"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_3.setText(_translate("self", "添加"))
        self.pushButton_2.setText(_translate("self", "删除"))
        self.pushButton.setText(_translate("self", "预览"))
        self.main_page.setTabText(self.main_page.indexOf(self.manage), _translate("self", "摄像头管理"))
        self.main_page.setTabText(self.main_page.indexOf(self.diary), _translate("self", "日志查询"))
        self.main_page.setTabText(self.main_page.indexOf(self.setting), _translate("self", "系统设置"))
        self.title_text.setText(_translate("self", "智能监控系统"))

    def Title_Button(self):
        # 关闭按钮
        self.close_btn.clicked.connect(self.close)

        def maximize_method():
            # 最大化按钮方法
            if window.isMaximized():
                self.showNormal()
                # print("restore")
            else:
                self.showMaximized()
                # print("maximize")

        self.max_btn.clicked.connect(maximize_method)

        # 最小化按钮
        self.min_btn.clicked.connect(self.showMinimized)

    def resizeEvent(self, evt):
        # print("resize")
        self.tool_btn_x = self.width() - self.tool_btn.width()
        self.tool_btn.move(self.tool_btn_x, self.tool_btn.y())


    def mousePressEvent(self, evt):    # 窗口移动
        if evt.x() <= self.tool_btn_x and evt.y() <= 30:
            # print("mousePress")
            self.start = self.mapToGlobal(evt.pos())
            self.pressing = True

    def mouseMoveEvent(self, evt):
        if self.pressing:
            # print("mouseMove")
            self.end = self.mapToGlobal(evt.pos())
            self.movement = self.end - self.start
            self.setGeometry(self.mapToGlobal(self.movement).x(),
                                    self.mapToGlobal(self.movement).y(),
                                    self.width(),
                                    self.height())
            self.start = self.end

    def mouseReleaseEvent(self, evt):
        # print("mouseRelease")
        self.pressing = False

    def videoDoubleClicked(self, msg):
        # print(msg)
        self.video.setCameraName(msg)
        self.home_page.setCurrentIndex(1)
        # self.maximize()

    # def maximize(self):
    #     # 监控窗口最大化
    #     # self.resize(931, 524)
    #     self.setParent(self.all)
    #     self.setGeometry(QtCore.QRect(10, 10, 931, 524))

    def videoBack(self, msg):
        # print(msg)
        self.home_page.setCurrentIndex(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MyWindow()
    # 程序进行循环等待状态
    app.exec_()