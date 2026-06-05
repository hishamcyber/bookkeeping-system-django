
# Create your views here.
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from records.models import Record
from django.db.models import Sum

def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('dashboard')

    return render(request, 'login.html')

@login_required
def dashboard(request):
    records = Record.objects.filter(user=request.user)

    income = records.filter(transaction_type='income').aggregate(
        total=Sum('amount')
    )['total'] or 0

    expense = records.filter(transaction_type='expense').aggregate(
        total=Sum('amount')
    )['total'] or 0

    balance = income - expense

    return render(request, 'dashboard.html', {
        'income': income,
        'expense': expense,
        'balance': balance,
        'records': records[:5]
    })


def user_logout(request):
    logout(request)
    return redirect('login')
