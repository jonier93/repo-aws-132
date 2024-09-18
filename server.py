from flask import Flask, render_template

app = Flask(__name__)

@app.route('/register_page')
def register():
    return render_template("register.html")

if __name__ == "__main__":
    ip = "172.31.1.56"
    port = "80"
    app.run(ip, port)