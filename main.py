from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello_world(): 
    return 'Hello World'

@app.route('/Hello')
def hello_Mees():
  return 'Hello Mees’
  
#if __name__ == '__main__':

  #app.run(debug = True)
app.run(host='0.0.0.0', port=81)


