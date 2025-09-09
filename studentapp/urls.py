from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('ststudy/',views.ststudy,name='ststudy'),
    path('viewnews/',views.viewnews,name='viewnews'),
    path('stfeed/',views.stfeed,name='stfeed'),
    path('viewstfeed/',views.viewstfeed,name='viewstfeed'),
    path('delfeed/',views.delfeed,name='delfeed')
]