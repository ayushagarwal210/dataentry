from django.shortcuts import render,HttpResponse,redirect
from home.models import table
from django.contrib import messages
# Create your views here.
def home(request):
    tables= table.objects.all()
    context={'tables':tables}
    return render(request,'index.html',context)

def search(request):
    search= request.GET['search']
    tablesfirst=table.objects.filter(first__icontains=search)
    tableslast=table.objects.filter(last__icontains=search)
    tablesphone=table.objects.filter(phone__icontains=search)
    tables=tablesfirst.union(tableslast.union(tablesphone))
    params={'tables':tables, 'search':search}
    return render(request,'search.html',params)

def create(request):
    if request.method=='POST':
        first = request.POST.get('first')
        last = request.POST.get('last')
        phone = request.POST.get('phone')
        create=table(first=first, last=last, phone=phone)
        create.save()
    return redirect('home')