from django.conf.urls import url
from registration_page_app import views

urlpatterns = [
    url(r'^$', views.register, name='register'),
]
