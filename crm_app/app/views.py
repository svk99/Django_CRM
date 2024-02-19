from django.shortcuts import render,redirect
from .models import Customer

# Create your views here.

def home(request):
    cust=Customer.objects.all()
    return render(request,'home.html',{'cust':cust})

def add(request):
    if request.method=='POST':
        print('Added')
        #Get user inputs
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        address=request.POST.get('address')

        c=Customer()
        c.name=name
        c.email=email
        c.phone_number=phone
        c.address=address
        c.save()
        return redirect('/app/home')
    return render(request,'add.html')

def delete(request,id):
    c=Customer.objects.get(pk=id)
    c.delete()

    return redirect('/app/home')

def delete_all(request):
    #if request.method == 'POST':
        # Delete all records
        c=Customer.objects.all()
        c.delete()
        return redirect('/app/home')

   # return render(request, 'delete_all.html')
    #return redirect('/app/home')
def update(request,id):
    cust=Customer.objects.get(pk=id)
    return render(request,'update.html',{'cust':cust})

def do_update(request,id):
    #id=request.POST.get('id')
    name=request.POST.get('name')
    email=request.POST.get('email')
    phone=request.POST.get('phone')
    address=request.POST.get('address')    

    c=Customer.objects.get(pk=id)
    c.name=name
    c.email=email
    c.phone_number=phone
    c.address=address

    c.save()
    return redirect('/app/home')

