from django import forms

from .models import *


class Sam(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sample_no'].widget.attrs['readonly'] = True

    class Meta:
        model = Sample
        fields = ('sample_no', 'pch', 'style', 'desc', 'sketch')


class Style(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['style_no'].widget.attrs['readonly'] = True

    class Meta:
        model = Stylemaster
        fields = ('style_no', 'item_no')


class StyleFull(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['style_no'].widget.attrs['readonly'] = True

    class Meta:
        model = Stylemaster
        fields = ('style_no', 'item_no', 'style', 'type', 'brand', 'category',
                  'item_group', 'season', 'responsible',
                  'approver', 'product_designer', 'production_merchant',
                  'pd_merchant', 'factory_merchant', 'sales_person', 'basic_uom',
                  'alt_uom', 'conversion_factor', 'currency', 'sales_price',
                  'sale_price_qty', 'buying_house_commission', 'licence',
                  'custom_group', 'national_dbk', 'rosl_group', 'propertys',
                  'order_confirmation_date', 'pcd', 'ex_factory_date')

class FabricForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fabric_no'].widget.attrs['readonly'] = True

    class Meta:
        model = Fabric
        fields = ('fabric_no', 'fabric_item_no', 'quality', 'composition',
                  'weave', 'count', 'construction', 'types', 'fabric_code')


class TrimsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['trim_no'].widget.attrs['readonly'] = True

    class Meta:
        model = Trims
        fields = ('trim_no', 'trim_item_no', 'quality', 'composition',
                  'size', 'color', 'construction', 'types', 'trim_code')

class Bom(forms.ModelForm):
    class Meta:
        model = BOM
        fields = ('item_no','fabconsumption','fabquality','fabwidth','fabunit','consumption','fabrate',
                  'trims','trimquality','trimspecific','trimunit','trimconsumption','trimrate')


class Bomselect(forms.ModelForm):
    class Meta:
        model = Stylemaster
        fields = ('item_no',)
