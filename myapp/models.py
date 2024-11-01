from django.db import models

class Human(models.Model):
    name = models.CharField(max_length=50)            # Поле для имени
    surname = models.CharField(max_length=50)         # Поле для фамилии
    date_birth = models.DateField()                   # Поле для даты рождения
    place_residence = models.CharField(max_length=100)  # Поле для места проживания

    def __str__(self):
        return f"{self.name} {self.surname}"
