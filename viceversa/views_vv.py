from django.http import HttpResponse
from django.shortcuts import render

def home_vv(request):
    return render(request, 'home_vv.html')


def reverse(request):
    user_text = request.GET['usertext']
    # print (user_text)
    reversed_text = user_text[::-1]
    if reversed_text.lower() == user_text.lower():
        return render(request, 'reverse.html', {'usertext': user_text, 'reversedtext': reversed_text, 'omonim': 'омоним.'})
    else: 
        return render(request, 'reverse.html', {'usertext': user_text, 'reversedtext': reversed_text, 'omonim': 'простое скучное.'})