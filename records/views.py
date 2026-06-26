from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Record
from .forms import RecordForm
from categories.models import SubCategory

@login_required
def records_list(request):
    records = Record.objects.filter(user=request.user)
    return render(request, 'records.html', {'records': records})

@login_required
def add_record(request):
    if request.method == 'POST':
        form = RecordForm(request.user, request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.user = request.user
            record.save()
            return redirect('records')
    else:
        form = RecordForm(user=request.user)
        print("Logged in user:", request.user)
        print("Main categories:", list(form.fields['main_category'].queryset))

    return render(request, 'add_record.html', {'form': form})

@login_required
def get_subcategories(request):
    main_id = request.GET.get('main_id')
    subs = SubCategory.objects.filter(main_category_id=main_id, user=request.user)
    data = [{'id': s.id, 'name': s.name} for s in subs]
    return JsonResponse({'subcategories': data})