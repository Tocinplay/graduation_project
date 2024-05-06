#训练脚本
import os
import cv2
import numpy as np
import pickle

current_id = 0

label_ids = {}
x_train = []
y_labels = []

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, 'dataset')

recognizer = cv2.face.LBPHFaceRecognizer_create()
classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt2.xml")

for root, dirs, files in os.walk(image_dir): #G:\face_recognition\faceReco\dataset\
    for dir in dirs:
        class_name = os.path.basename(dir)  # 获取班级 
        class_dir = os.path.join(root, dir) #class_dir:/dataset/2006802/
        for stu_dir in os.listdir(class_dir):
            path = os.path.join(class_dir, stu_dir) #path:/dataset/2006802/2020053862_lyy
            name_code = os.path.basename(path)
            if "_" in name_code:
                student_id, student_name = name_code.split('_')  # 分割学生 ID 和姓名
            else:
                print(f"Invalid directory name: {name_code}")
                student_id = class_name + '_null'
                student_name = name_code
                continue
            label = f"{class_name}_{student_id}_{student_name}"  # 将班级，学生 ID 和姓名组合成一个标签
            
            for base, image_dir, img in os.walk(path):
                for image in img:
                    img_path = os.path.join(base, image)
                    image = cv2.imread(img_path)  # 读取图像
                    print(img_path)
                    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 转灰度图
                    image_array = np.array(gray, "uint8")  # 转数组

                    # if not label in label_ids:
                    #     label_ids[label] = student_id  # 使用学生 ID 作为标签 ID

                    id_ = student_id

                    faces = classifier.detectMultiScale(image_array, scaleFactor=1.5, minNeighbors=5)

                    for (x, y, w, h) in faces:
                        roi = image_array[y:y+h,x:x+w]
                        x_train.append(roi)
                        y_labels.append(id_)

#print(x_train)
#print(y_labels)
with open("labels.pickle", "wb") as f:
	pickle.dump(label_ids, f)

recognizer.train(x_train, np.array(y_labels))
recognizer.save("mytrainer.xml")