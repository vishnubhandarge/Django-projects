from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def analyze(request):
    # get the text
    djtext = request.GET.get('text','default')
    removepunc = request.GET.get('removepunc', 'Off')
    fullcaps = request.GET.get('fullcaps', 'Off')
    lowerc = request.GET.get('lowerc', 'Off')
    capitali = request.GET.get('capitali', 'Off')

    print(removepunc)
    print(djtext)
    if removepunc =='on':

    # analyze the text
    # analyzed = djtext
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed punctuations','analyzed_text':analyzed}
        return render (request, "analyze.html", params)
    

    elif (fullcaps == 'on'):
        analyzed = ''
        analyzed = djtext.upper()
        params = {'purpose': 'After upper the content', 'analyzed_text': analyzed}
        return render  (request,'analyze.html', params)

    elif (lowerc == 'on'):
        analyzed = ''
        analyzed = djtext.lower()
        params = {'purpose': 'After lower', 'analyzed_text': analyzed}
        return render  (request,'analyze.html', params)

    elif (capitali == 'on'):
        analyzed = ''
        analyzed = djtext.capitalize()
        params = {'purpose': 'After capitalize', 'analyzed_text': analyzed}
        return render  (request,'analyze.html', params)


    else:
        return HttpResponse("Error")
