from django.urls import path
from . import views 
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import *

urlpatterns = [
    path('', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),
    path('admin_home_page', views.admin_home_page, name='admin_home_page'),
    path('driver_home_page', views.driver_home_page, name='driver_home_page'),
    path('logout', views.logout, name='logout'),
    path('profile_image', views.profile_image, name='profile_image'),


    path('admin_home_page/toggle-driver/<int:driver_id>/', views.toggle_driver_status, name='toggle_driver_status'),
    # path('admin_home_page/edit-driver/<int:driver_id>/', views.edit_driver, name='edit_driver'),
    path('admin_home_page/delete-driver/<int:driver_id>/', views.delete_driver, name='delete_driver'),

    
    path('accept-request/<int:patient_id>/', views.accept_request, name='accept_request'),
<<<<<<< HEAD
    # path('cancel-ride/<int:patient_id>/', views.cancel_ride, name='cancel_ride'),
    # path('finish-ride/<int:patient_id>/', views.finish_ride, name='finish_ride'),
=======
    path('call_ambulance', views.call_ambulance, name='call_ambulance'),
    path('patient_requests', views.patient_requests, name='patient_requests'),
    path('request_for_acception/<int:id>/', views.request_for_acception, name='request_for_acception'),

>>>>>>> 133a3d2 (Initial commit)


]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)