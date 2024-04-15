#Задача 4. Хорошего дня!
from flask import Flask
from datetime import datetime

app = Flask(__name__)

weekday = ('Хорошего понедельника!',
           'Хорошего вторника!',
           'Хорошей среды!',
           'Хорошего четверга!',
           'Хорошей пятницы!',
           'Хорошей субботы!',
           'Хорошего воскресенья!'
           )


@app.route("/hello-world/<name>")
def hello_world(name):
    day = datetime.now().weekday()
    return f'Привет, {name}. {weekday[day]}'


if __name__ == '__main__':
    app.run(debug=True)
