from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .models import *
from main.models import *
from .forms import *
from .filters import *
from django.contrib.auth.decorators import login_required
from main.decorators import *
from django.db.models import Q
from itertools import chain



# Create your views here.


# اضافة عقد جديد ----------------------------------------------------------------------
@login_required(login_url='login')

@add_new_contract

def add_new_contract(request):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)

    form = Contract_Detail_Form
    if request.method == 'POST':
        form = Contract_Detail_Form(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.creator = request.user
            instance.creator_name = user_profile.full_name
            instance.sector = user_profile.sector_name
            instance.project = user_profile.project_name
            instance.save()
            return redirect('contract_project_index')

    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'form':form,
        'user_profile':user_profile,

    }
    if request.user.is_staff:
        return render(request, 'contract/add_new_contract.html', context)
    else:
        return redirect('no_permission')



# اشعارات ----------------------------------------------------------------------

@login_required(login_url='login')
def contract_notification(request):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)
    notification = Actions.objects.all().filter(to_id=user_profile.id, is_read = False)
    notification_count = notification.count()



    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'user_profile':user_profile,
        'notification':notification,
        'notification_count':notification_count,

    }
    if request.user.is_staff:
        return render(request, 'contract/contract_notification.html', context)
    else:
        return redirect('no_permission')


@login_required(login_url='login')
def contract_notification_read(request, id):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)
    notification = Actions.objects.get(id=id)
    notification.is_read = True
    notification.save()
    



    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'user_profile':user_profile,
        'notification':notification,

    }
    if request.user.is_staff:
        return render(request, 'contract/contract_notification_read.html', context)
    else:
        return redirect('no_permission')


# تقارير ----------------------------------------------------------------------

@login_required(login_url='login')
def contract_project_report(request):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)

        # حساب الاصدار الجديد
    new = Contract_Detail.objects.all().filter(sgnllast_status_action='اصدار جديد')
    sector_project_report = new.filter(project = user_profile.project_name)

    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'user_profile':user_profile,
        'contract_report':sector_project_report,
    }
    if request.user.is_staff:
        return render(request, 'contract/contract_report.html', context)
    else:
        return redirect('no_permission')

# 3 types phase 2 --------------------------------------------------------------
@login_required(login_url='login')
@c_1_contract_sector_report_special_project
def contract_sector_report_special_project(request):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)

        # حساب الاصدار الجديد
    new = Contract_Detail.objects.all().filter(sgnllast_status_action='اصدار جديد')
    sector_manager_report = new.filter(project = user_profile.project_name)
    searchFilter = ContractFilter(request.GET, queryset=sector_manager_report.order_by('id'))
    sector_manager_report = searchFilter.qs

    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'user_profile':user_profile,
        'contract_report':sector_manager_report,
        'myFilter': searchFilter,
    }
    if request.user.is_staff:
        return render(request, 'contract/contract_report.html', context)
    else:
        return redirect('no_permission')

@login_required(login_url='login')
@c_2_contract_sector_report_special_sector
def contract_sector_report_special_sector(request):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)

        # حساب الاصدار الجديد
    new = Contract_Detail.objects.all().filter(sgnllast_status_action='اصدار جديد')
    sector_manager_report = new.filter(sector = user_profile.sector_name)
    searchFilter = ContractFilter(request.GET, queryset=sector_manager_report.order_by('id'))
    sector_manager_report = searchFilter.qs

    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'user_profile':user_profile,
        'contract_report':sector_manager_report,
        'myFilter': searchFilter,
    }
    if request.user.is_staff:
        return render(request, 'contract/contract_report.html', context)
    else:
        return redirect('no_permission')

@login_required(login_url='login')

def contract_sector_report_special_cost_estimation(request):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)

        # حساب الاصدار الجديد
    new = Contract_Detail.objects.all().filter(sgnllast_status_action='اصدار جديد')
    sector_manager_report = new.filter(cost_istimation = user_profile.sector_name)
    searchFilter = ContractFilter(request.GET, queryset=sector_manager_report.order_by('id'))
    sector_manager_report = searchFilter.qs

    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'user_profile':user_profile,
        'contract_report':sector_manager_report,
        'myFilter': searchFilter,
    }
    if request.user.is_staff:
        return render(request, 'contract/contract_report.html', context)
    else:
        return redirect('no_permission')

@login_required(login_url='login')
@c_main_contract_sector_report
def contract_sector_report(request):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)

        # حساب الاصدار الجديد
    new = Contract_Detail.objects.all().filter(sgnllast_status_action='اصدار جديد')
    sector_manager_report = new
    searchFilter = ContractFilter(request.GET, queryset=sector_manager_report.order_by('id'))
    sector_manager_report = searchFilter.qs

    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'user_profile':user_profile,
        'contract_report':sector_manager_report,
        'myFilter': searchFilter,
    }
    if request.user.is_staff:
        return render(request, 'contract/contract_report.html', context)
    else:
        return redirect('no_permission')

# 3 types phase 3 --------------------------------------------------------------

@login_required(login_url='login')
@c_1_contract_chech_data_report_special_project
def contract_chech_data_report_special_project(request):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)

    # حساب مراجعة البيانات
    check_data = Contract_Detail.objects.all().filter(sgnllast_status_action='مراجعة البيانات')
    check_data_report = check_data.filter(project = user_profile.project_name)
    searchFilter = ContractFilter(request.GET, queryset=check_data_report.order_by('id'))
    check_data_report = searchFilter.qs

    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'user_profile':user_profile,
        'contract_report':check_data_report,
        'myFilter': searchFilter,
    }
    if request.user.is_staff:
        return render(request, 'contract/contract_report.html', context)
    else:
        return redirect('no_permission')

@login_required(login_url='login')
@c_2_contract_chech_data_report_special_sector
def contract_chech_data_report_special_sector(request):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)

    # حساب مراجعة البيانات
    check_data = Contract_Detail.objects.all().filter(sgnllast_status_action='مراجعة البيانات')
    check_data_report = check_data.filter(sector = user_profile.sector_name)
    searchFilter = ContractFilter(request.GET, queryset=check_data_report.order_by('id'))
    check_data_report = searchFilter.qs

    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'user_profile':user_profile,
        'contract_report':check_data_report,
        'myFilter': searchFilter,
    }
    if request.user.is_staff:
        return render(request, 'contract/contract_report.html', context)
    else:
        return redirect('no_permission')

@login_required(login_url='login')

def contract_chech_data_report_special_cost_estimation(request):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)

    # حساب مراجعة البيانات
    check_data = Contract_Detail.objects.all().filter(sgnllast_status_action='مراجعة البيانات')
    check_data_report = check_data.filter(cost_istimation = user_profile.sector_name)
    searchFilter = ContractFilter(request.GET, queryset=check_data_report.order_by('id'))
    check_data_report = searchFilter.qs

    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'user_profile':user_profile,
        'contract_report':check_data_report,
        'myFilter': searchFilter,
    }
    if request.user.is_staff:
        return render(request, 'contract/contract_report.html', context)
    else:
        return redirect('no_permission')

@login_required(login_url='login')
@c_main_contract_chech_data_report
def contract_chech_data_report(request):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)

    # حساب مراجعة البيانات
    check_data = Contract_Detail.objects.all().filter(sgnllast_status_action='مراجعة البيانات')
    check_data_report = check_data
    searchFilter = ContractFilter(request.GET, queryset=check_data_report.order_by('id'))
    check_data_report = searchFilter.qs

    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'user_profile':user_profile,
        'contract_report':check_data_report,
        'myFilter': searchFilter,
    }
    if request.user.is_staff:
        return render(request, 'contract/contract_report.html', context)
    else:
        return redirect('no_permission')

# 3 types phase 4 --------------------------------------------------------------

@login_required(login_url='login')
@c_1_contract_cost_estimation_report_special_project
def contract_cost_estimation_report_special_project(request):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)

    # حساب تقدير التكاليف
    cost_estimation = Contract_Detail.objects.all().filter(sgnllast_status_action='تقدير التكاليف')
    cost_estimation_report = cost_estimation.filter(project = user_profile.project_name)
    searchFilter = ContractFilter(request.GET, queryset=cost_estimation_report.order_by('id'))
    cost_estimation_report = searchFilter.qs

    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'user_profile':user_profile,
        'contract_report':cost_estimation_report,
        'myFilter': searchFilter,
    }
    if request.user.is_staff:
        return render(request, 'contract/contract_report.html', context)
    else:
        return redirect('no_permission')

@login_required(login_url='login')
@c_2_contract_cost_estimation_report_special_sector
def contract_cost_estimation_report_special_sector(request):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)

    # حساب تقدير التكاليف
    cost_estimation = Contract_Detail.objects.all().filter(sgnllast_status_action='تقدير التكاليف')
    cost_estimation_report = cost_estimation.filter(sector = user_profile.sector_name)
    searchFilter = ContractFilter(request.GET, queryset=cost_estimation_report.order_by('id'))
    cost_estimation_report = searchFilter.qs

    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'user_profile':user_profile,
        'contract_report':cost_estimation_report,
        'myFilter': searchFilter,
    }
    if request.user.is_staff:
        return render(request, 'contract/contract_report.html', context)
    else:
        return redirect('no_permission')

