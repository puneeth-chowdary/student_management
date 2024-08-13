from django.shortcuts import render
from .forms import registerForms,deleteForms,searchform
from .models import register,dele
def display(request):
    if request.method=='POST':
        form=registerForms(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            address=form.cleaned_data['address']
            clas=form.cleaned_data['clas']
            school=form.cleaned_data['school']
            p=register(name=name,address=address,clas=clas,school=school)
            p.save()
            return render(request,'ack.html')
    else:
        form=registerForms()
    return render(request,'output.html',{'form':form})
def delk(request):
    if request.method=="POST":
        del_form=deleteForms(request.POST)
        if del_form.is_valid():
            name=del_form.cleaned_data['name']
            instance=register.objects.filter(name=name).delete()

    return render(request,'Delete.html')
def second(request):
    data=register.objects.all()
    return render(request,'second.html',{'data':data})
def search(request):
    if request.method=="POST":
        sea_form=searchform(request.POST)
        if sea_form.is_valid():
            name=sea_form.cleaned_data['name']
            id=register.objects.get(name=name)
            return render(request,'nic.html',{'id':id})
            

    return render(request,"search.html")