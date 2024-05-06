# This Python file uses the following encoding: utf-8
import sys
import os
from faceRecoui import Ui_faceReco

import cv2
import numpy as np
import pickle

#分类器使用
face_cascade = cv2.CascadeClassifier('F:/software/python/Lib/site-packages/cv2/data/haarcascade_frontalface_alt2.xml')  #人脸识别分类器

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import QImage, QPixmap    
from PyQt5.QtCore import QFile, QTimer, Qt
from PyQt5.uic import loadUi


class faceReco(QMainWindow, Ui_faceReco):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("人脸识别门禁系统")
        self.cap = cv2.VideoCapture(0)                      #使用第0个摄像头
        self.lbl_video.setScaledContents(True)              #设置label自适应大小
        #设置无边框
        self.setWindowFlag(Qt.FramelessWindowHint)

        #设置定时器来识别人脸，
        self.timer = QTimer()
        self.timer.timeout.connect(self.camera)
        self.camera_on()

        #编辑开关,识别框
        self.btn_start.setEnabled(False)
        self.led_name.setEnabled(False)
        self.led_class.setEnabled(False)
        self.led_code.setEnabled(False)
        #连接关闭按钮
        self.btn_stop.clicked.connect(self.camera_off)
        #连接开始按钮
        self.btn_start.clicked.connect(self.camera_on)

    def camera_on(self):
        self.cap = cv2.VideoCapture(0)
        self.timer.start(1)
        self.btn_start.setEnabled(False)
        self.btn_stop.setEnabled(True)

    def camera_off(self):
        self.timer.stop()
        self.cap.release()
        cv2.destroyAllWindows()
        self.btn_start.setEnabled(True)
        self.btn_stop.setEnabled(False)
        self.lbl_video.clear()

    def camera(self):
        if self.cap.isOpened():
            ret, frame = self.cap.read() #读取帧
            frame = cv2.flip(frame, 1)
            if ret:
                gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)  #转灰度图
                faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
                #检测人脸，变化因子scaleFactor1.5,临近值minNeighbor5.  只能传入灰度图来检测所以要转灰度图
                for (x, y, w, h) in faces:  #人脸坐标
                    #print(x, y, w, h)
                    #人脸画框
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (25,25,112), 2)
                    #rectangle(帧，起始坐标，终点坐标，BGR颜色，线条粗细）
                    #(25,25,112)夜空蓝色,(255,69,0)火焰橙红色,(0,128,0)翠绿色
                    #count += 1
                    #cv2.imwrite("dataset/" + str(count) + '.jpg', gray[y:y+h,x:x+w])

                #显示图像
                #cv2.imshow("gray",gray) #灰度图
                #cv2.imshow("frame",frame)
                self.display(frame)
            else:
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setText("打开视频失败")
                msg_box.setWindowTitle("错误信息")
                msg_box.setStandardButtons(QMessageBox.Ok)
            

    def display(self, frame):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = frame.shape
        bytes_per_line = ch * w
        img = QImage(frame, w, h, bytes_per_line, QImage.Format_RGB888)
        self.lbl_video.setPixmap(QPixmap.fromImage(img))
        
        




if __name__ == "__main__":
    app = QApplication([])
    widget = faceReco()
    widget.show()
    sys.exit(app.exec_())