@login_required(login_url='login')

def contract_cost_estimation_report_special_cost_estimation(request):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)

    # حساب تقدير التكاليف
    cost_estimation = Contract_Detail.objects.all().filter(sgnllast_status_action='تقدير التكاليف')
    cost_estimation_report = cost_estimation.filter(cost_istimation = user_profile.sector_name)
    searchFilter = ContractFilter(request.GET, queryset=cost_estimation_report.order_by('id'))
    cost_estimation_report = searchFilter.qs

    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'user_profile':user_profile,
        'contract_report':cost_estimation_report,
        'myFilter': searchFilter,
    }
    if request.user.is_staff:
        return render(request, 'contract/contract_report.html', context)
    else:
        return redirect('no_permission')

@login_required(login_url='login')
@c_main_contract_cost_estimation_report
def contract_cost_estimation_report(request):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)

    # حساب تقدير التكاليف
    cost_estimation = Contract_Detail.objects.all().filter(sgnllast_status_action='تقدير التكاليف')
    cost_estimation_report = cost_estimation
    searchFilter = ContractFilter(request.GET, queryset=cost_estimation_report.order_by('id'))
    cost_estimation_report = searchFilter.qs

    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'user_profile':user_profile,
        'contract_report':cost_estimation_report,
        'myFilter': searchFilter,
    }
    if request.user.is_staff:
        return render(request, 'contract/contract_report.html', context)
    else:
        return redirect('no_permission')

# 3 types phase 5 --------------------------------------------------------------

@login_required(login_url='login')
@c_1_contract_financial_report_special_project
def contract_financial_report_special_project(request):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)

    # حساب مراجعة المالية
    financial = Contract_Detail.objects.all().filter(sgnllast_status_action='مراجعة المالية')
    financial_report = financial.filter(project = user_profile.project_name)
    searchFilter = ContractFilter(request.GET, queryset=financial_report.order_by('id'))
    financial_report = searchFilter.qs

    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'user_profile':user_profile,
        'contract_report':financial_report,
        'myFilter': searchFilter,
    }
    if request.user.is_staff:
        return render(request, 'contract/contract_report.html', context)
    else:
        return redirect('no_permission')

@login_required(login_url='login')
@c_2_contract_financial_report_special_sector
def contract_financial_report_special_sector(request):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)

    # حساب مراجعة المالية
    financial = Contract_Detail.objects.all().filter(sgnllast_status_action='مراجعة المالية')
    financial_report = financial.filter(sector = user_profile.sector_name)
    searchFilter = ContractFilter(request.GET, queryset=financial_report.order_by('id'))
    financial_report = searchFilter.qs

    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'user_profile':user_profile,
        'contract_report':financial_report,
        'myFilter': searchFilter,
    }
    if request.user.is_staff:
        return render(request, 'contract/contract_report.html', context)
    else:
        return redirect('no_permission')

@login_required(login_url='login')

def contract_financial_report_special_cost_estimation(request):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)

    # حساب مراجعة المالية
    financial = Contract_Detail.objects.all().filter(sgnllast_status_action='مراجعة المالية')
    financial_report = financial.filter(cost_istimation = user_profile.sector_name)
    searchFilter = ContractFilter(request.GET, queryset=financial_report.order_by('id'))
    financial_report = searchFilter.qs

    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'user_profile':user_profile,
        'contract_report':financial_report,
        'myFilter': searchFilter,
    }
    if request.user.is_staff:
        return render(request, 'contract/contract_report.html', context)
    else:
        return redirect('no_permission')

@login_required(login_url='login')
@c_main_contract_financial_report
def contract_financial_report(request):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)

    # حساب مراجعة المالية
    financial = Contract_Detail.objects.all().filter(sgnllast_status_action='مراجعة المالية')
    financial_report = financial
    searchFilter = ContractFilter(request.GET, queryset=financial_report.order_by('id'))
    financial_report = searchFilter.qs

    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'user_profile':user_profile,
        'contract_report':financial_report,
        'myFilter': searchFilter,
    }
    if request.user.is_staff:
        return render(request, 'contract/contract_report.html', context)
    else:
        return redirect('no_permission')

# 3 types phase 6 --------------------------------------------------------------

@login_required(login_url='login')
@c_1_contract_copy_contract_report_special_project
def contract_copy_contract_report_special_project(request):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)

    # حساب ناسخ العقود
    copy_contract = Contract_Detail.objects.all().filter(sgnllast_status_action='ناسخ العقد')
    copy_contract_report = copy_contract.filter(project = user_profile.project_name)
    searchFilter = ContractFilter(request.GET, queryset=copy_contract_report.order_by('id'))
    copy_contract_report = searchFilter.qs


    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'user_profile':user_profile,
        'contract_report':copy_contract_report,
        'myFilter': searchFilter,
    }
    if request.user.is_staff:
        return render(request, 'contract/contract_report.html', context)
    else:
        return redirect('no_permission')

@login_required(login_url='login')
@c_2_contract_copy_contract_report_special_sector
def contract_copy_contract_report_special_sector(request):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)

    # حساب ناسخ العقود
    copy_contract = Contract_Detail.objects.all().filter(sgnllast_status_action='ناسخ العقد')
    copy_contract_report = copy_contract.filter(sector = user_profile.sector_name)
    searchFilter = ContractFilter(request.GET, queryset=copy_contract_report.order_by('id'))
    copy_contract_report = searchFilter.qs

    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'user_profile':user_profile,
        'contract_report':copy_contract_report,
        'myFilter': searchFilter,
    }
    if request.user.is_staff:
        return render(request, 'contract/contract_report.html', context)
    else:
        return redirect('no_permission')

@login_required(login_url='login')

def contract_copy_contract_report_special_cost_estimation(request):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)

    # حساب ناسخ العقود
    copy_contract = Contract_Detail.objects.all().filter(sgnllast_status_action='ناسخ العقد')
    copy_contract_report = copy_contract.filter(cost_istimation = user_profile.sector_name)
    searchFilter = ContractFilter(request.GET, queryset=copy_contract_report.order_by('id'))
    copy_contract_report = searchFilter.qs

    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'user_profile':user_profile,
        'contract_report':copy_contract_report,
        'myFilter': searchFilter,
    }
    if request.user.is_staff:
        return render(request, 'contract/contract_report.html', context)
    else:
        return redirect('no_permission')

@login_required(login_url='login')
@c_main_contract_copy_contract_report
def contract_copy_contract_report(request):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)

    # حساب ناسخ العقود
    copy_contract = Contract_Detail.objects.all().filter(sgnllast_status_action='ناسخ العقد')
    copy_contract_report = copy_contract
    searchFilter = ContractFilter(request.GET, queryset=copy_contract_report.order_by('id'))
    copy_contract_report = searchFilter.qs

    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'user_profile':user_profile,
        'contract_report':copy_contract_report,
        'myFilter': searchFilter,
    }
    if request.user.is_staff:
        return render(request, 'contract/contract_report.html', context)
    else:
        return redirect('no_permission')

# 3 types phase 7 --------------------------------------------------------------

@login_required(login_url='login')
@c_1_contract_check_contract_report_special_project
def contract_check_contract_report_special_project(request):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)

    # حساب مراجعة العقود
    check_contract = Contract_Detail.objects.all().filter(sgnllast_status_action='مراجعة العقد')
    check_contract_report = check_contract.filter(project = user_profile.project_name)
    searchFilter = ContractFilter(request.GET, queryset=check_contract_report.order_by('id'))
    check_contract_report = searchFilter.qs

    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'user_profile':user_profile,
        'contract_report':check_contract_report,
        'myFilter': searchFilter,
    }
    if request.user.is_staff:
        return render(request, 'contract/contract_report.html', context)
    else:
        return redirect('no_permission')

@login_required(login_url='login')
@c_2_contract_check_contract_report_special_sector
def contract_check_contract_report_special_sector(request):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)

    # حساب مراجعة العقود
    check_contract = Contract_Detail.objects.all().filter(sgnllast_status_action='مراجعة العقد')
    check_contract_report = check_contract.filter(sector = user_profile.sector_name)
    searchFilter = ContractFilter(request.GET, queryset=check_contract_report.order_by('id'))
    check_contract_report = searchFilter.qs

    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'user_profile':user_profile,
        'contract_report':check_contract_report,
        'myFilter': searchFilter,
    }
    if request.user.is_staff:
        return render(request, 'contract/contract_report.html', context)
    else:
        return redirect('no_permission')

@login_required(login_url='login')

