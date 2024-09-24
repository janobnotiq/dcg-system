from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from core.models import BaseModel

# Create your models here.
class Company(BaseModel):
    name = models.CharField(max_length=256,unique=True)
    phone = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
    
    # har bir kompaniyaning oylik deklaratsiyalari sonini hisoblash
    def declaration_count(self,month=None):
        if month is None:
            month = datetime.now().month
        
        # Tanlangan oydagi deklaratsiyalarni sanash (updated_at bo'yicha filtrlash)
        return Declaration.objects.filter(
            reciever=self,               # `self` - bu kompaniya
            status=Declaration.Status.FINISHED,
            updated_at__month=month,      # `updated_at` bo'yicha oy filtr
            updated_at__year=datetime.today().year,
        ).count()

    class Meta:
        verbose_name_plural = "Companies"


class Declaration(BaseModel):
    class Status(models.TextChoices):
        FINISHED = "FINISHED", "Finished"
        IN_PROCESS = "IN_PROCESS", "In process"

    
    class Modes(models.TextChoices):
        IM70 = "IM70", "IM 70"
        IM40 = "IM40", "IM 40"
        ND40 = "ND40", "ND 40"

    declarant = models.ForeignKey(User,on_delete=models.CASCADE)
    number_gtd = models.CharField(max_length=256,verbose_name="nomer gtd")
    reference_gtd = models.CharField(max_length=256)
    date_recorded = models.CharField(max_length=256)
    customs_mode = models.CharField(max_length=10,choices=Modes.choices)
    sender = models.CharField(max_length=256)
    reciever = models.ForeignKey(Company,on_delete=models.CASCADE)
    country = models.CharField(max_length=256)
    custom_price = models.DecimalField(max_digits=10,decimal_places=2,null=True, blank=True)
    factor_price = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    quantity = models.IntegerField()
    status = models.CharField(max_length=15,choices=Status.choices)

    def __str__(self) -> str:
        return f"{self.declarant.first_name} {self.declarant.last_name}ning deklaratsiyasi"
    
    class Meta:
        ordering = ["-updated_at",]



# Har bir xodimning tanlangan oydagi deklaratsiyalar sonini hisoblaydigan metod
def declaration_count(self, month=None):
    # Hozirgi oyni olish (agar hech narsa berilmagan bo'lsa)
    if month is None:
        month = datetime.now().month
    
    # Tanlangan oydagi deklaratsiyalarni sanash (updated_at bo'yicha filtrlash)
    return Declaration.objects.filter(
        declarant=self,               # `self` - bu xodim (user)
        status=Declaration.Status.FINISHED,
        updated_at__month=month,      # `updated_at` bo'yicha oy filtr
        updated_at__year=datetime.today().year,
    ).count()

# Methodni User modeliga qo'shamiz
User.add_to_class("declaration_count", declaration_count)
