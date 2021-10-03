
from . import views
from django.urls import path,include

urlpatterns = [
    path('',views.index,name="Index"),
    path('contact-us/',views.contact,name="Contact"),
]