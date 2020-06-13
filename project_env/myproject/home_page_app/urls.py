from django.conf.urls import url
from home_page_app import views

urlpatterns = [
    url(r'^$', views.homePage, name='homePage')
]