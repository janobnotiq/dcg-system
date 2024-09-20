from django.contrib.auth import logout
from django.shortcuts import redirect, render
from .forms import DeclarationForm, CompanyForm
from django.contrib.auth.decorators import login_required
from .models import Declaration

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
    declarations = Declaration.objects.filter(declarant=request.user)
    return render(request,"my_declarations.html",{"declarations":declarations})