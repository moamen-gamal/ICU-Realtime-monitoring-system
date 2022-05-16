from flask import Flask
from flask import request
patients_sensors =[0,1]
app = Flask(__name__)

@app.route('/main')
def hello():
    pass

@app.route('/sendData',methods= ['GET','POST'])
def send2firebase():
    content = request.json
    int(content["ID"])
    print (content)
    return "1"


if __name__ == '__main__':
    app.run('172.28.128.189',port=5000,threaded=True)