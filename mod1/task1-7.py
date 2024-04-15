from flask import Flask
import random
import datetime
import re

app = Flask(__name__)

lst_cats = ['корниш-рекс', 'русская голубая', 'шотландская вислоухая', 'мейн-кун', 'манчкин']
lst = ['Chevrolet', 'Renault', 'Ford', 'Lada']

with open('mod1/war_and_peace.txt', 'r', encoding='utf8') as f:
    lst_book_words = re.findall(r'\w+', f.read())


@app.route("/")
def hello():
    return 'Hello world'


@app.route('/cars')
def cars():
    return 'Chevrolet, Renault, Ford, Lada'


@app.route('/cats')
def cats():
    n = random.randint(0, 4)
    return lst_cats[n]


@app.route('/get_time/now')
def get_time_now():
    current_time = datetime.datetime.now().time()
    return f'Точное время:{current_time}'


@app.route('/get_time/future')
def get_time_future():
    current_time_after_hour = datetime.timedelta(hours=1) + datetime.datetime.now()
    return f'Точное время через час будет: {current_time_after_hour.time()}'


@app.route('/get_random_word')
def get_random_word():
    rand_word = random.choice(lst_book_words)
    return f'случайное слово: {rand_word}'


@app.route('/counter')
def counter():
    counter.visits += 1
    return f'счетчик:{counter.visits}'


counter.visits = 0

if __name__ == '__main__':
    app.run(debug=True, port=8000)
