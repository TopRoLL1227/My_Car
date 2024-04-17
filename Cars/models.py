from django.db import models


# Create your models here.
class Cars(models.Model):
    model = models.CharField(max_length=100)
    brand = models.CharField(max_lenght=100)
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
