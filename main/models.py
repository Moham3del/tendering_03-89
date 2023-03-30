


from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.


class User_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.IntegerField(null=True, blank=True)
    full_name = models.CharField(max_length=50, null=True, blank=True)
    project_number = models.CharField(max_length=15, null=True, blank=True)
    project_name = models.CharField(max_length=50, null=True, blank=True)
    sector_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.project_name)
    class Meta:
        verbose_name="profile"
        ordering = ['project_name']

@receiver(post_save, sender=User)
def creat_level(sender, instance, created, **kwargs):
    if created:
        User_Profile.objects.create(user=instance)


class User_ContractPermission(models.Model):

    choice = [
        ('Yes', 'Yes'),
        ('NO', 'No'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contract_app = models.CharField(max_length=250, choices=choice, null=True, blank=True)
    add_new_contract = models.CharField(max_length=250, choices=choice, null=True, blank=True)
    Sector_manager_action_2 = models.CharField(max_length=250, choices=choice, null=True, blank=True)
    Check_data_action_3 = models.CharField(max_length=250, choices=choice, null=True, blank=True)
    Cost_estimation_action_4 = models.CharField(max_length=250, choices=choice, null=True, blank=True)
    Financial_action_5 = models.CharField(max_length=250, choices=choice, null=True, blank=True)
    Copy_contract_action_6 = models.CharField(max_length=250, choices=choice, null=True, blank=True)
    Check_contract_action_7 = models.CharField(max_length=250, choices=choice, null=True, blank=True)
    TCTA_action_8 = models.CharField(max_length=250, choices=choice, null=True, blank=True)
    EVP_action_9 = models.CharField(max_length=250, choices=choice, null=True, blank=True)
    CEO_action_10 = models.CharField(max_length=250, choices=choice, null=True, blank=True)
    AssignAttach2_action_11 = models.CharField(max_length=250, choices=choice, null=True, blank=True)
    AssignAttach1_action_12 = models.CharField(max_length=250, choices=choice, null=True, blank=True)
    project_index = models.CharField(max_length=250, choices=choice, null=True, blank=True)
    sector_index = models.CharField(max_length=250, choices=choice, null=True, blank=True)
    main_index = models.CharField(max_length=250, choices=choice, null=True, blank=True)

    def __str__(self):
        return str(self.user)
    class Meta:
        verbose_name="User_ContractPermission"


@receiver(post_save, sender=User)
def creat_ContractPermission(sender, instance, created, **kwargs):
    if created:
        User_ContractPermission.objects.create(user=instance)


class User_TenderPermission(models.Model):

    choice = [
        ('Yes', 'Yes'),
        ('NO', 'No'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tender_app = models.CharField(max_length=250, choices=choice, null=True, blank=True)
    add_new_tender = models.CharField(max_length=250, choices=choice, null=True, blank=True)
    update_tender_detail = models.CharField(max_length=250, choices=choice, null=True, blank=True)
    tender_detail = models.CharField(max_length=250, choices=choice, null=True, blank=True)
    tender_report = models.CharField(max_length=250, choices=choice, null=True, blank=True)

    def __str__(self):
        return str(self.user)
    class Meta:
        verbose_name="User_TenderPermission"


@receiver(post_save, sender=User)
def creat_TenderPermission(sender, instance, created, **kwargs):
    if created:
        User_TenderPermission.objects.create(user=instance)


class User_ProjectPermission(models.Model):

    choice = [
        ('Yes', 'Yes'),
        ('NO', 'No'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    project_app = models.CharField(max_length=250, choices=choice, null=True, blank=True)
    add_new_project = models.CharField(max_length=250, choices=choice, null=True, blank=True)
    update_project_detail = models.CharField(max_length=250, choices=choice, null=True, blank=True)
    project_detail = models.CharField(max_length=250, choices=choice, null=True, blank=True)
    project_report = models.CharField(max_length=250, choices=choice, null=True, blank=True)

    def __str__(self):
        return str(self.user)
    class Meta:
        verbose_name="User_ProjectPermission"


@receiver(post_save, sender=User)
def creat_ProjectPermission(sender, instance, created, **kwargs):
    if created:
        User_ProjectPermission.objects.create(user=instance)