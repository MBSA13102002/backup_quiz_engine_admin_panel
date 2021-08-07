import random as r
import json
from firebase import Firebase
config = {
    "apiKey": "AIzaSyA1h6NqVizacIpvyUExiPzUy7LKbT5VV4c",
   "authDomain": "hackilo-edutech.firebaseapp.com",
    "databaseURL": "https://hackilo-edutech-default-rtdb.firebaseio.com",
    "projectId": "hackilo-edutech",
    "storageBucket": "hackilo-edutech.appspot.com",
    "messagingSenderId": "432434540165",
    "appId": "1:432434540165:web:e364ec66e0ae0e8e6cc3ec",
    "measurementId": "G-HVEVSTM0XC"
}
firebase = Firebase(config)
db = firebase.database()
options = "{}"
# options = '{"4545":{"opt":"computer","ans":"false"},"7894":{"opt":"lucy","ans":"false"} }'
y = json.loads(options)
print(y)



# print(y["hjhbjsdbfsd"]["opt"])
# sai = "subbar,Pen,Pencil,Eraser,Horlicks,"
# l=[]
# z=[]
# m = sai.split(",")
# for i in m:
#     if (i==''):
#         m.remove(i)
# for i in range(len(m)):
#     l.append(r.randint(1000,9999))
# for i in range(len(m)):
#     if (m[i]=="Pen"):
#         m[i]=m[i]+"_1"
#     else:

#         m[i]=m[i]+"_0"


# k = dict(zip(l,m))
# db.child("Chapter_List").child("-MgAkBoLwPR4XhZCrfYf").child("Question_List").child("-MgLZu_7WBSdfuLr_Lej").child("OPT_JSON").set(y)
# for i in k.each():
#     print(i.val())
# print(set(k))

