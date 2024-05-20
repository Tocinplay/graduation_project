# This Python file uses the following encoding: utf-8
import sys
import time
from form import Ui_faceReco
import cv2
import pickle
import requests
from datetime import datetime

#分类器使用
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt2.xml")  #人脸识别分类器
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("./mytrainer.xml")
# print(face_cascade)
labels = {}
with open("./labels.pickle","rb") as f:
	origin_labels = pickle.load(f) # {"tocin": 5}
	labels = {v:k for k, v in origin_labels.items()}


from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide2.QtGui import QImage, QPixmap    
from PySide2.QtCore import QTimer

def send_to_server(face_name, face_id, entry_count):
    # 将识别结果作为JSON数据发送
    data = {
        'face_name': face_name,
        'face_id': face_id,
        'entry_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),  # 添加当前时间
        'entry_status': '入校' if entry_count % 2 == 1 else '离校'  # 根据识别次数决定是入校还是离校
    }
    response = requests.post('https://tocin.top:8443/api/face_recognition', json=data)
    if response.status_code == 200:
        print('发送成功')
    else:
        print('发送失败，状态码：', response.status_code)

class faceReco(QMainWindow, Ui_faceReco):
    def __init__(self):
        super().__init__()
        self.entry_count = 0
        self.setupUi(self)

        self.setWindowTitle("人脸识别门禁系统")
        self.cap = cv2.VideoCapture(0)                      #使用第0个摄像头
        self.lbl_video.setScaledContents(True)              #设置label自适应大小
        #设置窗口最大化
        # self.setWindowState(Qt.WindowMaximized)

        #设置定时器来识别人脸，
        self.timer = QTimer()
        self.timer.timeout.connect(self.camera)
        self.camera_on()

        #编辑开关,识别框
        self.btn_start.setEnabled(False)
        self.led_name.setEnabled(False)
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
        self.led_name.clear()
        self.led_code.clear()
        self.lbl_image.clear()

    def camera(self):
        
        self.face_flag = 0
        self.face_1st = None
        self.face_time = None
        if self.cap.isOpened():
            ret, frame = self.cap.read() #读取帧
            frame = cv2.flip(frame, 1)
            if ret:
                gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)  #转灰度图
                faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
                #检测人脸，变化因子scaleFactor1.5,临近值minNeighbor5.  只能传入灰度图来检测所以要转灰度图
                for (x, y, w, h) in faces:  #人脸坐标
                    gray_roi = gray[y:y+h, x:x+w]
                    id_, conf = recognizer.predict(gray_roi)
                    print(id_, conf)
                    if conf >= 70: 
                        # print(labels[id_])
                        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 128, 0), 2)  
                        # cv2.putText(frame, str(labels[id_]).split('-')[1], (x, y-15), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,128,0), 2)
                        face_id = (str(labels[id_]).split('-')[0])
                        face_name = (str(labels[id_]).split('-')[1])
                        image_pt = QPixmap("dataset/" + str(labels[id_]) + '/1.jpg').scaled(178, 178)
                        self.led_name.setText(face_name)
                        self.led_code.setText(face_id)
                        self.lbl_image.setPixmap(image_pt)
                        print(face_name +"-"+face_id+"识别成功")
                        self.entry_count += 1  # 增加识别次数
                        send_to_server(face_name, face_id, self.entry_count)
                        #识别后暂停三秒
                        # time.sleep(3)

                    # else:
                    #     face_name = "未知"   
                        # self.led_name.clear()
                        # self.led_code.clear()
                        # self.lbl_image.clear()

            else:
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setText("打开视频失败")
                msg_box.setWindowTitle("错误信息")
                msg_box.setStandardButtons(QMessageBox.Ok)
            self.display(frame)

    #放到文本框中去
    def putOnlineEdit(self, id_ ):
        
        if self.face_flag == 0:
            self.face_flag = 1
            self.face_1st = id_
            
            self.face_time = time.time()         
        else:  
            if self.face_1st == id_ :
                if time.time() - self.face_time > 2.0 :
                    face_id = (str(labels[id_]).split('-')[1])
                    face_name = (str(labels[id_]).split('-')[0])
                    image_pt = QPixmap("dataset/" + str(labels[id_]) + '/1.jpg').scaled(178, 178)
                    self.led_name.setText(face_name)
                    self.led_code.setText(face_id)
                    self.lbl_image.setPixmap(image_pt)
                    print(face_name +"-"+face_id+"识别成功")
                self.face_flag = 0
                
    

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
