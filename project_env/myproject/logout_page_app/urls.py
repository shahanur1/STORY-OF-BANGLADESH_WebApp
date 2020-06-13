from django.conf.urls import url
from logout_page_app import views


urlpatterns = [
    url(r'^$', views.logout, name='logout')
]