from flask import Flask,render_template,request,redirect,url_for
app=Flask(__name__)
d={
    "MD01":{"id":"MD01","name":"dolo","price":350,"status":"production stage"},
   "MD02":{"id":"MD02","name":"pan","price":400,"status":"transport stage"}
   }
@app.route('/',methods=["GET","POST"])
def hello():
    if request.method=="GET":
        return render_template('home.html')
    else:
        val=request.form['med']
        if val in d:
            m=d[val]
            return render_template('home1.html',flag=1,id=m['id'],name=m['name'],price=m["price"],status=m["status"])
        else:
            return render_template('home1.html',flag=0)



@app.route('/track-medicine',methods=["GET","POST"])
def track_medicine():
    d={"MD01":{"id":"MD01","name":"dolo","price":350}}
    if request.method=="POST":
        return redirect(url_for('.hello',a=d))

if __name__ == '__main__':
    app.run(debug=True)



