# 门禁系统代码
1. main.py
主程序，门禁程序，从训练好数据集中取出数据来识别，labels.pickle和mytrainer.xml为训练好的数据，之后连接服务器上传门禁数据，服务器域名为'https://tocin.top:8443/api/face_recognition' ，用json格式来传输。
2. train.py
训练程序，从dataset文件中取出数据来训练数据，训练完之后生成labels.pickle和mytrainer.xml。
3. face_capture.py
人脸采集程序，一次性采集50张人脸，存储到dataset文件夹中，需要改这个代码第二个参数来改文件名和姓名。
cv2.imwrite("dataset/"+"2020053865-xh/" + str(count) + '.jpg', frame[y:y+h,x:x+w])
4. faceRecoui.py
form.ui转换后的python文件。

opencv版本使用的是 4.5.4.60，python-contrib-opencv包。