from flask import Flask
from flask import json
import logging
import sys
app = Flask(__name__)

logging.basicConfig(filename='app.log',level=logging.DEBUG)
root = logging.getLogger()
root.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s , %(message)s')
handler.setFormatter(formatter)
root.addHandler(handler)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')

@app.route("/status")
def status():
    response = app.response_class(
            response=json.dumps({"result":"OK - healthy"}),
            status=200,
            mimetype='application/json'
    )
    app.logger.debug("/status endpoint was reached")
    return response

@app.route("/metrics")
def metrics():
    response = app.response_class(
            response=json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":23}}),
            status=200,
            mimetype='application/json'
    )
    app.logger.debug("/metrics endpoint was reached")   
    return response