from django.db import models

# Create your models here.
class photo(models.Model):
    title=models.CharField(max_length=25)
    image = models.ImageField(upload_to='photos/')

    def __str__(self):
        return self.title



class Booking(models.Model):
    full_name=models.CharField(max_length=100)
    Phone_number=models.IntegerField()
    Email_id=models.EmailField()
    Booing_date=models.DateField()
    address = models.CharField(max_length=200)
    category=(('a','marrage'),('b','birthday'),('c','reception'),('d','engagement'),('e','govt.ceremony'))
    category=models.CharField(max_length=60,choices=category,null=True)

    def __str__(self):
        return self.full_name

class Review(models.Model):
    name = models.CharField(max_length=100)
    comment = models.TextField()
    rating = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    place=models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)