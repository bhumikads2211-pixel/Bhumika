from django.shortcuts import render

def Webpg(request):
    return render(request, 'webpg.html')
def Login(request):
    return render(request, 'login.html')
def Course(request):
    return render(request, 'courses.html')
def Certificate(request):
    return render(request, 'certificates.html')
def Questions(request):
    return render(request, 'questions.html')