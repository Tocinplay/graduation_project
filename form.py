# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_faceReco(object):
    def setupUi(self, faceReco):
        if not faceReco.objectName():
            faceReco.setObjectName(u"faceReco")
        faceReco.resize(640, 480)
        self.centralwidget = QWidget(faceReco)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lbl_video = QLabel(self.groupBox)
        self.lbl_video.setObjectName(u"lbl_video")

        self.verticalLayout_2.addWidget(self.lbl_video)


        self.horizontalLayout.addWidget(self.groupBox)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(200, 480))
        font = QFont()
        font.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font.setBold(True)
        font.setWeight(75)
        self.widget.setFont(font)
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_image = QLabel(self.widget)
        self.lbl_image.setObjectName(u"lbl_image")
        self.lbl_image.setMinimumSize(QSize(178, 178))
        self.lbl_image.setMaximumSize(QSize(200, 200))
        self.lbl_image.setFocusPolicy(Qt.NoFocus)
        self.lbl_image.setFrameShape(QFrame.Box)
        self.lbl_image.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_image)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_name = QLabel(self.widget)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setMaximumSize(QSize(150, 30))
        self.label_name.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_name)

        self.led_name = QLineEdit(self.widget)
        self.led_name.setObjectName(u"led_name")
        self.led_name.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_2.addWidget(self.led_name)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_stucode = QLabel(self.widget)
        self.label_stucode.setObjectName(u"label_stucode")
        self.label_stucode.setMaximumSize(QSize(150, 16777215))
        self.label_stucode.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_stucode)

        self.led_code = QLineEdit(self.widget)
        self.led_code.setObjectName(u"led_code")
        self.led_code.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_3.addWidget(self.led_code)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_start = QPushButton(self.widget)
        self.btn_start.setObjectName(u"btn_start")

        self.horizontalLayout_4.addWidget(self.btn_start)

        self.btn_stop = QPushButton(self.widget)
        self.btn_stop.setObjectName(u"btn_stop")

        self.horizontalLayout_4.addWidget(self.btn_stop)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.horizontalLayout.addWidget(self.widget)

        faceReco.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(faceReco)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 640, 26))
        faceReco.setMenuBar(self.menubar)

        self.retranslateUi(faceReco)

        QMetaObject.connectSlotsByName(faceReco)
    # setupUi

    def retranslateUi(self, faceReco):
        faceReco.setWindowTitle(QCoreApplication.translate("faceReco", u"faceReco", None))
        self.groupBox.setTitle(QCoreApplication.translate("faceReco", u"\u89c6\u9891\u533a\u57df", None))
        self.lbl_video.setText("")
        self.lbl_image.setText(QCoreApplication.translate("faceReco", u"\u4eba\u8138\u5934\u50cf", None))
        self.label_name.setText(QCoreApplication.translate("faceReco", u"\u59d3\u540d", None))
        self.label_stucode.setText(QCoreApplication.translate("faceReco", u"\u5b66\u53f7", None))
        self.btn_start.setText(QCoreApplication.translate("faceReco", u"\u5f00\u59cb", None))
        self.btn_stop.setText(QCoreApplication.translate("faceReco", u"\u505c\u6b62", None))
    # retranslateUi

