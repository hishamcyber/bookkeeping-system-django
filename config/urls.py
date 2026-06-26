from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect, render

def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return redirect('login')

def custom_404(request, exception):
    return render(request, '404.html', status=404)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('', include('accounts.urls')),
    path('records/', include('records.urls')),
    path('categories/', include('categories.urls')),
    path('reports/', include('reports.urls')),
    path('categories/', include('categories.urls')),
]

handler404 = custom_404