def contract_check_contract_report_special_cost_estimation(request):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)

    # حساب مراجعة العقود
    check_contract = Contract_Detail.objects.all().filter(sgnllast_status_action='مراجعة العقد')
    check_contract_report = check_contract.filter(cost_istimation = user_profile.sector_name)
    searchFilter = ContractFilter(request.GET, queryset=check_contract_report.order_by('id'))
    check_contract_report = searchFilter.qs

    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'user_profile':user_profile,
        'contract_report':check_contract_report,
        'myFilter': searchFilter,
    }
    if request.user.is_staff:
        return render(request, 'contract/contract_report.html', context)
    else:
        return redirect('no_permission')

@login_required(login_url='login')
@c_main_contract_check_contract_report
def contract_check_contract_report(request):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)

    # حساب مراجعة العقود
    check_contract = Contract_Detail.objects.all().filter(sgnllast_status_action='مراجعة العقد')
    check_contract_report = check_contract
    searchFilter = ContractFilter(request.GET, queryset=check_contract_report.order_by('id'))
    check_contract_report = searchFilter.qs

    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'user_profile':user_profile,
        'contract_report':check_contract_report,
        'myFilter': searchFilter,
    }
    if request.user.is_staff:
        return render(request, 'contract/contract_report.html', context)
    else:
        return redirect('no_permission')

# 3 types phase 8 --------------------------------------------------------------

@login_required(login_url='login')
@c_1_contract_tcta_report_special_project
def contract_tcta_report_special_project(request):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)

    # حساب اعتماد tcta
    tcta = Contract_Detail.objects.all().filter(sgnllast_status_action='اعتماد الاجراءات')
    tcta_report = tcta.filter(project = user_profile.project_name)
    searchFilter = ContractFilter(request.GET, queryset=tcta_report.order_by('id'))
    tcta_report = searchFilter.qs

    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'user_profile':user_profile,
        'contract_report':tcta_report,
        'myFilter': searchFilter,
    }
    if request.user.is_staff:
        return render(request, 'contract/contract_report.html', context)
    else:
        return redirect('no_permission')

@login_required(login_url='login')
@c_2_contract_tcta_report_special_sector
def contract_tcta_report_special_sector(request):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)

    # حساب اعتماد tcta
    tcta = Contract_Detail.objects.all().filter(sgnllast_status_action='اعتماد الاجراءات')
    tcta_report = tcta.filter(sector = user_profile.sector_name)
    searchFilter = ContractFilter(request.GET, queryset=tcta_report.order_by('id'))
    tcta_report = searchFilter.qs

    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'user_profile':user_profile,
        'contract_report':tcta_report,
        'myFilter': searchFilter,
    }
    if request.user.is_staff:
        return render(request, 'contract/contract_report.html', context)
    else:
        return redirect('no_permission')

@login_required(login_url='login')

def contract_tcta_report_special_cost_estimation(request):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)

    # حساب اعتماد tcta
    tcta = Contract_Detail.objects.all().filter(sgnllast_status_action='اعتماد الاجراءات')
    tcta_report = tcta.filter(cost_istimation = user_profile.sector_name)
    searchFilter = ContractFilter(request.GET, queryset=tcta_report.order_by('id'))
    tcta_report = searchFilter.qs

    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'user_profile':user_profile,
        'contract_report':tcta_report,
        'myFilter': searchFilter,
    }
    if request.user.is_staff:
        return render(request, 'contract/contract_report.html', context)
    else:
        return redirect('no_permission')

@login_required(login_url='login')
@c_main_contract_tcta_report
def contract_tcta_report(request):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)

    # حساب اعتماد tcta
    tcta = Contract_Detail.objects.all().filter(sgnllast_status_action='اعتماد الاجراءات')
    tcta_report = tcta
    searchFilter = ContractFilter(request.GET, queryset=tcta_report.order_by('id'))
    tcta_report = searchFilter.qs

    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'user_profile':user_profile,
        'contract_report':tcta_report,
        'myFilter': searchFilter,
    }
    if request.user.is_staff:
        return render(request, 'contract/contract_report.html', context)
    else:
        return redirect('no_permission')

# 3 types phase 9 --------------------------------------------------------------

@login_required(login_url='login')
@c_1_contract_evp_report_special_project
def contract_evp_report_special_project(request):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)

    # حساب اعتماد evp
    evp = Contract_Detail.objects.all().filter(sgnllast_status_action='نائب الرئيس التنفيذي')
    evp_report = evp.filter(project = user_profile.project_name)
    searchFilter = ContractFilter(request.GET, queryset=evp_report.order_by('id'))
    evp_report = searchFilter.qs

    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'user_profile':user_profile,
        'contract_report':evp_report,
        'myFilter': searchFilter,
    }
    if request.user.is_staff:
        return render(request, 'contract/contract_report.html', context)
    else:
        return redirect('no_permission')

@login_required(login_url='login')
@c_2_contract_evp_report_special_sector
def contract_evp_report_special_sector(request):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)

    # حساب اعتماد evp
    evp = Contract_Detail.objects.all().filter(sgnllast_status_action='نائب الرئيس التنفيذي')
    evp_report = evp.filter(sector = user_profile.sector_name)
    searchFilter = ContractFilter(request.GET, queryset=evp_report.order_by('id'))
    evp_report = searchFilter.qs

    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'user_profile':user_profile,
        'contract_report':evp_report,
        'myFilter': searchFilter,
    }
    if request.user.is_staff:
        return render(request, 'contract/contract_report.html', context)
    else:
        return redirect('no_permission')

@login_required(login_url='login')

def contract_evp_report_special_cost_estimation(request):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)

    # حساب اعتماد evp
    evp = Contract_Detail.objects.all().filter(sgnllast_status_action='نائب الرئيس التنفيذي')
    evp_report = evp.filter(cost_istimation = user_profile.sector_name)
    searchFilter = ContractFilter(request.GET, queryset=evp_report.order_by('id'))
    evp_report = searchFilter.qs

    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'user_profile':user_profile,
        'contract_report':evp_report,
        'myFilter': searchFilter,
    }
    if request.user.is_staff:
        return render(request, 'contract/contract_report.html', context)
    else:
        return redirect('no_permission')

@login_required(login_url='login')
@c_main_contract_evp_report
def contract_evp_report(request):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)

    # حساب اعتماد evp
    evp = Contract_Detail.objects.all().filter(sgnllast_status_action='نائب الرئيس التنفيذي')
    evp_report = evp
    searchFilter = ContractFilter(request.GET, queryset=evp_report.order_by('id'))
    evp_report = searchFilter.qs

    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'user_profile':user_profile,
        'contract_report':evp_report,
        'myFilter': searchFilter,
    }
    if request.user.is_staff:
        return render(request, 'contract/contract_report.html', context)
    else:
        return redirect('no_permission')

# 3 types phase 10 --------------------------------------------------------------
@login_required(login_url='login')
@c_1_contract_ceo_report_special_project
def contract_ceo_report_special_project(request):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)

    # حساب اعتماد ceo
    ceo = Contract_Detail.objects.all().filter(sgnllast_status_action='الرئيس التنفيذي')
    ceo_report = ceo.filter(project = user_profile.project_name)
    searchFilter = ContractFilter(request.GET, queryset=ceo_report.order_by('id'))
    ceo_report = searchFilter.qs

    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'user_profile':user_profile,
        'contract_report':ceo_report,
        'myFilter': searchFilter,
    }
    if request.user.is_staff:
        return render(request, 'contract/contract_report.html', context)
    else:
        return redirect('no_permission')

@login_required(login_url='login')
@c_2_contract_ceo_report_special_sector
def contract_ceo_report_special_sector(request):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)

    # حساب اعتماد ceo
    ceo = Contract_Detail.objects.all().filter(sgnllast_status_action='الرئيس التنفيذي')
    ceo_report = ceo.filter(sector = user_profile.sector_name)
    searchFilter = ContractFilter(request.GET, queryset=ceo_report.order_by('id'))
    ceo_report = searchFilter.qs

    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'user_profile':user_profile,
        'contract_report':ceo_report,
        'myFilter': searchFilter,
    }
    if request.user.is_staff:
        return render(request, 'contract/contract_report.html', context)
    else:
        return redirect('no_permission')

@login_required(login_url='login')

def contract_ceo_report_special_cost_estimation(request):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)

    # حساب اعتماد ceo
    ceo = Contract_Detail.objects.all().filter(sgnllast_status_action='الرئيس التنفيذي')
    ceo_report = ceo.filter(cost_istimation = user_profile.sector_name)
    searchFilter = ContractFilter(request.GET, queryset=ceo_report.order_by('id'))
    ceo_report = searchFilter.qs

    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'user_profile':user_profile,
        'contract_report':ceo_report,
        'myFilter': searchFilter,
    }
    if request.user.is_staff:
        return render(request, 'contract/contract_report.html', context)
    else:
        return redirect('no_permission')

