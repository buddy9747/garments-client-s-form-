from django.urls import path
from stylemaster import views
from M3_Project import settings
from django.conf.urls.static import static

urlpatterns=[
    path('sample/', views.sample, name='sample'),
    path('stylemaster/', views.style, name='style'),
    path('stylefull/', views.stylefull, name='stylefull'),
    path('fabric/', views.fabric, name='fabric'),
    path('trims/', views.trims, name='trims'),
    
    path('preview/',views.preview,name='preview'),
    path('BOM_selection/',views.bom_select,name='bom_select'),
    path('bomfill/',views.bomfill,name='bomfill'),
    path('Bill_of_materials/',views.bom,name='bom'),
    path('updatefab/<int:pk>',views.updatefab.as_view(),name='updatefab'),
    path('updatetri/<int:pk>',views.updatetri.as_view(),name='updatetri'),
    path('update/<int:pk>',views.update.as_view(),name='update'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
