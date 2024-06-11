from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:over6688@localhost/tocin_schoolhome'  # 请替换为你的数据库 URI
db = SQLAlchemy(app)

class FaceData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    face_name = db.Column(db.String(80))
    face_id = db.Column(db.String(20))
    entry_time = db.Column(db.String(20))
    entry_status = db.Column(db.String(20))

    def __init__(self, face_name, face_id, entry_time, entry_status):
        self.face_name = face_name
        self.face_id = face_id
        self.entry_time = entry_time
        self.entry_status = entry_status

@app.route('/api/face_recognition', methods=['POST'])
def receive_face_recognition():
    data = request.get_json()
    face_data = FaceData(data['face_name'], data['face_id'], data['entry_time'], data['entry_status'])
    db.session.add(face_data)
    db.session.commit()
    return {'message': 'Data received successfully'}, 200

@app.route('/api/get_face_data', methods=['GET'])
def get_face_data():
    data = FaceData.query.all()
    return jsonify([{'face_name': d.face_name, 'face_id': d.face_id, 'entry_time': d.entry_time, 'entry_status': d.entry_status} for d in data])

@app.route('/api/get_face_data/<face_id>', methods=['GET'])
def get_face_data_by_id(face_id):
    data = FaceData.query.filter_by(face_id=face_id).all()
    return jsonify([{'face_name': d.face_name, 'face_id': d.face_id, 'entry_time': d.entry_time, 'entry_status': d.entry_status} for d in data])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # 创建数据库表
    app.run(host='0.0.0.0', port=8990)
