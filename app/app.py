from flask import Flask
app = Flask(_name_)

@app.route('/')
def hello():
return "Hello from jenkins+Docker+GitHub!"

if _name_ == '__main__':
    app.run(host='0.0.0.0',port=5000)