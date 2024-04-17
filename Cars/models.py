from django.db import models
import uuid


class Brand(models.Model):
    Audi = 'Audi'
    Bmw = 'Bmw'
    Mercedes_Benz = 'Mercedes-Benz'
    Volkswagen = 'Volkswagen'
    Skoda = 'Skoda'
    Hyundai = 'Hyundai'
    Chevrolet = 'Chevrolet'
    Ford = 'Ford'
    Honda = 'Honda'
    Infinity = 'Infinity'
    Lexus = 'Lexus'
    Nissan = 'Nissan'
    Mazda = 'Mazda'
    Mitsubishi = 'Mitsubishi'
    Subaru = 'Subaru'
    Peugeot = 'Peugeot'
    Toyota = 'Toyota'

    CAR_CHOICES = [
        (Audi, 'Audi'),
        (Bmw, 'Bmw'),
        (Mercedes_Benz, 'Mercedes-Benz'),
        (Volkswagen, 'Volkswagen'),
        (Skoda, 'Skoda'),
        (Hyundai, 'Hyundai'),
        (Chevrolet, 'Chevrolet'),
        (Ford, 'Ford'),
        (Honda, 'Honda'),
        (Infinity, 'Infinity'),
        (Lexus, 'Lexus'),
        (Nissan, 'Nissan'),
        (Mazda, 'Mazda'),
        (Mitsubishi, 'Mitsubishi'),
        (Subaru, 'Subaru'),
        (Peugeot, 'Peugeot'),
        (Toyota, 'Toyota'),
    ]

    brand_name = models.CharField(max_length=100)

    def __str__(self):
        return f'Бренд - {self.brand_name}'


class Cars(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    model = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=False, null=True, verbose_name='brand')
    generation = models.CharField(max_length=100)
    engine = models.FloatField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    horsepower = models.IntegerField(null=True, blank=True)
    kw = models.IntegerField(null=True, blank=True)
    color = models.CharField(null=True, blank=True)

    def __str__(self):
        return (f'Модель - {self.model}'
                f'Бренд - {self.brand}'
                f'Модифікація кузова - {self.generation}'
                f'Двигун - {self.engine}'
                f'Рік випуску - {self.year}'
                f'Кінські сили - {self.horsepower}'
                f'Кіловати - {self.kw}'
                f'Колір - {self.color}')
