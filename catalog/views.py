from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def home(request):
    return render(request, 'catalog/home.html')

def contacts(request):
    if request.method == 'POST':
        # Обработка данных формы
        return render(request, 'catalog/contacts.html', {'success': True})
    return render(request, 'catalog/contacts.html')