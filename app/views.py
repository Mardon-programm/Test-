from django.shortcuts import render, redirect
from .models import Contact
from django.contrib.auth import authenticate, login
from .forms import  RegistrationForm



def home(request):
    contact_info = Contact.objects.first() 
    return render(request, 'index_2.html', {'contact_info': contact_info})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Здесь можно добавить код для отправки подтверждения на email или телефон
            login(request, user)
            return redirect('home')  # Перенаправление на домашнюю страницу после успешной регистрации
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})
