import firebase_admin
from firebase_admin import credentials , db

from datetime import datetime

current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

cred = credentials.Certificate("serviceAccountKey.json")

firebase_admin.initialize_app(cred, {
    'databaseURL': "https://speed-typing-test-shashi-singh-default-rtdb.firebaseio.com/"  # For Realtime Database 
})

ref = db.reference("test")
data = ref.get()

def checkUniqueUser(username): 
    for key,value in data.items():
        for names,entry in value.items():
            if entry==username:
                # print("found")
                return True
    return False

def initialiseNewUser(username,password):
    newValue = {
        "name":username,
        "password":password
    }
    ref.child(username).update(newValue)

def uploadCurrentData(username,wpm,accuracy):
    date = formatted_datetime
    newValue = {
        date:{
            "wpm" : wpm,
            "accuracy" : accuracy
        },
    }
    if(username!="Login"):
        ref.child(username).child("history").push(newValue)