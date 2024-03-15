from django.urls import path
from django.views.generic import DetailView

from tapls.views import NewsListView

from tapls.models import Tapls

from tapls.views import tapls_detail_view


app_name = 'tapls'

urlpatterns = [
    path('', NewsListView.as_view(), name='tapls_list'),
    path('tapls/<int:pk>/', tapls_detail_view, name='details'),
]