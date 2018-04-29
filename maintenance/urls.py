from django.conf.urls import url

from maintenance import views

### These API endpoints are illustrated on https://app.swaggerhub.com/apis/Parrot/parrot-fix_api/1.0.0

urlpatterns = [
    url(r'^maintenance/$', views.NewMaintReqView.as_view()),
    url(r'^maintenance/rooms/$', views.RoomsListView.as_view()),
    url(r'^maintenance/rooms/(?P<room_id>[0-9]+)/$', views.MaintenanceItemListView.as_view()),
    url(r'^maintenance/apartment/(?P<apartment_key>[0-9]+)/$', views.MaintenanceListView.as_view()),
    url(r'^maintenance/(?P<maint_id>[0-9]+)/$', views.MaintenanceDetailView.as_view()),
    url(r'^maintenance/(?P<maint_id>[0-9]+)/update/$', views.MaintenanceUpdateView.as_view()),
    url(r'^maintenance/(?P<maint_id>[0-9]+)/comment/$', views.MaintenanceCommentView.as_view()),
    url(r'^maintenance/staff/(?P<staff_id>[0-9]+)/$', views.StaffMaintenanceView.as_view()),
    url(r'^maintenance/category/(?P<category_id>[0-9]+)/$', views.CategoryMaintenanceView.as_view()),
    url(r'^maintenance/new_issue/$', views.MaintenanceIssue.as_view()),
]