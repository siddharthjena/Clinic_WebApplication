from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name = 'home'),
    path('register/',views.register,name = 'register'),
    path('doc_reg/',views.doctor_register,name = 'doc_reg'),
    path('patient_reg/',views.patient_register,name = 'patient_reg'),
    path('login/',views.login,name = 'login'),
    path('patient_dashboard/',views.patient_dashboard,name = 'patient_dashboard'),
    path('book_appointment/',views.book_appointment,name = 'book_appointment'),
    path('doctor_dashboard/',views.doctor_dashboard,name = 'doctor_dashboard'),
    path('doc_pers_details/',views.doc_pers_details,name = 'doc_pers_details'),


]