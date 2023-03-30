
from django.shortcuts import render, redirect
from .models import *
from main.models import *
from .forms import *
from .filters import *
from django.contrib.auth.decorators import login_required
from main.decorators import *

# Create your views here.


@login_required(login_url='login')
@tendering_main_index

def tendering_main_index(request):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)

    detail = T_detail.objects.all()

    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,

        'AllTenders':detail.count(),
        'OngoingTenders':detail.filter(t_status='جارية').count(),
        'OngoingTendersPercentag':round((detail.filter(t_status='جارية').count()/detail.count())*100),
        'SubmittedTenders':detail.filter(t_status='تم التقديم').count(),
        'SubmittedTendersPercentag':round((detail.filter(t_status='تم التقديم').count()/detail.count())*100),
        'CancelededTenders':detail.filter(t_status='ملغية').count(),
        'CancelededTendersPercentag':round((detail.filter(t_status='ملغية').count()/detail.count())*100),
    }
    if request.user.is_staff:
        return render(request, 'tendering/tendering_main_index.html', context)
    else:
        return redirect('no_permission')


@login_required(login_url='login')

@tendering_user_index

def tendering_user_index(request):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    context = {

        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        
    }
    if request.user.is_staff:
        return render(request, 'tendering/tendering_user_index.html', context)
    else:
        return redirect('no_permission')
    
@login_required(login_url='login')
@add_new_tender

def add_new_tender(request):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)

    form = T_detail_Form()
    if request.method == 'POST':
        form = T_detail_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tender_details')
    context = {
        
        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,

        'form':form,
        
        }
    if request.user.is_staff:
        return render(request, 'tendering/add_new_tender.html', context)
    else:
        return redirect('no_permission')

@login_required(login_url='login')
@update_tender

def update_tender(request,id):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)

    pp = T_detail.objects.filter(t_status='جارية')
    update_tender = pp.get(id=id)
    form = T_detail_Form(instance=update_tender)
    if request.method == 'POST':
        form = T_detail_Form(request.POST, instance=update_tender)
        if form.is_valid():
            form.save()
            return redirect('tender_details')
    context = {
        
        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        
        'form':form,
               }
    if request.user.is_staff:
        return render(request, 'tendering/update_tender.html', context)
    else:
        return redirect('no_permission')

@login_required(login_url='login')
@preview_tender
def tender_details(request):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)

    detail = T_detail.objects.all()
    t_count = T_detail.objects.all()
    searchFilter = TenderFilter(request.GET, queryset=detail.order_by('-no'))
    detail = searchFilter.qs
    context = {
        
        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        
        'myFilter': searchFilter,
        't_count': t_count.count(),
               
               }
    if request.user.is_staff:
        return render(request, 'tendering/tender_details.html', context)
    else:
        return redirect('no_permission')

@login_required(login_url='login')
@preview_tender
def tender_details_details(request, id):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)

    t_d = T_detail.objects.get(id=id)
    context = {
        
        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,
        
        'mm': t_d,
               
               }
    if request.user.is_staff:
        return render(request, 'tendering/tender_details_details.html', context)
    else:
        return redirect('no_permission')




@login_required(login_url='login')
@preview_tender
def tender_report(request):

    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)

    detail = T_detail.objects.all()
    detail_count = T_detail.objects.all()
    searchFilter = TenderFilter(request.GET, queryset=detail.filter(t_status='جارية').order_by('submit_date'))
    detail = searchFilter.qs.filter
    context = {
        
        'user_tender_permission':user_tender_permission,
        'user_contract_permission':user_contract_permission,
        'user_project_permission':user_project_permission,

        'myFilter': searchFilter,
        'detail_count': detail_count.filter(t_status='جارية').count(),
               
               }
    
    if request.user.is_staff:
        return render(request, 'tendering/tender_report.html', context)
    else:
        return redirect('no_permission')