from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
    return """
        <body style='font-family: segoe-ui;'>
            <center>
                <label style='font-size: 16px;'>increment.io Status</label>
                <br>
                <hr>
                <br>
                <label style='font-size: 30px; color: green;  font-weight: bold;'>ONLINE</label>
            </center>
        </body>
    """

def run():
    app.run(host="0.0.0.0", port="8080")

def keep_alive():
    server = Thread(target=run)
    server.start()
