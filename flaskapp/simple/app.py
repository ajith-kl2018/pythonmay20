from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('sample.html')

@app.route('/test')
def test():
   return render_template('test.html')

if __name__ == '__main__':
   app.run()
