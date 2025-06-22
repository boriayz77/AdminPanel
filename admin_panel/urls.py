
from django.urls import path
from dashboard.views import user_list

urlpatterns = [
    path('', user_list),
]
