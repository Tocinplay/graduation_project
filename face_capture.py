import cv2
import numpy as np

cap = cv2.VideoCapture(0)  #从video0获取图像
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt2.xml')  #人脸识别分类器
print(face_cascade)


count = 0

while True:
	ret, frame = cap.read() #读取帧
	if ret:
		gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)  #转灰度图
		faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(32, 32) )
		#检测人脸，变化因子scaleFactor1.5,临近值minNeighbor5.  只能传入灰度图来检测所以要转灰度图
		for (x, y, w, h) in faces:  #人脸坐标
			#print(x, y, w, h)
			#人脸画框
			cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 128, 0), 2)  
		 	#rectangle(帧，起始坐标，终点坐标，BGR颜色，线条粗细）
			#(25,25,112)夜空蓝色,(255,69,0)火焰橙红色,(0,128,0)翠绿色
			count += 1
			cv2.imwrite("dataset/"+"2020053865-xh/" + str(count) + '.jpg', frame[y:y+h,x:x+w])
			
		#显示图像
		#cv2.imshow("gray",gray) #灰度图
		cv2.imshow("frame",frame)
	else:
		print("Error")
	#按q退出
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
	elif count == 50:
		break

cap.release()
cv2.destroyALLWindows()

