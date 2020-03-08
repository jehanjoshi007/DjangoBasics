#python manage.py shell to bring up the shell
#from custmanager.models import *

#Return all customers
customers = Customer.objects.all()

#returns first customer
firstcustomer = Customer.objects.first()

#returns last customer
lastcustomer = Customer.objects.last()

#returns single customer by name
customerbyname = Customer.objects.get(name="Test")

#return customer by id
custid = Customer.objects.get(id=4)

#returning all orders related to first customer
relatedorders = firstcustomer.order_set.all()

#return customer from orders
order = Order.objects.first()
custdata = order.customer.name

#using filter to filter data
filter = Product.objects.filter(category="NonWoven")

#Using order by
ascending = Product.objects.all().order_by('id')
dscending = Product.objects.all().order_by('-id')

# Return product tag (Many-Many fields)
filtered = Product.objects.filter(tags__name="Automobile")

#Count of each product ordered

allorders = {}

for order in firstcustomer.order_set.all():
    if order.product.name in allorders:
        allorders[order.product.name] += 1
    else:
        allorders[order.product.name] = 1


#Accessing Child from Parent

class ParentModel(models.Model):
	name = models.CharField(max_length=200, null=True)

class ChildModel(models.Model):
	parent = models.ForeignKey(Customer)
	name = models.CharField(max_length=200, null=True)

parent = ParentModel.objects.first()
#Returns all child models related to parent
parent.childmodel_set.all()

#How to perform join and group by
cust_orders = Order.objects.select_related('customer','product').order_by('ponumber','linenumber').all()
