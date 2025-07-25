# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'met_main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QProgressBar, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_METMainWindow(object):
    def setupUi(self, METMainWindow):
        if not METMainWindow.objectName():
            METMainWindow.setObjectName(u"METMainWindow")
        METMainWindow.resize(1610, 972)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(METMainWindow.sizePolicy().hasHeightForWidth())
        METMainWindow.setSizePolicy(sizePolicy)
        METMainWindow.setMinimumSize(QSize(0, 0))
        METMainWindow.setStyleSheet(u"/*-----QScrollArea-----*/\n"
"QScrollArea\n"
"{\n"
"	border: 0px solid black; \n"
"	margin: 0px 0px 0px 0px;\n"
"	border-style:none;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLayout-----*/\n"
"QLayout\n"
"{\n"
"	border-style:none;\n"
"	border-radius: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QWidget-----*/\n"
"QWidget\n"
"{\n"
"	background-color: transparent;\n"
"	color: #000000;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QFrame-----*/\n"
"QFrame\n"
"{\n"
"	border-style:none;\n"
"	border-radius: 5px;\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(27, 39, 50, 255),stop:1 rgba(47, 53, 74, 255));\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLabel-----*/\n"
"QLabel\n"
"{\n"
"	background-color: transparent;\n"
"	color: #c2c7d5;\n"
"	font-size: 13px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QPushButton-----*/\n"
"QPushButton\n"
"{\n"
"	background-color: hsv(187, 100%, 70%);\n"
"	color: rgb(255, 255, 255);\n"
"	font-size: 16px;\n"
"	font-weight: bold;\n"
"	padding: 5px;\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"}\n"
""
                        "\n"
"\n"
"QPushButton::hover\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 hsv(187, 100%, 70%),stop:1 hsv(180, 100%, 90%));\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"	background-color: hsv(180, 100%, 100%);\n"
"\n"
"}\n"
"\n"
"QPushButton::disabled\n"
"{\n"
"	background-color: hsv(180, 0%, 50%);\n"
"	color: hsv(0, 0%, 40%);\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QProgressBar-----*/\n"
"QProgressBar\n"
"{\n"
"	background-color: hsv(187, 100%, 70%);\n"
"	color: rgb(255, 255, 255);\n"
"	font-size: 13px;\n"
"	font-weight: bold;\n"
"	padding: -1px;\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QProgressBar:chunk\n"
"{\n"
"	background-color: hsv(180, 100%, 90%);\n"
"	color: rgb(255, 255, 255);\n"
"	font-size: 20px;\n"
"	font-weight: bold;\n"
"	padding: -1px;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"\n"
"/*-----QCheckBox-----*/\n"
"QCheckBox\n"
"{\n"
"	background-color: transparent;\n"
"	color: #fff;\n"
"	font-size: 10px;\n"
"	font-weight"
                        ": bold;\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QCheckBox-----*/\n"
"QCheckBox::indicator\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid darkgray;\n"
"    width: 12px;\n"
"    height: 12px;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image:url(\"./ressources/check.png\");\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.511, x2:1, y2:0.511, stop:0 rgba(0, 172, 149, 255),stop:0.995192 rgba(54, 197, 177, 255));;\n"
"    border: 1px solid #607cff;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:unchecked:hover\n"
"{\n"
"    border: 1px solid #08b099;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::disabled\n"
"{\n"
"	color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:disabled\n"
"{\n"
"	background-color: #656565;\n"
"	color: #656565;\n"
"    border: 1px solid #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLineEdit-----*/\n"
"QLineEdit\n"
"{\n"
"	background-color: #c2c7d5;\n"
"	color: #000;\n"
"	font-weight"
                        ": bold;\n"
"	border: none;\n"
"	border-radius: 2px;\n"
"	padding: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QListView-----*/\n"
"QListView\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(50, 61, 80, 255),stop:1 rgba(44, 49, 69, 255));\n"
"	color: #fff;\n"
"	font-size: 12px;\n"
"	font-weight: bold;\n"
"	border: 1px solid #191919;\n"
"	show-decoration-selected: 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item\n"
"{\n"
"	color: #31cecb;\n"
"	background-color: #454e5e;\n"
"	border: none;\n"
"	padding: 5px;\n"
"	border-radius: 0px;\n"
"	padding-left : 10px;\n"
"	height: 42px;\n"
"\n"
"}\n"
"\n"
"QListView::item:selected\n"
"{\n"
"	color: #31cecb;\n"
"	background-color: #454e5e;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:!selected\n"
"{\n"
"	color:white;\n"
"	background-color: transparent;\n"
"	border: none;\n"
"	padding-left : 10px;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:!selected:hover\n"
"{\n"
"	color: #bbbcba;\n"
"	background-color: #454e5e;\n"
"	border: none;\n"
"	padding-left"
                        " : 10px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QTreeView-----*/\n"
"QTreeView \n"
"{\n"
"	background-color: #232939;\n"
"	show-decoration-selected: 0;\n"
"	color: #c2c8d7;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::item \n"
"{\n"
"	border-top-color: transparent;\n"
"	border-bottom-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::item:hover \n"
"{\n"
"	background-color: #606060;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::item:selected \n"
"{\n"
"	background-color: #0ab19a;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::item:selected:active\n"
"{\n"
"	background-color: #0ab19a;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed,\n"
"QTreeView::branch:closed:has-children:has-siblings \n"
"{\n"
"	image: url(://tree-closed.png);\n"
"\n"
"}\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings,\n"
"QTreeView::branch:open:has-children:has-siblings  \n"
"{\n"
"	image: url(://tree-open.png);\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QTableView & QTableWidget-----*/\n"
""
                        "QTableView\n"
"{\n"
"    background-color: #232939;\n"
"	border: 1px solid gray;\n"
"    color: #f0f0f0;\n"
"    gridline-color: #232939;\n"
"    outline : 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::disabled\n"
"{\n"
"    background-color: #242526;\n"
"    border: 1px solid #32414B;\n"
"    color: #656565;\n"
"    gridline-color: #656565;\n"
"    outline : 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::item:hover \n"
"{\n"
"    background-color: #606060;\n"
"    color: #f0f0f0;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::item:selected \n"
"{\n"
"	background-color: #0ab19a;\n"
"    color: #F0F0F0;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::item:selected:disabled\n"
"{\n"
"    background-color: #1a1b1c;\n"
"    border: 2px solid #525251;\n"
"    color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableCornerButton::section\n"
"{\n"
"	background-color: #343a49;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section\n"
"{\n"
"	color: #fff;\n"
"	border-top: 0px;\n"
"	border-bottom: 1px solid gray;\n"
"	border-right: 1px solid gray;\n"
""
                        "	background-color: #343a49;\n"
