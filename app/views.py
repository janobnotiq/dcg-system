from datetime import datetime
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
from django.views import View

from .forms import DeclarationForm, CompanyForm
from .models import Declaration, Company

# bosh sahifa uchun view
@login_required
def home_view(request):
    user = request.user
    cont = {
        "user":user,
    }
    return render(request,"index.html",context=cont)

# tizimdan chiqish
def logout_view(request):
    logout(request)
    return redirect("login")

# dekalaratsiya qo'shish
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

# deklaratsiya muvaffaqiyatli qo'shildi sahifasi uchun
@login_required
def declaration_success_view(request):
    return render(request,"declaration-success.html")

# kompaniya qo'shish
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

# xodimning bugungi qilgan deklaratsiyalari
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

# jarayondagi deklaratsiyalar
@login_required
def in_process_declarations(request):
    declarations = Declaration.objects.filter(declarant=request.user,status=Declaration.Status.IN_PROCESS)
    return render(request,"in-process-declarations.html",{"declarations":declarations})

# xodimlar ro'yhati
@login_required
def employees_list(request):
    if request.user.is_superuser:
        employees = User.objects.filter(is_staff=False)
        return render(request,"employees.html",{"employees":employees})
    else:
        employees = User.objects.filter(id=request.user.pk)
        return render(request,"employees.html",{"employees":employees})

# kompaniyalar ro'yhati
@login_required
def companies_list(request):
    companies = Company.objects.all()
    return render(request,"companies.html",{"companies":companies})

# deklaratsiyaning statusini yangilash
class DeclarationUpdateView(LoginRequiredMixin,UpdateView):
    model = Declaration
    form_class = DeclarationForm
    template_name = "update-declaration.html"
    success_url = reverse_lazy("my-declarations")

    def get_queryset(self):
        return Declaration.objects.filter(declarant=self.request.user)
    


class DeclarationReportView(View):
    def get(self, request, declarant_id):
        # Foydalanuvchi ID'si bilan deklaratsiyalarni olish
        declarant = User.objects.filter(id=declarant_id).last()
        declarations = Declaration.objects.filter(declarant=declarant,status=Declaration.Status.FINISHED)
        from datetime import datetime

        for declaration in declarations:
            if isinstance(declaration.updated_at, str):
                declaration.updated_at = datetime.fromisoformat(declaration.updated_at)
            else:
                declaration.updated_at = declaration.updated_at  # Agar bu allaqachon datetime bo'lsa

        return render(request, 'declarant-report.html', {
            'declarations': declarations,
            'count': declarations.count(),
            'declarant': declarant,
        })

class DeclarationFilterView(View):
    def post(self, request, username):
        declarant = User.objects.filter(username=username).last()
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        if isinstance(start_date, str):
            start_date = datetime.fromisoformat(start_date)

        if isinstance(end_date, str):
            end_date = datetime.fromisoformat(end_date)

        # Foydalanuvchi ID'si bilan sanalar oralig'idagi deklaratsiyalarni olish
        declarations = Declaration.objects.filter(
            declarant=declarant,
            updated_at__gte=start_date,
            updated_at__lte=end_date,
            status=Declaration.Status.FINISHED,
        )

        return render(request, 'declarant-report-filter.html', {
            'declarations': declarations,
            'count': declarations.count(),
            'declarant': declarant,
            "start_date": start_date.date(),
            "end_date": end_date.date(),
        })
