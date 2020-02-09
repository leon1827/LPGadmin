from . import views
from django.urls import path


app_name = 'cylinders'
urlpatterns = [
    path('', views.index, name='index'),
    path('page1_gp/', views.page1_gp, name='page1_gp'),
    path('addGp/', views.addGp, name='addGp'),
    
    path('gp_code/<str:gp_code>', views.lookupBygp, name='lookupBygp'),
]