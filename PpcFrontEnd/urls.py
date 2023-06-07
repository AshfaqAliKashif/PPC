from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('ContactUs/', views.contact, name="contact"),
    path('institutionsList/', views.institutionsList, name="institutionsList"),
    path('login/', views.do_login, name="do_login"),
    path('download/', views.download, name="download"),
    path('tenders/', views.Tenders, name="Tenders"),
    path('Examination/', views.Examination, name="Examination"),
    path('SiteMap/', views.sitemap, name="sitemap"),
    path('faqs/', views.Faqs, name="Faqs"),
    path('Notifications/', views.Notifications, name="Notifications"),
    path('Budget/', views.Budget, name="Budget"),
    path('Services/', views.Services, name="Services"),
    path('Functions/', views.Functions, name="Functions"),
    path('registeredPharmDList/', views.PharmD, name="PharmD"),
    path('registeredTechnicianCollegesList/', views.technician, name="technician"),
    path('PharmacyAssistant/', views.PharmacyAssistant, name="PharmacyAssistant"),
    path('GoodStandingCertificate/', views.GoodStandingCertificate, name="GoodStandingCertificate"),
    path('base/', views.base, name="base"),
    

]



