from django.shortcuts import render,redirect
from . models import Task
from django.shortcuts import render,get_object_or_404
from django.contrib import messages
from  django.views.generic.edit import DeleteView
from django.views.generic.detail import DetailView


def demo(request):
    task1 = Task.objects.all()
    if request.method=='POST':
        num=request.POST.get('num','')
        name=request.POST.get('name','')
        decription=request.POST.get('decription','')
        task=Task(num=num,name=name,decription=decription)
        task.save()
    return render(request,'home.html',{'task1':task1})

def delete (request,id):
    task=Task.objects.get(id=id)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request, 'delete.html')
    # return render(request,'delete.html')

def update(request, id):
    contact1 = Task.objects.all()
    contact = Task.objects.get(id=id)

    if request.method == 'POST':
        num = request.POST.get('num', '')
        name = request.POST.get('name', '')
        decription = request.POST.get('decription', '')

        contact.num = num
        contact.name = name
        contact.decription = decription
        contact.save()

        return redirect('/')

    return render(request, 'update.html', {'contact1': contact1, 'contact': contact})


