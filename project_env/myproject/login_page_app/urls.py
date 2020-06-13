from django.conf.urls import url
from login_page_app import views


urlpatterns = [
    url(r'^$', views.login, name='login')
]
