#Задача 5. Максимальное число.
from flask import Flask

app = Flask(__name__)


@app.route("/max_number/<path:nums>")
def max_nums(nums):
    nums = nums.split('/')
    try:
        nums_int = [int(x) for x in nums]
    except ValueError:
        return 'Ошибка, должны быть только числа!'
    return f'Максимальное число: {max(nums_int)}'


if __name__ == '__main__':
    app.run(debug=True)
