from django.urls import path
from .views import *


urlpatterns = [
    path("get_key/", GetKey.as_view()),
    path("use_key/", UseKey.as_view()),
    path("check_key/", CheckKey.as_view()),
    path("count_keys/", CountKeys.as_view()),
]
