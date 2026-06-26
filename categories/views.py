from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import MainCategory, SubCategory

@login_required
def category_list(request):
    main_categories = MainCategory.objects.filter(user=request.user).prefetch_related('subcategory_set')
    return render(request, 'category_list.html', {
        'main_categories': main_categories
    })

@login_required
def add_category(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        category_type = request.POST.get('category_type')
        main_category_id = request.POST.get('main_category')

        if category_type == 'main':
            MainCategory.objects.create(name=name, user=request.user)
        elif category_type == 'sub' and main_category_id:
            main = get_object_or_404(MainCategory, id=main_category_id, user=request.user)
            SubCategory.objects.create(name=name, main_category=main, user=request.user)

        return redirect('category_list')

    main_categories = MainCategory.objects.filter(user=request.user)
    return render(request, 'add_category.html', {
        'main_categories': main_categories
    })

@login_required
def delete_category(request, category_type, category_id):
    if category_type == 'main':
        category = get_object_or_404(MainCategory, id=category_id, user=request.user)
    else:
        category = get_object_or_404(SubCategory, id=category_id, user=request.user)

    if request.method == 'POST':
        category.delete()
        return redirect('category_list')

    return render(request, 'confirm_delete.html', {
        'category': category
    })