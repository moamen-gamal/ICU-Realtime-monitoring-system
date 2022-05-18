from flask import Flask
from flask import request
from icuBase import *

idx =0

patients_sensors =[0]
app = Flask(__name__)

@app.route('/main')
def hello():
    pass

@app.route('/sendData',methods= ['GET','POST'])
def send2firebase():
    global idx
    content = request.json
    print (content)
    if(content["ID"] > len(patients_sensors)):
        diff = int(content["ID"]) - len(patients_sensors)
        while (diff >=0):
            patients_sensors.append(0)
            diff = diff -1
    addReadings1(int(content["ID"]),idx,content["TEMP"])
    addReadings2(int(content["ID"]),idx,content["LDR"])
    addReadings1(1,idx,content["TEMP"]+5)
    addReadings2(1,idx,content["TEMP"]+5)
    idx = idx+1
    return str(patients_sensors[int(content["ID"])])

@app.route('/getState',methods=['GET','POST'])
def state():
    id = request.args.get("id")
    
    if(int(id)> len(patients_sensors)):
        diff = int(id) - len(patients_sensors)
        while (diff >=0):
            patients_sensors.append(0)
            diff = diff -1
    patients_sensors[int(id)] = int(request.args.get("val"))
    return"ok"
if __name__ == '__main__':
    app.run('192.168.43.251',port=5000,threaded=True)