from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import  messages
from django.http import HttpResponse
from stylemaster.models import *
# Create your views here.
from .forms import *
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy
import mathfilters



def sample(request):
    if (request.method == 'POST'):
        form = Sam(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Your Sample is recorded</h1>')
        else:
            messages.error(request, "Error")

    else:
        form = Sam()
    return render(request, 'stylemaster/sample.html', {'form': form})


def style(request):
    if (request.method == 'POST'):
        form = Style(request.POST)
        if form.is_valid():
            s = Sample.objects.all()
            global item
            item = request.POST.get('item_no')
            for i in s:
                if (str(i.id) == item):
                    global value1
                    global value2
                    global value3
                    value1 = i.style
                    value2 = i.desc
                    value3 = i.sketch
            return redirect('/stylefull')
            # return render(request,'stylemaster/stylefull.html',context)
        else:
            messages.error(request, "Error")
            # form['category'].data=i.style
            # form['type'].data=i.desc
            # item=request.GET.values()
            # item=form['item_no'].data
            # item=form['item_no'].field.value
            # form.save()

    else:
        form = Style()
    return render(request, 'stylemaster/style_master.html', {'form': form})


def stylefull(request):
    if (request.method == 'POST'):
        form = StyleFull(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/fabric')
        else:
            messages.error(request, "Error")
    else:
        global value1
        global value2
        global value3
        global item
        form = StyleFull(initial={'item_no': item, 'style': value1, 'type': value2,'sketch':value3})
    return render(request, 'stylemaster/stylefull.html', {'form': form})

def fabric(request):
    if (request.method == 'POST'):
        form = FabricForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/trims')
        else:
            messages.error(request, "Error")

    else:
        global item
        form = FabricForm(initial={'fabric_item_no':item})
    return render(request, 'stylemaster/fabric.html', {'form': form})

def trims(request):
    if (request.method == 'POST'):
        form = TrimsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/preview')
        else:
            messages.error(request, "Error")

    else:
        global  item
        form = TrimsForm(initial={'trim_item_no':item})
    return render(request, 'stylemaster/trim.html', {'form': form})

def preview(request):
    global item
    a=Stylemaster.objects.filter(item_no=item)
    b=Fabric.objects.filter(fabric_item_no=item)
    c=Trims.objects.filter(trim_item_no=item)
    return render(request, 'stylemaster/preview.html',{'a':a,'b':b,'c':c})

class update(UpdateView):
    model = Stylemaster
    fields = ('style_no', 'item_no', 'style', 'type', 'brand', 'category',
              'item_group', 'season', 'responsible',
              'approver', 'product_designer', 'production_merchant',
              'pd_merchant', 'factory_merchant', 'sales_person', 'basic_uom',
              'alt_uom', 'conversion_factor', 'currency', 'sales_price',
              'sale_price_qty', 'buying_house_commission', 'licence',
              'custom_group', 'national_dbk', 'rosl_group', 'propertys',
              'order_confirmation_date', 'pcd', 'ex_factory_date')
    def fun(self,request):
        global item
        item = request.POST.get('item_no')
        print(item)
        return super().fun(request)
    template_name = "stylemaster/stylefull.html"
    success_url = reverse_lazy('preview')

class updatefab(UpdateView):
    model=Fabric
    fields=('fabric_no','fabric_item_no','quality','composition','weave',
                'count','construction','types','fabric_code')
    def fun(self,request):
        global item
        item = request.POST.get('item_no')
        print(item)
        return super().fun(request)
    template_name = "stylemaster/fabric.html"
    success_url = reverse_lazy('preview')

class updatetri(UpdateView):
    model=Trims
    fields=('trim_no','trim_item_no','quality','composition','size',
                'color','construction','types','trim_code')
    def fun(self,request):
        global item
        item = request.POST.get('item_no')
        print(item)
        return super().fun(request)
    template_name = "stylemaster/trim.html"
    success_url = reverse_lazy('preview')

'''
def user_edit(request):

    if request.method == 'POST':
        user_form = Stylemaster(request.POST, instance=request.user)
        profile_form = FabricForm(request.POST, instancel=request.user.profile)

        if all([user_form.is_valid(), profile_form.is_valid()]):
            user = user_form.save()
            profile = profile_form.save()
            return redirect(user)

    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    return render(request, 'accounts/user_form.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })'''

def bom_select(request):
    if (request.method == 'POST'):
        form = Bomselect(request.POST)
        if form.is_valid():
            s = Sample.objects.all()
            global items
            items = request.POST.get('item_no')

            return redirect('/Bill_of_materials')
            #return render(request,'stylemaster/bom.html')
        else:
            messages.error(request, "Error")

    else:
        form = Bomselect()
    return render(request, 'stylemaster/bom_select.html', {'form': form})

def bom(request):
    global items
    a = Stylemaster.objects.filter(item_no=items)
    b = Fabric.objects.filter(fabric_item_no=items)
    c = Trims.objects.filter(trim_item_no=items)
    d = BOM.objects.filter(item_no=items)

    return render(request, 'stylemaster/bom.html', {'a': a, 'b': b, 'c': c,'d':d})

def bomfill(request):
    if (request.method == 'POST'):
        form = Bom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/bomfill')
        else:
            messages.error(request, "Error")

    else:

        form = Bom()
    return render(request, 'stylemaster/bom_fill.html', {'form': form})
