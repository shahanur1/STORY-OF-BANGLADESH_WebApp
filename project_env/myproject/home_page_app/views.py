from django.shortcuts import render

# Create your views here.

def homePage(request):
    return render(request, 'home_page_app/home_page.html')
