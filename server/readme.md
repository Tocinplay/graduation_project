# 服务器代码
###  face_reco.py
该文件为flask服务器程序，与mysql数据库配合使用
app.config['SQLALCHEMY_DATABASE_URI'] = # 这个后面的路径为mysql数据库连接路径 
'mysql+pymysql://账号:密码@localhost/数据库名'

### schoolhome.sql
mysql数据库文件

### flask.conf
nginx配置文件，该文件放在“/etc/nginx/sites-enabled” 目录下。
`sudo systemctl reload nginx` 重载nginx，启动服务

### face_reco.service
系统服务文件，确保我的程序一直保持运行，该文件放在“/etc/systemd/system/”目录下。
`systemctl start face_reco.service` 启动该服务
`sudo systemctl stop face_reco.service` 停止服务
`sudo systemctl status face_reco.service` 查看服务状态
`sudo systemctl enable face_reco.service` 启用服务
`sudo systemctl disable face_reco.service` 禁用服务（取消其在启动时自动运行）

