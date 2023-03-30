from django.shortcuts import redirect


def notLoggedUser(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func




def allowedUsers(allowedGroups=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                
                group = request.user.groups.all()[2].name
                
            if group in allowedGroups:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('no_permission')
        return wrapper_func
    return decorator


def tendering_main_index(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='tendering_main_index').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func


def tendering_user_index(view_func):
    def wrapper_func(request, *args, **kwargs):        
        if request.user.groups.filter(name='tendering_user_index').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func

# CONTRACT DECORATORS ------------------ CONTRACT DECORATORS ---------------------- CONTRACT DECORATORS -------------------

def contract_main_index(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='contract_main_index').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func


def contract_user_index(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='contract_user_index').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func


def add_new_contract(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='add_new_contract').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func


def preview_contract(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='preview_contract').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func

def c_1_contract_sector_report_special_project(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='c_1_contract_sector_report_special_project').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func

def c_2_contract_sector_report_special_sector(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='c_2_contract_sector_report_special_sector').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func

def c_main_contract_sector_report(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='c_main_contract_sector_report').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func

def c_1_contract_chech_data_report_special_project(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='c_1_contract_chech_data_report_special_project').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func

def c_2_contract_chech_data_report_special_sector(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='c_2_contract_chech_data_report_special_sector').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func

def c_main_contract_chech_data_report(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='c_main_contract_chech_data_report').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func

def c_1_contract_cost_estimation_report_special_project(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='c_1_contract_cost_estimation_report_special_project').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func

def c_2_contract_cost_estimation_report_special_sector(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='c_2_contract_cost_estimation_report_special_sector').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func

def c_main_contract_cost_estimation_report(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='c_main_contract_cost_estimation_report').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func

def c_1_contract_financial_report_special_project(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='c_1_contract_financial_report_special_project').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func

def c_2_contract_financial_report_special_sector(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='c_2_contract_financial_report_special_sector').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func

def c_main_contract_financial_report(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='c_main_contract_financial_report').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func

def c_1_contract_copy_contract_report_special_project(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='c_1_contract_copy_contract_report_special_project').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func

def c_2_contract_copy_contract_report_special_sector(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='c_2_contract_copy_contract_report_special_sector').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func

def c_main_contract_copy_contract_report(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='c_main_contract_copy_contract_report').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func

def c_1_contract_check_contract_report_special_project(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='c_1_contract_check_contract_report_special_project').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func

def c_2_contract_check_contract_report_special_sector(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='c_2_contract_check_contract_report_special_sector').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func

def c_main_contract_check_contract_report(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='c_main_contract_check_contract_report').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func

def c_1_contract_tcta_report_special_project(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='c_1_contract_tcta_report_special_project').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func

def c_2_contract_tcta_report_special_sector(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='c_2_contract_tcta_report_special_sector').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func

def c_main_contract_tcta_report(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='c_main_contract_tcta_report').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func

def c_1_contract_evp_report_special_project(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='c_1_contract_evp_report_special_project').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func

def c_2_contract_evp_report_special_sector(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='c_2_contract_evp_report_special_sector').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func

def c_main_contract_evp_report(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='c_main_contract_evp_report').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func

def c_1_contract_ceo_report_special_project(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='c_1_contract_ceo_report_special_project').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func

def c_2_contract_ceo_report_special_sector(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='c_2_contract_ceo_report_special_sector').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func

def c_main_contract_ceo_report(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='c_main_contract_ceo_report').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func

def c_1_contract_asgn2_report_special_project(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='c_1_contract_asgn2_report_special_project').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func

def c_2_contract_asgn2_report_special_sector(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='c_2_contract_asgn2_report_special_sector').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func

def c_main_contract_asgn2_report(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='c_main_contract_asgn2_report').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func

def c_1_contract_asgn1_report_special_project(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='c_1_contract_asgn1_report_special_project').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func

def c_2_contract_asgn1_report_special_sector(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='c_2_contract_asgn1_report_special_sector').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func

def c_main_contract_asgn1_report(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='c_main_contract_asgn1_report').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func

def c_1_contract_refuse_report_special_project(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='c_1_contract_refuse_report_special_project').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func

def c_2_contract_refuse_report_special_sector(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='c_2_contract_refuse_report_special_sector').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func

def c_main_contract_refuse_report(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='c_main_contract_refuse_report').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func

def c_1_contract_complete_report_special_project(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='c_1_contract_complete_report_special_project').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func

def c_2_contract_complete_report_special_sector(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='c_2_contract_complete_report_special_sector').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func

def c_main_contract_complete_report(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='c_main_contract_complete_report').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func

def c_1_contract_project_index(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='c_1_contract_project_index').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func

def c_2_sector_manager_action(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='c_2_sector_manager_action').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func

def c_3_check_data_action(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='c_3_check_data_action').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func

def c_4_cost_estimation_action(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='c_4_cost_estimation_action').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func

def c_5_financial_action(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='c_5_financial_action').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func

def c_6_copy_contract_action(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='c_6_copy_contract_action').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func

def c_7_check_contract_action(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='c_7_check_contract_action').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func

def c_8_tcta_action(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='c_8_tcta_action').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func

def c_9_evp_action(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='c_9_evp_action').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func

def c_10_ceo_action(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='c_10_ceo_action').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func

def c_11_assignAttach2_action(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='c_11_assignAttach2_action').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func

def c_12_assignAttach1_action(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='c_12_assignAttach1_action').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func

# PROJECT DECORATORS ------------------ PROJECT DECORATORS ---------------------- PROJECT DECORATORS -------------------

def project_main_index(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='project_main_index').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func


def project_user_index(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='project_user_index').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func


def add_new_tender(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='add_new_tender').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func


def update_tender(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='update_tender').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func


def preview_tender(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='preview_tender').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func



def add_new_project(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='add_new_project').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func


def preview_project(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='preview_project').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func