@login_required(login_url='login')
@c_main_contract_ceo_report
def contract_ceo_report(request):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)

    # حساب اعتماد ceo
    ceo = Contract_Detail.objects.all().filter(sgnllast_status_action='الرئيس التنفيذي')
    ceo_report = ceo
    searchFilter = ContractFilter(request.GET, queryset=ceo_report.order_by('id'))
    ceo_report = searchFilter.qs

    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'user_profile':user_profile,
        'contract_report':ceo_report,
        'myFilter': searchFilter,
    }
    if request.user.is_staff:
        return render(request, 'contract/contract_report.html', context)
    else:
        return redirect('no_permission')

# 3 types phase 11 --------------------------------------------------------------

@login_required(login_url='login')
@c_1_contract_asgn2_report_special_project
def contract_asgnmnt_report_special_project(request):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)

    # حساب اعتماد asgnmnt
    asgnmnt = Contract_Detail.objects.all().filter(sgnllast_status_action='توقيعات')
    asgnmnt_report = asgnmnt.filter(project = user_profile.project_name)
    searchFilter = ContractFilter(request.GET, queryset=asgnmnt_report.order_by('id'))
    asgnmnt_report = searchFilter.qs

    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'user_profile':user_profile,
        'contract_report':asgnmnt_report,
        'myFilter': searchFilter,
    }
    if request.user.is_staff:
        return render(request, 'contract/contract_report.html', context)
    else:
        return redirect('no_permission')

@login_required(login_url='login')
@c_2_contract_asgn2_report_special_sector
def contract_asgnmnt_report_special_sector(request):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)

    # حساب اعتماد asgnmnt
    asgnmnt = Contract_Detail.objects.all().filter(sgnllast_status_action='توقيعات')
    asgnmnt_report = asgnmnt.filter(sector = user_profile.sector_name)
    searchFilter = ContractFilter(request.GET, queryset=asgnmnt_report.order_by('id'))
    asgnmnt_report = searchFilter.qs

    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'user_profile':user_profile,
        'contract_report':asgnmnt_report,
        'myFilter': searchFilter,
    }
    if request.user.is_staff:
        return render(request, 'contract/contract_report.html', context)
    else:
        return redirect('no_permission')

@login_required(login_url='login')

def contract_asgnmnt_report_special_cost_estimation(request):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)

    # حساب اعتماد asgnmnt
    asgnmnt = Contract_Detail.objects.all().filter(sgnllast_status_action='توقيعات')
    asgnmnt_report = asgnmnt.filter(cost_istimation = user_profile.sector_name)
    searchFilter = ContractFilter(request.GET, queryset=asgnmnt_report.order_by('id'))
    asgnmnt_report = searchFilter.qs

    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'user_profile':user_profile,
        'contract_report':asgnmnt_report,
        'myFilter': searchFilter,
    }
    if request.user.is_staff:
        return render(request, 'contract/contract_report.html', context)
    else:
        return redirect('no_permission')

@login_required(login_url='login')
@c_main_contract_asgn2_report
def contract_asgnmnt_report(request):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)

    # حساب اعتماد asgnmnt
    asgnmnt = Contract_Detail.objects.all().filter(sgnllast_status_action='توقيعات')
    asgnmnt_report = asgnmnt
    searchFilter = ContractFilter(request.GET, queryset=asgnmnt_report.order_by('id'))
    asgnmnt_report = searchFilter.qs

    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'user_profile':user_profile,
        'contract_report':asgnmnt_report,
        'myFilter': searchFilter,
    }
    if request.user.is_staff:
        return render(request, 'contract/contract_report.html', context)
    else:
        return redirect('no_permission')




# 3 types phase refuse --------------------------------------------------------------

@login_required(login_url='login')
@c_1_contract_refuse_report_special_project
def contract_refuse_report_special_project(request):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)

    # حساب refuse
    refuse = Contract_Detail.objects.all().filter(sgnllast_status_action='رفض')
    refuse_report = refuse.filter(project = user_profile.project_name)
    searchFilter = ContractFilter(request.GET, queryset=refuse_report.order_by('id'))
    refuse_report = searchFilter.qs

    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'user_profile':user_profile,
        'contract_report':refuse_report,
        'myFilter': searchFilter,
    }
    if request.user.is_staff:
        return render(request, 'contract/contract_report.html', context)
    else:
        return redirect('no_permission')

@login_required(login_url='login')
@c_2_contract_refuse_report_special_sector
def contract_refuse_report_special_sector(request):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)

    # حساب refuse
    refuse = Contract_Detail.objects.all().filter(sgnllast_status_action='رفض')
    refuse_report = refuse.filter(sector = user_profile.sector_name)
    searchFilter = ContractFilter(request.GET, queryset=refuse_report.order_by('id'))
    refuse_report = searchFilter.qs

    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'user_profile':user_profile,
        'contract_report':refuse_report,
        'myFilter': searchFilter,
    }
    if request.user.is_staff:
        return render(request, 'contract/contract_report.html', context)
    else:
        return redirect('no_permission')

@login_required(login_url='login')

def contract_refuse_report_special_cost_estimation(request):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)

    # حساب refuse
    refuse = Contract_Detail.objects.all().filter(sgnllast_status_action='رفض')
    refuse_report = refuse.filter(cost_istimation = user_profile.sector_name)
    searchFilter = ContractFilter(request.GET, queryset=refuse_report.order_by('id'))
    refuse_report = searchFilter.qs

    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'user_profile':user_profile,
        'contract_report':refuse_report,
        'myFilter': searchFilter,
    }
    if request.user.is_staff:
        return render(request, 'contract/contract_report.html', context)
    else:
        return redirect('no_permission')

@login_required(login_url='login')
@c_main_contract_refuse_report
def contract_refuse_report(request):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)

    # حساب refuse
    refuse = Contract_Detail.objects.all().filter(sgnllast_status_action='رفض')
    refuse_report = refuse
    searchFilter = ContractFilter(request.GET, queryset=refuse_report.order_by('id'))
    refuse_report = searchFilter.qs

    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'user_profile':user_profile,
        'contract_report':refuse_report,
        'myFilter': searchFilter,
    }
    if request.user.is_staff:
        return render(request, 'contract/contract_report.html', context)
    else:
        return redirect('no_permission')

# 3 types phase complete --------------------------------------------------------------

@login_required(login_url='login')
@c_1_contract_complete_report_special_project
def contract_complete_report_special_project(request):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)
    
    

    # حساب complete
    complete = Contract_Detail.objects.all().filter(sgnllast_status_action='مكتمل')
    complete_report = complete.filter(project = user_profile.project_name)

    searchFilter = ContractFilter(request.GET, queryset=complete_report.order_by('contract_no'))
    complete_report = searchFilter.qs

    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'user_profile':user_profile,
        'contract_report':complete_report,
        'myFilter': searchFilter,
    }
    if request.user.is_staff:
        return render(request, 'contract/contract_report.html', context)
    else:
        return redirect('no_permission')

@login_required(login_url='login')
@c_2_contract_complete_report_special_sector
def contract_complete_report_special_sector(request):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)
    

    # حساب complete
    complete = Contract_Detail.objects.all().filter(sgnllast_status_action='مكتمل')
    complete_report = complete.filter(sector = user_profile.sector_name)

    searchFilter = ContractFilter(request.GET, queryset=complete_report.order_by('contract_no'))
    complete_report = searchFilter.qs

    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'user_profile':user_profile,
        'contract_report':complete_report,
        'myFilter': searchFilter,
    }
    if request.user.is_staff:
        return render(request, 'contract/contract_report.html', context)
    else:
        return redirect('no_permission')

@login_required(login_url='login')

def contract_complete_report_special_cost_estimation(request):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)
    

    # حساب complete
    complete = Contract_Detail.objects.all().filter(sgnllast_status_action='مكتمل')
    complete_report = complete.filter(cost_istimation = user_profile.sector_name)

    searchFilter = ContractFilter(request.GET, queryset=complete_report.order_by('contract_no'))
    complete_report = searchFilter.qs

    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'user_profile':user_profile,
        'contract_report':complete_report,
        'myFilter': searchFilter,
    }
    if request.user.is_staff:
        return render(request, 'contract/contract_report.html', context)
    else:
        return redirect('no_permission')

@login_required(login_url='login')
@c_main_contract_complete_report
def contract_complete_report(request):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)

    # حساب complete
    complete = Contract_Detail.objects.all().filter(sgnllast_status_action='مكتمل')
    complete_report = complete

    searchFilter = ContractFilter(request.GET, queryset=complete_report.order_by('contract_no'))
    complete_report = searchFilter.qs

    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'user_profile':user_profile,
        'contract_report':complete_report,
        'myFilter': searchFilter,
    }
    if request.user.is_staff:
        return render(request, 'contract/contract_report.html', context)
    else:
        return redirect('no_permission')

# dashboards ----------------------------------------------------------------------

