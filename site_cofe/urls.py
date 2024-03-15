from django.urls import path

from site_cofe.views import SiteListView

app_name = "site_cofe"

urlpatterns = [
    path('main/', SiteListView.as_view(), name="main")
]