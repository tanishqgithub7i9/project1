from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('adminlogin',views.adlogin,name='adlogin'),
    path('logout/',views.logout,name='logout'),
    path('reg/',views.reg,name='reg'),
    path('Login/',views.Login,name='Login'),
    path("biotech/org.html", views.org, name="org_html"),
    path("biotech/home.html", views.home, name="home_html"),
    path("biotech/why_biotech.html", views.why_biotech, name="why_biotech_html"),
    path("biotech/location.html", views.location, name="location_html"),
    path("biotech/certification.html", views.certification, name="certification_html"),
    path("biotech/collaborators.html", views.collaborators, name="collaborators_html"),
    path("biotech/knowledge_network.html", views.knowledge_network, name="knowledge_network_html"),
    path("biotech/outreach_activity.html", views.outreach_activity, name="outreach_activity_html"),
    
]