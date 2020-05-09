from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('sample.html')

@app.route('/curve')
def curve():
   return render_template('FlattenTheCurve.html')

if __name__ == '__main__':
   app.run()

