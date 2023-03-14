from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def HomePage():
    return render_template('HomePage.html')



@app.route('/Catalog' )
def Catalog(Username):
    return render_template('Catalog.html')

@app.route('/Login', methods = ['POST', 'GET'])
def Login():
  if request.method == 'POST':
    print("submitted")
    redirect(Flask.url_for('Catalog', Username = "zaza"))
  return render_template('Login.html')


app.run(host='0.0.0.0', port=81)
