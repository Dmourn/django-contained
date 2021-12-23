from django.urls import path, include
from rest_framework import routers, renderers
from . import views

from rest_framework.urlpatterns import format_suffix_patterns


app_name='clockify'

urlpatterns = [
    path('contacts/', views.ContactsList.as_view(), name='contacts'),
    path('accounts/', views.AccountsList.as_view(), name='accounts'),
    path('accounts/<int:account_id>/', views.AccountsDetailView.as_view(), name='accounts-detail'),
    path('client/', views.ClockifyClientList.as_view(), name='client'),
    path('client/<int:clientId>/', views.ClockifyClientDetailView.as_view(), name='client-detail'),
    path('time/', views.ClockifyTimeEntryList.as_view(), name='time'),
    path('project/', views.ClockifyProjectCreateList.as_view(), name='project'),
]
