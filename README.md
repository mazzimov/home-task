# Домашнее задание: Модель Human в Django

## Описание задания

В рамках домашнего задания была создана модель `Human` в Django с полями:
- `name` – имя человека,
- `surname` – фамилия человека,
- `date_birth` – дата рождения,
- `place_residence` – место проживания.

Модель была создана, миграции были применены, и данные сохранены в базе данных SQLite.

## Шаги выполнения

### 1. Создание проекта и приложения

- Создан проект Django с именем `myproject`.
- В проекте создано приложение `myapp`, в котором определена модель `Human`.

### 2. Описание модели Human

Модель находится в файле `myapp/models.py` и выглядит следующим образом:

```python
from django.db import models

class Human(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    date_birth = models.DateField()
    place_residence = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} {self.surname}"
