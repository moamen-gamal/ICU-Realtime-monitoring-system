


# from firebase import firebase
# fb_app = firebase.FirebaseApplication('https://ohmynewone-default-rtdb.firebaseio.com', None)
# result = fb_app.get('/Firstperson', None)
# print(result)



# Imports
#-------------------------------------------------------------------------------
import pyrebase
from datetime import datetime



# Config/Setup
#-------------------------------------------------------------------------------
firebaseConfig = {
    "apiKey": "AIzaSyCCY9jFdTiGK2eGzklWpk144mKV0Mco9BA",
    "authDomain": "ohmynewone.firebaseapp.com",
    "databaseURL": "https://ohmynewone-default-rtdb.firebaseio.com",
    "projectId": "ohmynewone",
    "storageBucket": "ohmynewone.appspot.com",
    "messagingSenderId": "294615109835",
    "appId": "1:294615109835:web:0d83a3d05721f46d60cb4e",
    "measurementId": "G-15BCC4QT6R"
 };
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

now = datetime.now()
current_time = now.strftime("%H%M%S")
#-------------------------------------------------------------------------------
# Create Data
# data is written like that: data1 = {"sensor1": 21.0, "sensor2": 11.5, "led": True}
def addReadings1(patientId,numid ,sensor1 ):
    #data = {"sensor1": sensor1 , "sensor2": sensor2}
    db.child(patientId).child("TEMP").child(numid).set(sensor1)
def addReadings2(patientId,numid, sensor2 ):
    #data = {"sensor1": sensor1 , "sensor2": sensor2}
    db.child(patientId).child("LDR").child(numid).set(sensor2)

#-------------------------------------------------------------------------------

# get latest 50 readings
def read50(patientId):
    patient =  db.child(patientId).get().val()
    items = list(patient.items())
    if (len(items)> 50):
    
        print(items[-50])
    
    else:
       print(items) 
    
    
# Read all Data of patient
def readPatient(patientId):

    patient = db.child(patientId).get()
    print(patient.val())

# Read latest Data of patient
def readLast(patientId):

    patient =  db.child(patientId).get().val()
    items = list(patient.items())
    print(items[-1])

def readSensor(patientId, sensor, num):
    patient =  db.child(patientId).get().val()
    items = list(patient.items())
    for x in range(num):
        print(items[-x][1][sensor])
#-------------------------------------------------------------------------------
# # Update Data
# def updateSensor(patientId, sensor,value):
#     db.child(patientId).child(current_time).update({sensor : value})

#-------------------------------------------------------------------------------
# Remove Data

# #Delete 1 Value
# db.child("FirstPerson").child("seneor1").remove()

# #Delete whole Node
# db.child("FirstPerson").remove()

#-------------------------------------------------------------------------------
