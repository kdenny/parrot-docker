from django.conf.urls import url

from complex_management import views

urlpatterns = [
    url(r'^login/$', obtain_jwt_token),
]