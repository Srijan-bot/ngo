from django.contrib import admin
from django.conf import settings
from django.urls import path
from home import views
from django.conf.urls.static import static
urlpatterns = [
    path('',views.index,name='home'),
    path('/contri',views.contri,name='contri'),
    path('about/',views.about,name='about')

]

