from django.urls import path
from . import views


urlpatterns = [
    path('tendering_main_index/', views.tendering_main_index, name='tendering_main_index'),
    path('tendering_user_index/', views.tendering_user_index, name='tendering_user_index'),
    path('add_new_tender/', views.add_new_tender, name='add_new_tender'),
    path('update_tender/<int:id>', views.update_tender, name='update_tender'),
    path('tender_details/', views.tender_details, name='tender_details'),
    path('tender_report/', views.tender_report, name='tender_report'),
    path('tender_details_details/<int:id>', views.tender_details_details, name='tender_details_details'),
]