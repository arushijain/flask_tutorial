from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route('/admin')
def hello_admin():
   return 'Hello Admin'

@app.route('/success/<name>')
def success(name):
   return render_template('hello_world.html', name=name);

@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest

@app.route("/")
def index():
   return render_template("index.html")

@app.route('/result')
def result():
   dict = {'phy':50,'che':60,'maths':70}
   return render_template('table.html', result = dict)

@app.route('/marks/<int:score>')
def marks(score):
	return render_template('marks.html', marks = score)

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest',guest = name))

if __name__ == '__main__':
    app.run(debug=True)

