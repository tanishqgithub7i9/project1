from django.urls import path
from .import views

urlpatterns =[
    path('',views.index,name='dash'),
    path('adnews/',views.adnews,name="adnews"),
    path('adbranch/',views.adbranch,name="adbranch"),
    path('adcourse/',views.adcourse,name="adcourse"),
    path('adsession/',views.adsession,name="adsession"),
    path('editsession/<id>',views.editsession,name='editsession'),
    path('editbranch/<id>',views.editbranch,name='editbranch'),
    path('editcourse/<id>',views.editcourse,name='editcourse'),
    path('deletebranch/<id>',views.deletebranch,name='deletebranch'),
    path('deletecourse/<id>',views.deletecourse,name='deletecourse'),
    path('deletesession/<id>',views.deletesession,name='deletesession'),
    path('adstudy/',views.adstudy,name='adstudy'),
    path('viewstudy/',views.viewstudy,name='viewstudy'),
    path('editstudy/<id>',views.editstudy,name='editstudy'),
    path('deletestudy/<id>',views.deletestudy,name='deletestudy'),
    # path('editnews/<id>',views.editnews,name='editnews'),
    # path('deletenews/<id>',views.deletenews,name='deletenews'),
]
