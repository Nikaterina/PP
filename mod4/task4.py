# Время работы системы.
import sys

from flask import Flask

app = Flask(__name__)


a = sys.stdin.readline().split(' ')[1:]
uptime_ = ''.join(a)


@app.route("/uptime", methods=['GET'])
def uptime() -> str:
    UPTIME = uptime_
    return f"Current uptime is {UPTIME}"


if __name__ == '__main__':
    app.run(debug=True)
