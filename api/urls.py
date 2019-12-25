from django.urls import path

from api.views import PageList

urlpatterns = [
    path('wiki/', PageList.as_view(), name='wiki_list'),
]
