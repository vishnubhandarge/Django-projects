from django.http import HttpResponse

def code(request):
    return HttpResponse('''<a href="https://www.codewithharry.com/">code_with_harry<a> <br>''' 
        '''<a href="https://learningmonkey.in/"> Learning monkey/a> <br>'''
        '''<a href="https:https://www.w3schools.com/"> w3schools</a> <br>'''
        '''<a href="https://openai.com/blog/chatgpt"> Chatgpt</a> <br>'''
        '''<a href="https://www.youtube.com/"> YouTube</a>''')