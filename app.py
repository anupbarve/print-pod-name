import os
from flask import Flask
from flask import jsonify
app = Flask(__name__)

def get_pod_name():
    pod_name = os.getenv('MY_POD_NAME')
    return pod_name

@app.route('/pod_name')
def podname():
    pod_name = get_pod_name() 
    print(pod_name)
    return str(pod_name) 

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    print("I am inside hello world")
    return 'Hello World! I can make change at route: /change'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
