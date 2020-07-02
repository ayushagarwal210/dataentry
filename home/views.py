from django.shortcuts import render,HttpResponse
from home.models import table
# Create your views here.
def home(request):
    tables= table.objects.all()
    context={'tables':tables}
    return render(request,'index.html',context)

def search(request):
    search= request.GET['search']
    tables=table.objects.filter(first__icontains=search)
    params={'tables':tables, 'search':search}
    return render(request,'search.html',params)