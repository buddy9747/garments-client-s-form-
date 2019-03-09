from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.http import HttpResponse
from .models import *


def register(request):
    if (request.method == 'POST'):
        form = UserCreationForm(request.POST)
        if (form.is_valid()):
            user = form.save()
            user.refresh_from_db()
            user.employee.desig = form.cleaned_data['desig']
            user.save()
            return redirect('/login')
        else:
            messages.error(request, "Error")
    else:
        form = UserCreationForm()

    args = {'form': form}
    return render(request, 'category/signup.html', args)


def query(request):
    if (request.method == 'POST'):
        form = MyForm(request.POST)
        if (form.is_valid()):
            n = form.cleaned_data.get('name')
            s = form.cleaned_data.get('fact')
            print(s)
            if (str(s) == 'Garment'):
                form = MyForm1(request.POST, initial={'fact': s, 'name': n})
                if (form.is_valid()):
                    s1 = form.cleaned_data.get('fab')
                    print(s1)
                    form = MyForm2(request.POST, initial={'fact': s, 'name': n,
                                                          'fab': s1})
                    if (form.is_valid()):
                        s2 = form.cleaned_data.get('was')
                        w = Wash.objects.get(wash=s2)
                        form = MyForm3(w, request.POST, initial={'fact': s, 'name': n,
                                                                 'fab': s1, 'was': s2})
                        if form.is_valid():
                            s3 = form.cleaned_data.get('cate')
                            cc = Category.objects.get(category=s3)
                            form = MyForm4(cc, request.POST, initial={'fact': s, 'name': n,
                                                                      'fab': s1, 'was': s2, 'cate': s3})
                            if (form.is_valid()):
                                s4 = form.cleaned_data.get('subcat')
                                dd = Subcategory.objects.get(subcategory=s4)
                                form = MyForm5(dd, request.POST, initial={'fact': s, 'name': n,
                                                                          'fab': s1, 'was': s2, 'cate': s3,
                                                                          'subcat': s4})
                                if (form.is_valid()):
                                    s5 = form.cleaned_data.get('dept')
                                    sec = Department.objects.get(department=s5)
                                    form = MyForm6(sec, request.POST, initial={'fact': s, 'name': n,
                                                                               'fab': s1, 'was': s2, 'cate': s3,
                                                                               'subcat': s4, 'dept': s5})
                                    if (form.is_valid()):
                                        s6 = form.cleaned_data.get('sect')
                                        sub = Sections.objects.get(section=s6)
                                        form = MyForm7(sub, request.POST, initial={'fact': s, 'name': n,
                                                                                   'fab': s1, 'was': s2, 'cate': s3,
                                                                                   'subcat': s4, 'dept': s5,
                                                                                   'sect': s6})
                                        if (form.is_valid()):
                                            s7 = form.cleaned_data.get('subsect')
                                            print(s7)
                                            form.save()
                                            return HttpResponse('<h1>Good Your data is saved</h1>')

            elif (str(s) == 'Hardgoods'):
                form = YourForm(request.POST, initial={'fact': s, 'name': n})
                if (form.is_valid()):
                    s1 = form.cleaned_data.get('cate')
                    cc = Category.objects.get(category=s1)
                    form = YourForm2(cc, request.POST, initial={'fact': s, 'name': n, 'cate': s1})
                    if (form.is_valid()):
                        s2 = form.cleaned_data.get('subcat')
                        print(s2)
                        form.save()
                        return HttpResponse('<h1>Good Your data is saved</h1>')
            else:
                form = OurForm(request.POST, initial={'fact': s, 'name': n})
                if (form.is_valid()):
                    s1 = form.cleaned_data.get('cate')
                    cc = Category.objects.get(category=s1)
                    form = OurForm2(cc, request.POST, initial={'fact': s, 'name': n, 'cate': s1})
                    if (form.is_valid()):
                        s2 = form.cleaned_data.get('subcat')
                        print(s2)
                        form.save()
                        return HttpResponse('<h1>Good Your data is saved</h1>')
    else:
        form = MyForm()
    return render(request, 'category/query.html', {'form': form})


def fun():
    form = MyForm()
    value = form['fact'].data
    if (str(value) == 'Hardgoods' or str(value) == 'Home Furnishing'):
        return True
    else:
        return False


