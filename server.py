from flask import Flask
from flask import request
patients_sensors =[0]
app = Flask(__name__)

@app.route('/main')
def hello():
    pass

@app.route('/sendData',methods= ['GET','POST'])
def send2firebase():
    content = request.json
    print (content)
    if(int(content["ID"]) > len(patients_sensors)):
        patients_sensors.append(0)
    return str(patients_sensors[int(content["ID"])])


if __name__ == '__main__':
    app.run('192.168.1.2',port=5000,threaded=True)