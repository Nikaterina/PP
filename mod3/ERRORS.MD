##  Найденные ошибки
***
### Ошибка № 1
#### Неверные отступы класса Person
Пробелы перед функциями вместо табуляции
***
### Ошибка № 2
#### Возвращение отрицательного возраста
###### Текст ошибки
>Traceback (most recent call last):
  File "D:\Документы\Учеба\Прикладное программирование\PP hw\PP\mod3\task4.py", line 24, in test_correct_get_age
    self.assertTrue(self.Person.get_age() > 0)
AssertionError: False is not true

Перепутаны местами self.yob b now.year
```python
import datetime
def get_age(self):
    now = datetime.datetime.now()
    return self.yob - now.year
```
***
### Ошибка № 3
#### Открыт доступ к данным класса извне

Пример
```python
def __init__(self, name, year_of_birth, address=''):
    self.name = name
    self.yob = year_of_birth
    self.address = address
```
Должно быть
```python
def __init__(self, name, year_of_birth, address=''):
    self.__name = name
    self.__yob = year_of_birth
    self.__address = address
```