"    margin-top:1px;\n"
"	margin-bottom:1px;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:disabled\n"
"{\n"
"    background-color: #525251;\n"
"    color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:checked\n"
"{\n"
"    color: #fff;\n"
"    background-color: #0ab19a;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:checked:disabled\n"
"{\n"
"    color: #656565;\n"
"    background-color: #525251;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::vertical::first,\n"
"QHeaderView::section::vertical::only-one\n"
"{\n"
"    border-top: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::vertical\n"
"{\n"
"    border-top: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::horizontal::first,\n"
"QHeaderView::section::horizontal::only-one\n"
"{\n"
"    border-left: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::horizontal\n"
"{\n"
"    border-left: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QScrollBar-----*"
                        "/\n"
"QScrollBar:horizontal \n"
"{\n"
"    background-color: transparent;\n"
"    height: 8px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:horizontal \n"
"{\n"
"    border: none;\n"
"	min-width: 100px;\n"
"    background-color: #56576c;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal, \n"
"QScrollBar::sub-line:horizontal,\n"
"QScrollBar::add-page:horizontal, \n"
"QScrollBar::sub-page:horizontal \n"
"{\n"
"    width: 0px;\n"
"    background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar:vertical \n"
"{\n"
"    background-color: transparent;\n"
"    width: 8px;\n"
"    margin: 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical \n"
"{\n"
"    border: none;\n"
"	min-height: 100px;\n"
"    background-color: #56576c;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical, \n"
"QScrollBar::sub-line:vertical,\n"
"QScrollBar::add-page:vertical, \n"
"QScrollBar::sub-page:vertical \n"
"{\n"
"    height: 0px;\n"
"    background-color: transparent;\n"
"\n"
""
                        "}\n"
"")
        self.centralwidget = QWidget(METMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.centralwidget.setStyleSheet(u"#centralwidget {background: white}")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.start_frame = QFrame(self.centralwidget)
        self.start_frame.setObjectName(u"start_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.start_frame.sizePolicy().hasHeightForWidth())
        self.start_frame.setSizePolicy(sizePolicy1)
        self.start_frame.setMinimumSize(QSize(360, 0))
        self.start_frame.setMaximumSize(QSize(360, 16777215))
        self.start_frame.setStyleSheet(u"QPushButton{\n"
"font-size:20px\n"
"}\n"
"#start_frame {background: transparent}")
        self.start_frame.setFrameShape(QFrame.StyledPanel)
        self.start_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.start_frame)
        self.verticalLayout_8.setSpacing(5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(5, 5, 5, 5)
        self.maya_version_frame = QFrame(self.start_frame)
        self.maya_version_frame.setObjectName(u"maya_version_frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.maya_version_frame.sizePolicy().hasHeightForWidth())
        self.maya_version_frame.setSizePolicy(sizePolicy2)
        self.maya_version_frame.setFrameShape(QFrame.StyledPanel)
        self.maya_version_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.maya_version_frame)
        self.verticalLayout_13.setSpacing(5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(5, 5, 5, 5)
        self.label_8 = QLabel(self.maya_version_frame)
        self.label_8.setObjectName(u"label_8")
        sizePolicy2.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy2)
        self.label_8.setStyleSheet(u"color: hsl(333, 100%, 50%); font-weight: bold")
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_8.setWordWrap(True)

        self.verticalLayout_13.addWidget(self.label_8)


        self.verticalLayout_8.addWidget(self.maya_version_frame)

        self.frame2 = QFrame(self.start_frame)
        self.frame2.setObjectName(u"frame2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame2.sizePolicy().hasHeightForWidth())
        self.frame2.setSizePolicy(sizePolicy3)
        self.frame2.setMinimumSize(QSize(0, 0))
        self.frame2.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_5 = QVBoxLayout(self.frame2)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.label_4 = QLabel(self.frame2)
        self.label_4.setObjectName(u"label_4")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy4)
        self.label_4.setMinimumSize(QSize(263, 0))
        font = QFont()
        font.setKerning(True)
        self.label_4.setFont(font)
        self.label_4.setTextFormat(Qt.PlainText)
        self.label_4.setScaledContents(False)
        self.label_4.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.label_4)

        self.metahuman_to_obj_button = QPushButton(self.frame2)
        self.metahuman_to_obj_button.setObjectName(u"metahuman_to_obj_button")
        sizePolicy3.setHeightForWidth(self.metahuman_to_obj_button.sizePolicy().hasHeightForWidth())
        self.metahuman_to_obj_button.setSizePolicy(sizePolicy3)
        self.metahuman_to_obj_button.setMinimumSize(QSize(0, 100))
        self.metahuman_to_obj_button.setMaximumSize(QSize(16777215, 100))
        font1 = QFont()
        font1.setBold(True)
        self.metahuman_to_obj_button.setFont(font1)

        self.verticalLayout_5.addWidget(self.metahuman_to_obj_button)


        self.verticalLayout_8.addWidget(self.frame2)

        self.frame1 = QFrame(self.start_frame)
        self.frame1.setObjectName(u"frame1")
        sizePolicy3.setHeightForWidth(self.frame1.sizePolicy().hasHeightForWidth())
        self.frame1.setSizePolicy(sizePolicy3)
        self.frame1.setMinimumSize(QSize(0, 0))
        self.frame1.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_6 = QVBoxLayout(self.frame1)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.label_5 = QLabel(self.frame1)
        self.label_5.setObjectName(u"label_5")
        sizePolicy4.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy4)
        self.label_5.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.label_5)

        self.obj_to_metahuman_button = QPushButton(self.frame1)
        self.obj_to_metahuman_button.setObjectName(u"obj_to_metahuman_button")
        sizePolicy3.setHeightForWidth(self.obj_to_metahuman_button.sizePolicy().hasHeightForWidth())
        self.obj_to_metahuman_button.setSizePolicy(sizePolicy3)
        self.obj_to_metahuman_button.setMinimumSize(QSize(0, 100))
        self.obj_to_metahuman_button.setMaximumSize(QSize(16777215, 100))

        self.verticalLayout_6.addWidget(self.obj_to_metahuman_button)


        self.verticalLayout_8.addWidget(self.frame1)

        self.frame_7 = QFrame(self.start_frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_7)
        self.verticalLayout_15.setSpacing(5)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(5, 5, 5, 5)
        self.label_10 = QLabel(self.frame_7)
        self.label_10.setObjectName(u"label_10")
        sizePolicy4.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy4)
        self.label_10.setWordWrap(True)

        self.verticalLayout_15.addWidget(self.label_10)

        self.discord_label = QLabel(self.frame_7)
        self.discord_label.setObjectName(u"discord_label")
        self.discord_label.setOpenExternalLinks(True)

        self.verticalLayout_15.addWidget(self.discord_label, 0, Qt.AlignHCenter)


        self.verticalLayout_8.addWidget(self.frame_7)

        self.new_version_frame = QFrame(self.start_frame)
        self.new_version_frame.setObjectName(u"new_version_frame")
        sizePolicy3.setHeightForWidth(self.new_version_frame.sizePolicy().hasHeightForWidth())
        self.new_version_frame.setSizePolicy(sizePolicy3)
        self.new_version_frame.setFrameShape(QFrame.StyledPanel)
        self.new_version_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.new_version_frame)
        self.verticalLayout_12.setSpacing(5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(5, 5, 5, 5)
        self.label_7 = QLabel(self.new_version_frame)
        self.label_7.setObjectName(u"label_7")
        sizePolicy4.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy4)

        self.verticalLayout_12.addWidget(self.label_7)

        self.changes_label = QLabel(self.new_version_frame)
        self.changes_label.setObjectName(u"changes_label")

        self.verticalLayout_12.addWidget(self.changes_label)

        self.update_button = QPushButton(self.new_version_frame)
        self.update_button.setObjectName(u"update_button")
        self.update_button.setMinimumSize(QSize(0, 40))
        self.update_button.setMaximumSize(QSize(16777215, 40))
        self.update_button.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: hsl(50, 100%, 50%);\n"
