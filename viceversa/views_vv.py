from django.http import HttpResponse
from django.shortcuts import render

def home_vv(request):
    return render(request, 'home_vv.html')


def reverse(request):
    user_text = request.GET['usertext']
    # print (user_text)
    word_counter = len(user_text.split())  # Разделяет по пробелам по умолчанию (.split()) и записывает в list, считает количество элементов list.
    reversed_text = user_text[::-1]

    return render(request, 'reverse.html', {'usertext': user_text, 'reversedtext': reversed_text, 'wordcounter': word_counter}) 


    # if reversed_text.lower() == user_text.lower():
    #     return render(request, 'reverse.html', {'usertext': user_text, 'reversedtext': reversed_text, 'omonim': 'омоним.'})
    # else: 
    #     return render(request, 'reverse.html', {'usertext': user_text, 'reversedtext': reversed_text, 'omonim': 'простое скучное.'})