@login_required(login_url='login')
@contract_main_index
def contract_main_index(request):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)
    notification = Actions.objects.all().filter(to_id=user_profile.id, is_read = False)
    notification_count = notification.count()
    all = Contract_Detail.objects.all().count()
    # حساب الاصدار الجديد
    new = Contract_Detail.objects.all().filter(sgnllast_status_action='اصدار جديد')
    sector_manager_count = new.count()

    # حساب مراجعة البيانات
    check_data = Contract_Detail.objects.all().filter(sgnllast_status_action='مراجعة البيانات')
    check_data_count = check_data.count()

    # حساب تقدير التكاليف
    cost_estimation = Contract_Detail.objects.all().filter(sgnllast_status_action='تقدير التكاليف')
    cost_estimation_count = cost_estimation.count()

    # حساب مراجعة المالية
    financial = Contract_Detail.objects.all().filter(sgnllast_status_action='مراجعة المالية')
    financial_count = financial.count()

    # حساب ناسخ العقود
    copy_contract = Contract_Detail.objects.all().filter(sgnllast_status_action='ناسخ العقد')
    copy_contract_count = copy_contract.count()

    # حساب مراجعة العقود
    check_contract = Contract_Detail.objects.all().filter(sgnllast_status_action='مراجعة العقد')
    check_contract_count = check_contract.count()

    # حساب اعتماد tcta
    tcta = Contract_Detail.objects.all().filter(sgnllast_status_action='اعتماد الاجراءات')
    tcta_count = tcta.count()

    # حساب اعتماد evp
    evp = Contract_Detail.objects.all().filter(sgnllast_status_action='نائب الرئيس التنفيذي')
    evp_count = evp.count()

    # حساب اعتماد ceo
    ceo = Contract_Detail.objects.all().filter(sgnllast_status_action='الرئيس التنفيذي')
    ceo_count = ceo.count()

    # حساب اعتماد asgnmnt
    asgnmnt = Contract_Detail.objects.all().filter(sgnllast_status_action='توقيعات')
    asgnmnt_count = asgnmnt.count()

    # حساب الرفض
    refuse = Contract_Detail.objects.all().filter(sgnllast_status_action='رفض')
    refuse_count = refuse.count()

    # حساب المكتمل
    complete = Contract_Detail.objects.all().filter(sgnllast_status_action='مكتمل')
    complete_count = complete.count()
    try:
        complete_percentage = round((complete_count/all)*100)
    except ZeroDivisionError:
        complete_percentage = 0

    # حساب الجاري
    inprogress = Contract_Detail.objects.all().filter(~Q(sgnllast_status_action='مكتمل'), ~Q(sgnllast_status_action='رفض'))
    inprogress_count = inprogress.count()



    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'user_profile':user_profile,
        'sector_manager_count':sector_manager_count,
        'check_data_count':check_data_count,
        'cost_estimation_count':cost_estimation_count,
        'financial_count':financial_count,
        'copy_contract_count':copy_contract_count,
        'check_contract_count':check_contract_count,
        'tcta_count':tcta_count,
        'evp_count':evp_count,
        'ceo_count':ceo_count,
        'asgn2_count':asgnmnt_count,
        'refuse_count':refuse_count,
        'complete_count':complete_count,
        'inprogress_count':inprogress_count,
        'notification_count':notification_count,
        'all':all,
        'complete_percentage':complete_percentage,

    }
    if request.user.is_staff:
        return render(request, 'contract/contract_main_index.html', context)
    else:
        return redirect('no_permission')
    

def contract_main_index_viewall(request):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)
    notification = Actions.objects.all().filter(to_id=user_profile.id, is_read = False)
    notification_count = notification.count()
    all = Contract_Detail.objects.all().count()
    complete = Contract_Detail.objects.all().filter(sgnllast_status_action='مكتمل')
    complete_count = complete.count()
    try:
        complete_percentage = round((complete_count/all)*100)
    except ZeroDivisionError:
        complete_percentage = 0

    contract_report = Contract_Detail.objects.all()
    searchFilter = ContractFilter(request.GET, queryset=contract_report.order_by('id'))
    contract_report = searchFilter.qs

    # حساب الرفض
    refuse = Contract_Detail.objects.all().filter(sgnllast_status_action='رفض')
    refuse_count = refuse.count()
    
    # حساب الجاري
    inprogress = Contract_Detail.objects.all().filter(~Q(sgnllast_status_action='مكتمل'), ~Q(sgnllast_status_action='رفض'))
    inprogress_count = inprogress.count()


    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'user_profile':user_profile,
        'contract_report':contract_report,
        'myFilter': searchFilter,

        'notification_count':notification_count,
        'complete_count':complete_count,
        'inprogress_count':inprogress_count,
        'all':all,
        'complete_percentage':complete_percentage,
        'refuse_count':refuse_count,

    }
    if request.user.is_staff:
        return render(request, 'contract/contract_main_index_viewall.html', context)
    else:
        return redirect('no_permission')


@login_required(login_url='login')
@contract_user_index
def contract_sector_index(request):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)
    notification = Actions.objects.all().filter(to_id=user_profile.id, is_read = False)
    notification_count = notification.count()
    all = Contract_Detail.objects.all().filter(sector = user_profile.sector_name).count()
    # حساب الاصدار الجديد
    new = Contract_Detail.objects.all().filter(sgnllast_status_action='اصدار جديد')
    sector_manager_count = new.filter(sector = user_profile.sector_name).count()

    # حساب مراجعة البيانات
    check_data = Contract_Detail.objects.all().filter(sgnllast_status_action='مراجعة البيانات')
    check_data_count = check_data.filter(sector = user_profile.sector_name).count()

    # حساب تقدير التكاليف
    cost_estimation = Contract_Detail.objects.all().filter(sgnllast_status_action='تقدير التكاليف')
    cost_estimation_count = cost_estimation.filter(sector = user_profile.sector_name).count()

    # حساب مراجعة المالية
    financial = Contract_Detail.objects.all().filter(sgnllast_status_action='مراجعة المالية')
    financial_count = financial.filter(sector = user_profile.sector_name).count()

    # حساب ناسخ العقود
    copy_contract = Contract_Detail.objects.all().filter(sgnllast_status_action='ناسخ العقد')
    copy_contract_count = copy_contract.filter(sector = user_profile.sector_name).count()

    # حساب مراجعة العقود
    check_contract = Contract_Detail.objects.all().filter(sgnllast_status_action='مراجعة العقد')
    check_contract_count = check_contract.filter(sector = user_profile.sector_name).count()

    # حساب اعتماد tcta
    tcta = Contract_Detail.objects.all().filter(sgnllast_status_action='اعتماد الاجراءات')
    tcta_count = tcta.filter(sector = user_profile.sector_name).count()

    # حساب اعتماد evp
    evp = Contract_Detail.objects.all().filter(sgnllast_status_action='نائب الرئيس التنفيذي')
    evp_count = evp.filter(sector = user_profile.sector_name).count()

    # حساب اعتماد ceo
    ceo = Contract_Detail.objects.all().filter(sgnllast_status_action='الرئيس التنفيذي')
    ceo_count = ceo.filter(sector = user_profile.sector_name).count()

    # حساب اعتماد asgnmnt
    asgnmnt = Contract_Detail.objects.all().filter(sgnllast_status_action='توقيعات')
    asgnmnt_count = asgnmnt.filter(sector = user_profile.sector_name).count()

    # حساب الرفض
    refuse = Contract_Detail.objects.all().filter(sgnllast_status_action='رفض')
    refuse_count = refuse.filter(sector = user_profile.sector_name).count()

    # حساب المكتمل
    complete = Contract_Detail.objects.all().filter(sgnllast_status_action='مكتمل')
    complete_count = complete.filter(sector = user_profile.sector_name).count()
    try:
        complete_percentage = round((complete_count/all)*100)
    except ZeroDivisionError:
        complete_percentage = 0
    
    # حساب الجاري
    inprogress = Contract_Detail.objects.all().filter(~Q(sgnllast_status_action='مكتمل'), ~Q(sgnllast_status_action='رفض'))
    inprogress_count = inprogress.filter(sector = user_profile.sector_name).count()



    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'user_profile':user_profile,
        'sector_manager_count':sector_manager_count,
        'check_data_count':check_data_count,
        'cost_estimation_count':cost_estimation_count,
        'financial_count':financial_count,
        'copy_contract_count':copy_contract_count,
        'check_contract_count':check_contract_count,
        'tcta_count':tcta_count,
        'evp_count':evp_count,
        'ceo_count':ceo_count,
        'asgn2_count':asgnmnt_count,
        'refuse_count':refuse_count,
        'complete_count':complete_count,
        'inprogress_count':inprogress_count,
        'notification_count':notification_count,
        'all':all,
        'complete_percentage':complete_percentage,

    }
    if request.user.is_staff:
        return render(request, 'contract/contract_main_index.html', context)
    else:
        return redirect('no_permission')

    
