from django.db import models

class Solicitud(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    id_number = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    country = models.CharField(max_length=50)


    def __str__(self):
        return '{} - {}'.format(self.name, self.email)
    

