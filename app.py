from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route("/")
def hello():

        contents = ""
        try:
            f = open('/etc/config/surprise', 'rb')
            for line in f.readlines():
                contents += line
        except IOError:
            contents =  " \"/etc/config/surprise\": Error reading file:"

        html = "<h3>HAPPY {name}!</h3>" \
               "<b>Hostname:</b> {hostname}<br/>" \
               "<b>Content:</b> {contents}"
        return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), contents=contents)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
