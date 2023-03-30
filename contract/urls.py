from django.urls import path
from . import views


urlpatterns = [
    path('contract_main_index/', views.contract_main_index, name='contract_main_index'),
    path('contract_main_index_viewall/', views.contract_main_index_viewall, name='contract_main_index_viewall'),
    path('contract_sector_index/', views.contract_sector_index, name='contract_sector_index'),
    path('contract_sector_index_viewall/', views.contract_sector_index_viewall, name='contract_sector_index_viewall'),
    path('contract_project_index/', views.contract_project_index, name='contract_project_index'),
    path('contract_project_index_viewall/', views.contract_project_index_viewall, name='contract_project_index_viewall'),
    path('contract_cost_estimation_index/', views.contract_cost_estimation_index, name='contract_cost_estimation_index'),
    path('contract_cost_estimation_index_viewall/', views.contract_cost_estimation_index_viewall, name='contract_cost_estimation_index_viewall'),

# اضافة عقد جديد
    path('add_new_contract/', views.add_new_contract, name='add_new_contract'),

# تقارير -----------------------------------------------------
    path('contract_notification/', views.contract_notification, name='contract_notification'),
    path('contract_notification_read/<int:id>', views.contract_notification_read, name='contract_notification_read'),
# phase 2 ---------------
    path('contract_sector_report_special_project/', views.contract_sector_report_special_project, name='contract_sector_report_special_project'),
    path('contract_sector_report_special_sector/', views.contract_sector_report_special_sector, name='contract_sector_report_special_sector'),
    path('contract_sector_report_special_cost_estimation/', views.contract_sector_report_special_cost_estimation, name='contract_sector_report_special_cost_estimation'),
    path('contract_sector_report/', views.contract_sector_report, name='contract_sector_report'),
# phase 3 ---------------
    path('contract_chech_data_report_special_project/', views.contract_chech_data_report_special_project, name='contract_chech_data_report_special_project'),
    path('contract_chech_data_report_special_sector/', views.contract_chech_data_report_special_sector, name='contract_chech_data_report_special_sector'),
    path('contract_chech_data_report_special_cost_estimation/', views.contract_chech_data_report_special_cost_estimation, name='contract_chech_data_report_special_cost_estimation'),
    path('contract_chech_data_report/', views.contract_chech_data_report, name='contract_chech_data_report'),
# phase 4 ---------------
    path('contract_cost_estimation_report_special_project/', views.contract_cost_estimation_report_special_project, name='contract_cost_estimation_report_special_project'),
    path('contract_cost_estimation_report_special_sector/', views.contract_cost_estimation_report_special_sector, name='contract_cost_estimation_report_special_sector'),
    path('contract_cost_estimation_report_special_cost_estimation/', views.contract_cost_estimation_report_special_cost_estimation, name='contract_cost_estimation_report_special_cost_estimation'),
    path('contract_cost_estimation_report/', views.contract_cost_estimation_report, name='contract_cost_estimation_report'),
# phase 5 ---------------
    path('contract_financial_report_special_project/', views.contract_financial_report_special_project, name='contract_financial_report_special_project'),
    path('contract_financial_report_special_sector/', views.contract_financial_report_special_sector, name='contract_financial_report_special_sector'),
    path('contract_financial_report_special_cost_estimation/', views.contract_financial_report_special_cost_estimation, name='contract_financial_report_special_cost_estimation'),
    path('contract_financial_report/', views.contract_financial_report, name='contract_financial_report'),
# phase 6 ---------------
    path('contract_copy_contract_report_special_project/', views.contract_copy_contract_report_special_project, name='contract_copy_contract_report_special_project'),
    path('contract_copy_contract_report_special_sector/', views.contract_copy_contract_report_special_sector, name='contract_copy_contract_report_special_sector'),
    path('contract_copy_contract_report_special_cost_estimation/', views.contract_copy_contract_report_special_cost_estimation, name='contract_copy_contract_report_special_cost_estimation'),
    path('contract_copy_contract_report/', views.contract_copy_contract_report, name='contract_copy_contract_report'),
 # phase 7 ---------------
    path('contract_check_contract_report_special_project/', views.contract_check_contract_report_special_project, name='contract_check_contract_report_special_project'),
    path('contract_check_contract_report_special_sector/', views.contract_check_contract_report_special_sector, name='contract_check_contract_report_special_sector'),
    path('contract_check_contract_report_special_cost_estimation/', views.contract_check_contract_report_special_cost_estimation, name='contract_check_contract_report_special_cost_estimation'),
    path('contract_check_contract_report/', views.contract_check_contract_report, name='contract_check_contract_report'),
 # phase 8 ---------------   
    path('contract_tcta_report_special_project/', views.contract_tcta_report_special_project, name='contract_tcta_report_special_project'),
    path('contract_tcta_report_special_sector/', views.contract_tcta_report_special_sector, name='contract_tcta_report_special_sector'),
    path('contract_tcta_report_special_cost_estimation/', views.contract_tcta_report_special_cost_estimation, name='contract_tcta_report_special_cost_estimation'),
    path('contract_tcta_report/', views.contract_tcta_report, name='contract_tcta_report'),
# phase 9 ---------------
    path('contract_evp_report_special_project/', views.contract_evp_report_special_project, name='contract_evp_report_special_project'),
    path('contract_evp_report_special_sector/', views.contract_evp_report_special_sector, name='contract_evp_report_special_sector'),
    path('contract_evp_report_special_cost_estimation/', views.contract_evp_report_special_cost_estimation, name='contract_evp_report_special_cost_estimation'),
    path('contract_evp_report/', views.contract_evp_report, name='contract_evp_report'),
# phase 10 ---------------
    path('contract_ceo_report_special_project/', views.contract_ceo_report_special_project, name='contract_ceo_report_special_project'),
    path('contract_ceo_report_special_sector/', views.contract_ceo_report_special_sector, name='contract_ceo_report_special_sector'),
    path('contract_ceo_report_special_cost_estimation/', views.contract_ceo_report_special_cost_estimation, name='contract_ceo_report_special_cost_estimation'),
    path('contract_ceo_report/', views.contract_ceo_report, name='contract_ceo_report'),
# phase 11 ---------------
    path('contract_asgnmnt_report_special_project/', views.contract_asgnmnt_report_special_project, name='contract_asgnmnt_report_special_project'),
    path('contract_asgnmnt_report_special_sector/', views.contract_asgnmnt_report_special_sector, name='contract_asgnmnt_report_special_sector'),
    path('contract_asgnmnt_report_special_cost_estimation/', views.contract_asgnmnt_report_special_cost_estimation, name='contract_asgnmnt_report_special_cost_estimation'),
    path('contract_asgnmnt_report/', views.contract_asgnmnt_report, name='contract_asgnmnt_report'),

# refuse ---------------
    path('contract_refuse_report_special_project/', views.contract_refuse_report_special_project, name='contract_refuse_report_special_project'),
    path('contract_refuse_report_special_sector/', views.contract_refuse_report_special_sector, name='contract_refuse_report_special_sector'),
    path('contract_refuse_report_special_cost_estimation/', views.contract_refuse_report_special_cost_estimation, name='contract_refuse_report_special_cost_estimation'),
    path('contract_refuse_report/', views.contract_refuse_report, name='contract_refuse_report'),
# complete ---------------
    path('contract_complete_report_special_project/', views.contract_complete_report_special_project, name='contract_complete_report_special_project'),
    path('contract_complete_report_special_sector/', views.contract_complete_report_special_sector, name='contract_complete_report_special_sector'),
    path('contract_complete_report_special_cost_estimation/', views.contract_complete_report_special_cost_estimation, name='contract_complete_report_special_cost_estimation'),
    path('contract_complete_report/', views.contract_complete_report, name='contract_complete_report'),

# اجراءات
    path('sector_manager_action/<str:pk>', views.sector_manager_action, name='sector_manager_action'),
    path('check_data_action/<str:pk>', views.check_data_action, name='check_data_action'),
    path('cost_estimation_action/<str:pk>', views.cost_estimation_action, name='cost_estimation_action'),
    path('financial_action/<str:pk>', views.financial_action, name='financial_action'),
    path('copy_contract_action/<str:pk>', views.copy_contract_action, name='copy_contract_action'),
    path('check_contract_action/<str:pk>', views.check_contract_action, name='check_contract_action'),
    path('tcta_action/<str:pk>', views.tcta_action, name='tcta_action'),
    path('evp_action/<str:pk>', views.evp_action, name='evp_action'),
    path('ceo_action/<str:pk>', views.ceo_action, name='ceo_action'),
    path('assignmnt_action/<str:pk>', views.assignmnt_action, name='assignmnt_action'),

]