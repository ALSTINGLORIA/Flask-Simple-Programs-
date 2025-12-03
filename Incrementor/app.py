from flask import Flask,render_template,redirect, url_for

app = Flask(__name__)
count = 0
@app.route('/')
def home():
    return render_template("home.html",count = count)

@app.route('/counter',methods=['POST'])
def counter():
    global count
    count+=1
    return redirect(url_for('home'))

app.run()
