from django.http import HttpResponse
from  django.shortcuts import render

# Code for video ===========================6
# def index(request):
#     return HttpResponse( 'Hello')
#
# def about(request):
#     return HttpResponse( 'about')
#
# def ex1(request):
#     sites = ['''<h1>For Entertainment </h1><a href = "https://www.youtube.com" >youtube video</a>''',
#              '''<h1>For Interaction </h1><a href = "https://www.facebook.com" >Facebook</a>''',
#              '''<h1>For Insight   </h1><a href = "https://www.ted.com/talks" >Ted Talk</a>''',
#              '''<h1>For Internship   </h1><a href="https://internshala.com" >Intenship</a>''',
#              ]
#     return HttpResponse((sites))

# Code for video -----------------------------------7

# def index(request):
#     cool = {'name': 'Arslan','city': 'Lahore'}
#     return render(request,'index.html',cool)
#     # return HttpResponse("Home")
#
# def removepunc(request):
#     return HttpResponse("remove punc")
#
# def capfirst(request):
#     return HttpResponse("capitalize first")
#
# def newlineremove(request):
#     return HttpResponse("capitalize first")
#
#
# def spaceremove(request):
#     return HttpResponse("space remover")
#
# def charcount(request):
#     return HttpResponse("charcount ")
#
# Code------------------------------ for video 8

# def index(request):
#     cool = {'name': 'Arslan','city': 'Lahore'}
#     return render(request,'index.html',cool)
#     # return HttpResponse("Home")
#
# def removepunc(request):
#     dgtext = request.GET.get('text', 'default')
#     return HttpResponse("remove punc")
#
# def capfirst(request):
#     return HttpResponse("capitalize first")
#
# def newlineremove(request):
#     return HttpResponse("capitalize first")
#
#
# def spaceremove(request):
#     return HttpResponse("space remover")
#
# def charcount(request):
#     return HttpResponse("charcount ")

# Code------------------------------ for video 9

def index(request):
    cool = {'name': 'Arslan','city': 'Lahore'}
    return render(request,'index.html',cool)
    # return HttpResponse("Home")


# ----------------------------


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
        # print(analysed)
        # print('-----------------------------------------------')
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
