# Текущие процессы
import subprocess, shlex
from flask import Flask, request

app = Flask(__name__)
#/ps?arg=a&arg=u&arg=x


@app.route("/ps/", methods=["GET"])
def ps() -> str:
    args: list[str] = request.args.getlist('arg')
    clean_user_cmd = shlex.quote(''.join(args))
    result = str(subprocess.check_output(["ps", clean_user_cmd]))[2:]
    return f"<pre>Your result</pre>\n{result}"


if __name__ == "__main__":
    app.run(debug=True)
