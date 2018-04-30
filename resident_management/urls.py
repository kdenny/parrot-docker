from django.conf.urls import url

from packagemanager import views
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token
from resident_management.views import *

urlpatterns = [
    url(r'^login/$', obtain_jwt_token),
    url(r'^verify_token/$', verify_jwt_token),
    url(r'^get_username/$', Username.as_view()),
    url(r'^resident/(?P<apt_no>[0-9]+)/home/$', ResidentHomeView.as_view()),
]