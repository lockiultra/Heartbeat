from django.urls import path
from trauma.views import *

urlpatterns = [
    path('', TraumaView.as_view(), name='trauma_index'),
    path('lstm/', TraumaLSTMView.as_view(), name='lstm')
]