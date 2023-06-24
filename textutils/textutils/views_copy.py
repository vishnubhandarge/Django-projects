from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    # get the text
    djtext = request.GET.get('text', 'default')

    # Check checkbox values
    removepunc = request.GET.get('removepunc', 'Off')
    uppercase = request.GET.get('uppercase', 'Off')
    lowercase = request.GET.get('lowercase', 'Off')
    extraspaceremover = request.GET.get('extraspaceremover', 'Off')
    newlineremover = request.GET.get('newlineremover', 'Off')
    charcount = request.GET.get('charcount', 'Off')
    wordcount = request.GET.get('wordcount', 'Off')

    print(removepunc)
    print(djtext)

    # If checkboxes are on
    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed punctuations', 'analyzed_text': analyzed}
        return render(request, "analyze.html", params)

    elif (uppercase == 'on'):
        analyzed = ''
        analyzed = djtext.upper()
        params = {'purpose': 'After upper the content',
                  'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif (lowercase == 'on'):
        analyzed = ''
        analyzed = djtext.lower()
        params = {'purpose': 'After lower', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif (extraspaceremover == 'on'):
        analyzed = ''
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'After removing extra spaces',
                  'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif (newlineremover == 'on'):
        analyzed = ''
        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char
        params = {'purpose': 'removed new lines', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif (charcount == "on"):
        analyzed = len(djtext)
        params = {'purpose': 'total char are', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif (wordcount == "on"):
        words = djtext.split()
        analyzed = len(words)
        params = {'purpose': 'total words are', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse("Error")
