import os

from flask import Flask, session, url_for, redirect, render_template, request, abort, flash
from database import db_connect,  admin_loginact,student_reg,faculty_reg, student_loginact,admin_viewsuggestion,sdeleteact, faculty_viewcomplaints,vothercomplaints
from database import faculty_loginact,complaint, admin_viewcomplaints,bdeleteact,afaqs,viewnotification,addssuggestion, addnotification,admin_viewfaqs,fdeleteact
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route("/")
def FUN_root():
    return render_template("index.html")
@app.route("/admin.html")
def admin():
    return render_template("admin.html")
@app.route("/faculty.html")
def faculty():
    return render_template("faculty.html")
@app.route("/student.html")
def student():
    return render_template("student.html")

@app.route("/facultyreg.html")
def facultyreg():
    return render_template("facultyreg.html")
@app.route("/studentreg.html")
def studentreg():
    return render_template("studentreg.html")

@app.route("/adminhome.html")
def adminhome():
    return render_template("adminhome.html")

@app.route("/addcomplaints.html")
def addcomplaints():
    return render_template("addcomplaints.html")

@app.route("/studenthome.html")
def studenthome():
    return render_template("studenthome.html")

@app.route("/facultyhome.html")
def facultyhome():
    return render_template("facultyhome.html")

@app.route("/addfaqs.html")
def addfaqs():
    return render_template("addfaqs.html")

@app.route("/addnotifications.html")
def addnotifications():
    return render_template("addnotifications.html")

@app.route("/addsuggestion.html")
def addsuggestion():
    return render_template("addsuggestion.html")



# -------------------------------Registration-----------------------------------------------------------------    
@app.route("/studentregact", methods = ['GET','POST'])
def studentregact():
   if request.method == 'POST':      
      status = student_reg(request.form['username'],request.form['password'],request.form['rollno'],request.form['email'],request.form['address'],request.form['mobile'])
      if status == 1:
       return render_template("student.html",m1="sucess")
      else:
       return render_template("student.html",m1="failed")

@app.route("/facultyregact", methods = ['GET','POST'])
def facultyregact():
   if request.method == 'POST':      
      status = faculty_reg(request.form['username'],request.form['password'],request.form['dept'],request.form['email'],request.form['address'],request.form['mobile'])
      if status == 1:
       return render_template("faculty.html",m1="sucess")
      else:
       return render_template("faculty.html",m1="failed")


@app.route("/addcomplaintact", methods = ['GET','POST'])
def complaintact():
   if request.method == 'POST':      
      status = complaint(request.form['name'],request.form['des'])
      if status == 1:
       return render_template("addcomplaints.html",m1="sucess")
      else:
       return render_template("addcomplaints.html",m1="failed")
# -------------------------------Registration End-----------------------------------------------------------------
# -------------------------------Loginact-----------------------------------------------------------------
@app.route("/adminlogact", methods=['GET', 'POST'])       
def adminlogact():
    if request.method == 'POST':
        status = admin_loginact(request.form['username'], request.form['password'])
        print(status)
        if status == 1:
            session['username'] = request.form['username']
            return render_template("adminhome.html", m1="sucess")
        else:
            return render_template("admin.html", m1="Login Failed")

@app.route("/studentlogact", methods=['GET', 'POST'])       
def studentlogact():
        if request.method == 'POST':
           status = student_loginact(request.form['username'], request.form['password'])
           print(status)
        if status == 1:
            session['username'] = request.form['username']
            return render_template("studenthome.html", m1="sucess")
        else:
            return render_template("student.html", m1="Login Failed")

@app.route("/facultylogact", methods=['GET', 'POST'])       
def facultylogact():
    if request.method == 'POST':
        status = faculty_loginact(request.form['username'], request.form['password'])
        print(status)
        if status == 1:
            session['username'] = request.form['username']
            return render_template("facultyhome.html", m1="sucess")
        else:
            return render_template("faculty.html", m1="Login Failed")
# -------------------------------Loginact End-----------------------------------------------------------------

@app.route("/addfaqsact", methods = ['GET','POST'])
def addfaqsact():
   if request.method == 'POST':      
      status = afaqs(request.form['name'])
      if status == 1:
       return render_template("addfaqs.html",m1="sucess")
      else:
       return render_template("addfaqs.html",m1="failed")

@app.route("/addsuggestionact", methods = ['GET','POST'])
def addsuggestionact():
   if request.method == 'POST':      
      status = addssuggestion(request.form['name'],request.form['description'])
      if status == 1:
       return render_template("addsuggestion.html",m1="sucess")
      else:
       return render_template("addsuggestion.html",m1="failed")

@app.route("/addnotificationact", methods = ['GET','POST'])
def addnotificationact():
   if request.method == 'POST':      
      status = addnotification(request.form['name'],request.form['notification'])
      if status == 1:
       return render_template("addnotifications.html",m1="sucess")
      else:
       return render_template("addnotifications.html",m1="failed")


@app.route("/aviewcomplaints.html")
def aviewcomplaints():
    data = admin_viewcomplaints()
    print(data)
    return render_template("aviewcomplaints.html", vcomplaint = data)

@app.route("/fviewcomplaints.html")
def fviewcomplaints():
    data = faculty_viewcomplaints()
    print(data)
    return render_template("fviewcomplaints.html", vcomplaint = data)
    
@app.route("/bdelete")
def bdelete():
    status = bdeleteact(request.args.get('name'),request.args.get('description'))
    data = admin_viewcomplaints()
    if status == 1:
       return render_template("aviewcomplaints.html",m1="sucess",vcomplaint=data)
    else:
       return render_template("aviewcomplaints.html",m1="failed",vcomplaint=data)

@app.route("/aviewsugg.html")
def aviewsugg():
    data = admin_viewsuggestion()
    print(data)
    return render_template("aviewsugg.html", vsuggestion = data)

@app.route("/viewsugg.html")
def viewsugg():
    data = admin_viewsuggestion()
    print(data)
    return render_template("viewsugg.html", vsuggestion = data)

@app.route("/fviewfaq.html")
def fviewfaq():
    data = admin_viewfaqs()
    print(data)
    return render_template("fviewfaq.html", vfaqs = data)

@app.route("/s_viewfaq.html")
def s_viewfaq():
    data = admin_viewfaqs()
    print(data)
    return render_template("s_viewfaq.html", vfaqs = data)

@app.route("/viewnotification.html")
def view_notification():
    data = viewnotification()
    print(data)
    return render_template("viewnotification.html", viewnotification = data)

@app.route("/viewotherscomplaints.html")
def view_scomplaints():
    data = vothercomplaints()
    print(data)
    return render_template("viewotherscomplaints.html", sothercomplaints = data)


@app.route("/sdelete")
def sdelete():
    status = sdeleteact(request.args.get('name'),request.args.get('suggestion'))
    data = admin_viewsuggestion()
    if status == 1:
       return render_template("aviewsugg.html",m1="sucess",vsuggestion=data)
    else:
       return render_template("aviewsugg.html",m1="failed",vsuggestion=data)

@app.route("/aviewfaq.html")
def aviewfaq():
    data = admin_viewfaqs()
    print(data)
    return render_template("aviewfaq.html", vfaqs = data)

@app.route("/fdelete")
def fdelete():
    status = fdeleteact(request.args.get('name'))
    data = admin_viewfaqs()
    if status == 1:
       return render_template("aviewfaq.html",m1="sucess",vfaqs=data)
    else:
       return render_template("aviewfaq.html",m1="failed",vfaqs=data)
   
if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)
