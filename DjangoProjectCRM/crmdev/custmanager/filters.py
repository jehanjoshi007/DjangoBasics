import django_filters
from .models import *
from django_filters import DateFilter

class OrderFilter(django_filters.FilterSet):
    #lte = less than or equat to and gte=greater than or equalto
    start_date = DateFilter(field_name="date_created", lookup_expr="gte")
    #end_date = DateFilter(field_name="date_created", lookup_expr="lte")
    #Using a contains filter for text fields
    #note = CharFilter(field_name='note',lookup_expr='icontains')
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer','date_created','note']
