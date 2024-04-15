# Валидаторы. Создание.
"""
Довольно неудобно использовать встроенный валидатор NumberRange для ограничения числа по его длине.
Создадим свой для поля phone. Создайте валидатор обоими способами.
Валидатор должен принимать на вход параметры min и max — минимальная и максимальная длина,
а также опциональный параметр message (см. рекомендации к предыдущему заданию).
"""
from typing import Optional

from flask_wtf import FlaskForm
from wtforms import ValidationError, Field, IntegerField
from wtforms.validators import InputRequired


def number_length(min_: int, max_: int, message: Optional[str] = None):
    def _number_length(field: Field):
        data = field.data
        if len(str(data)) > max_ or len(str(data)) < min_:
            raise ValidationError(message=message)
    return _number_length


class NumberLength:
    def __init__(self, min_=None, max_=None, message=None):
        self.message = message
        self.min = min_
        self.max = max_

    def __call__(self, form: FlaskForm, field: Field):
        data = field.data
        if len(str(data)) > self.max or len(str(data)) < self.min:
            raise ValidationError(message=self.message)


number = IntegerField(validators=[InputRequired(), NumberLength()])