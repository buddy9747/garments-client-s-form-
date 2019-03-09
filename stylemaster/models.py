from django.db import models
from datetime import date
# Create your models here.
class Approver(models.Model):
    approve=models.CharField(max_length=100)

    def __str__(self):
        return str(self.approve)

class ProductionMerchant(models.Model):
    production_mrchant=models.CharField(max_length=100)

    def __str__(self):
        return str(self.production_mrchant)

class FactoryMerchant(models.Model):
    factory_mrchant=models.CharField(max_length=100)

    def __str__(self):
        return str(self.factory_mrchant)

class PDMerchant(models.Model):
    pd_mrchant=models.CharField(max_length=100)

    def __str__(self):
        return str(self.pd_mrchant)

class CustomGroup(models.Model):
    custom_grp=models.CharField(max_length=100)

    def __str__(self):
        return str(self.custom_grp)

class Sample(models.Model):
    def number():
        no = Sample.objects.count()
        if no == None:
            return 1
        else:
            return no + 1

    sample_no = models.IntegerField(unique=True, default=number)
    pch=models.CharField(max_length=10)
    style=models.CharField(max_length=100)
    desc=models.TextField(max_length=2500)
    sketch=models.FileField(upload_to="static/images")

    def __str__(self):
        return str(self.pch)

class Stylemaster(models.Model):
    def number():
        no = Stylemaster.objects.count()
        if no == None:
            return 1
        else:
            return no + 1

    style_no = models.IntegerField(unique=True, default=number)
    item_no=models.ForeignKey(Sample,on_delete=models.CASCADE)
    style=models.CharField(max_length=100)
    type=models.CharField(max_length=100)
    brand=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    item_group=models.CharField(max_length=100)
    season=models.CharField(max_length=100,null=True,blank=True)
    responsible=models.CharField(max_length=100)
    approver=models.ForeignKey(Approver,on_delete=models.CASCADE)
    product_designer=models.CharField(max_length=100,null=True,blank=True)
    production_merchant=models.ForeignKey(ProductionMerchant,on_delete=models.CASCADE)
    pd_merchant=models.ForeignKey(PDMerchant,on_delete=models.CASCADE,null=True,blank=True)
    factory_merchant=models.ForeignKey(FactoryMerchant,on_delete=models.CASCADE,null=True,blank=True)
    sales_person=models.CharField(max_length=100)
    basic_uom=models.CharField(max_length=100)
    alt_uom=models.CharField(max_length=100,null=True,blank=True)
    conversion_factor=models.CharField(max_length=100,null=True,blank=True)
    currency=models.CharField(max_length=100)
    sales_price=models.CharField(max_length=100)
    sale_price_qty=models.CharField(max_length=100,null=True,blank=True)
    buying_house_commission=models.CharField(max_length=100,null=True,blank=True)
    licence=models.CharField(max_length=100,null=True,blank=True)
    custom_group=models.ForeignKey(CustomGroup,on_delete=models.CASCADE,null=True,blank=True)
    national_dbk=models.DecimalField(default=0,max_digits=7,decimal_places=4,null=True,blank=True)
    rosl_group=models.CharField(max_length=100,null=True,blank=True)
    propertys=models.CharField(max_length=100,null=True,blank=True)
    order_confirmation_date=models.DateField(("Date"), default=date.today,null=True,blank=True)
    pcd=models.DateField(null=True,blank=True)
    ex_factory_date=models.DateField(null=True,blank=True)

    def __str__(self):
        return str(self.item_no)


FB = [('Fabric00001', 'Fabric00001'),
      ('Fabric00002', 'Fabric00002'),
      ]


class Fabric(models.Model):
    def number():
        no = Fabric.objects.count()
        if no == None:
            return 1
        else:
            return no + 1

    fabric_no = models.IntegerField(unique=True, default=number)
    fabric_item_no = models.ForeignKey(Stylemaster,on_delete=models.CASCADE)
    quality = models.CharField(max_length=20, null=True, blank=True)
    composition = models.CharField(max_length=30)
    weave = models.CharField(max_length=20, null=True, blank=True)
    count = models.CharField(max_length=5, null=True, blank=True)
    construction = models.CharField(max_length=10)
    types = models.CharField(max_length=50, null=True, blank=True)
    fabric_code = models.CharField(max_length=15, choices=FB)

    def __str__(self):
        return str(self.fabric_item_no)


TM = [('Trim00001', 'Trim00001'),
      ('Trim00002', 'Trim00002'),
      ]

''
class Trims(models.Model):
    def number():
        no = Trims.objects.count()
        if no == None:
            return 1
        else:
            return no + 1

    trim_no = models.IntegerField(unique=True, default=number)
    trim_item_no = models.ForeignKey(Stylemaster, on_delete=models.CASCADE)
    quality = models.CharField(max_length=20, null=True, blank=True)
    composition = models.CharField(max_length=30)
    size = models.CharField(max_length=5)
    color = models.CharField(max_length=10, null=True, blank=True)
    construction = models.CharField(max_length=10)
    types = models.CharField(max_length=50, null=True, blank=True)
    trim_code = models.CharField(max_length=10, choices=TM)

    def __str__(self):
        return str(self.trim_item_no)


class BOM(models.Model):
    item_no=models.ForeignKey(Stylemaster,on_delete=models.CASCADE)
    fabconsumption=models.CharField(max_length=20)
    fabquality=models.CharField(max_length=20)
    fabwidth=models.CharField(max_length=10)
    fabunit=models.CharField(max_length=5)
    consumption=models.DecimalField(max_digits=12,decimal_places=5)
    fabrate=models.DecimalField(max_digits=12,decimal_places=5)
    trims=models.CharField(max_length=20)
    trimquality=models.CharField(max_length=20)
    trimspecific=models.CharField(max_length=10)
    trimunit=models.CharField(max_length=5)
    trimconsumption=models.DecimalField(max_digits=12,decimal_places=5)
    trimrate=models.DecimalField(max_digits=12,decimal_places=5)

    def __str__(self):
        return str(self.item_no)
