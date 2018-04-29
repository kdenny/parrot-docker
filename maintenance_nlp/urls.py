from django.conf.urls import url

from maintenance_nlp import views

### These API endpoints are illustrated on https://app.swaggerhub.com/apis/Parrot/parrot-fix_api/1.0.0

urlpatterns = [
    url(r'^maintenance/parse_text/$', views.MaintenanceText.as_view())
]