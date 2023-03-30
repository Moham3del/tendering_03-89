from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from main.models import *
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from datetime import date, timezone
from dateutil.relativedelta import relativedelta
from django.utils.timezone import datetime
from itertools import chain



# Create your models here.



def validate_rc(value):
    limit = date.today() + relativedelta(days=15)
    
    if value < limit:
        raise ValidationError(
            ('صلاحية 30 يوم على الأقل'),
            params={'value': value},
        )


class Contract_Detail(models.Model):


    contract_value = [
        ('حسب المنفذ على الطبيعة', 'حسب المنفذ على الطبيعة'),
        ('قيمة', 'قيمة'),
    ]

    contract_type = [
        ('توريد + تنفيذ', 'توريد + تنفيذ'),
        ('توريد', 'توريد'),
        ('تنفيذ', 'تنفيذ'),
    ]

    cost_istimation = [
        ('إنشاءات (أ)', 'إنشاءات (أ)'),
        ('بنية تحتية (ج)', 'بنية تحتية (ج)'),
    ]

    establishment_company = [
        ('مؤسسة', 'مؤسسة'),
        ('شركة', 'شركة'),
    ]
    price_analysis_status = [
        
        ('مطلوب', 'مطلوب'),
        ('غير مطلوب', 'غير مطلوب'),
    ]
    # creator
    contract_no = models.IntegerField(null=True, blank=True)
    contract_year = models.IntegerField(null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    creator = models.CharField(max_length=250, null=True, blank=True)
    creator_name = models.CharField(max_length=250, null=True, blank=True)
    sector = models.CharField(max_length=250, null=True, blank=True)
    project = models.CharField(max_length=250, null=True, blank=True)

    # contract

    works_type = models.CharField(max_length=250, null=False, blank=False)
    contract_type =  models.CharField(max_length=250, choices=contract_type, null=False, blank=False)
    contract_value =  models.IntegerField(null=False, blank=False)
    contract_duration =  models.IntegerField(null=False, blank=False)
    cost_istimation =  models.CharField(max_length=250, choices=cost_istimation, null=False, blank=False)
    secondParty_name = models.CharField(max_length=250, null=False, blank=False)
    price_analysis_status = models.CharField(max_length=250, choices=price_analysis_status, null=False, blank=False)
    price_analysis = models.FileField(null=True, blank=False, upload_to='files/%Y/%m/%d')
    # bank_account =  models.IntegerField(null=False, blank=False)
    iban =  models.IntegerField(null=False, blank=False)
    tax_number =  models.IntegerField(null=True, blank=True)
    signature_authorization =  models.FileField(null=True, blank=False, upload_to='files/%Y/%m/%d')
    delegated_nam = models.CharField(max_length=250, null=False, blank=False)
    delegated_title = models.CharField(max_length=250, null=False, blank=False)
    gov_id_no = models.CharField(max_length=250, null=False, blank=False)
    second_party_representative = models.CharField(max_length=250, null=True, blank=True)
    phone_no = models.IntegerField(null=False, blank=False)
    email = models.EmailField(null=False, blank=False, max_length=50)
    postal_code = models.CharField(max_length=20, null=False, blank=False)
    address = models.CharField(max_length=250, null=False, blank=False)
    commercial_register =  models.FileField(null=False, blank=False, upload_to='files/%Y/%m/%d')
    commercial_register_date =  models.DateField(null=False, blank=False, validators=[validate_rc])
    establishment_company = models.CharField(max_length=250,choices=establishment_company, null=False, blank=False)
    association_contract =  models.FileField(null=True, blank=True, upload_to='files/%Y/%m/%d')
    zakat_Income_certificate =  models.FileField(null=False, blank=False, upload_to='files/%Y/%m/%d')
    sub_contractor_profile =  models.FileField(null=True, blank=True, upload_to='files/%Y/%m/%d')
    project_original_contract_quantities_table_copy =  models.FileField(null=True, blank=True, upload_to='files/%Y/%m/%d')
    contract_quantities_table =  models.FileField(null=False, blank=False, upload_to='files/%Y/%m/%d', validators=[FileExtensionValidator(['xlsx'])])
    special_conditions =  models.TextField(null=False, blank=False)
    payment_terms =  models.TextField(null=False, blank=False)
    
    # اشارة اعتماد مدير القطاع
    sgnlsectorManager_action_creator =models.CharField(max_length=250, null=True, blank=True)
    sgnlsectorManager_action_creator_name =models.CharField(max_length=250, null=True, blank=True)
    sgnlsectorManager_action_date = models.DateTimeField(null=True, blank=True)
    sgnlsectorManager_action = models.CharField(max_length=250, null=True, blank=True)
    sgnlsectorManager_action_note = models.CharField(max_length=250, null=True, blank=True)

    # اشارة اعتماد مراجع البيانات
    sgnlcheckData_action_creator =models.CharField(max_length=250, null=True, blank=True)
    sgnlcheckData_action_creator_name =models.CharField(max_length=250, null=True, blank=True)
    sgnlcheckData_action_date = models.DateTimeField(null=True, blank=True)
    sgnlcheckData_action = models.CharField(max_length=250, null=True, blank=True)

    # اشارة اعتماد تقدير التكاليف
    sgnlcostEstimation_action_creator =models.CharField(max_length=250, null=True, blank=True)
    sgnlcostEstimation_action_creator_name =models.CharField(max_length=250, null=True, blank=True)
    sgnlcostEstimation_action_date = models.DateTimeField(null=True, blank=True)
    sgnlcostEstimation_action = models.CharField(max_length=250, null=True, blank=True)
    sgnlcostEstimation_actionFile = models.FileField(null=True, blank=True, upload_to='files/%Y/%m/%d')

    # اشارة اعتماد المالية
    sgnlfinancial_action_creator =models.CharField(max_length=250, null=True, blank=True)
    sgnlfinancial_action_creator_name =models.CharField(max_length=250, null=True, blank=True)
    sgnlfinancial_action_date = models.DateTimeField(null=True, blank=True)
    sgnlfinancial_action = models.CharField(max_length=250, null=True, blank=True)
    sgnlfinancial_action_note = models.CharField(max_length=250, null=True, blank=True)

    # اشارة ناسخ العقود
    sgnlcopyContract_action_creator =models.CharField(max_length=250, null=True, blank=True)
    sgnlcopyContract_action_creator_name =models.CharField(max_length=250, null=True, blank=True)
    sgnlcopyContract_action_date = models.DateTimeField(null=True, blank=True)
    sgnlcopyContract_action = models.CharField(max_length=250, null=True, blank=True)
    sgnlcopyContract_actionFile = models.FileField(null=True, blank=True, upload_to='files/%Y/%m/%d')

    # اشارة مراجع العقود
    sgnlcheckContract_action_creator =models.CharField(max_length=250, null=True, blank=True)
    sgnlcheckContract_action_creator_name =models.CharField(max_length=250, null=True, blank=True)
    sgnlcheckContract_action_date = models.DateTimeField(null=True, blank=True)
    sgnlcheckContract_action = models.CharField(max_length=250, null=True, blank=True)
    sgnlcheckContract_action_note = models.CharField(max_length=250, null=True, blank=True)
    sgnlcheckContract_actionFile = models.FileField(null=True, blank=True, upload_to='files/%Y/%m/%d')

    # اشارة tcta
    sgnltcta_action_creator =models.CharField(max_length=250, null=True, blank=True)
    sgnltcta_action_creator_name =models.CharField(max_length=250, null=True, blank=True)
    sgnltcta_action_date = models.DateTimeField(null=True, blank=True)
    sgnltcta_action = models.CharField(max_length=250, null=True, blank=True)
    sgnltcta_action_note = models.CharField(max_length=250, null=True, blank=True)

    # اشارة evp
    sgnlevp_action_creator =models.CharField(max_length=250, null=True, blank=True)
    sgnlevp_action_creator_name =models.CharField(max_length=250, null=True, blank=True)
    sgnlevp_action_date = models.DateTimeField(null=True, blank=True)
    sgnlevp_action = models.CharField(max_length=250, null=True, blank=True)
    sgnlevp_action_note = models.CharField(max_length=250, null=True, blank=True)
    

    # اشارة ceo
    sgnlceo_action_creator =models.CharField(max_length=250, null=True, blank=True)
    sgnlceo_action_creator_name =models.CharField(max_length=250, null=True, blank=True)
    sgnlceo_action_date = models.DateTimeField(null=True, blank=True)
    sgnlceo_action = models.CharField(max_length=250, null=True, blank=True)
    sgnlceo_action_note = models.CharField(max_length=250, null=True, blank=True)

    # اشارة assignmnt
    sgnlassignmnt_action_creator =models.CharField(max_length=250, null=True, blank=True)
    sgnlassignmnt_action_creator_name =models.CharField(max_length=250, null=True, blank=True)
    sgnlassignmnt_action_date = models.DateTimeField(null=True, blank=True)
    copy_contract_assign = models.CharField(max_length=250, null=True, blank=True)
    financial_assign = models.CharField(max_length=250, null=True, blank=True)
    check_contract_assign = models.CharField(max_length=250, null=True, blank=True)
    second_party_assign = models.CharField(max_length=250, null=True, blank=True)
    first_party_assign = models.CharField(max_length=250, null=True, blank=True)
    sgnlassignmnt_actionFile = models.FileField(null=True, blank=True, upload_to='files/%Y/%m/%d')

    # اشارة last_status
    sgnllast_status_action = models.CharField(max_length=250, null=True, blank=True, default='اصدار جديد')
    sgnllast_status_note = models.CharField(max_length=250, null=True, blank=True)


    def __str__(self):
        return str(self.id)
    class Meta:
        verbose_name="Contract_Detail"
        ordering = ['id']

    @property
    def Request_duration(self):
        today = datetime.now(timezone.utc)
        
        request_duration = today - self.creation_date
        if request_duration.days > 0:
            request_duration1 = request_duration - relativedelta(hours=24)
            return str(request_duration.days) + ' يوم ' + str(request_duration1)[21:22] + ' ساعة'
        else:
           return str(request_duration)[:4] + ' ساعة'

    @property
    def Contract_duration(self):

        
        request_duration = self.sgnlassignmnt_action_date - self.creation_date
        if request_duration.days > 0:
            request_duration1 = request_duration - relativedelta(hours=24)
            return str(request_duration.days) + ' يوم ' + str(request_duration1)[21:22] + ' ساعة'
        else:
           return str(request_duration)[:4] + ' ساعة'

    @property
    def Contract_code(self):

        
        if self.contract_no is not None:
            code =str(self.contract_year)+  '/' + str(self.contract_no)
            return code


        




class Actions(models.Model):

    request_no = models.ForeignKey(Contract_Detail, on_delete=models.CASCADE, null=True, blank=True, related_name='Actions')
    action_creator = models.CharField(max_length=250, null=True, blank=True)
    action_creator_name = models.CharField(max_length=250, null=True, blank=True)
    action_notes = models.TextField(max_length=250, null=False, blank=False)
    action_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    action_file =  models.FileField(null=True, blank=True, upload_to='files/%Y/%m/%d')
    to = models.ForeignKey(User_Profile, on_delete=models.CASCADE, null=False, blank=False, related_name='Action_to')
    is_read = models.BooleanField(default=False)
    extra_id = models.IntegerField(null=True, blank=True)




    def __str__(self):
        return str(self.request_no)
    class Meta:
        verbose_name="Action"
        ordering = ['action_date']



class Actions_records(models.Model):


    action_no = models.ForeignKey(Contract_Detail, on_delete=models.CASCADE, related_name='Actions_records')
    action_creator =models.CharField(max_length=250, null=True, blank=True)
    action_creator_name =models.CharField(max_length=250, null=True, blank=True)
    action_date = models.DateTimeField(null=True, blank=True, auto_now=True)
    action = models.CharField(max_length=250, null=True, blank=True)
    action_note = models.CharField(max_length=250, null=True, blank=True)
    action_file =  models.FileField(null=True, blank=True, upload_to='files/%Y/%m/%d')


    def __str__(self):
        return str(self.id)
    class Meta:
        verbose_name="Actions_records"


class Sector_manager_action(models.Model):


    action = [
    ('قبول', 'قبول'),
    ('رفض', 'رفض'),
]
    action_no = models.ForeignKey(Contract_Detail, on_delete=models.CASCADE, related_name='Sector_manager_action')
    action_creator =models.CharField(max_length=250, null=True, blank=True)
    action_creator_name =models.CharField(max_length=250, null=True, blank=True)
    action_date = models.DateTimeField(null=True, blank=True, auto_now=True)
    action = models.CharField(max_length=250, null=False, blank=False, choices=action)
    action_note = models.CharField(max_length=250, null=True, blank=True)


    def __str__(self):
        return str(self.id)
    class Meta:
        verbose_name="Sector_manager_action"


@receiver(post_save, sender=Sector_manager_action)
def creat_Actions_records(sender, instance, created, **kwargs):
    if created:
        Actions_records.objects.create(action_no=instance.action_no, action_creator = instance.action_creator, action_creator_name = instance.action_creator_name, action_date = datetime.now(), action = instance.action, action_note = instance.action_note)
        



@receiver(pre_save, sender=Sector_manager_action)
def update_sector_status(sender, instance, *args, **kwargs):
    if instance.action and instance.action_no_id is not None:
        Contract_Detail = instance.action_no
        Contract_Detail.sgnlsectorManager_action_creator = instance.action_creator
        Contract_Detail.sgnlsectorManager_action_creator_name = instance.action_creator_name
        Contract_Detail.sgnlsectorManager_action_date = datetime.now()
        Contract_Detail.sgnlsectorManager_action = instance.action
        Contract_Detail.sgnlsectorManager_action_note = instance.action_note
        Contract_Detail.save(update_fields=('sgnlsectorManager_action_creator',))
        Contract_Detail.save(update_fields=('sgnlsectorManager_action_creator_name',))
        Contract_Detail.save(update_fields=('sgnlsectorManager_action_date',))
        Contract_Detail.save(update_fields=('sgnlsectorManager_action',))
        Contract_Detail.save(update_fields=('sgnlsectorManager_action_note',))

        if instance.action == 'قبول':
            Contract_Detail.sgnllast_status_action = 'مراجعة البيانات'
        elif instance.action == 'رفض':
            Contract_Detail.sgnllast_status_action = 'رفض'
        Contract_Detail.save(update_fields=('sgnllast_status_action',))



class Check_data_action(models.Model):


    action = [
    ('قبول', 'قبول'),
]
    action_no = models.ForeignKey(Contract_Detail, on_delete=models.CASCADE, related_name='Check_data_action')
    action_creator =models.CharField(max_length=250)
    action_creator_name =models.CharField(max_length=250)
    action_date = models.DateTimeField(null=True, blank=True, auto_now=True)
    action = models.CharField(max_length=250, null=False, blank=False, choices=action)


    def __str__(self):
        return str(self.id)
    class Meta:
        verbose_name="Check_data_action"

@receiver(post_save, sender=Check_data_action)
def creat_Actions_records(sender, instance, created, **kwargs):
    if created:
        Actions_records.objects.create(action_no=instance.action_no, action_creator = instance.action_creator, action_creator_name = instance.action_creator_name, action_date = datetime.now(), action = instance.action)
          

@receiver(pre_save, sender=Check_data_action)
def update_Check_data_status(sender, instance, *args, **kwargs):
    if instance.action and instance.action_no_id is not None:
        Contract_Detail = instance.action_no
        Contract_Detail.sgnlcheckData_action_creator = instance.action_creator
        Contract_Detail.sgnlcheckData_action_creator_name = instance.action_creator_name
        Contract_Detail.sgnlcheckData_action_date = datetime.now()
        Contract_Detail.sgnlcheckData_action = instance.action
        Contract_Detail.save(update_fields=('sgnlcheckData_action_creator',))
        Contract_Detail.save(update_fields=('sgnlcheckData_action_creator_name',))
        Contract_Detail.save(update_fields=('sgnlcheckData_action_date',))
        Contract_Detail.save(update_fields=('sgnlcheckData_action',))

        if instance.action == 'قبول':
            Contract_Detail.sgnllast_status_action = 'تقدير التكاليف'
        Contract_Detail.save(update_fields=('sgnllast_status_action',))



class Cost_estimation_action(models.Model):


    action = [
    ('قبول', 'قبول'),
    ('تحديث', 'تحديث'),
]
    action_no = models.ForeignKey(Contract_Detail, on_delete=models.CASCADE, related_name='Cost_estimation_action')
    action_creator =models.CharField(max_length=250)
    action_creator_name =models.CharField(max_length=250)
    action_date = models.DateTimeField(null=True, blank=True, auto_now=True)
    action = models.CharField(max_length=250, null=False, blank=False, choices=action)
    action_file =  models.FileField(null=False, blank=False, upload_to='files/%Y/%m/%d')


    def __str__(self):
        return str(self.id)
    class Meta:
        verbose_name="Cost_estimation_action"

@receiver(post_save, sender=Cost_estimation_action)
def creat_Actions_records(sender, instance, created, **kwargs):
    if created:
        Actions_records.objects.create(action_no=instance.action_no, action_creator = instance.action_creator, action_creator_name = instance.action_creator_name, action_date = datetime.now(), action = instance.action, action_file = instance.action_file)
          

        


@receiver(pre_save, sender=Cost_estimation_action)
def update_Cost_estimation_status(sender, instance, *args, **kwargs):
    if instance.action and instance.action_no_id is not None:
        Contract_Detail = instance.action_no
        Contract_Detail.sgnlcostEstimation_action_creator = instance.action_creator
        Contract_Detail.sgnlcostEstimation_action_creator_name = instance.action_creator_name
        Contract_Detail.sgnlcostEstimation_action_date = datetime.now()
        Contract_Detail.sgnlcostEstimation_action = instance.action
        Contract_Detail.sgnlcostEstimation_actionFile = instance.action_file
        Contract_Detail.save(update_fields=('sgnlcostEstimation_action_creator',))
        Contract_Detail.save(update_fields=('sgnlcostEstimation_action_creator_name',))
        Contract_Detail.save(update_fields=('sgnlcostEstimation_action_date',))
        Contract_Detail.save(update_fields=('sgnlcostEstimation_action',))
        Contract_Detail.save(update_fields=('sgnlcostEstimation_actionFile',))

        if instance.action == 'قبول':
            Contract_Detail.sgnllast_status_action = 'مراجعة المالية'

        elif instance.action == 'تحديث':
            Contract_Detail.sgnllast_status_action = 'مراجعة المالية'
        Contract_Detail.save(update_fields=('sgnllast_status_action',))



class Financial_action(models.Model):


    action = [
    ('قبول', 'قبول'),
    ('ملاحظات', 'ملاحظات'),
]
    action_no = models.ForeignKey(Contract_Detail, on_delete=models.CASCADE, related_name='Financial_action')
    action_creator =models.CharField(max_length=250)
    action_creator_name =models.CharField(max_length=250)
    action_date = models.DateTimeField(null=True, blank=True, auto_now=True)
    action = models.CharField(max_length=250, null=False, blank=False, choices=action)
    action_note = models.CharField(max_length=250, null=True, blank=True)


    def __str__(self):
        return str(self.id)
    class Meta:
        verbose_name="Financial_action"

@receiver(post_save, sender=Financial_action)
def creat_Actions_records(sender, instance, created, **kwargs):
    if created:
        Actions_records.objects.create(action_no=instance.action_no, action_creator = instance.action_creator, action_creator_name = instance.action_creator_name, action_date = datetime.now(), action = instance.action, action_note = instance.action_note)
          

        

@receiver(pre_save, sender=Financial_action)
def update_Financial_status(sender, instance, *args, **kwargs):
    if instance.action and instance.action_no_id is not None:
        Contract_Detail = instance.action_no
        Contract_Detail.sgnlfinancial_action_creator = instance.action_creator
        Contract_Detail.sgnlfinancial_action_creator_name = instance.action_creator_name
        Contract_Detail.sgnlfinancial_action_date = datetime.now()
        Contract_Detail.sgnlfinancial_action = instance.action
        Contract_Detail.sgnlfinancial_action_note = instance.action_note
        Contract_Detail.save(update_fields=('sgnlfinancial_action_creator',))
        Contract_Detail.save(update_fields=('sgnlfinancial_action_creator_name',))
        Contract_Detail.save(update_fields=('sgnlfinancial_action_date',))
        Contract_Detail.save(update_fields=('sgnlfinancial_action',))
        Contract_Detail.save(update_fields=('sgnlfinancial_action_note',))

        if instance.action == 'قبول':
            Contract_Detail.sgnllast_status_action = 'ناسخ العقد'

        elif instance.action == 'ملاحظات':
            Contract_Detail.sgnllast_status_action = 'تقدير التكاليف'
        Contract_Detail.save(update_fields=('sgnllast_status_action',))
        
def next_number():
    
    
    data = Contract_code._base_manager.filter(
        date__year=now().year
    ).aggregate(
        max_number=Max('number')
    )['max_number'] or 0
    return data + 1

from django.db.models import Max
from django.utils.timezone import now

class Contract_code(models.Model):
   request_no = models.OneToOneField(Contract_Detail, on_delete=models.CASCADE)
   ID = models.AutoField(primary_key=True)
   date = models.DateField(auto_now_add=True)
   year = models.IntegerField(default=now().year, null=True, blank=True)
   number = models.IntegerField(default=next_number, editable=True, null=True, blank=True)



@receiver(pre_save, sender=Contract_code)
def update_Contract_code(sender, instance, *args, **kwargs):
    if instance.number and instance.request_no_id is not None:
        Contract_Detail = instance.request_no
        Contract_Detail.contract_no = instance.number
        Contract_Detail.contract_year = instance.year
        Contract_Detail.save(update_fields=('contract_no',))
        Contract_Detail.save(update_fields=('contract_year',))



class Copy_contract_action(models.Model):


    action = [
    ('قبول', 'قبول'),
    ('تحديث', 'تحديث'),
]
    action_no = models.ForeignKey(Contract_Detail, on_delete=models.CASCADE, related_name='Copy_contract_action')
    action_creator =models.CharField(max_length=250)
    action_creator_name =models.CharField(max_length=250)
    action_date = models.DateTimeField(null=True, blank=True, auto_now=True)
    action = models.CharField(max_length=250, null=False, blank=False, choices=action)
    action_file =  models.FileField(null=False, blank=False, upload_to='files/%Y/%m/%d', validators=[FileExtensionValidator(['pdf'])])


    def __str__(self):
        return str(self.id)
    class Meta:
        verbose_name="Copy_contract_action"

@receiver(post_save, sender=Copy_contract_action)
def creat_Actions_records(sender, instance, created, **kwargs):
    if created:
        Actions_records.objects.create(action_no=instance.action_no, action_creator = instance.action_creator, action_creator_name = instance.action_creator_name, action_date = datetime.now(), action = instance.action, action_file = instance.action_file)
          

        

@receiver(pre_save, sender=Copy_contract_action)
def update_Copy_contract_status(sender, instance, *args, **kwargs):
    if instance.action and instance.action_no_id is not None:
        Contract_Detail = instance.action_no
        Contract_Detail.sgnlcopyContract_action_creator = instance.action_creator
        Contract_Detail.sgnlcopyContract_action_creator_name = instance.action_creator_name
        Contract_Detail.sgnlcopyContract_action_date = datetime.now()
        Contract_Detail.sgnlcopyContract_action = instance.action
        Contract_Detail.sgnlcopyContract_actionFile = instance.action_file
        Contract_Detail.save(update_fields=('sgnlcopyContract_action_creator',))
        Contract_Detail.save(update_fields=('sgnlcopyContract_action_creator_name',))
        Contract_Detail.save(update_fields=('sgnlcopyContract_action_date',))
        Contract_Detail.save(update_fields=('sgnlcopyContract_action',))
        Contract_Detail.save(update_fields=('sgnlcopyContract_actionFile',))

        if instance.action == 'قبول':
            Contract_Detail.sgnllast_status_action = 'مراجعة العقد'

        elif instance.action == 'تحديث':
            Contract_Detail.sgnllast_status_action = 'مراجعة العقد'
        Contract_Detail.save(update_fields=('sgnllast_status_action',))



class Check_contract_action(models.Model):


    action = [
    ('قبول', 'قبول'),
    ('ملاحظات', 'ملاحظات'),
    ('تحديث مدير المناقصات', 'تحديث مدير المناقصات'),
    ('تحديث نائب الرئيس التنفيذي', 'تحديث نائب الرئيس التنفيذي'),
    ('تحديث الرئيس التنفيذي', 'تحديث الرئيس التنفيذي'),
]
    action_no = models.ForeignKey(Contract_Detail, on_delete=models.CASCADE, related_name='Check_contract_action')
    action_creator =models.CharField(max_length=250)
    action_creator_name =models.CharField(max_length=250)
    action_date = models.DateTimeField(null=True, blank=True, auto_now=True)
    action = models.CharField(max_length=250, null=False, blank=False, choices=action)
    action_note = models.CharField(max_length=250, null=True, blank=True)
    action_file =  models.FileField(null=True, blank=True, upload_to='files/%Y/%m/%d')


    def __str__(self):
        return str(self.id)
    class Meta:
        verbose_name="Check_contract_action"

@receiver(post_save, sender=Check_contract_action)
def creat_Actions_records(sender, instance, created, **kwargs):
    if created:
        Actions_records.objects.create(action_no=instance.action_no, action_creator = instance.action_creator, action_creator_name = instance.action_creator_name, action_date = datetime.now(), action = instance.action, action_note = instance.action_note, action_file = instance.action_file)
          

        

@receiver(pre_save, sender=Check_contract_action)
def update_Check_contract_status(sender, instance, *args, **kwargs):
    if instance.action and instance.action_no_id is not None:
        Contract_Detail = instance.action_no
        Contract_Detail.sgnlcheckContract_action_creator = instance.action_creator
        Contract_Detail.sgnlcheckContract_action_creator_name = instance.action_creator_name
        Contract_Detail.sgnlcheckContract_action_date = datetime.now()
        Contract_Detail.sgnlcheckContract_action = instance.action
        Contract_Detail.sgnlcheckContract_action_note = instance.action_note
        Contract_Detail.sgnlcheckContract_actionFile = instance.action_file
        Contract_Detail.save(update_fields=('sgnlcheckContract_action_creator',))
        Contract_Detail.save(update_fields=('sgnlcheckContract_action_creator_name',))
        Contract_Detail.save(update_fields=('sgnlcheckContract_action_date',))
        Contract_Detail.save(update_fields=('sgnlcheckContract_action',))
        Contract_Detail.save(update_fields=('sgnlcheckContract_action_note',))
        Contract_Detail.save(update_fields=('sgnlcheckContract_actionFile',))

        if instance.action == 'قبول':
            Contract_Detail.sgnllast_status_action = 'اعتماد الاجراءات'

        if instance.action == 'ملاحظات':
            Contract_Detail.sgnllast_status_action = 'ناسخ العقد'

        if instance.action == 'تحديث مدير المناقصات':
            Contract_Detail.sgnllast_status_action = 'اعتماد الاجراءات'

        if instance.action == 'تحديث نائب الرئيس التنفيذي':
            Contract_Detail.sgnllast_status_action = 'نائب الرئيس التنفيذي'

        if instance.action == 'تحديث الرئيس التنفيذي':
            Contract_Detail.sgnllast_status_action = 'الرئيس التنفيذي'

        Contract_Detail.save(update_fields=('sgnllast_status_action',))


class TCTA_action(models.Model):


    action = [
    ('قبول', 'قبول'),
    ('ملاحظات', 'ملاحظات'),
    ('رفض', 'رفض'),
]
    action_no = models.ForeignKey(Contract_Detail, on_delete=models.CASCADE, related_name='TCTA_action')
    action_creator =models.CharField(max_length=250)
    action_creator_name =models.CharField(max_length=250)
    action_date = models.DateTimeField(null=True, blank=True, auto_now=True)
    action = models.CharField(max_length=250, null=False, blank=False, choices=action)
    action_note = models.CharField(max_length=250, null=True, blank=True)


    def __str__(self):
        return str(self.id)
    class Meta:
        verbose_name="TCTA_action"

@receiver(post_save, sender=TCTA_action)
def creat_Actions_records(sender, instance, created, **kwargs):
    if created:
        Actions_records.objects.create(action_no=instance.action_no, action_creator = instance.action_creator, action_creator_name = instance.action_creator_name, action_date = datetime.now(), action = instance.action, action_note = instance.action_note)
          

        
@receiver(pre_save, sender=TCTA_action)
def update_TCTA_status(sender, instance, *args, **kwargs):
    if instance.action and instance.action_no_id is not None:
        Contract_Detail = instance.action_no
        Contract_Detail.sgnltcta_action_creator = instance.action_creator
        Contract_Detail.sgnltcta_action_creator_name = instance.action_creator_name
        Contract_Detail.sgnltcta_action_date = datetime.now()
        Contract_Detail.sgnltcta_action = instance.action
        Contract_Detail.sgnltcta_action_note = instance.action_note
        Contract_Detail.save(update_fields=('sgnltcta_action_creator_name',))
        Contract_Detail.save(update_fields=('sgnltcta_action_creator',))
        Contract_Detail.save(update_fields=('sgnltcta_action_date',))
        Contract_Detail.save(update_fields=('sgnltcta_action',))
        Contract_Detail.save(update_fields=('sgnltcta_action_note',))

        
        if instance.action == 'قبول':
            Contract_Detail.sgnllast_status_action = 'نائب الرئيس التنفيذي'

        if instance.action == 'ملاحظات':
            Contract_Detail.sgnllast_status_action = 'مراجعة العقد'

        if instance.action == 'رفض':
            Contract_Detail.sgnllast_status_action = 'رفض'

        Contract_Detail.save(update_fields=('sgnllast_status_action',))



class EVP_action(models.Model):


    action = [
    ('قبول', 'قبول'),
    ('ملاحظات', 'ملاحظات'),
    ('رفض', 'رفض'),
]
    action_no = models.ForeignKey(Contract_Detail, on_delete=models.CASCADE, related_name='EVP_action')
    action_creator =models.CharField(max_length=250)
    action_creator_name =models.CharField(max_length=250)
    action_date = models.DateTimeField(null=True, blank=True, auto_now=True)
    action = models.CharField(max_length=250, null=False, blank=False, choices=action)
    action_note = models.CharField(max_length=250, null=True, blank=True)


    def __str__(self):
        return str(self.id)
    class Meta:
        verbose_name="EVP_action"


@receiver(post_save, sender=EVP_action)
def creat_Actions_records(sender, instance, created, **kwargs):
    if created:
        Actions_records.objects.create(action_no=instance.action_no, action_creator = instance.action_creator, action_creator_name = instance.action_creator_name, action_date = datetime.now(), action = instance.action, action_note = instance.action_note)
          


        

@receiver(pre_save, sender=EVP_action)
def update_EVP_status(sender, instance, *args, **kwargs):
    if instance.action and instance.action_no_id is not None:
        Contract_Detail = instance.action_no
        Contract_Detail.sgnlevp_action_creator = instance.action_creator
        Contract_Detail.sgnlevp_action_creator_name = instance.action_creator_name
        Contract_Detail.sgnlevp_action_date = datetime.now()
        Contract_Detail.sgnlevp_action = instance.action
        Contract_Detail.sgnlevp_action_note = instance.action_note
        Contract_Detail.save(update_fields=('sgnlevp_action_creator',))
        Contract_Detail.save(update_fields=('sgnlevp_action_creator_name',))
        Contract_Detail.save(update_fields=('sgnlevp_action_date',))
        Contract_Detail.save(update_fields=('sgnlevp_action',))
        Contract_Detail.save(update_fields=('sgnlevp_action_note',))

        
        
        if instance.action == 'قبول':
            Contract_Detail.sgnllast_status_action = 'الرئيس التنفيذي'

        if instance.action == 'ملاحظات':
            Contract_Detail.sgnllast_status_action = 'مراجعة العقد'

        if instance.action == 'رفض':
            Contract_Detail.sgnllast_status_action = 'رفض'

        Contract_Detail.save(update_fields=('sgnllast_status_action',))



class CEO_action(models.Model):


    action = [
    ('قبول', 'قبول'),
    ('ملاحظات', 'ملاحظات'),
    ('رفض', 'رفض'),
]
    action_no = models.ForeignKey(Contract_Detail, on_delete=models.CASCADE, related_name='CEO_action')
    action_creator =models.CharField(max_length=250)
    action_creator_name =models.CharField(max_length=250)
    action_date = models.DateTimeField(null=True, blank=True, auto_now=True)
    action = models.CharField(max_length=250, null=False, blank=False, choices=action)
    action_note = models.CharField(max_length=250, null=True, blank=True)


    def __str__(self):
        return str(self.id)
    class Meta:
        verbose_name="CEO_action"


@receiver(post_save, sender=CEO_action)
def creat_Actions_records(sender, instance, created, **kwargs):
    if created:
        Actions_records.objects.create(action_no=instance.action_no, action_creator = instance.action_creator, action_creator_name = instance.action_creator_name, action_date = datetime.now(), action = instance.action, action_note = instance.action_note)
          


        

@receiver(pre_save, sender=CEO_action)
def update_CEO_status(sender, instance, *args, **kwargs):
    if instance.action and instance.action_no_id is not None:
        Contract_Detail = instance.action_no
        Contract_Detail.sgnlceo_action_creator = instance.action_creator
        Contract_Detail.sgnlceo_action_creator_name = instance.action_creator_name
        Contract_Detail.sgnlceo_action_date = datetime.now()
        Contract_Detail.sgnlceo_action = instance.action
        Contract_Detail.sgnlceo_action_note = instance.action_note
        Contract_Detail.save(update_fields=('sgnlceo_action_creator',))
        Contract_Detail.save(update_fields=('sgnlceo_action_creator_name',))
        Contract_Detail.save(update_fields=('sgnlceo_action_date',))
        Contract_Detail.save(update_fields=('sgnlceo_action',))
        Contract_Detail.save(update_fields=('sgnlceo_action_note',))

                
        if instance.action == 'قبول':
            Contract_Detail.sgnllast_status_action = 'توقيعات'

        if instance.action == 'ملاحظات':
            Contract_Detail.sgnllast_status_action = 'مراجعة العقد'

        if instance.action == 'رفض':
            Contract_Detail.sgnllast_status_action = 'رفض'

        Contract_Detail.save(update_fields=('sgnllast_status_action',))



class Assignmnt_action(models.Model):


    action = [
    ('تم', 'تم'),
]
    action_no = models.ForeignKey(Contract_Detail, on_delete=models.CASCADE, related_name='Assignmnt_action')
    action_creator =models.CharField(max_length=250)
    action_creator_name =models.CharField(max_length=250)
    action_date = models.DateTimeField(null=True, blank=True, auto_now=True)
    copy_contract_assign = models.CharField(max_length=250, null=False, blank=False, choices=action)
    financial_assign = models.CharField(max_length=250, null=False, blank=False, choices=action)
    check_contract_assign = models.CharField(max_length=250, null=False, blank=False, choices=action)
    second_party_assign = models.CharField(max_length=250, null=False, blank=False, choices=action)
    first_party_assign = models.CharField(max_length=250, null=False, blank=False, choices=action)
    action_file =  models.FileField(null=False, blank=False, upload_to='files/%Y/%m/%d', validators=[FileExtensionValidator(['pdf'])])



    def __str__(self):
        return str(self.id)
    class Meta:
        verbose_name="Assignmnt_action"


@receiver(post_save, sender=Assignmnt_action)
def creat_Actions_records(sender, instance, created, **kwargs):
    if created:
        Actions_records.objects.create(action_no=instance.action_no, action_creator = instance.action_creator, action_creator_name = instance.action_creator_name, action_date = datetime.now(), action = 'تم', action_file = instance.action_file)
          






@receiver(pre_save, sender=Assignmnt_action)
def update_Assignmnt_status(sender, instance, *args, **kwargs):
    if instance.action and instance.action_no_id is not None:
        Contract_Detail = instance.action_no
        Contract_Detail.sgnlassignmnt_action_creator = instance.action_creator
        Contract_Detail.sgnlassignmnt_action_creator_name = instance.action_creator_name
        Contract_Detail.sgnlassignmnt_action_date = datetime.now()
        Contract_Detail.copy_contract_assign = instance.copy_contract_assign
        Contract_Detail.financial_assign = instance.financial_assign
        Contract_Detail.check_contract_assign = instance.check_contract_assign
        Contract_Detail.first_party_assign = instance.first_party_assign
        Contract_Detail.second_party_assign = instance.second_party_assign
        Contract_Detail.sgnlassignmnt_actionFile = instance.action_file

        Contract_Detail.save(update_fields=('sgnlassignmnt_action_creator',))
        Contract_Detail.save(update_fields=('sgnlassignmnt_action_creator_name',))
        Contract_Detail.save(update_fields=('sgnlassignmnt_action_date',))
        Contract_Detail.save(update_fields=('copy_contract_assign',))
        Contract_Detail.save(update_fields=('financial_assign',))
        Contract_Detail.save(update_fields=('check_contract_assign',))
        Contract_Detail.save(update_fields=('first_party_assign',))
        Contract_Detail.save(update_fields=('second_party_assign',))
        Contract_Detail.save(update_fields=('sgnlassignmnt_actionFile',))


        if instance.copy_contract_assign == 'تم' and instance.financial_assign == 'تم' and instance.check_contract_assign == 'تم' and instance.first_party_assign == 'تم' and instance.second_party_assign == 'تم':

            Contract_Detail.sgnllast_status_action = 'مكتمل'

        Contract_Detail.save(update_fields=('sgnllast_status_action',))




class Contract_template(models.Model):


    template_des =models.CharField(max_length=250, null=True, blank=True)
    template = models.FileField(null=False, blank=False, upload_to='files')



    def __str__(self):
        return str(self.template_des)
    class Meta:
        verbose_name="Contract_template"