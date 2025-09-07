# Геометрические фигуры и анализ данных PySpark

## Структура проекта
```bash
project/
├── task_2/
│ ├── figures/
│ │ ├── __init__.py
│ │ ├── virtual.py 
│ │ ├── circle.py 
│ │ └── triangle.py
│ ├── test/
│ │ ├── test_circle.py
│ │ └── test_triangle.py
│ ├── __init__.py
│ └── main.py 
└── task_3/
└── dataframe.py # Анализ данных PySpark
```

## Запуск программ

### Task 2: Геометрические фигуры

```bash
cd task_2

python main.py
```

Для запуска тестов воспользовать:
```bash
pip install requirements.txt

pytest .
```
### Task 3: Анализ данных PySpark

Установка зависимостей:

```bash
pip install pyspark
```

Запуск:

```bash
cd task_3

python dataframe.py
```

