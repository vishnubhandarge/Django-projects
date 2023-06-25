from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    # get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    # By using POST method you will not see containt going to the server in url
    removepunc = request.POST.get('removepunc', 'Off')
    uppercase = request.POST.get('uppercase', 'Off')
    lowercase = request.POST.get('lowercase', 'Off')
    extraspaceremover = request.POST.get('extraspaceremover', 'Off')
    newlineremover = request.POST.get('newlineremover', 'Off')
    charcount = request.POST.get('charcount', 'Off')
    wordcount = request.POST.get('wordcount', 'Off')

    # If checkboxes are on
    if (removepunc == 'on'):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if (uppercase == 'on'):
        analyzed = ''
        analyzed = djtext.upper()
        params = {'purpose': 'After upper the content',
                  'analyzed_text': analyzed}
        djtext = analyzed

    if (lowercase == 'on'):
        analyzed = ''
        analyzed = djtext.lower()
        params = {'purpose': 'After lower', 'analyzed_text': analyzed}
        djtext = analyzed

    if (extraspaceremover == 'on'):
        analyzed = ''
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'After removing extra spaces',
                  'analyzed_text': analyzed}
        djtext = analyzed

    if (newlineremover == 'on'):
        analyzed = ''
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'removed new lines', 'analyzed_text': analyzed}
        djtext = analyzed

    if (charcount == "on"):
        analyzed = len(djtext)
        params = {'purpose': 'total char are', 'analyzed_text': analyzed}
        djtext = analyzed

    if (wordcount == "on"):
        words = djtext.split()
        analyzed = len(words)
        params = {'purpose': 'total words are', 'analyzed_text': analyzed}
        djtext = analyzed

    # If checkboxes are off
    if (removepunc != 'on' and uppercase != 'on' and lowercase != 'on' and extraspaceremover != 'on' and newlineremover != 'on' and charcount != "on" and wordcount != "on"):
        return HttpResponse("Error")

    return render(request, 'analyze.html', params)
