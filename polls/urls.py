from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('<int:question_id>/', detail),
    # path('', index),
]
