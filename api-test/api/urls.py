from django.urls import path, include
from rest_framework import routers, renderers

from rest_framework.urlpatterns import format_suffix_patterns


router = routers.DefaultRouter()

app_name='api'

#urlpatterns = format_suffix_patterns([
urlpatterns = [
    path('', include(router.urls)),
    path('clockify/', include('clockify.urls', namespace='clockify')),
]
