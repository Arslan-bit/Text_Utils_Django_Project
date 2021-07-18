from django.http import HttpResponse
from  django.shortcuts import render

def index(request):
    cool = {'name': 'Arslan','city': 'Lahore'}
    return render(request,'index.html',cool)
    # return HttpResponse("Home")



def analyze(request):
    dgtext = request.POST.get('text', 'default')
    removepunc =    request.POST.get('removepunc', 'off')
    fullcaps =    request.POST.get('fullcaps', 'off')
    extraspaceremover =    request.POST.get('extraspaceremover', 'off')
    newlineremover =    request.POST.get('newlineremover', 'off')

    if removepunc =='on':

        x = 'true'
        # analyzed = dgtext
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analysed = ""
        for char in dgtext:
            if char not in punctuations:
                analysed = analysed + char


        parms = {'purpose': 'Remove Punctuations','analyzed_text':analysed}
        dgtext = analysed


    if fullcaps =='on':

        x = 'true'
        analysed = ""
        for char in dgtext:
            analysed = analysed + str(char.upper())

        parms = {'purpose': 'Change Upper Case', 'analyzed_text': analysed}
        dgtext = analysed


    if extraspaceremover =='on':

        x = 'true'
        analyzed = ""
        for index, char in enumerate(dgtext):
            if not (dgtext[index] == " " and dgtext[index + 1] == " "):
                analyzed = analyzed + char

        parms = {'purpose': 'Extra Space Remover', 'analyzed_text': analyzed}
        djtext = analyzed


    if (newlineremover == "on"):
        x = 'true'

        analyzed = ""
        for char in dgtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
            else:
                print("no")
        parms = {'purpose': 'New Line Remover', 'analyzed_text': analyzed}



    if(extraspaceremover !='on' and fullcaps !='on' and removepunc !='on' and newlineremover !='on'):
        parms = {'purpose': 'Cannot Add value and Select', 'analyzed_text': 'Error!'}

        x = 'falls'

    if x == 'true':
        return render(request, 'analyze.html', parms)
    else:

        return render(request, 'error.html', parms)
