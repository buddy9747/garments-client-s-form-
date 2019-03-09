from django import forms
from .models import *
from rest_framework import serializers


class MyForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('name', 'fact')


class MyForm1(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('name', 'fact', 'fab')


class MyForm2(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('name', 'fact', 'fab', 'was')


class MyForm3(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('name', 'fact', 'fab', 'was', 'cate')

    def __init__(self, value, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cate'].queryset = Category.objects.filter(name=value)


class MyForm4(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('name', 'fact', 'fab', 'was', 'cate', 'subcat')

    def __init__(self, value, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subcat'].queryset = Subcategory.objects.filter(name=value)
        # fields = ('name','fact','fab','was','cate','subcat','dept','sect','subsect')


class MyForm5(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('name', 'fact', 'fab', 'was', 'cate', 'subcat', 'dept')

    def __init__(self, value, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['dept'].queryset = Department.objects.filter(name=value)


class MyForm6(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('name', 'fact', 'fab', 'was', 'cate', 'subcat', 'dept', 'sect')

    def __init__(self, value, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sect'].queryset = Sections.objects.filter(name=value)


class MyForm7(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('name', 'fact', 'fab', 'was', 'cate', 'subcat', 'dept', 'sect', 'subsect')

    def __init__(self, value, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subsect'].queryset = Subsection.objects.filter(name=value)


class YourForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('name', 'fact', 'cate')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cate'].queryset = Category.objects.filter(cat=2)


class YourForm2(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('name', 'fact', 'cate', 'subcat')

    def __init__(self, val, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cate'].queryset = Category.objects.filter(cat=2)
        self.fields['subcat'].queryset = Subcategory.objects.filter(name=val)


class OurForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('name', 'fact', 'cate')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cate'].queryset = Category.objects.filter(cat=3)


class OurForm2(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('name', 'fact', 'cate', 'subcat')

    def __init__(self, val, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cate'].queryset = Category.objects.filter(cat=3)
        self.fields['subcat'].queryset = Subcategory.objects.filter(name=val)


