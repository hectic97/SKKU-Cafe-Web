from django.shortcuts import render, redirect

from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'안녕하세요 {username}님')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'User/register.html', {'form': form})
