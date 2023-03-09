from csk.views import *
from django.urls import path
app_name='nothing'
urlpatterns=[
    path('dhoni/', dhoni, name='dhoni'),
    path('raina/',raina, name='raina'),
]