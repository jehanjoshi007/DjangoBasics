from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200, null=True,unique=True)
    email = models.CharField(max_length=200, null=True,unique=True)
    phone = models.CharField(max_length=200,null=True)
    state = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.name


class Product(models.Model):
    CATEGORY = (('NonWoven','NonWoven'),
              ('Woven','Woven'),
              ('Other','Other'))
    name = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=200, null=True,choices=CATEGORY)
    description =  models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name




class Order(models.Model):
    STATUS = (('To Be Planned','To Be Planned'),
              ('Planned','Planned'),
              ('On Hold','On Hold'))
    customer = models.ForeignKey(Customer, null=True, on_delete = models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete = models.SET_NULL)
    ponumber = models.CharField(max_length=200, null=True)
    linenumber = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    QuantityY2 =  models.FloatField(null=True)
    QuantityRolls =  models.FloatField(null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    status =models.CharField(max_length=200, null=True,choices=STATUS)


    def display_totalprice(self):
        return self.price * self.QuantityY2
