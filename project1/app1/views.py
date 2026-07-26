from django.shortcuts import render,redirect
from django.http import HttpResponse
from app1.models import *
# Create your views here.
def home(req):
    if req.method=='POST':
        d=req.POST.get('item_id')
        c=menuitem.objects.get(d)
        return render(req,'menu_details.html',{'item':c})
    menu=menuitem.objects.all().order_by('-id')[:3]
    return render(req,'home.html',{'recent_items':menu})

def menu_list(req):
    return render(req,'menu_list.html',{'menu_items':menuitem.objects.all()})

def menu_details(req):
    if req.method=='POST':
        d=req.POST.get('item_id')
        c=menuitem.objects.get(id=d)
        table_=dinning_table.objects.all()
        return render(req,'menu_details.html',{'item':c,'available_tables':table_})
    else:
        return render(req,'menu_list.html',{'menu_items':menuitem.objects.all()})
def category_list(req):
    category_=category.objects.all()
    return render(req,'category_list.html',{'categories':category_})

def chef_list(req):
    return render(req,'chef_list.html',{'chefs':chef.objects.all()})

def add_menu_item(req):
    obj=add_menuitem
    if req.method=='POST':
        form=add_menuitem(req.POST)
        form.save() 
        return redirect('menu_list')
    else:

        return render(req,'add_menu_item.html',{'key':obj})
    
def add_new_chef(req):
    obj=new_chef
    if req.method=='POST':
        form=new_chef(req.POST)
        form.save() 
        return redirect('chef_list')
        
        
    else:
        return render(req,'add_chef.html',{'key':obj})