def contract_sector_index_viewall(request):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)
    notification = Actions.objects.all().filter(to_id=user_profile.id, is_read = False)
    notification_count = notification.count()
    all = Contract_Detail.objects.all().filter(sector = user_profile.sector_name).count()
    complete = Contract_Detail.objects.all().filter(sgnllast_status_action='مكتمل')
    complete_count = complete.filter(sector = user_profile.sector_name).count()

    try:
        complete_percentage = round((complete_count/all)*100)
    except ZeroDivisionError:
        complete_percentage = 0

        # حساب الرفض
    refuse = Contract_Detail.objects.all().filter(sgnllast_status_action='رفض')
    refuse_count = refuse.filter(sector = user_profile.sector_name).count()
    # حساب الجاري
    inprogress = Contract_Detail.objects.all().filter(~Q(sgnllast_status_action='مكتمل'), ~Q(sgnllast_status_action='رفض'))
    inprogress_count = inprogress.filter(sector = user_profile.sector_name).count()


    contract_report = Contract_Detail.objects.all().filter(sector = user_profile.sector_name)
    searchFilter = ContractFilter(request.GET, queryset=contract_report.order_by('id'))
    contract_report = searchFilter.qs


    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'user_profile':user_profile,
        'contract_report':contract_report,
        'myFilter': searchFilter,

        'notification_count':notification_count,
        'complete_count':complete_count,
        'inprogress_count':inprogress_count,
        'all':all,
        'refuse_count':refuse_count,
        'complete_percentage':complete_percentage,

    }
    if request.user.is_staff:
        return render(request, 'contract/contract_main_index_viewall.html', context)
    else:
        return redirect('no_permission')
    
    
@login_required(login_url='login')
@c_1_contract_project_index
def contract_project_index(request):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)
    notification = Actions.objects.all().filter(to_id=user_profile.id, is_read = False)
    notification_count = notification.count()
    all = Contract_Detail.objects.all().filter(project = user_profile.project_name).count()
    # حساب الاصدار الجديد
    new = Contract_Detail.objects.all().filter(sgnllast_status_action='اصدار جديد')
    sector_manager_count = new.filter(project = user_profile.project_name).count()

    # حساب مراجعة البيانات
    check_data = Contract_Detail.objects.all().filter(sgnllast_status_action='مراجعة البيانات')
    check_data_count = check_data.filter(project = user_profile.project_name).count()

    # حساب تقدير التكاليف
    cost_estimation = Contract_Detail.objects.all().filter(sgnllast_status_action='تقدير التكاليف')
    cost_estimation_count = cost_estimation.filter(project = user_profile.project_name).count()

    # حساب مراجعة المالية
    financial = Contract_Detail.objects.all().filter(sgnllast_status_action='مراجعة المالية')
    financial_count = financial.filter(project = user_profile.project_name).count()

    # حساب ناسخ العقود
    copy_contract = Contract_Detail.objects.all().filter(sgnllast_status_action='ناسخ العقد')
    copy_contract_count = copy_contract.filter(project = user_profile.project_name).count()

    # حساب مراجعة العقود
    check_contract = Contract_Detail.objects.all().filter(sgnllast_status_action='مراجعة العقد')
    check_contract_count = check_contract.filter(project = user_profile.project_name).count()

    # حساب اعتماد tcta
    tcta = Contract_Detail.objects.all().filter(sgnllast_status_action='اعتماد الاجراءات')
    tcta_count = tcta.filter(project = user_profile.project_name).count()

    # حساب اعتماد evp
    evp = Contract_Detail.objects.all().filter(sgnllast_status_action='نائب الرئيس التنفيذي')
    evp_count = evp.filter(project = user_profile.project_name).count()

    # حساب اعتماد ceo
    ceo = Contract_Detail.objects.all().filter(sgnllast_status_action='الرئيس التنفيذي')
    ceo_count = ceo.filter(project = user_profile.project_name).count()

    # حساب اعتماد asgnmnt
    asgnmnt = Contract_Detail.objects.all().filter(sgnllast_status_action='توقيعات')
    asgnmnt_count = asgnmnt.filter(project = user_profile.project_name).count()

    # حساب الرفض
    refuse = Contract_Detail.objects.all().filter(sgnllast_status_action='رفض')
    refuse_count = refuse.filter(project = user_profile.project_name).count()

    # حساب المكتمل
    complete = Contract_Detail.objects.all().filter(sgnllast_status_action='مكتمل')
    complete_count = complete.filter(project = user_profile.project_name).count()
    try:
        complete_percentage = round((complete_count/all)*100)
    except ZeroDivisionError:
        complete_percentage = 0
    
    # حساب الجاري
    inprogress = Contract_Detail.objects.all().filter(~Q(sgnllast_status_action='مكتمل'), ~Q(sgnllast_status_action='رفض'))
    inprogress_count = inprogress.filter(project = user_profile.project_name).count()



    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'user_profile':user_profile,
        'sector_manager_count':sector_manager_count,
        'check_data_count':check_data_count,
        'cost_estimation_count':cost_estimation_count,
        'financial_count':financial_count,
        'copy_contract_count':copy_contract_count,
        'check_contract_count':check_contract_count,
        'tcta_count':tcta_count,
        'evp_count':evp_count,
        'ceo_count':ceo_count,
        'asgn2_count':asgnmnt_count,
        'refuse_count':refuse_count,
        'complete_count':complete_count,
        'inprogress_count':inprogress_count,
        'notification_count':notification_count,
        'all':all,
        'complete_percentage':complete_percentage,

    }
    if request.user.is_staff:
        return render(request, 'contract/contract_main_index.html', context)
    else:
        return redirect('no_permission')


    
def contract_project_index_viewall(request):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)
    notification = Actions.objects.all().filter(to_id=user_profile.id, is_read = False)
    notification_count = notification.count()
    all = Contract_Detail.objects.all().filter(project = user_profile.project_name).count()
    complete = Contract_Detail.objects.all().filter(sgnllast_status_action='مكتمل')
    complete_count = complete.filter(project = user_profile.project_name).count()

    try:
        complete_percentage = round((complete_count/all)*100)
    except ZeroDivisionError:
        complete_percentage = 0

        # حساب الرفض
    refuse = Contract_Detail.objects.all().filter(sgnllast_status_action='رفض')
    refuse_count = refuse.filter(project = user_profile.project_name).count()
    # حساب الجاري
    inprogress = Contract_Detail.objects.all().filter(~Q(sgnllast_status_action='مكتمل'), ~Q(sgnllast_status_action='رفض'))
    inprogress_count = inprogress.filter(project = user_profile.project_name).count()


    contract_report = Contract_Detail.objects.all().filter(project = user_profile.project_name)
    searchFilter = ContractFilter(request.GET, queryset=contract_report.order_by('id'))
    contract_report = searchFilter.qs


    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'user_profile':user_profile,
        'contract_report':contract_report,
        'myFilter': searchFilter,

        'notification_count':notification_count,
        'complete_count':complete_count,
        'inprogress_count':inprogress_count,
        'all':all,
        'refuse_count':refuse_count,
        'complete_percentage':complete_percentage,

    }
    if request.user.is_staff:
        return render(request, 'contract/contract_main_index_viewall.html', context)
    else:
        return redirect('no_permission')



