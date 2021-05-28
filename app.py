from flask import Flask,render_template,request,redirect,url_for
import requests
import json
app=Flask(__name__)

@app.route('/',methods=["GET","POST"])
def hello():
    if request.method=="GET":
        return render_template('home.html')
    else:
        val=request.form['med']
        r=requests.get('http://localhost:8080/api/query/'+str(val))
        print(r.json())
        if r.status_code == 200:
            m=r.json()['response']
            print(m)
            return render_template('home1.html',flag=1,med=m)
        else:
            print("fast")
            return render_template('home1.html',flag=0)

@app.route('/admin',methods=["GET","POST"])
def admin():
    if request.method=="GET":
        
        return render_template('admin.html',flag=0)
    else:
        obj={
            "carid":request.form["carid"],
            "make":request.form["make"],
            "model":request.form["model"],
            "colour":request.form["colour"],
            "owner":request.form["owner"]
        }
              

        r=requests.post('https://sri-server.herokuapp.com/api/addcar/',data=obj)
        return render_template("admin.html",flag=1)

@app.route('/change',methods=["POST"])
def change():
    res=requests.put('https://sri-server.herokuapp.com/api/changeowner/'+str(request.form["pid"]),data={"owner":request.form["powner"]})
    return render_template("admin.html",flag=2)


@app.route('/display',methods=["GET"])
def display():
    res=requests.get('https://sri-server.herokuapp.com/api/queryallcars')

    return render_template("admin.html",flag=3,allmed=res.json()['response'])

        




if __name__ == '__main__':
    app.run(debug=True)



