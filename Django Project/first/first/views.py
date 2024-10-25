from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "textu.html")

def spaceremover(request):
    return HttpResponse("spaceremover")

def capitalize(request):
    return HttpResponse("capitalize")

def removepunct(request):
    inputtext = request.GET.get('text', 'default')
    removepunct = request.GET.get('removepunct', 'off')
    capitalize = request.GET.get('capitalize', 'off')
    spaceremover=request.GET.get('spaceremover', 'off')
    if removepunct == "on":
        punctuations = '''!@$%^&*'==''''()_+-+{}[];:">#<,.?/'''
        analyzed = ""
        for char in inputtext:
            if char not in punctuations:
                analyzed = analyzed + char
        user_text = {'Task': 'Remove Punctuation', 'analyzed_text': analyzed}
        return render(request, 'analyse.html', user_text)

    elif capitalize == "on":
        analyzed = ""
        for char in inputtext:
            analyzed = analyzed + char.upper()
        user_text = {'Task': 'Capitalized Text', 'analyzed_text': analyzed}
        return render(request, 'analyse.html', user_text)
    elif spaceremover == "on":
        analyzed=inputtext
        analyzed = inputtext.replace(" ", "")
        user_text = {'Task': 'Space Remover', 'analyzed_text': analyzed}
        return render(request, 'analyse.html', user_text)
    
    if removepunct != "on" and capitalize != "on" and spaceremover != "on":
        return HttpResponse("<center>Please select one of the options to analyze your text.</center>")

def about(request):
    return HttpResponse("<h1>Hi Guys</h1>")

def home(request):
    return HttpResponse("Welcome to the channel")

