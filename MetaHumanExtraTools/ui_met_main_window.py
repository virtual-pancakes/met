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
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_METMainWindow(object):
    def setupUi(self, METMainWindow):
        if not METMainWindow.objectName():
            METMainWindow.setObjectName(u"METMainWindow")
        METMainWindow.resize(1089, 605)
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
"\n"
""
                        "\n"
"}\n"
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
"\n"
"/*-----QCheckBox-----*/\n"
"QCheckBox\n"
"{\n"
"	background-color: transparent;\n"
"	color: #fff;\n"
"	font-size: 10px;\n"
"	font-weight: bold;\n"
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
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.511, x2:1, y2:0.511, stop:0"
                        " rgba(0, 172, 149, 255),stop:0.995192 rgba(54, 197, 177, 255));;\n"
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
"	font-weight: bold;\n"
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
"	color: #3"
                        "1cecb;\n"
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
"	padding-left : 10px;\n"
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
"	background-"
                        "color: #0ab19a;\n"
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
"    color: #"
                        "f0f0f0;\n"
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
""
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
"/*-----QScrollBar-----*/\n"
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
"    wid"
                        "th: 0px;\n"
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
"}\n"
"")
        self.centralwidget = QWidget(METMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.centralwidget.setStyleSheet(u"#centralwidget {background: white}")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.start_frame = QFrame(self.centralwidget)
        self.start_frame.setObjectName(u"start_frame")
        sizePolicy.setHeightForWidth(self.start_frame.sizePolicy().hasHeightForWidth())
        self.start_frame.setSizePolicy(sizePolicy)
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
        self.frame2 = QFrame(self.start_frame)
        self.frame2.setObjectName(u"frame2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame2.sizePolicy().hasHeightForWidth())
        self.frame2.setSizePolicy(sizePolicy2)
        self.frame2.setMinimumSize(QSize(0, 0))
        self.frame2.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_5 = QVBoxLayout(self.frame2)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.label_4 = QLabel(self.frame2)
        self.label_4.setObjectName(u"label_4")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy3)
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
        sizePolicy2.setHeightForWidth(self.metahuman_to_obj_button.sizePolicy().hasHeightForWidth())
        self.metahuman_to_obj_button.setSizePolicy(sizePolicy2)
        self.metahuman_to_obj_button.setMinimumSize(QSize(0, 100))
        self.metahuman_to_obj_button.setMaximumSize(QSize(16777215, 100))
        font1 = QFont()
        font1.setBold(True)
        self.metahuman_to_obj_button.setFont(font1)

        self.verticalLayout_5.addWidget(self.metahuman_to_obj_button)


        self.verticalLayout_8.addWidget(self.frame2)

        self.frame1 = QFrame(self.start_frame)
        self.frame1.setObjectName(u"frame1")
        sizePolicy2.setHeightForWidth(self.frame1.sizePolicy().hasHeightForWidth())
        self.frame1.setSizePolicy(sizePolicy2)
        self.frame1.setMinimumSize(QSize(0, 0))
        self.frame1.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_6 = QVBoxLayout(self.frame1)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.label_5 = QLabel(self.frame1)
        self.label_5.setObjectName(u"label_5")
        sizePolicy3.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy3)
        self.label_5.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.label_5)

        self.obj_to_metahuman_button = QPushButton(self.frame1)
        self.obj_to_metahuman_button.setObjectName(u"obj_to_metahuman_button")
        sizePolicy2.setHeightForWidth(self.obj_to_metahuman_button.sizePolicy().hasHeightForWidth())
        self.obj_to_metahuman_button.setSizePolicy(sizePolicy2)
        self.obj_to_metahuman_button.setMinimumSize(QSize(0, 100))
        self.obj_to_metahuman_button.setMaximumSize(QSize(16777215, 100))

        self.verticalLayout_6.addWidget(self.obj_to_metahuman_button)


        self.verticalLayout_8.addWidget(self.frame1)

        self.debug_frame = QFrame(self.start_frame)
        self.debug_frame.setObjectName(u"debug_frame")
        sizePolicy2.setHeightForWidth(self.debug_frame.sizePolicy().hasHeightForWidth())
        self.debug_frame.setSizePolicy(sizePolicy2)
        self.debug_frame.setMinimumSize(QSize(0, 0))
        self.debug_frame.setFrameShape(QFrame.NoFrame)
        self.verticalLayout = QVBoxLayout(self.debug_frame)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.label_3 = QLabel(self.debug_frame)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.debug_button = QPushButton(self.debug_frame)
        self.debug_button.setObjectName(u"debug_button")
        sizePolicy2.setHeightForWidth(self.debug_button.sizePolicy().hasHeightForWidth())
        self.debug_button.setSizePolicy(sizePolicy2)
        self.debug_button.setMinimumSize(QSize(0, 100))

        self.verticalLayout.addWidget(self.debug_button)

        self.import_dna_button = QPushButton(self.debug_frame)
        self.import_dna_button.setObjectName(u"import_dna_button")

        self.verticalLayout.addWidget(self.import_dna_button)


        self.verticalLayout_8.addWidget(self.debug_frame)


        self.horizontalLayout_2.addWidget(self.start_frame)

        self.modes_frame = QFrame(self.centralwidget)
        self.modes_frame.setObjectName(u"modes_frame")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.modes_frame.sizePolicy().hasHeightForWidth())
        self.modes_frame.setSizePolicy(sizePolicy4)
        self.modes_frame.setStyleSheet(u"#modes_frame {background: transparent}")
        self.modes_frame.setFrameShape(QFrame.StyledPanel)
        self.modes_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.modes_frame)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.back_frame = QFrame(self.modes_frame)
        self.back_frame.setObjectName(u"back_frame")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.back_frame.sizePolicy().hasHeightForWidth())
        self.back_frame.setSizePolicy(sizePolicy5)
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
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.back_button.sizePolicy().hasHeightForWidth())
        self.back_button.setSizePolicy(sizePolicy6)
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

        self.new_geometry_frame = QFrame(self.modes_frame)
        self.new_geometry_frame.setObjectName(u"new_geometry_frame")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.new_geometry_frame.sizePolicy().hasHeightForWidth())
        self.new_geometry_frame.setSizePolicy(sizePolicy7)
        self.new_geometry_frame.setMinimumSize(QSize(0, 0))
        self.new_geometry_frame.setFrameShape(QFrame.StyledPanel)
        self.new_geometry_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.new_geometry_frame)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.label_2 = QLabel(self.new_geometry_frame)
        self.label_2.setObjectName(u"label_2")
        sizePolicy6.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy6)

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
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.combined_button.sizePolicy().hasHeightForWidth())
        self.combined_button.setSizePolicy(sizePolicy8)
        self.combined_button.setMinimumSize(QSize(0, 31))

        self.horizontalLayout_4.addWidget(self.combined_button)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setMinimumSize(QSize(80, 0))

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
        sizePolicy8.setHeightForWidth(self.eyes_button.sizePolicy().hasHeightForWidth())
        self.eyes_button.setSizePolicy(sizePolicy8)
        self.eyes_button.setMinimumSize(QSize(0, 31))

        self.horizontalLayout_5.addWidget(self.eyes_button)

        self.pushButton_4 = QPushButton(self.frame_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setEnabled(False)
        self.pushButton_4.setMinimumSize(QSize(80, 0))

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
        sizePolicy8.setHeightForWidth(self.eyelashes_button.sizePolicy().hasHeightForWidth())
        self.eyelashes_button.setSizePolicy(sizePolicy8)
        self.eyelashes_button.setMinimumSize(QSize(0, 31))

        self.horizontalLayout_6.addWidget(self.eyelashes_button)

        self.eyelashes_autogenerated_button = QPushButton(self.frame_3)
        self.eyelashes_autogenerated_button.setObjectName(u"eyelashes_autogenerated_button")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.eyelashes_autogenerated_button.sizePolicy().hasHeightForWidth())
        self.eyelashes_autogenerated_button.setSizePolicy(sizePolicy9)
        self.eyelashes_autogenerated_button.setMinimumSize(QSize(80, 0))
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
        sizePolicy8.setHeightForWidth(self.teeth_button.sizePolicy().hasHeightForWidth())
        self.teeth_button.setSizePolicy(sizePolicy8)
        self.teeth_button.setMinimumSize(QSize(0, 31))

        self.horizontalLayout_7.addWidget(self.teeth_button)

        self.teeth_autogenerated_button = QPushButton(self.frame_4)
        self.teeth_autogenerated_button.setObjectName(u"teeth_autogenerated_button")
        sizePolicy9.setHeightForWidth(self.teeth_autogenerated_button.sizePolicy().hasHeightForWidth())
        self.teeth_autogenerated_button.setSizePolicy(sizePolicy9)
        self.teeth_autogenerated_button.setMinimumSize(QSize(80, 0))
        self.teeth_autogenerated_button.setStyleSheet(u"font-size: 10px")

        self.horizontalLayout_7.addWidget(self.teeth_autogenerated_button)


        self.verticalLayout_4.addWidget(self.frame_4)


        self.verticalLayout_2.addWidget(self.new_geometry_frame)

        self.select_metahuman_frame = QFrame(self.modes_frame)
        self.select_metahuman_frame.setObjectName(u"select_metahuman_frame")
        sizePolicy7.setHeightForWidth(self.select_metahuman_frame.sizePolicy().hasHeightForWidth())
        self.select_metahuman_frame.setSizePolicy(sizePolicy7)
        self.select_metahuman_frame.setFrameShape(QFrame.StyledPanel)
        self.select_metahuman_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.select_metahuman_frame)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.label = QLabel(self.select_metahuman_frame)
        self.label.setObjectName(u"label")
        self.label.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.label)

        self.metahuman_folder_button = QPushButton(self.select_metahuman_frame)
        self.metahuman_folder_button.setObjectName(u"metahuman_folder_button")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.metahuman_folder_button.sizePolicy().hasHeightForWidth())
        self.metahuman_folder_button.setSizePolicy(sizePolicy10)
        self.metahuman_folder_button.setMinimumSize(QSize(0, 37))
        self.metahuman_folder_button.setMaximumSize(QSize(16777215, 37))

        self.verticalLayout_3.addWidget(self.metahuman_folder_button)


        self.verticalLayout_2.addWidget(self.select_metahuman_frame)

        self.symmetrize_frame = QFrame(self.modes_frame)
        self.symmetrize_frame.setObjectName(u"symmetrize_frame")
        sizePolicy7.setHeightForWidth(self.symmetrize_frame.sizePolicy().hasHeightForWidth())
        self.symmetrize_frame.setSizePolicy(sizePolicy7)
        self.symmetrize_frame.setStyleSheet(u"")
        self.symmetrize_frame.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_9 = QVBoxLayout(self.symmetrize_frame)
        self.verticalLayout_9.setSpacing(5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.label_6 = QLabel(self.symmetrize_frame)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_9.addWidget(self.label_6)

        self.symmetrize_frame2 = QFrame(self.symmetrize_frame)
        self.symmetrize_frame2.setObjectName(u"symmetrize_frame2")
        self.symmetrize_frame2.setStyleSheet(u"#symmetrize_frame2 {background: transparent}")
        self.symmetrize_frame2.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_3 = QHBoxLayout(self.symmetrize_frame2)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.original_button = QPushButton(self.symmetrize_frame2)
        self.original_button.setObjectName(u"original_button")
        sizePolicy11 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.original_button.sizePolicy().hasHeightForWidth())
        self.original_button.setSizePolicy(sizePolicy11)
        self.original_button.setMinimumSize(QSize(145, 0))
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
        self.original_button.setChecked(True)

        self.horizontalLayout_3.addWidget(self.original_button)

        self.symmetrize_button = QPushButton(self.symmetrize_frame2)
        self.symmetrize_button.setObjectName(u"symmetrize_button")
        sizePolicy11.setHeightForWidth(self.symmetrize_button.sizePolicy().hasHeightForWidth())
        self.symmetrize_button.setSizePolicy(sizePolicy11)
        self.symmetrize_button.setMinimumSize(QSize(145, 0))
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
        self.symmetrize_button.setChecked(False)

        self.horizontalLayout_3.addWidget(self.symmetrize_button)


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
        self.metahuman_to_obj_run_button.setStyleSheet(u"font-size:20px")

        self.verticalLayout_7.addWidget(self.metahuman_to_obj_run_button)

        self.obj_to_metahuman_run_button = QPushButton(self.run_frame)
        self.obj_to_metahuman_run_button.setObjectName(u"obj_to_metahuman_run_button")
        self.obj_to_metahuman_run_button.setEnabled(False)
        self.obj_to_metahuman_run_button.setMinimumSize(QSize(0, 100))
        self.obj_to_metahuman_run_button.setStyleSheet(u"font-size:20px")

        self.verticalLayout_7.addWidget(self.obj_to_metahuman_run_button)


        self.verticalLayout_2.addWidget(self.run_frame)


        self.horizontalLayout_2.addWidget(self.modes_frame)

        self.running_frame = QFrame(self.centralwidget)
        self.running_frame.setObjectName(u"running_frame")
        sizePolicy3.setHeightForWidth(self.running_frame.sizePolicy().hasHeightForWidth())
        self.running_frame.setSizePolicy(sizePolicy3)
        self.running_frame.setMinimumSize(QSize(369, 0))
        self.running_frame.setStyleSheet(u"#running_frame {background: transparent}")
        self.running_frame.setFrameShape(QFrame.StyledPanel)
        self.running_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.running_frame)
        self.verticalLayout_10.setSpacing(5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(5, 5, 5, 5)
        self.frame_6 = QFrame(self.running_frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_6)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(5, 5, 5, 5)
        self.running_label = QLabel(self.frame_6)
        self.running_label.setObjectName(u"running_label")
        self.running_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.running_label)

        self.go_to_metahuman_folder_button = QPushButton(self.frame_6)
        self.go_to_metahuman_folder_button.setObjectName(u"go_to_metahuman_folder_button")

        self.verticalLayout_11.addWidget(self.go_to_metahuman_folder_button)


        self.verticalLayout_10.addWidget(self.frame_6)


        self.horizontalLayout_2.addWidget(self.running_frame)

        METMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(METMainWindow)

        QMetaObject.connectSlotsByName(METMainWindow)
    # setupUi

    def retranslateUi(self, METMainWindow):
        METMainWindow.setWindowTitle(QCoreApplication.translate("METMainWindow", u"Metahuman Extra Tools", None))
        self.label_4.setText(QCoreApplication.translate("METMainWindow", u"Export a Metahuman to .obj files and edit it's geometry with any application.", None))
        self.metahuman_to_obj_button.setText(QCoreApplication.translate("METMainWindow", u"Metahuman to .OBJ", None))
        self.label_5.setText(QCoreApplication.translate("METMainWindow", u"Create new Metahuman head and body DNA from .obj files.", None))
        self.obj_to_metahuman_button.setText(QCoreApplication.translate("METMainWindow", u".OBJ to Metahuman", None))
        self.label_3.setText(QCoreApplication.translate("METMainWindow", u"Debug", None))
        self.debug_button.setText(QCoreApplication.translate("METMainWindow", u"Debug", None))
        self.import_dna_button.setText(QCoreApplication.translate("METMainWindow", u"import dna", None))
        self.back_button.setText(QCoreApplication.translate("METMainWindow", u"<", None))
        self.mode_label.setText(QCoreApplication.translate("METMainWindow", u"Mode", None))
        self.label_2.setText(QCoreApplication.translate("METMainWindow", u"New geometry:", None))
        self.combined_button.setText(QCoreApplication.translate("METMainWindow", u"combined", None))
        self.pushButton_2.setText(QCoreApplication.translate("METMainWindow", u"OBJ", None))
        self.eyes_button.setText(QCoreApplication.translate("METMainWindow", u"eyes", None))
        self.pushButton_4.setText(QCoreApplication.translate("METMainWindow", u"OBJ", None))
        self.eyelashes_button.setText(QCoreApplication.translate("METMainWindow", u"eyelashes", None))
        self.eyelashes_autogenerated_button.setText(QCoreApplication.translate("METMainWindow", u"auto generated", None))
        self.teeth_button.setText(QCoreApplication.translate("METMainWindow", u"teeth", None))
        self.teeth_autogenerated_button.setText(QCoreApplication.translate("METMainWindow", u"auto generated", None))
        self.label.setText(QCoreApplication.translate("METMainWindow", u"Select Metahuman folder generated by Metahuman Creator DCC Export.", None))
        self.metahuman_folder_button.setText(QCoreApplication.translate("METMainWindow", u"Metahuman folder", None))
        self.label_6.setText(QCoreApplication.translate("METMainWindow", u"Symmetry:", None))
        self.original_button.setText(QCoreApplication.translate("METMainWindow", u"Keep Original", None))
        self.symmetrize_button.setText(QCoreApplication.translate("METMainWindow", u"Symmetrize", None))
        self.metahuman_to_obj_run_button.setText(QCoreApplication.translate("METMainWindow", u"Run", None))
        self.obj_to_metahuman_run_button.setText(QCoreApplication.translate("METMainWindow", u"Run", None))
        self.running_label.setText(QCoreApplication.translate("METMainWindow", u"Running...", None))
        self.go_to_metahuman_folder_button.setText(QCoreApplication.translate("METMainWindow", u"go to Metahuman folder", None))
    # retranslateUi

