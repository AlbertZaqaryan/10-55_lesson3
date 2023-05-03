from django.db import models

# Create your models here.

class HomeInfo(models.Model):

    name = models.CharField('HomeInfo name', max_length=200)
    about = models.TextField('HomeInfo about')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']

class Car(models.Model):

    model = models.CharField('Car model', max_length=100)
    img = models.ImageField('Car image', upload_to='car_images')
    price = models.PositiveBigIntegerField('Car price')

    def __str__(self):
        return self.model
    

class Cart(models.Model):

    car = models.ForeignKey(Car, on_delete=models.CASCADE)