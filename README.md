# Tetrika Junior Tasks

![Python 3.11](https://img.shields.io/badge/python-3.11-blue?logo=python&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/beautifulsoup4-4.13.4-yellow?logo=python)
![Requests](https://img.shields.io/badge/requests-2.32.3-lightgrey?logo=python)

Репозиторий содержит решения трёх технических заданий, выполненных в рамках отбора на стажировку/позицию Junior Python Developer.

## Условия выполнения

- Для решения использовать python версии 3.9 или выше 
- Для задания 2 можно использовать библиотеки, задачи 1 и 3 реализовать, используя встроенные средства языка
- Решение каждой задачи должно быть в папке с ее условием, в файле solution.py или в модуле solution
- К каждой задаче необходимо написать тесты

## Задания

### 1. [`@strict`](task1/task1.md)   — типобезопасный декоратор

#### Требование
- Реализовать декоратор, проверяющий соответствие типов переданных аргументов аннотациям в сигнатуре функции.

#### Реализация
 - [`task1/solution/strict_deco.py`](task1/solution/strict_deco.py)

#### Тестирование

```
python -m pytest task1/test/test_strict.py
```

---

### 2. [Парсинг Wikipedia](task2/task2.md) - Животные по алфавиту

#### Требование
- спарсить русскоязычную Википедию (категория «Животные по алфавиту») и сохранить в CSV-файл количество записей по каждой букве.

#### Реализация
- [`task2/solution/main.py`](task2/solution/main.py)

#### Тестирование

```
python -m unittest task2/test/test_animals.py
```

---

### 3. [Совместное присутствие на уроке](task3/task3.md)

#### Требование
- определить общее время пересечения интервалов присутствия ученика и преподавателя на фоне урока.


#### Реализация
- [`task3/solution/total_appearance.py`](task3/solution/total_appearance.py)

#### Тестирование

```
python -m pytest task3/test/test_appearance.py
```

---

## Установка

```bash
# Клонируй проект
git clone https://github.com/wpotoke/tetrika-junior.git

# Перейди в папку
cd tetrika-junior

# Создай и активируй виртуальное окружение
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Установи зависимости
pip install -r requirements.txt
```

## Автор

Решения выполнил [Данила](t.me/amigos_mixtapes) в рамках [технического задания](https://gitlab.com/heiwa.local/tetrika-junior/-/tree/main) от [Тетрика](https://tetrika-school.ru/).
