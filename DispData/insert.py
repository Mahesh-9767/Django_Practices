import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DispData.settings')
import django
django.setup()


from myapp.models import student9767
from faker import Faker
def inserting(n):
    for i in range(n):
        f=Faker(n)
        name=f.name()
        add=f.city()
        age=f.random_int(min=10,max=30)
        dob=f.date()
        student9767.objects.get_or_create(name=name,add=add,age=age,dob=dob)
        
n=int(input('Enter a Number :'))
inserting(n)
print(f'{n} data is Inserting Successfully')
        