"	color: rgb(255, 255, 255);\n"
"	font-size: 20px;\n"
"	font-weight: bold;\n"
"	padding: 5px;\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 hsl(50, 100%, 50%),stop:1 hsl(50, 100%, 65%));\n"
"}\n"
"QPushButton::pressed\n"
"{\n"
"	background-color: hsl(50, 100%, 70%);\n"
"}")

        self.verticalLayout_12.addWidget(self.update_button)

        self.update_progress_bar = QProgressBar(self.new_version_frame)
        self.update_progress_bar.setObjectName(u"update_progress_bar")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.update_progress_bar.sizePolicy().hasHeightForWidth())
        self.update_progress_bar.setSizePolicy(sizePolicy5)
        self.update_progress_bar.setMinimumSize(QSize(0, 40))
        self.update_progress_bar.setMaximumSize(QSize(16777215, 40))
        self.update_progress_bar.setStyleSheet(u"QProgressBar\n"
"{\n"
"	background-color: hsl(50, 100%, 50%);\n"
"}\n"
"\n"
"QProgressBar:chunk\n"
"{\n"
"	background-color: hsv(180, 100%, 90%);\n"
"}")
        self.update_progress_bar.setValue(5)
        self.update_progress_bar.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.update_progress_bar)

        self.restart_met_button = QPushButton(self.new_version_frame)
        self.restart_met_button.setObjectName(u"restart_met_button")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.restart_met_button.sizePolicy().hasHeightForWidth())
        self.restart_met_button.setSizePolicy(sizePolicy6)
        self.restart_met_button.setMinimumSize(QSize(0, 40))
        self.restart_met_button.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_12.addWidget(self.restart_met_button)

        self.updated_successfully_label = QLabel(self.new_version_frame)
        self.updated_successfully_label.setObjectName(u"updated_successfully_label")
        self.updated_successfully_label.setStyleSheet(u"color: hsl(177, 100%, 50%); font-weight: bold")

        self.verticalLayout_12.addWidget(self.updated_successfully_label, 0, Qt.AlignHCenter)

        self.update_failed_frame = QFrame(self.new_version_frame)
        self.update_failed_frame.setObjectName(u"update_failed_frame")
        sizePolicy3.setHeightForWidth(self.update_failed_frame.sizePolicy().hasHeightForWidth())
        self.update_failed_frame.setSizePolicy(sizePolicy3)
        self.update_failed_frame.setStyleSheet(u"background: transparent")
        self.update_failed_frame.setFrameShape(QFrame.StyledPanel)
        self.update_failed_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.update_failed_frame)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.update_failed_frame)
        self.label_9.setObjectName(u"label_9")
        sizePolicy4.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy4)
        self.label_9.setStyleSheet(u"color: hsl(333, 100%, 50%); font-weight: bold")
        self.label_9.setWordWrap(True)

        self.verticalLayout_14.addWidget(self.label_9)

        self.artstation_link_label = QLabel(self.update_failed_frame)
        self.artstation_link_label.setObjectName(u"artstation_link_label")

        self.verticalLayout_14.addWidget(self.artstation_link_label, 0, Qt.AlignHCenter)

        self.fab_link_label = QLabel(self.update_failed_frame)
        self.fab_link_label.setObjectName(u"fab_link_label")

        self.verticalLayout_14.addWidget(self.fab_link_label, 0, Qt.AlignHCenter)


        self.verticalLayout_12.addWidget(self.update_failed_frame)


        self.verticalLayout_8.addWidget(self.new_version_frame)

        self.debug_frame = QFrame(self.start_frame)
        self.debug_frame.setObjectName(u"debug_frame")
        sizePolicy3.setHeightForWidth(self.debug_frame.sizePolicy().hasHeightForWidth())
        self.debug_frame.setSizePolicy(sizePolicy3)
        self.debug_frame.setMinimumSize(QSize(0, 0))
        self.debug_frame.setFrameShape(QFrame.NoFrame)
        self.verticalLayout = QVBoxLayout(self.debug_frame)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.label_3 = QLabel(self.debug_frame)
        self.label_3.setObjectName(u"label_3")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy7)

        self.verticalLayout.addWidget(self.label_3)

        self.debug_button = QPushButton(self.debug_frame)
        self.debug_button.setObjectName(u"debug_button")
        sizePolicy3.setHeightForWidth(self.debug_button.sizePolicy().hasHeightForWidth())
        self.debug_button.setSizePolicy(sizePolicy3)
        self.debug_button.setMinimumSize(QSize(0, 100))
        self.debug_button.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.debug_button)

        self.select_reference_vertices_button = QPushButton(self.debug_frame)
        self.select_reference_vertices_button.setObjectName(u"select_reference_vertices_button")
        self.select_reference_vertices_button.setMinimumSize(QSize(0, 40))
        self.select_reference_vertices_button.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout.addWidget(self.select_reference_vertices_button)

        self.import_dna_button = QPushButton(self.debug_frame)
        self.import_dna_button.setObjectName(u"import_dna_button")
        self.import_dna_button.setMinimumSize(QSize(0, 40))
        self.import_dna_button.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout.addWidget(self.import_dna_button)

        self.frame_5 = QFrame(self.debug_frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.joints_button = QPushButton(self.frame_5)
        self.joints_button.setObjectName(u"joints_button")
        self.joints_button.setMinimumSize(QSize(0, 40))
        self.joints_button.setMaximumSize(QSize(16777215, 40))
        self.joints_button.setStyleSheet(u"/*-----QPushButton-----*/\n"
"QPushButton\n"
"{\n"
"	background-color: hsv(187, 100%, 50%);\n"
"	color: hsv(0, 0, 50%);\n"
"	font-weight: bold;\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 hsv(187, 100%, 50%),stop:1 hsv(180, 100%, 70%));\n"
"}\n"
"QPushButton::pressed\n"
"{\n"
"	background-color: hsv(180, 100%, 100%);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton::checked\n"
"{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: hsv(180, 100%, 90%);\n"
"}\n"
"QPushButton::checked::hover\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 hsv(180, 100%, 90%),stop:1 hsv(180, 100%, 100%));\n"
"}\n"
"QPushButton::checked::pressed\n"
"{\n"
"	background-color: hsv(180, 100%, 100%);\n"
"}")
        self.joints_button.setCheckable(True)
        self.joints_button.setChecked(False)

        self.horizontalLayout_8.addWidget(self.joints_button)

        self.skinweights_button = QPushButton(self.frame_5)
        self.skinweights_button.setObjectName(u"skinweights_button")
        self.skinweights_button.setMinimumSize(QSize(0, 40))
        self.skinweights_button.setMaximumSize(QSize(16777215, 40))
        self.skinweights_button.setStyleSheet(u"/*-----QPushButton-----*/\n"
"QPushButton\n"
"{\n"
"	background-color: hsv(187, 100%, 50%);\n"
"	color: hsv(0, 0, 50%);\n"
"	font-weight: bold;\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 hsv(187, 100%, 50%),stop:1 hsv(180, 100%, 70%));\n"
"}\n"
"QPushButton::pressed\n"
"{\n"
"	background-color: hsv(180, 100%, 100%);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton::checked\n"
"{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: hsv(180, 100%, 90%);\n"
"}\n"
"QPushButton::checked::hover\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 hsv(180, 100%, 90%),stop:1 hsv(180, 100%, 100%));\n"
"}\n"
"QPushButton::checked::pressed\n"
"{\n"
"	background-color: hsv(180, 100%, 100%);\n"
"}")
        self.skinweights_button.setCheckable(True)
        self.skinweights_button.setChecked(False)

        self.horizontalLayout_8.addWidget(self.skinweights_button)

        self.riglogic_button = QPushButton(self.frame_5)
        self.riglogic_button.setObjectName(u"riglogic_button")
        self.riglogic_button.setMinimumSize(QSize(0, 40))
        self.riglogic_button.setMaximumSize(QSize(16777215, 40))
        self.riglogic_button.setStyleSheet(u"/*-----QPushButton-----*/\n"
"QPushButton\n"
"{\n"
"	background-color: hsv(187, 100%, 50%);\n"
"	color: hsv(0, 0, 50%);\n"
"	font-weight: bold;\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 hsv(187, 100%, 50%),stop:1 hsv(180, 100%, 70%));\n"
"}\n"
"QPushButton::pressed\n"
"{\n"
"	background-color: hsv(180, 100%, 100%);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton::checked\n"
"{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: hsv(180, 100%, 90%);\n"
"}\n"
"QPushButton::checked::hover\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 hsv(180, 100%, 90%),stop:1 hsv(180, 100%, 100%));\n"
"}\n"
"QPushButton::checked::pressed\n"
"{\n"
"	background-color: hsv(180, 100%, 100%);\n"
"}")
        self.riglogic_button.setCheckable(True)
        self.riglogic_button.setChecked(False)

        self.horizontalLayout_8.addWidget(self.riglogic_button)


        self.verticalLayout.addWidget(self.frame_5)


        self.verticalLayout_8.addWidget(self.debug_frame)


        self.horizontalLayout_2.addWidget(self.start_frame)

        self.modes_frame = QFrame(self.centralwidget)
        self.modes_frame.setObjectName(u"modes_frame")
        sizePolicy1.setHeightForWidth(self.modes_frame.sizePolicy().hasHeightForWidth())
        self.modes_frame.setSizePolicy(sizePolicy1)
        self.modes_frame.setStyleSheet(u"#modes_frame {background: transparent}")
        self.modes_frame.setFrameShape(QFrame.StyledPanel)
        self.modes_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.modes_frame)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.back_frame = QFrame(self.modes_frame)
        self.back_frame.setObjectName(u"back_frame")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.back_frame.sizePolicy().hasHeightForWidth())
        self.back_frame.setSizePolicy(sizePolicy8)
        self.back_frame.setMinimumSize(QSize(350, 0))
        self.back_frame.setMaximumSize(QSize(16777215, 40))
        self.back_frame.setFrameShape(QFrame.StyledPanel)
        self.back_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.back_frame)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.back_button = QPushButton(self.back_frame)
        self.back_button.setObjectName(u"back_button")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.back_button.sizePolicy().hasHeightForWidth())
        self.back_button.setSizePolicy(sizePolicy9)
        self.back_button.setMinimumSize(QSize(30, 30))
        self.back_button.setMaximumSize(QSize(30, 30))
        self.back_button.setStyleSheet(u"font-size: 24px; padding-bottom: 9px; padding-right: 6px; ")

        self.horizontalLayout.addWidget(self.back_button)

        self.horizontalSpacer = QSpacerItem(30, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.mode_label = QLabel(self.back_frame)
        self.mode_label.setObjectName(u"mode_label")
        self.mode_label.setStyleSheet(u"font-size: 16px; color: white; font-weight: bold;")

        self.horizontalLayout.addWidget(self.mode_label, 0, Qt.AlignHCenter)

        self.horizontalSpacer_2 = QSpacerItem(50, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addWidget(self.back_frame)

        self.select_metahuman_frame = QFrame(self.modes_frame)
        self.select_metahuman_frame.setObjectName(u"select_metahuman_frame")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.select_metahuman_frame.sizePolicy().hasHeightForWidth())
        self.select_metahuman_frame.setSizePolicy(sizePolicy10)
        self.select_metahuman_frame.setFrameShape(QFrame.StyledPanel)
        self.select_metahuman_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.select_metahuman_frame)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.label = QLabel(self.select_metahuman_frame)
        self.label.setObjectName(u"label")
        sizePolicy4.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy4)
        self.label.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.label)

        self.metahuman_folder_button = QPushButton(self.select_metahuman_frame)
        self.metahuman_folder_button.setObjectName(u"metahuman_folder_button")
        sizePolicy4.setHeightForWidth(self.metahuman_folder_button.sizePolicy().hasHeightForWidth())
        self.metahuman_folder_button.setSizePolicy(sizePolicy4)
        self.metahuman_folder_button.setMinimumSize(QSize(0, 40))
        self.metahuman_folder_button.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_3.addWidget(self.metahuman_folder_button)


        self.verticalLayout_2.addWidget(self.select_metahuman_frame)

        self.new_geometry_frame = QFrame(self.modes_frame)
        self.new_geometry_frame.setObjectName(u"new_geometry_frame")
        sizePolicy6.setHeightForWidth(self.new_geometry_frame.sizePolicy().hasHeightForWidth())
        self.new_geometry_frame.setSizePolicy(sizePolicy6)
        self.new_geometry_frame.setMinimumSize(QSize(0, 0))
        self.new_geometry_frame.setFrameShape(QFrame.StyledPanel)
        self.new_geometry_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.new_geometry_frame)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.label_2 = QLabel(self.new_geometry_frame)
        self.label_2.setObjectName(u"label_2")
        sizePolicy4.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy4)
        self.label_2.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.label_2)

        self.frame = QFrame(self.new_geometry_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setSpacing(2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.combined_button = QPushButton(self.frame)
        self.combined_button.setObjectName(u"combined_button")
        sizePolicy11 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.combined_button.sizePolicy().hasHeightForWidth())
        self.combined_button.setSizePolicy(sizePolicy11)
        self.combined_button.setMinimumSize(QSize(0, 40))
        self.combined_button.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_4.addWidget(self.combined_button)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setMinimumSize(QSize(80, 40))
        self.pushButton_2.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_4.addWidget(self.pushButton_2)


        self.verticalLayout_4.addWidget(self.frame)

        self.frame_2 = QFrame(self.new_geometry_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setSpacing(2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.eyes_button = QPushButton(self.frame_2)
        self.eyes_button.setObjectName(u"eyes_button")
        sizePolicy11.setHeightForWidth(self.eyes_button.sizePolicy().hasHeightForWidth())
        self.eyes_button.setSizePolicy(sizePolicy11)
        self.eyes_button.setMinimumSize(QSize(0, 40))
        self.eyes_button.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_5.addWidget(self.eyes_button)

        self.pushButton_4 = QPushButton(self.frame_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setEnabled(False)
        self.pushButton_4.setMinimumSize(QSize(80, 40))
        self.pushButton_4.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_5.addWidget(self.pushButton_4)


        self.verticalLayout_4.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.new_geometry_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setSpacing(2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.eyelashes_button = QPushButton(self.frame_3)
        self.eyelashes_button.setObjectName(u"eyelashes_button")
        self.eyelashes_button.setEnabled(False)
        sizePolicy11.setHeightForWidth(self.eyelashes_button.sizePolicy().hasHeightForWidth())
        self.eyelashes_button.setSizePolicy(sizePolicy11)
        self.eyelashes_button.setMinimumSize(QSize(0, 40))
        self.eyelashes_button.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_6.addWidget(self.eyelashes_button)

        self.eyelashes_autogenerated_button = QPushButton(self.frame_3)
        self.eyelashes_autogenerated_button.setObjectName(u"eyelashes_autogenerated_button")
        sizePolicy2.setHeightForWidth(self.eyelashes_autogenerated_button.sizePolicy().hasHeightForWidth())
        self.eyelashes_autogenerated_button.setSizePolicy(sizePolicy2)
        self.eyelashes_autogenerated_button.setMinimumSize(QSize(80, 40))
        self.eyelashes_autogenerated_button.setMaximumSize(QSize(16777215, 40))
        self.eyelashes_autogenerated_button.setStyleSheet(u"font-size: 10px")

        self.horizontalLayout_6.addWidget(self.eyelashes_autogenerated_button)


        self.verticalLayout_4.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.new_geometry_frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_7.setSpacing(2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.teeth_button = QPushButton(self.frame_4)
        self.teeth_button.setObjectName(u"teeth_button")
        self.teeth_button.setEnabled(False)
        sizePolicy11.setHeightForWidth(self.teeth_button.sizePolicy().hasHeightForWidth())
        self.teeth_button.setSizePolicy(sizePolicy11)
        self.teeth_button.setMinimumSize(QSize(0, 40))
        self.teeth_button.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_7.addWidget(self.teeth_button)

        self.teeth_autogenerated_button = QPushButton(self.frame_4)
        self.teeth_autogenerated_button.setObjectName(u"teeth_autogenerated_button")
        sizePolicy2.setHeightForWidth(self.teeth_autogenerated_button.sizePolicy().hasHeightForWidth())
        self.teeth_autogenerated_button.setSizePolicy(sizePolicy2)
        self.teeth_autogenerated_button.setMinimumSize(QSize(80, 40))
        self.teeth_autogenerated_button.setMaximumSize(QSize(16777215, 40))
        self.teeth_autogenerated_button.setStyleSheet(u"font-size: 10px")

        self.horizontalLayout_7.addWidget(self.teeth_autogenerated_button)


        self.verticalLayout_4.addWidget(self.frame_4)


        self.verticalLayout_2.addWidget(self.new_geometry_frame)

        self.symmetrize_frame = QFrame(self.modes_frame)
        self.symmetrize_frame.setObjectName(u"symmetrize_frame")
        sizePolicy10.setHeightForWidth(self.symmetrize_frame.sizePolicy().hasHeightForWidth())
        self.symmetrize_frame.setSizePolicy(sizePolicy10)
        self.symmetrize_frame.setStyleSheet(u"")
        self.symmetrize_frame.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_9 = QVBoxLayout(self.symmetrize_frame)
        self.verticalLayout_9.setSpacing(5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.label_6 = QLabel(self.symmetrize_frame)
        self.label_6.setObjectName(u"label_6")
        sizePolicy4.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy4)
        self.label_6.setWordWrap(True)

        self.verticalLayout_9.addWidget(self.label_6)

        self.symmetrize_frame2 = QFrame(self.symmetrize_frame)
        self.symmetrize_frame2.setObjectName(u"symmetrize_frame2")
        self.symmetrize_frame2.setStyleSheet(u"#symmetrize_frame2 {background: transparent}")
        self.symmetrize_frame2.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_3 = QHBoxLayout(self.symmetrize_frame2)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.symmetrize_button = QPushButton(self.symmetrize_frame2)
        self.symmetrize_button.setObjectName(u"symmetrize_button")
        sizePolicy12 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.symmetrize_button.sizePolicy().hasHeightForWidth())
        self.symmetrize_button.setSizePolicy(sizePolicy12)
        self.symmetrize_button.setMinimumSize(QSize(145, 40))
        self.symmetrize_button.setMaximumSize(QSize(16777215, 40))
        self.symmetrize_button.setStyleSheet(u"/*-----QPushButton-----*/\n"
"QPushButton\n"
"{\n"
"	background-color: hsv(187, 100%, 50%);\n"
"	color: hsv(0, 0, 50%);\n"
"	font-weight: bold;\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 hsv(187, 100%, 50%),stop:1 hsv(180, 100%, 70%));\n"
"}\n"
"QPushButton::pressed\n"
"{\n"
"	background-color: hsv(180, 100%, 100%);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton::checked\n"
"{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: hsv(180, 100%, 90%);\n"
"}\n"
"QPushButton::checked::hover\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 hsv(180, 100%, 90%),stop:1 hsv(180, 100%, 100%));\n"
"}\n"
"QPushButton::checked::pressed\n"
"{\n"
"	background-color: hsv(180, 100%, 100%);\n"
"}")
        self.symmetrize_button.setCheckable(True)
        self.symmetrize_button.setChecked(True)

        self.horizontalLayout_3.addWidget(self.symmetrize_button)

        self.original_button = QPushButton(self.symmetrize_frame2)
        self.original_button.setObjectName(u"original_button")
        sizePolicy12.setHeightForWidth(self.original_button.sizePolicy().hasHeightForWidth())
        self.original_button.setSizePolicy(sizePolicy12)
        self.original_button.setMinimumSize(QSize(145, 40))
        self.original_button.setMaximumSize(QSize(16777215, 40))
        self.original_button.setStyleSheet(u"/*-----QPushButton-----*/\n"
"QPushButton\n"
"{\n"
"	background-color: hsv(187, 100%, 50%);\n"
"	color: hsv(0, 0, 50%);\n"
"	font-weight: bold;\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 hsv(187, 100%, 50%),stop:1 hsv(180, 100%, 70%));\n"
"}\n"
"QPushButton::pressed\n"
"{\n"
"	background-color: hsv(180, 100%, 100%);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton::checked\n"
"{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: hsv(180, 100%, 90%);\n"
"}\n"
"QPushButton::checked::hover\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 hsv(180, 100%, 90%),stop:1 hsv(180, 100%, 100%));\n"
"}\n"
"QPushButton::checked::pressed\n"
"{\n"
"	background-color: hsv(180, 100%, 100%);\n"
"}")
        self.original_button.setCheckable(True)
        self.original_button.setChecked(False)

        self.horizontalLayout_3.addWidget(self.original_button)


        self.verticalLayout_9.addWidget(self.symmetrize_frame2)


        self.verticalLayout_2.addWidget(self.symmetrize_frame)

        self.run_frame = QFrame(self.modes_frame)
        self.run_frame.setObjectName(u"run_frame")
        self.run_frame.setFrameShape(QFrame.StyledPanel)
        self.run_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.run_frame)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(5, 5, 5, 5)
        self.metahuman_to_obj_run_button = QPushButton(self.run_frame)
        self.metahuman_to_obj_run_button.setObjectName(u"metahuman_to_obj_run_button")
        self.metahuman_to_obj_run_button.setEnabled(False)
        self.metahuman_to_obj_run_button.setMinimumSize(QSize(0, 100))
        self.metahuman_to_obj_run_button.setStyleSheet(u"")

        self.verticalLayout_7.addWidget(self.metahuman_to_obj_run_button)

        self.obj_to_metahuman_run_button = QPushButton(self.run_frame)
        self.obj_to_metahuman_run_button.setObjectName(u"obj_to_metahuman_run_button")
        self.obj_to_metahuman_run_button.setEnabled(False)
        self.obj_to_metahuman_run_button.setMinimumSize(QSize(0, 100))
        self.obj_to_metahuman_run_button.setStyleSheet(u"")

        self.verticalLayout_7.addWidget(self.obj_to_metahuman_run_button)


        self.verticalLayout_2.addWidget(self.run_frame)


        self.horizontalLayout_2.addWidget(self.modes_frame)

        self.running_frame = QFrame(self.centralwidget)
        self.running_frame.setObjectName(u"running_frame")
        sizePolicy.setHeightForWidth(self.running_frame.sizePolicy().hasHeightForWidth())
        self.running_frame.setSizePolicy(sizePolicy)
        self.running_frame.setMinimumSize(QSize(480, 0))
        self.running_frame.setStyleSheet(u"#running_frame {background: transparent}")
        self.running_frame.setFrameShape(QFrame.StyledPanel)
        self.running_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.running_frame)
        self.verticalLayout_10.setSpacing(5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(5, 5, 5, 5)
        self.frame_6 = QFrame(self.running_frame)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy13 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)
        sizePolicy13.setHorizontalStretch(0)
        sizePolicy13.setVerticalStretch(0)
        sizePolicy13.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy13)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_6)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(5, 5, 5, 5)
        self.metahuman_to_obj_info_frame = QFrame(self.frame_6)
        self.metahuman_to_obj_info_frame.setObjectName(u"metahuman_to_obj_info_frame")
        sizePolicy.setHeightForWidth(self.metahuman_to_obj_info_frame.sizePolicy().hasHeightForWidth())
        self.metahuman_to_obj_info_frame.setSizePolicy(sizePolicy)
        self.metahuman_to_obj_info_frame.setStyleSheet(u"background: transparent")
        self.metahuman_to_obj_info_frame.setFrameShape(QFrame.StyledPanel)
        self.metahuman_to_obj_info_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.metahuman_to_obj_info_frame)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.metahuman_to_obj_info_frame)
        self.label_12.setObjectName(u"label_12")
        sizePolicy6.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy6)
        self.label_12.setMinimumSize(QSize(460, 0))
        self.label_12.setStyleSheet(u"background: transparent")
        self.label_12.setWordWrap(True)

        self.verticalLayout_16.addWidget(self.label_12)


        self.verticalLayout_11.addWidget(self.metahuman_to_obj_info_frame)

        self.obj_to_metahuman_info_frame = QFrame(self.frame_6)
        self.obj_to_metahuman_info_frame.setObjectName(u"obj_to_metahuman_info_frame")
        sizePolicy14 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Ignored)
        sizePolicy14.setHorizontalStretch(0)
        sizePolicy14.setVerticalStretch(0)
        sizePolicy14.setHeightForWidth(self.obj_to_metahuman_info_frame.sizePolicy().hasHeightForWidth())
        self.obj_to_metahuman_info_frame.setSizePolicy(sizePolicy14)
        self.obj_to_metahuman_info_frame.setStyleSheet(u"#obj_to_metahuman_info_frame {background: transparent}")
        self.obj_to_metahuman_info_frame.setFrameShape(QFrame.StyledPanel)
        self.obj_to_metahuman_info_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.obj_to_metahuman_info_frame)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.obj_to_metahuman_info_frame)
        self.label_11.setObjectName(u"label_11")
        sizePolicy6.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy6)
        self.label_11.setMinimumSize(QSize(460, 0))
        self.label_11.setWordWrap(True)

        self.verticalLayout_17.addWidget(self.label_11)

        self.dna_options_body_label = QLabel(self.obj_to_metahuman_info_frame)
        self.dna_options_body_label.setObjectName(u"dna_options_body_label")
        sizePolicy.setHeightForWidth(self.dna_options_body_label.sizePolicy().hasHeightForWidth())
        self.dna_options_body_label.setSizePolicy(sizePolicy)
        self.dna_options_body_label.setStyleSheet(u"background: green")

        self.verticalLayout_17.addWidget(self.dna_options_body_label)

        self.label_13 = QLabel(self.obj_to_metahuman_info_frame)
        self.label_13.setObjectName(u"label_13")
        sizePolicy6.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy6)
        self.label_13.setMouseTracking(True)
        self.label_13.setWordWrap(True)

        self.verticalLayout_17.addWidget(self.label_13)

        self.dna_options_head_label = QLabel(self.obj_to_metahuman_info_frame)
        self.dna_options_head_label.setObjectName(u"dna_options_head_label")
        sizePolicy.setHeightForWidth(self.dna_options_head_label.sizePolicy().hasHeightForWidth())
        self.dna_options_head_label.setSizePolicy(sizePolicy)
        self.dna_options_head_label.setStyleSheet(u"background: green")

        self.verticalLayout_17.addWidget(self.dna_options_head_label)

        self.label_14 = QLabel(self.obj_to_metahuman_info_frame)
        self.label_14.setObjectName(u"label_14")
        sizePolicy6.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy6)
        self.label_14.setWordWrap(True)

        self.verticalLayout_17.addWidget(self.label_14)


        self.verticalLayout_11.addWidget(self.obj_to_metahuman_info_frame)

        self.running_progress_bar = QProgressBar(self.frame_6)
        self.running_progress_bar.setObjectName(u"running_progress_bar")
        sizePolicy5.setHeightForWidth(self.running_progress_bar.sizePolicy().hasHeightForWidth())
        self.running_progress_bar.setSizePolicy(sizePolicy5)
        self.running_progress_bar.setMinimumSize(QSize(0, 40))
        self.running_progress_bar.setMaximumSize(QSize(16777215, 40))
        self.running_progress_bar.setStyleSheet(u"")
        self.running_progress_bar.setValue(1)
        self.running_progress_bar.setAlignment(Qt.AlignCenter)
        self.running_progress_bar.setTextVisible(True)
        self.running_progress_bar.setInvertedAppearance(False)
        self.running_progress_bar.setTextDirection(QProgressBar.TopToBottom)

        self.verticalLayout_11.addWidget(self.running_progress_bar)

        self.go_to_metahuman_folder_button = QPushButton(self.frame_6)
        self.go_to_metahuman_folder_button.setObjectName(u"go_to_metahuman_folder_button")
        sizePolicy15 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy15.setHorizontalStretch(0)
        sizePolicy15.setVerticalStretch(0)
        sizePolicy15.setHeightForWidth(self.go_to_metahuman_folder_button.sizePolicy().hasHeightForWidth())
        self.go_to_metahuman_folder_button.setSizePolicy(sizePolicy15)
        self.go_to_metahuman_folder_button.setMinimumSize(QSize(0, 40))
        self.go_to_metahuman_folder_button.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_11.addWidget(self.go_to_metahuman_folder_button)

        self.done_label = QLabel(self.frame_6)
        self.done_label.setObjectName(u"done_label")
        sizePolicy16 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Maximum)
        sizePolicy16.setHorizontalStretch(0)
        sizePolicy16.setVerticalStretch(0)
        sizePolicy16.setHeightForWidth(self.done_label.sizePolicy().hasHeightForWidth())
        self.done_label.setSizePolicy(sizePolicy16)
        self.done_label.setStyleSheet(u"color: hsl(177, 100%, 50%); font-weight: bold")
        self.done_label.setAlignment(Qt.AlignCenter)
        self.done_label.setWordWrap(True)

        self.verticalLayout_11.addWidget(self.done_label)


        self.verticalLayout_10.addWidget(self.frame_6)


        self.horizontalLayout_2.addWidget(self.running_frame)

        self.edit_bs_frame = QFrame(self.centralwidget)
        self.edit_bs_frame.setObjectName(u"edit_bs_frame")
        sizePolicy.setHeightForWidth(self.edit_bs_frame.sizePolicy().hasHeightForWidth())
        self.edit_bs_frame.setSizePolicy(sizePolicy)
        self.edit_bs_frame.setStyleSheet(u"#edit_bs_frame {background: transparent}")
        self.edit_bs_frame.setFrameShape(QFrame.StyledPanel)
        self.edit_bs_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.edit_bs_frame)
        self.verticalLayout_20.setSpacing(5)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(5, 5, 5, 5)
        self.edit_bs_frame_inner = QFrame(self.edit_bs_frame)
        self.edit_bs_frame_inner.setObjectName(u"edit_bs_frame_inner")
        sizePolicy15.setHeightForWidth(self.edit_bs_frame_inner.sizePolicy().hasHeightForWidth())
        self.edit_bs_frame_inner.setSizePolicy(sizePolicy15)
        self.edit_bs_frame_inner.setMinimumSize(QSize(400, 0))
        self.edit_bs_frame_inner.setMaximumSize(QSize(400, 16777215))
        self.edit_bs_frame_inner.setFrameShape(QFrame.StyledPanel)
        self.edit_bs_frame_inner.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.edit_bs_frame_inner)
        self.verticalLayout_18.setSpacing(5)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(5, 50, 5, 50)
        self.scrollArea = QScrollArea(self.edit_bs_frame_inner)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(0, 100))
        self.scrollArea.setMaximumSize(QSize(16777215, 100))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 390, 100))
        self.verticalLayout_19 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_19.setSpacing(5)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(5, 5, 5, 5)
        self.pushButton = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_19.addWidget(self.pushButton)

        self.pushButton_3 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_19.addWidget(self.pushButton_3)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_18.addWidget(self.scrollArea)

        self.animation_frame = QFrame(self.edit_bs_frame_inner)
        self.animation_frame.setObjectName(u"animation_frame")
        sizePolicy6.setHeightForWidth(self.animation_frame.sizePolicy().hasHeightForWidth())
        self.animation_frame.setSizePolicy(sizePolicy6)
        self.animation_frame.setFrameShape(QFrame.StyledPanel)
        self.animation_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.animation_frame)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.animation_button = QPushButton(self.animation_frame)
        self.animation_button.setObjectName(u"animation_button")

        self.horizontalLayout_9.addWidget(self.animation_button)

        self.animation_label = QLabel(self.animation_frame)
        self.animation_label.setObjectName(u"animation_label")

        self.horizontalLayout_9.addWidget(self.animation_label)


        self.verticalLayout_18.addWidget(self.animation_frame)


        self.verticalLayout_20.addWidget(self.edit_bs_frame_inner)


        self.horizontalLayout_2.addWidget(self.edit_bs_frame)

        METMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(METMainWindow)

        QMetaObject.connectSlotsByName(METMainWindow)
    # setupUi

    def retranslateUi(self, METMainWindow):
        METMainWindow.setWindowTitle(QCoreApplication.translate("METMainWindow", u"Metahuman Extra Tools", None))
        self.label_8.setText(QCoreApplication.translate("METMainWindow", u"Minimum Maya version required is 2023.3", None))
        self.label_4.setText(QCoreApplication.translate("METMainWindow", u"Export a MetaHuman to .obj files and edit it's geometry with any application", None))
        self.metahuman_to_obj_button.setText(QCoreApplication.translate("METMainWindow", u"MetaHuman to .OBJ", None))
        self.label_5.setText(QCoreApplication.translate("METMainWindow", u"Create new MetaHuman head and body DNA from .obj files", None))
        self.obj_to_metahuman_button.setText(QCoreApplication.translate("METMainWindow", u".OBJ to MetaHuman", None))
        self.label_10.setText(QCoreApplication.translate("METMainWindow", u"Come into the Discord server to ask anything and share your experience:", None))
        self.discord_label.setText(QCoreApplication.translate("METMainWindow", u"<a href='https://discord.gg/XdQN8WWV'>Discord</a>", None))
        self.label_7.setText(QCoreApplication.translate("METMainWindow", u"New version available:", None))
        self.changes_label.setText("")
        self.update_button.setText(QCoreApplication.translate("METMainWindow", u"Update", None))
        self.update_progress_bar.setFormat(QCoreApplication.translate("METMainWindow", u"Updating...", None))
        self.restart_met_button.setText(QCoreApplication.translate("METMainWindow", u"Restart MET to apply changes", None))
        self.updated_successfully_label.setText(QCoreApplication.translate("METMainWindow", u"Updated successfully", None))
        self.label_9.setText(QCoreApplication.translate("METMainWindow", u"Failed to check for updates. Please check for the latest version available at:", None))
        self.artstation_link_label.setText(QCoreApplication.translate("METMainWindow", u"<a href='https://www.artstation.com/marketplace/p/pR97n/metahuman-extra-tools'>ArtStation</a>", None))
        self.fab_link_label.setText(QCoreApplication.translate("METMainWindow", u"<a href='https://www.fab.com/listings/22f90398-c29e-4b74-a80a-9c5b5ae19d47'>Fab</a>", None))
        self.label_3.setText(QCoreApplication.translate("METMainWindow", u"Debug", None))
        self.debug_button.setText(QCoreApplication.translate("METMainWindow", u"Debug", None))
        self.select_reference_vertices_button.setText(QCoreApplication.translate("METMainWindow", u"select reference vertices", None))
        self.import_dna_button.setText(QCoreApplication.translate("METMainWindow", u"import dna", None))
        self.joints_button.setText(QCoreApplication.translate("METMainWindow", u"joints", None))
        self.skinweights_button.setText(QCoreApplication.translate("METMainWindow", u"skin weights", None))
        self.riglogic_button.setText(QCoreApplication.translate("METMainWindow", u"rig logic", None))
        self.back_button.setText(QCoreApplication.translate("METMainWindow", u"<", None))
        self.mode_label.setText(QCoreApplication.translate("METMainWindow", u"Mode", None))
        self.label.setText(QCoreApplication.translate("METMainWindow", u"Select the MetaHuman folder generated by MetaHuman Creator DCC Export (the folder that contains both head.dna and body.dna)", None))
        self.metahuman_folder_button.setText(QCoreApplication.translate("METMainWindow", u"MetaHuman folder", None))
        self.label_2.setText(QCoreApplication.translate("METMainWindow", u"Select your new combined and eyes meshes. You can also provide eyelashes and teeth or let them be auto-generated. These meshes need to have the same topology and vertex order as the ones generated by MetaHuman to .OBJ", None))
        self.combined_button.setText(QCoreApplication.translate("METMainWindow", u"combined", None))
        self.pushButton_2.setText(QCoreApplication.translate("METMainWindow", u"OBJ", None))
        self.eyes_button.setText(QCoreApplication.translate("METMainWindow", u"eyes", None))
        self.pushButton_4.setText(QCoreApplication.translate("METMainWindow", u"OBJ", None))
        self.eyelashes_button.setText(QCoreApplication.translate("METMainWindow", u"eyelashes", None))
        self.eyelashes_autogenerated_button.setText(QCoreApplication.translate("METMainWindow", u"auto generated", None))
        self.teeth_button.setText(QCoreApplication.translate("METMainWindow", u"teeth", None))
        self.teeth_autogenerated_button.setText(QCoreApplication.translate("METMainWindow", u"auto generated", None))
        self.label_6.setText(QCoreApplication.translate("METMainWindow", u"Symmetrize MetaHuman maintaining topology and vertex order or keep original asymmetry. Symmetrize is recommended for easier editing", None))
        self.symmetrize_button.setText(QCoreApplication.translate("METMainWindow", u"Symmetrize", None))
        self.original_button.setText(QCoreApplication.translate("METMainWindow", u"Keep Original", None))
        self.metahuman_to_obj_run_button.setText(QCoreApplication.translate("METMainWindow", u"Run", None))
        self.obj_to_metahuman_run_button.setText(QCoreApplication.translate("METMainWindow", u"Run", None))
        self.label_12.setText(QCoreApplication.translate("METMainWindow", u"<html><head/><body><p>Please keep in mind that you need to maintain topology, vertex order and mesh distribution on the generated meshes. If you disrupt these properties you will need to restore them by performing a wrapping process with tools like Faceform Wrap or similar. Even if you maintain topology and vertex order, wrapping is still recommended for optimal mesh distribution.</p><p>MetaHuman to .OBJ will generate, inside the MetaHuman folder, two extra folders with &quot;new&quot; and &quot;old&quot; OBJs. The recommended workflow is to edit the new OBJs and keep the old OBJs intact, as a representation of the original MetaHuman, in case you need them for reference or wrapping. You will also find inside the new OBJs folder a set of textures that you can use to check mesh distribution.</p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("METMainWindow", u"<html><head/><body><p>.OBJ to MetaHuman will generate an extra folder inside the MetaHuman folder with new DNA for your MetaHuman. You can use this new DNA to update your MetaHuman in MetaHuman Creator.</p><p>First, in MetaHuman Creator, you will need to remove the rig that was previously applied.</p><p>Then conform to the new body DNA: go to &quot;Body&quot; &gt; &quot;Conform&quot; &gt; &quot;Import DNA&quot;, select your new body DNA file, and import with the following options:</p></body></html>", None))
        self.dna_options_body_label.setText("")
        self.label_13.setText(QCoreApplication.translate("METMainWindow", u"<html><head/><body><p><br/>Next conform to the new head DNA: go to &quot;Head&quot; &gt; &quot;Conform&quot; &gt; &quot;Import DNA&quot;, select your new head DNA file, and import with the following options:</p></body></html>", None))
        self.dna_options_head_label.setText("")
        self.label_14.setText(QCoreApplication.translate("METMainWindow", u"<html><head/><body><p><br/>Finally, create either &quot;Full Rig&quot; or &quot;Joints Only Rig&quot;. The difference between the two is that Full Rig enables the corrective Blend Shapes.</p><p>Once the rig is created you can check your updated MetaHuman using the template animations in the preview panel. Please be aware that the BodyROM animation has some problems with the fingers that are very visible around frame 180. This is an issue of the animation itself, you can see this behaviour even on the Preset MetaHumans.</p></body></html>", None))
        self.running_progress_bar.setFormat(QCoreApplication.translate("METMainWindow", u"Running...", None))
        self.go_to_metahuman_folder_button.setText(QCoreApplication.translate("METMainWindow", u"Go to MetaHuman folder", None))
        self.done_label.setText(QCoreApplication.translate("METMainWindow", u"Done!", None))
        self.pushButton.setText(QCoreApplication.translate("METMainWindow", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("METMainWindow", u"PushButton", None))
        self.animation_button.setText(QCoreApplication.translate("METMainWindow", u"Facial Animation", None))
        self.animation_label.setText(QCoreApplication.translate("METMainWindow", u"...", None))
    # retranslateUi