@login_required(login_url='login')
@c_4_cost_estimation_action
def contract_cost_estimation_index(request):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)
    notification = Actions.objects.all().filter(to_id=user_profile.id, is_read = False)
    notification_count = notification.count()
    all = Contract_Detail.objects.all().filter(cost_istimation = user_profile.sector_name).count()
    # حساب الاصدار الجديد
    new = Contract_Detail.objects.all().filter(sgnllast_status_action='اصدار جديد')
    sector_manager_count = new.filter(cost_istimation = user_profile.sector_name).count()

    # حساب مراجعة البيانات
    check_data = Contract_Detail.objects.all().filter(sgnllast_status_action='مراجعة البيانات')
    check_data_count = check_data.filter(cost_istimation = user_profile.sector_name).count()

    # حساب تقدير التكاليف
    cost_estimation = Contract_Detail.objects.all().filter(sgnllast_status_action='تقدير التكاليف')
    cost_estimation_count = cost_estimation.filter(cost_istimation = user_profile.sector_name).count()

    # حساب مراجعة المالية
    financial = Contract_Detail.objects.all().filter(sgnllast_status_action='مراجعة المالية')
    financial_count = financial.filter(cost_istimation = user_profile.sector_name).count()

    # حساب ناسخ العقود
    copy_contract = Contract_Detail.objects.all().filter(sgnllast_status_action='ناسخ العقد')
    copy_contract_count = copy_contract.filter(cost_istimation = user_profile.sector_name).count()

    # حساب مراجعة العقود
    check_contract = Contract_Detail.objects.all().filter(sgnllast_status_action='مراجعة العقد')
    check_contract_count = check_contract.filter(cost_istimation = user_profile.sector_name).count()

    # حساب اعتماد tcta
    tcta = Contract_Detail.objects.all().filter(sgnllast_status_action='اعتماد الاجراءات')
    tcta_count = tcta.filter(cost_istimation = user_profile.sector_name).count()

    # حساب اعتماد evp
    evp = Contract_Detail.objects.all().filter(sgnllast_status_action='نائب الرئيس التنفيذي')
    evp_count = evp.filter(cost_istimation = user_profile.sector_name).count()

    # حساب اعتماد ceo
    ceo = Contract_Detail.objects.all().filter(sgnllast_status_action='الرئيس التنفيذي')
    ceo_count = ceo.filter(cost_istimation = user_profile.sector_name).count()

    # حساب اعتماد asgnmnt
    asgnmnt = Contract_Detail.objects.all().filter(sgnllast_status_action='توقيعات')
    asgnmnt_count = asgnmnt.filter(cost_istimation = user_profile.sector_name).count()

    # حساب الرفض
    refuse = Contract_Detail.objects.all().filter(sgnllast_status_action='رفض')
    refuse_count = refuse.filter(cost_istimation = user_profile.sector_name).count()

    # حساب المكتمل
    complete = Contract_Detail.objects.all().filter(sgnllast_status_action='مكتمل')
    complete_count = complete.filter(cost_istimation = user_profile.sector_name).count()
    try:
        complete_percentage = round((complete_count/all)*100)
    except ZeroDivisionError:
        complete_percentage = 0
    
    # حساب الجاري
    inprogress = Contract_Detail.objects.all().filter(~Q(sgnllast_status_action='مكتمل'), ~Q(sgnllast_status_action='رفض'))
    inprogress_count = inprogress.filter(cost_istimation = user_profile.sector_name).count()



    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'user_profile':user_profile,
        'sector_manager_count':sector_manager_count,
        'check_data_count':check_data_count,
        'cost_estimation_count':cost_estimation_count,
        'financial_count':financial_count,
        'copy_contract_count':copy_contract_count,
        'check_contract_count':check_contract_count,
        'tcta_count':tcta_count,
        'evp_count':evp_count,
        'ceo_count':ceo_count,
        'asgn2_count':asgnmnt_count,
        'refuse_count':refuse_count,
        'complete_count':complete_count,
        'inprogress_count':inprogress_count,
        'notification_count':notification_count,
        'all':all,
        'complete_percentage':complete_percentage,

    }
    if request.user.is_staff:
        return render(request, 'contract/contract_main_index.html', context)
    else:
        return redirect('no_permission')


def contract_cost_estimation_index_viewall(request):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)
    notification = Actions.objects.all().filter(to_id=user_profile.id, is_read = False)
    notification_count = notification.count()
    all = Contract_Detail.objects.all().filter(cost_istimation = user_profile.sector_name).count()
    complete = Contract_Detail.objects.all().filter(sgnllast_status_action='مكتمل')
    complete_count = complete.filter(cost_istimation = user_profile.sector_name).count()

    try:
        complete_percentage = round((complete_count/all)*100)
    except ZeroDivisionError:
        complete_percentage = 0

        # حساب الرفض
    refuse = Contract_Detail.objects.all().filter(sgnllast_status_action='رفض')
    refuse_count = refuse.filter(cost_istimation = user_profile.sector_name).count()

    # حساب الجاري
    inprogress = Contract_Detail.objects.all().filter(~Q(sgnllast_status_action='مكتمل'), ~Q(sgnllast_status_action='رفض'))
    inprogress_count = inprogress.filter(cost_istimation = user_profile.sector_name).count()


    contract_report = Contract_Detail.objects.all().filter(cost_istimation = user_profile.sector_name)
    searchFilter = ContractFilter(request.GET, queryset=contract_report.order_by('id'))
    contract_report = searchFilter.qs


    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'user_profile':user_profile,
        'contract_report':contract_report,
        'myFilter': searchFilter,

        'notification_count':notification_count,
        'complete_count':complete_count,
        'inprogress_count':inprogress_count,
        'all':all,
        'refuse_count':refuse_count,
        'complete_percentage':complete_percentage,

    }
    if request.user.is_staff:
        return render(request, 'contract/contract_main_index_viewall.html', context)
    else:
        return redirect('no_permission')


# اجراءات ----------------------------------------------------------------------

@login_required(login_url='login')
@c_2_sector_manager_action
def sector_manager_action(request, pk):
    
    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)
    

    form = get_object_or_404(Contract_Detail, id=pk)
    form1 = form.Actions.all()
    Actions_records = form.Actions_records.all()

    

    
#  الملاحظات 
    form_action = Action_Form
    if request.method == 'POST':
        form_action = Action_Form(request.POST, request.FILES)
        if form_action.is_valid():
            instance = form_action.save(commit=False)
            instance.action_creator = user_profile.project_name
            instance.action_creator_name = user_profile.full_name
            instance.save()
            return HttpResponseRedirect(request.path_info)
        

#  اجراء مدير القطاع 
    sector_action = Sector_Form
    if request.method == 'POST':
        sector_action = Sector_Form(request.POST, request.FILES)
        if sector_action.is_valid():
            instance = sector_action.save(commit=False)
            instance.action_creator = user_profile.project_name
            instance.save()
            return redirect('contract_sector_index')
        

        

    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'form':form,
        'form1':form1,
        'user_profile':user_profile,
        'form_action':form_action,
        'sector_action':sector_action,
        'Actions_records':Actions_records,

    }
    if request.user.is_staff:
        return render(request, 'contract/sector_manager_action.html', context)
    else:
        return redirect('no_permission')

@login_required(login_url='login')
@c_3_check_data_action
def check_data_action(request, pk):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)
    

    form = get_object_or_404(Contract_Detail, id=pk)
    form1 = form.Actions.all()
    Actions_records = form.Actions_records.all()


    
#  الملاحظات 
    form_action = Action_Form
    if request.method == 'POST':
        form_action = Action_Form(request.POST, request.FILES)
        if form_action.is_valid():
            instance = form_action.save(commit=False)
            instance.action_creator = user_profile.project_name
            instance.action_creator_name = user_profile.full_name
            instance.save()
            return HttpResponseRedirect(request.path_info)
    
#  اجراء مراجعة البيانات       
    check_data_action = Check_data_Form
    if request.method == 'POST':
        check_data_action = Check_data_Form(request.POST, request.FILES)
        if check_data_action.is_valid():
            instance = check_data_action.save(commit=False)
            instance.action_creator = user_profile.project_name
            instance.save()
            return redirect('contract_main_index')

        

    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'form':form,
        'form1':form1,
        'user_profile':user_profile,
        'form_action':form_action,
        'check_data_action':check_data_action,
        'Actions_records':Actions_records,



    }
    if request.user.is_staff:
        return render(request, 'contract/sector_manager_action.html', context)
    else:
        return redirect('no_permission')
    
@login_required(login_url='login')
@c_4_cost_estimation_action
def cost_estimation_action(request, pk):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)
    

    form = get_object_or_404(Contract_Detail, id=pk)
    form1 = form.Actions.all()
    Actions_records = form.Actions_records.all()

    
#  الملاحظات 
    form_action = Action_Form
    if request.method == 'POST':
        form_action = Action_Form(request.POST, request.FILES)
        if form_action.is_valid():
            instance = form_action.save(commit=False)
            instance.action_creator = user_profile.project_name
            instance.action_creator_name = user_profile.full_name
            instance.save()
            return HttpResponseRedirect(request.path_info)
        
#  اجراء تقدير التكاليف      
    cost_estimation_action = Cost_estimation_Form
    if request.method == 'POST':
        cost_estimation_action = Cost_estimation_Form(request.POST, request.FILES)
        if cost_estimation_action.is_valid():
            instance = cost_estimation_action.save(commit=False)
            instance.action_creator = user_profile.project_name
            instance.save()
            return redirect('contract_main_index') 
        

    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'form':form,
        'form1':form1,
        'user_profile':user_profile,
        'form_action':form_action,
        'cost_estimation_action':cost_estimation_action,
        'Actions_records':Actions_records,

    }
    if request.user.is_staff:
        return render(request, 'contract/sector_manager_action.html', context)
    else:
        return redirect('no_permission')
    
@login_required(login_url='login')
@c_5_financial_action
def financial_action(request, pk):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)
    

    form = get_object_or_404(Contract_Detail, id=pk)
    form1 = form.Actions.all()
    Actions_records = form.Actions_records.all()

    
#  الملاحظات 
    form_action = Action_Form
    if request.method == 'POST':
        form_action = Action_Form(request.POST, request.FILES)
        if form_action.is_valid():
            instance = form_action.save(commit=False)
            instance.action_creator = user_profile.project_name
            instance.action_creator_name = user_profile.full_name
            instance.save()
            return HttpResponseRedirect(request.path_info)
        
