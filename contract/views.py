from django.shortcuts import render
from app.models import Company, Declaration
from .models import Dosmotr, Contract


def company_report(request,pk):
    company = Company.objects.filter(id=pk).last()
    declarations = Declaration.objects.filter(reciever=company).all()
    contracts = Contract.objects.filter(reciever=company).all()
    dosmotrs = Dosmotr.objects.filter(reciever=company).all()

    context = {
        "company": company,
        "declarations": declarations.count(),
        "contracts": contracts.count(),
        "dosmotrs": dosmotrs.count(),
    }

    return render(request,"company-report.html",context)