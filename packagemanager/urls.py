from django.conf.urls import url

from packagemanager import views

urlpatterns = [
    url(r'^packages/$', views.PackagesListView.as_view()),
    url(r'^package_pickup/$', views.PackagePickup.as_view()),
    url(r'^check_barcode/$', views.CheckBarcode.as_view()),
    url(r'^apartments/$', views.ApartmentsListView.as_view()),
    url(r'^home_view/$', views.PackagesByFloor.as_view()),
    url(r'^packages/(?P<apartment_key>[0-9]+)/$', views.PackagesListView.as_view()),
    url(r'^apartments/(?P<apartment_key>[0-9]+)/$', views.ApartmentResidentsView.as_view()),
]