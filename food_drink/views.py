from django.shortcuts import render

def food(request):
    return render(request, 'food_menu.html')

def drink(request):
    return render(request, 'drink_menu.html')