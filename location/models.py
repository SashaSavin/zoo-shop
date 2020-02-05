from django.db import models


class Country(models.Model):
    country_name = models.CharField(max_length=30)

    def __str__(self):
        return self.country_name


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='cities')
    city_name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.country.country_name},{self.city_name}'


class Address(models.Model):
    street = models.CharField(max_length=30)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='addresses')

    def __str__(self):
        return f'{self.city.city_name},{self.street}'

