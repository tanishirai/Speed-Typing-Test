import firebase_admin
from firebase_admin import credentials , db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://speed-typing-test-shashi-singh-default-rtdb.firebaseio.com/"  # For Realtime Database 
})


print(db.reference().get())
