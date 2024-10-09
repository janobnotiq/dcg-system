from django.db import models
from core.models import BaseModel

from django.contrib.auth.models import User
from app.models import Company

# Create your models here.

class Contract(BaseModel):
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
    date_recorded = models.DateField(verbose_name="qayd etilgan sana")
    customs_mode = models.CharField(max_length=10,choices=Modes.choices)
    sender = models.CharField(max_length=256)
    reciever = models.ForeignKey(Company,on_delete=models.CASCADE)
    country = models.CharField(max_length=256)
    custom_price = models.DecimalField(max_digits=10,decimal_places=2,null=True, blank=True)
    factor_price = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    quantity = models.IntegerField()
    status = models.CharField(max_length=15,choices=Status.choices)

    def __str__(self) -> str:
        return f"{self.declarant.first_name} {self.declarant.last_name}ning kontrakti"
    
    class Meta:
        ordering = ["-updated_at",]


class Dosmotr(BaseModel):
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
    date_recorded = models.DateField(verbose_name="qayd etilgan sana")
    customs_mode = models.CharField(max_length=10,choices=Modes.choices)
    sender = models.CharField(max_length=256)
    reciever = models.ForeignKey(Company,on_delete=models.CASCADE)
    country = models.CharField(max_length=256)
    custom_price = models.DecimalField(max_digits=10,decimal_places=2,null=True, blank=True)
    factor_price = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    quantity = models.IntegerField()
    status = models.CharField(max_length=15,choices=Status.choices)

    def __str__(self) -> str:
        return f"{self.declarant.first_name} {self.declarant.last_name}ning dosmotri"
    
    class Meta:
        ordering = ["-updated_at",]
