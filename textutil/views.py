# file created by - praveen


from django.http import HttpResponse
from django.shortcuts import render
# practice -1
# def index(request):
#     # we can use html also
#     return HttpResponse('''''''<h1>hello</h1>  <a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7">click me i m link</a> ''')
#
# def about(request):
#     return HttpResponse("hello praveen bhai")


  # practice 2

def index(request):
    return render(request,'index.html')
    # return HttpResponse("Home")

def analyze (request):
    #get the text
    djtext = request.POST.get('text','default')

    # check box values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    charcount = request.POST.get('charcount', 'off')



    if removepunc == "on":

        analyzed = ""
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^`{|}~'''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose':'Removed punctuations','analyzed_text':analyzed}
        djtext = analyzed

    if (fullcaps == 'on'):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Change To Upper case', 'analyzed_text': analyzed}
        djtext = analyzed


    if(newlineremover=='on'):

        analyzed = ""
        for char in djtext:
            if ((char != '\n') and (char != '\r')):
                analyzed = analyzed + char
        params = {'purpose': 'New Line Remover', 'analyzed_text': analyzed}
        djtext = analyzed



    if(extraspaceremover == 'on'):

        analyzed = ""
        for index, char in enumerate(djtext):
            if not((djtext[index]==" ") and (djtext[index + 1]==" ")):
                analyzed = analyzed + char
        params = {'purpose': 'Extra Space Remover', 'analyzed_text': analyzed}
        djtext = analyzed

    if(charcount == 'on'):
        analyzed = int(djtext.count(''))-1
        analyzed = 'Character count is   '+ str(analyzed)
        params = {'purpose': 'Character count is ..', 'analyzed_text':analyzed}
        djtext = analyzed

    if(removepunc != 'on' and fullcaps != 'on' and newlineremover != 'on' and extraspaceremover != 'on' and charcount != 'on') :
       return HttpResponse('Please Select Relevent OptionS')

    return render(request, 'analyze.html', params)
