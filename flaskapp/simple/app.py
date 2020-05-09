from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('sample.html')

@app.route('/test')
def test():
   return render_template('test.html')

@app.route('/static')
def api():
   return "<h1> Welcome to Static text </h1> "

if __name__ == '__main__':
   app.run()
