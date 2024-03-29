from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # content = '''
    # <h1>Welcome to my first Django Project!</h1>
    # <a href='/polls'>Click on my polls app</a>
    # '''
    return render(request, 'home.html')
    # return HttpResponse(content)
