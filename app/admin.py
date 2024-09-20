from django.contrib import admin
from .models import Company, Declaration
from unfold.admin import ModelAdmin


@admin.register(Company)
class CompanyAdmin(ModelAdmin):
    ordering = ["-created_at",]


@admin.register(Declaration)
class DeclarationAdmin(ModelAdmin):
    ordering = ["-created_at",]