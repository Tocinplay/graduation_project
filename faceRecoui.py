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
        faceReco.resize(480, 320)
        self.centralwidget = QWidget(faceReco)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")

        self.horizontalLayout.addWidget(self.widget_2)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(150, 16777215))
        font = QFont()
        font.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font.setBold(True)
        font.setWeight(75)
        self.widget.setFont(font)
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_image = QLabel(self.widget)
        self.lbl_image.setObjectName(u"lbl_image")
        self.lbl_image.setMinimumSize(QSize(128, 128))
        self.lbl_image.setMaximumSize(QSize(150, 16777215))
        self.lbl_image.setFocusPolicy(Qt.NoFocus)
        self.lbl_image.setFrameShape(QFrame.Box)
        self.lbl_image.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_image)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.label_name = QLabel(self.widget)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setMaximumSize(QSize(150, 16777215))
        self.label_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_name)

        self.led_name = QLineEdit(self.widget)
        self.led_name.setObjectName(u"led_name")
        self.led_name.setMaximumSize(QSize(150, 16777215))

        self.verticalLayout.addWidget(self.led_name)

        self.label_stucode = QLabel(self.widget)
        self.label_stucode.setObjectName(u"label_stucode")
        self.label_stucode.setMaximumSize(QSize(150, 16777215))
        self.label_stucode.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_stucode)

        self.led_code = QLineEdit(self.widget)
        self.led_code.setObjectName(u"led_code")
        self.led_code.setMaximumSize(QSize(150, 16777215))

        self.verticalLayout.addWidget(self.led_code)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.widget)

        faceReco.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(faceReco)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 480, 26))
        faceReco.setMenuBar(self.menubar)

        self.retranslateUi(faceReco)

        QMetaObject.connectSlotsByName(faceReco)
    # setupUi

    def retranslateUi(self, faceReco):
        faceReco.setWindowTitle(QCoreApplication.translate("faceReco", u"faceReco", None))
        self.lbl_image.setText(QCoreApplication.translate("faceReco", u"\u4eba\u8138\u5934\u50cf", None))
        self.label_name.setText(QCoreApplication.translate("faceReco", u"\u59d3\u540d", None))
        self.label_stucode.setText(QCoreApplication.translate("faceReco", u"\u5b66\u53f7", None))
    # retranslateUi

