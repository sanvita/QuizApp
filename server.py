from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

#Pirmā lapa, kas tiks ielādēta
@app.route('/')
def root():
    return render_template("index.html")
    
#Pārbaudes lapa, lai saprastu, ka kods vispār strādā
@app.route('/health')
def health():
  return "OK"

if __name__ == '_main_':
  app.run(debug="true")