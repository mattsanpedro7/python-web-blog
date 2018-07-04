from flask import Flask

# tell python we are creating Flask app
# __name__: a built in (private) variable
app = Flask(__name__) # '__main__'

# create endpoint
@app.route('/')
def hello_method():
    return 'Hello, dudes'

# requirement to run app
if __name__ == '__main__':
    app.run()