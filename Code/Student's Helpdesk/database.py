import sqlite3
import hashlib
import datetime
import MySQLdb
from flask import session


def db_connect():
    _conn = MySQLdb.connect(host="localhost", user="user",
                            passwd="password", db="mydatabase")
    c = _conn.cursor()

    return c, _conn



# -------------------------------Registration-----------------------------------------------------------------

def student_reg(username, password, rollno, email, address,mobile):
    try:
        c, conn = db_connect()
        print(username, password, rollno, email, address,mobile)
        j = c.execute("insert into student (username, password, rollno, email, address,mobile) values ('"+username +
                      "','"+password+"','"+rollno+"','"+email+"','"+address+"','"+mobile+"')")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))

def faculty_reg(username, password, dept, email, address,mobile):
    try:
        c, conn = db_connect()
        print(username, password, dept, email, address,mobile)
        j = c.execute("insert into faculty (username, password, dept, email, address,mobile) values ('"+username +
                      "','"+password+"','"+dept+"','"+email+"','"+address+"','"+mobile+"')")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))

def complaint(name,des):
    try:
        c, conn = db_connect()
        print(name,des)
        j = c.execute("insert into complaint (name,description) values ('"+name+"','"+des+"')")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))  

def afaqs(name):
    try:
        c, conn = db_connect()
        print(name)
        j = c.execute("insert into faqs (name) values ('"+name+"')")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))  

def addssuggestion(name,description):
    try:
        c, conn = db_connect()
        print(name,description)
        j = c.execute("insert into sugesstion (name,description) values ('"+name+"','"+description+"')")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))  

def addnotification(name,notification):
    try:
        c, conn = db_connect()
        print(name,notification)
        j = c.execute("insert into notification (name,notification) values ('"+name+"','"+notification+"')")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))  

def admin_viewcomplaints():
    c, conn = db_connect()
    c.execute("select name,description from complaint")
    result = c.fetchall()
    conn.close()
    print("result")
    return result
              
def bdeleteact(name, description):
    c, conn = db_connect()
    j = c.execute("delete from complaint where name='" +
                  name+"' and description='"+description+"'")
    conn.commit()
    conn.close()
    return j

def faculty_viewcomplaints():
    c, conn = db_connect()
    c.execute("select name,description from complaint")
    result = c.fetchall()
    conn.close()
    print("result")
    return result

def admin_viewsuggestion():
    c, conn = db_connect()
    c.execute("select name,description from sugesstion")
    result = c.fetchall()
    conn.close()
    print("result")
    return result
              
def sdeleteact(name, suggestion):
    c, conn = db_connect()
    j = c.execute("delete from sugesstion where name='" +
                  name+"' and description='"+suggestion+"'")
    conn.commit()
    conn.close()
    return j

def admin_viewfaqs():
    c, conn = db_connect()
    c.execute("select * from faqs")
    result = c.fetchall()
    conn.close()
    print("result")
    return result

def viewnotification():
    c, conn = db_connect()
    c.execute("select * from notification")
    result = c.fetchall()
    conn.close()
    print("result")
    return result

def vothercomplaints():
    c, conn = db_connect()
    c.execute("select * from complaint ")
    result = c.fetchall()
    conn.close()
    print("result")
    return result
              
def fdeleteact(name):
    c, conn = db_connect()
    j = c.execute("delete from faqs where name='" +
                  name+"' ")
    conn.commit()
    conn.close()
    return j








                        
# -------------------------------Registration End-----------------------------------------------------------------
# -------------------------------Loginact Start-----------------------------------------------------------------

def admin_loginact(username, password):
    try:
        c, conn = db_connect()
        j = c.execute("select * from admin where username='" +
                      username+"' and password='"+password+"'")
        c.fetchall()
        conn.close()
        return j
    except Exception as e:
        return(str(e))

def student_loginact(username, password):
    try:
        c, conn = db_connect()
        j = c.execute("select * from student where username='" +
                      username+"' and password='"+password+"'")
        c.fetchall()
        conn.close()
        return j
    except Exception as e:
        return(str(e))

def faculty_loginact(username, password):
    try:
        c, conn = db_connect()
        j = c.execute("select * from faculty where username='" +
                      username+"' and password='"+password+"'")
        c.fetchall()
        conn.close()
        return j
    except Exception as e:
        return(str(e))

if __name__ == "__main__":
    print(db_connect())
