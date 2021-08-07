from flask import Flask,render_template,request,redirect, url_for
import random 
import json,ast
from firebase import Firebase
def handle_catch(caller, on_exception):
    try:
         return caller()
    except:
         return on_exception
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
app = Flask(__name__)
# =========================================================
Types_Of_Questions = db.child("Question_Types").get()
# =======================================================


@app.route("/",methods = ['GET','POST'])
def home():
    Chapter_List = db.child("Chapter_List").get()
    if request.method == 'POST':
        Chapter_Name=request.form.get("Chapter_Name")
        id =random.randint(10000,99999)
        data = {
            "ChapterName":Chapter_Name,
            "Chapter_ID":id,
            "No_of_Questions":0
        }
        db.child("Chapter_List").push(data)
        Chapter_List_New = db.child("Chapter_List").get()
        return render_template("index.html",Chapter_List = Chapter_List_New,handle_catch=handle_catch)
    return render_template("index.html",Chapter_List = Chapter_List,handle_catch=handle_catch)




@app.route("/chapter/<string:chapter_key>/",methods = ['GET','POST'])
def chapter_details(chapter_key):
    if request.method == 'POST':
        Question=request.form.get("Question")
        Question_Type=request.form.get("Question_Type")
        id =random.randint(100000,999999)
        data = {
            "Question":Question,
            "Question_Type":Question_Type,
            "Question_ID":id
        }
        number = db.child("Chapter_List").child(chapter_key).child("No_of_Questions").get()
        db.child("Chapter_List").child(chapter_key).child("No_of_Questions").set(number.val()+1)
        db.child("Chapter_List").child(chapter_key).child("Question_List").push(data)
        Chapter_List_New = db.child("Chapter_List").get()
        for item in Chapter_List_New.each():
            if (item.key()==chapter_key):
                chapter=item
                return render_template("chapter_detail.html",chapter=chapter,handle_catch=handle_catch)
    chapter_data = db.child("Chapter_List").get()
    for item in chapter_data.each():
        if (item.key()==chapter_key):
            chapter=item
            return render_template("chapter_detail.html",chapter=chapter,handle_catch=handle_catch)




@app.route("/question/<string:chapter_key>/<string:question_key>/",methods = ['GET','POST'])
def question_detail(chapter_key,question_key):
    if request.method == 'POST':
        Question=request.form.get("Question")
        Question_Type=request.form.get("Question_Type")
        Question_Ids=request.form.get("Question_Tag_Ids")
        Options_Ids=request.form.get("Options_Tag_Ids")
        # y = json.loads(Options_Ids)
        if Options_Ids!="":
            y = ast.literal_eval(Options_Ids)
        else:
            y=" "
        # l=[]
        # m = Options_Ids.split(",")
        # for i in m:
        #     if (i==''):
        #         m.remove(i)
        # for i in range(len(m)):
        #     l.append(random.randint(1000,9999))
        # k = dict(zip(l,m))
        update_data = {
            "Question":Question,
            "Question_Type":Question_Type,
            "TAG_Ids":Question_Ids,
            "OPT_JSON":y
            
        }
        db.child("Chapter_List").child(chapter_key).child("Question_List").child(question_key).update(update_data)
        return redirect(url_for('question_detail',chapter_key=chapter_key,question_key=question_key))

    Chapter_Data = db.child("Chapter_List").get()
    for item in Chapter_Data.each():
        if (item.key()==chapter_key):
            for key,value in item.val()["Question_List"].items():
                if(key==question_key):
                    return render_template("question_detail.html",question_data=value,chapter_key = chapter_key,question_key = key,ques_types = Types_Of_Questions, handle_catch=handle_catch)




@app.route("/delete/chapter/<string:chapter_key>/",methods = ['GET','POST'])
def chapter_delete(chapter_key):
    Chapter_Data = db.child("Chapter_List").get()
    for item in Chapter_Data.each():
        if (item.key()==chapter_key):
            db.child("Chapter_List").child(chapter_key).remove()
            return redirect(url_for('home'))
            # return render_template("index.html",Chapter_List = db.child("Chapter_List").get(),handle_catch=handle_catch)



@app.route("/chapter/<string:chapter_key_first>/delete/question/<string:chapter_key>/<string:question_key>/",methods = ['GET','POST'])
def question_delete(chapter_key_first,chapter_key,question_key):
    Chapter_Data = db.child("Chapter_List").get()
    for item in Chapter_Data.each():
        if (item.key()==chapter_key):
             for key in item.val()["Question_List"].keys():
                    if(key==question_key):
                        db.child("Chapter_List").child(chapter_key).child("Question_List").child(key).remove()
                        number = db.child("Chapter_List").child(chapter_key).child("No_of_Questions").get()
                        db.child("Chapter_List").child(chapter_key).child("No_of_Questions").set(number.val()-1)
                        return redirect(url_for('chapter_details',chapter_key=chapter_key))
            # return render_template("index.html",Chapter_List = db.child("Chapter_List").get(),handle_catch=handle_catch)



app.run()