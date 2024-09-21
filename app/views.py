from django.utils import timezone
from datetime import date


from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from .forms import DeclarationForm, CompanyForm
from django.contrib.auth.decorators import login_required
from .models import Declaration, Company

@login_required
def home_view(request):
    user = request.user
    cont = {
        "user":user,
    }
    return render(request,"index.html",context=cont)


def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def add_declaration(request):
    if request.method == 'POST':
        form = DeclarationForm(request.POST)
        if form.is_valid():
            declaration = form.save(commit=False)  # Hozircha saqlamaymiz
            declaration.declarant = request.user   # Deklarantni user bilan bog'laymiz
            declaration.save()  # Endi ma'lumotni saqlaymiz
            return redirect('declaration-success')  # Muvaffaqiyatli deklaratsiya uchun yo'naltirish
    else:
        form = DeclarationForm()
    
    return render(request, 'add-declaration.html', {'form': form})


@login_required
def declaration_success_view(request):
    return render(request,"declaration-success.html")


@login_required
def add_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            company = form.save()
            print(company.name)
            return redirect('home')  # Muvaffaqiyatli deklaratsiya uchun yo'naltirish
    else:
        form = CompanyForm()
    
    return render(request, 'add-company.html', {'form': form})


@login_required
def declaration_list_view(request):
    today = timezone.now().date()
    declarations = Declaration.objects.filter(
        declarant=request.user,
        updated_at__date=today
        )
    for i in declarations:
        print(i.updated_at)
    return render(request,"my_declarations.html",{"declarations":declarations})


@login_required
def in_process_declarations(request):
    declarations = Declaration.objects.filter(declarant=request.user,status=Declaration.Status.IN_PROCESS)
    return render(request,"in-process-declarations.html",{"declarations":declarations})


@login_required
def employees_list(request):
    if request.user.is_superuser:
        employees = User.objects.filter(is_staff=False)
        return render(request,"employees.html",{"employees":employees})
    else:
        employees = User.objects.filter(id=request.user.pk)
        return render(request,"employees.html",{"employees":employees})


@login_required
def companies_list(request):
    companies = Company.objects.all()
    return render(request,"companies.html",{"companies":companies})