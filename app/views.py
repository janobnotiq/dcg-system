from django.contrib.auth import logout
from django.shortcuts import redirect, render
from .forms import DeclarationForm
from django.contrib.auth.decorators import login_required

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