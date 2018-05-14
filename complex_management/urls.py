from django.conf.urls import url

from complex_management import views

urlpatterns = [
    url(r'^floorplans/$', views.FloorplanView.as_view()),
    url(r'^floorplans/(?P<floorplan_id>[0-9]+)/$', views.FloorplanView.as_view()),
    url(r'^properties/$', views.PropertyView.as_view()),
    url(r'^property/(?P<property_id>[0-9]+)/$', views.PropertyView.as_view()),
    url(r'^property/(?P<property_id>[0-9]+)/floorplans/', views.FloorplanView.as_view()),
    url(r'^rooms/(?P<room_id>[0-9]+)/$', views.RoomItemList.as_view()),
    # url(r'^rooms/(?P<room_id>[0-9]+)/items/(?P<item_id>[0-9]+)', views.ItemIssues.as_view()),

    # url(r'^rooms/(?P<room_id>[\w\-]+)/$', views.RoomItems.as_view()),
    # url(r'^rooms/(?P<room_id>[\w\-]+)/items/(?P<item_id>[\w\-]+)/$', views.ItemIssues.as_view()),
]