#  اجراء مراجعة المالية       
        
    financial_action = Financial_Form
    if request.method == 'POST':
        financial_action = Financial_Form(request.POST, request.FILES)
        if financial_action.is_valid():
            instance = financial_action.save(commit=False)
            instance.action_creator = user_profile.project_name
            instance.save()
            return redirect('contract_main_index') 
        

    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'form':form,
        'form1':form1,
        'user_profile':user_profile,
        'form_action':form_action,
        'financial_action':financial_action,
        'Actions_records':Actions_records,


    }
    if request.user.is_staff:
        return render(request, 'contract/sector_manager_action.html', context)
    else:
        return redirect('no_permission')
    
@login_required(login_url='login')
@c_6_copy_contract_action
def copy_contract_action(request, pk):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)
    template = Contract_template.objects.all()

    form = get_object_or_404(Contract_Detail, id=pk)
    form1 = form.Actions.all()
    Actions_records = form.Actions_records.all()

    
#  الملاحظات 
    form_action = Action_Form
    if request.method == 'POST':
        form_action = Action_Form(request.POST, request.FILES)
        if form_action.is_valid():
            instance = form_action.save(commit=False)
            instance.action_creator = user_profile.project_name
            instance.action_creator_name = user_profile.full_name
            instance.save()
            return HttpResponseRedirect(request.path_info)
    
#  رقم العقد 
    form_contract_code = Contract_code_Form
    if request.method == 'POST':
        form_contract_code = Contract_code_Form(request.POST)
        if form_contract_code.is_valid():
            instance = form_contract_code.save(commit=False)
            instance.save()
            return HttpResponseRedirect(request.path_info)
        
#  اجراء نسخ العقد            
    copy_contract_action = Copy_contract_Form
    if request.method == 'POST':
        copy_contract_action = Copy_contract_Form(request.POST, request.FILES)
        if copy_contract_action.is_valid():
            instance = copy_contract_action.save(commit=False)
            instance.action_creator = user_profile.project_name
            instance.save()
            return redirect('contract_main_index') 
        

    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'form':form,
        'form1':form1,
        'user_profile':user_profile,
        'form_action':form_action,
        'copy_contract_action':copy_contract_action,
        'template':template,
        'Actions_records':Actions_records,

        'form_contract_code':form_contract_code,
    }
    if request.user.is_staff:
        return render(request, 'contract/sector_manager_action.html', context)
    else:
        return redirect('no_permission')
    
@login_required(login_url='login')
@c_7_check_contract_action
def check_contract_action(request, pk):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)
    

    form = get_object_or_404(Contract_Detail, id=pk)
    form1 = form.Actions.all()
    Actions_records = form.Actions_records.all()

    
#  الملاحظات 
    form_action = Action_Form
    if request.method == 'POST':
        form_action = Action_Form(request.POST, request.FILES)
        if form_action.is_valid():
            instance = form_action.save(commit=False)
            instance.action_creator = user_profile.project_name
            instance.action_creator_name = user_profile.full_name
            instance.save()
            return HttpResponseRedirect(request.path_info)
        
#  اجراء مراجعة العقد           
    check_contract_action = Check_contract_Form
    if request.method == 'POST':
        check_contract_action = Check_contract_Form(request.POST, request.FILES)
        if check_contract_action.is_valid():
            instance = check_contract_action.save(commit=False)
            instance.action_creator = user_profile.project_name
            instance.save()
            return redirect('contract_main_index') 
        

    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'form':form,
        'form1':form1,
        'user_profile':user_profile,
        'form_action':form_action,
        'check_contract_action':check_contract_action,
        'Actions_records':Actions_records,

    }
    if request.user.is_staff:
        return render(request, 'contract/sector_manager_action.html', context)
    else:
        return redirect('no_permission')
    
@login_required(login_url='login')
@c_8_tcta_action
def tcta_action(request, pk):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)
    

    form = get_object_or_404(Contract_Detail, id=pk)
    form1 = form.Actions.all()
    Actions_records = form.Actions_records.all()

#  الملاحظات 
    form_action = Action_Form
    if request.method == 'POST':
        form_action = Action_Form(request.POST, request.FILES)
        if form_action.is_valid():
            instance = form_action.save(commit=False)
            instance.action_creator = user_profile.project_name
            instance.action_creator_name = user_profile.full_name
            instance.save()
            return HttpResponseRedirect(request.path_info)
        
#  اجراء مدير tcta       
    tcta_action = TCTA_Form
    if request.method == 'POST':
        tcta_action = TCTA_Form(request.POST, request.FILES)
        if tcta_action.is_valid():
            instance = tcta_action.save(commit=False)
            instance.action_creator = user_profile.project_name
            instance.save()
            return redirect('contract_main_index') 
        

    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'form':form,
        'form1':form1,
        'user_profile':user_profile,
        'form_action':form_action,
        'tcta_action':tcta_action,
        'Actions_records':Actions_records,

    }
    if request.user.is_staff:
        return render(request, 'contract/sector_manager_action.html', context)
    else:
        return redirect('no_permission')

@login_required(login_url='login')
@c_9_evp_action
def evp_action(request, pk):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)
    

    form = get_object_or_404(Contract_Detail, id=pk)
    form1 = form.Actions.all()
    Actions_records = form.Actions_records.all()

#  الملاحظات 
    form_action = Action_Form
    if request.method == 'POST':
        form_action = Action_Form(request.POST, request.FILES)
        if form_action.is_valid():
            instance = form_action.save(commit=False)
            instance.action_creator = user_profile.project_name
            instance.action_creator_name = user_profile.full_name
            instance.save()
            return HttpResponseRedirect(request.path_info)
        
#  اجراء نائب الرئيس التنفيذي       
    evp_action = EVP_Form
    if request.method == 'POST':
        evp_action = EVP_Form(request.POST, request.FILES)
        if evp_action.is_valid():
            instance = evp_action.save(commit=False)
            instance.action_creator = user_profile.project_name
            instance.save()
            return redirect('contract_main_index') 
    
        

    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'form':form,
        'form1':form1,
        'user_profile':user_profile,
        'form_action':form_action,
        'evp_action':evp_action,
        'Actions_records':Actions_records,

    }
    if request.user.is_staff:
        return render(request, 'contract/sector_manager_action.html', context)
    else:
        return redirect('no_permission')
    
@login_required(login_url='login')
@c_10_ceo_action
def ceo_action(request, pk):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)
    

    form = get_object_or_404(Contract_Detail, id=pk)
    form1 = form.Actions.all()
    Actions_records = form.Actions_records.all()

    
#  الملاحظات 
    form_action = Action_Form
    if request.method == 'POST':
        form_action = Action_Form(request.POST, request.FILES)
        if form_action.is_valid():
            instance = form_action.save(commit=False)
            instance.action_creator = user_profile.project_name
            instance.action_creator_name = user_profile.full_name
            instance.save()
            return HttpResponseRedirect(request.path_info)
        
#  اجراء الرئيس التنفيذي       


    ceo_action = CEO_Form
    if request.method == 'POST':
        ceo_action = CEO_Form(request.POST, request.FILES)
        if ceo_action.is_valid():
            instance = ceo_action.save(commit=False)
            instance.action_creator = user_profile.project_name
            instance.save()
            return redirect('contract_main_index') 
        
        

    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'form':form,
        'form1':form1,
        'user_profile':user_profile,
        'form_action':form_action,
        'ceo_action':ceo_action,
        'Actions_records':Actions_records,

    }
    if request.user.is_staff:
        return render(request, 'contract/sector_manager_action.html', context)
    else:
        return redirect('no_permission')
    
@login_required(login_url='login')
@c_11_assignAttach2_action
def assignmnt_action(request, pk):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    user_profile = User_Profile.objects.get(user=request.user)
    

    form = get_object_or_404(Contract_Detail, id=pk)
    form1 = form.Actions.all()  
    Actions_records = form.Actions_records.all()

#  الملاحظات 
    form_action = Action_Form
    if request.method == 'POST':
        form_action = Action_Form(request.POST, request.FILES)
        if form_action.is_valid():
            instance = form_action.save(commit=False)
            instance.action_creator = user_profile.project_name
            instance.action_creator_name = user_profile.full_name
            instance.save()
            return HttpResponseRedirect(request.path_info)
        
#  اجراء توقيع الطرف الثاني       
    assignmnt_action = Assignmnt_Form
    if request.method == 'POST':
        assignmnt_action = Assignmnt_Form(request.POST, request.FILES)
        if assignmnt_action.is_valid():
            instance = assignmnt_action.save(commit=False)
            instance.action_creator = user_profile.project_name
            instance.save()
            return redirect('contract_main_index') 
        

    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        'form':form,
        'form1':form1,
        'user_profile':user_profile,
        'form_action':form_action,
        'assignmnt_action':assignmnt_action,
        'Actions_records':Actions_records,

    }
    if request.user.is_staff:
        return render(request, 'contract/sector_manager_action.html', context)
    else:
        return redirect('no_permission')
    

