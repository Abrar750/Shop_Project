from django.urls import path
from store.views.index import index

urlpatterns = [
    path('',index)
]
