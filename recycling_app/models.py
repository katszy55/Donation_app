from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Institution(models.Model):
    FUNDACJA = 'fundacja'
    ORGANIZACJA_POZARZADOWA = 'organizacja pozarządowa'
    ZBIÓRKA_LOKALNA = 'zbiórka lokalna'

    TYPE_CHOICES = (
        (FUNDACJA , 'Fundacja'),
        (ORGANIZACJA_POZARZADOWA, 'Organizacja pozarządowa'),
        (ZBIÓRKA_LOKALNA, 'Zbóirka lokalna')
    )

    name = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=100, choices=TYPE_CHOICES, default=FUNDACJA),
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name





