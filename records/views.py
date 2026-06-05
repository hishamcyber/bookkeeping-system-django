from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Record
from .forms import RecordForm

@login_required
def records_list(request):
    records = Record.objects.filter(user=request.user)
    return render(request, 'records.html', {'records': records})


@login_required
def add_record(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.user = request.user
            record.save()
            return redirect('dashboard')
    else:
        form = RecordForm()

    return render(request, 'add_record.html', {'form': form})