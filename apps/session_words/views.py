from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

def index(request):
    return render(request, 'session_words/index.html')

def add_words(request):
    if request.method == "POST":
        print request.POST
        date = strftime("%I:%M %p, %B %d, %Y", gmtime())
        word_dict = {
            "word" : request.POST['word'],
            "color" : request.POST['color'],
            "big" : request.POST['big'],
            "time" : str(date)
        }
        if not 'wordList' in request.session:
            request.session['wordList'] = []
        message_log = request.session['wordList']
        message_log.append(word_dict)
        request.session['wordList'] = message_log
        return redirect('/')
    else:
        return redirect('/')

def clear(request):
    request.session.clear()
    return redirect('/')