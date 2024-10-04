from flask import Flask

app = Flask(__name__)

from routes.route import *

if __name__ == "__main__":
    ip = "172.31.1.56"
    port = "80"
    app.run(ip, port, debug=True) 
 