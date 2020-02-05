from django.db import models
from django.contrib.auth.models import AbstractUser


class Image(models.Model):
    image = models.ImageField(upload_to='images/')


class CustomUser(AbstractUser):
    city = models.ForeignKey('location.Address',
                             on_delete=models.SET_NULL,
                             related_name='users',
                             blank=True, null=True),

    avatar = models.ForeignKey(Image, on_delete=models.SET_NULL, related_name='users',
                               blank=True, null=True)

    phone = models.CharField(unique=True, blank=True, null=True, max_length=15)

    def __str__(self):
        return self.username


class Kind(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class SubKind(models.Model):
    name = models.CharField(max_length=30)
    kind = models.ForeignKey(Kind, on_delete=models.CASCADE, related_name='subkinds')

    def __str__(self):
        return f'{self.kind.name},{self.name}'


class Advert(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='adverts')
    name = models.CharField(max_length=30)
    age = models.PositiveSmallIntegerField(blank=True, null=True)
    kind = models.ForeignKey(SubKind, on_delete=models.CASCADE, related_name='adverts')
    price = models.DecimalField(max_digits=13, decimal_places=2)
    added = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    avatars = models.ManyToManyField(Image, related_name='adverts')

    def __str__(self):
        return f'{self.name}, {self.user.username}'


class ImageForAdvert(models.Model):
    adv_image = models.ForeignKey(Advert, on_delete=models.CASCADE, related_name='adverts_image')

