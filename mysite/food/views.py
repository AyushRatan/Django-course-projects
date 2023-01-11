from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.template import loader

# Create your views here.
'''def index(request):
    item_list = Item.objects.all()
    #template = loader.get_template("food/index.html")
    context = {
        "item_list" : item_list,
    }
    #return HttpResponse(template.render(context,request))
    return render(request,"food/index.html",context)'''

class IndexClassView(ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'item_list'



def item(request):
    return HttpResponse("<h1>This is an item view</h1>")


'''def detail(request,item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        "item":item,
    }
    return render(request,"food/detail.html",context)'''

class FoodDetail(DetailView):
    model = Item
    template_name = "food/detail.html"

def create_item(request):
    form = ItemForm(request.POST or None)
    context = {
        'form':form
    }

    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request,'food/item-form.html',context)

# class based create view

class CreateI


def update_item(request,id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None,instance=item)

    context = {
        'form':form,
        'item':item,
    }

    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request,'food/item-form.html',context)

def delete_item(request,id):
    item = Item.objects.get(id=id)
    context = {
        'item':item,
    }

    if request.method == 'POST':
        item.delete()
        return redirect('food:index')

    return render(request,'food/item-delete.html',context)
