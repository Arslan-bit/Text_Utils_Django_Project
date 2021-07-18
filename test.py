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
    removepunc_and_fullcapss =    request.POST.get('removepunc_and_fullcaps', 'off')

    if removepunc =='on':
        # analyzed = dgtext
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analysed = ""
        for char in dgtext:
            if char not in punctuations:
                analysed = analysed + char


        parms = {'purpose': 'Remove Punctuations','analyzed_text':analysed}
        return render(request,'analyze.html',parms)


    elif fullcaps =='on':
        analysed = ""
        for char in dgtext:
            analysed = analysed + str(char.upper())
        # print(analysed)
        # print('-----------------------------------------------')
        parms = {'purpose': 'Change Upper Case', 'analyzed_text': analysed}
        return render(request, 'analyze.html', parms)



    elif removepunc_and_fullcapss =='on':

        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analysed = ""
        for char in dgtext:
            if char not in punctuations:
                analysed = analysed + char


        analysed1 = ""
        for char in analysed:
            analysed1 = analysed1 + str(char.upper())


        parms = {'purpose': 'remove punctuations & Change Upper Case', 'analyzed_text': analysed1}
        return render(request, 'analyze.html', parms)



    else:
        parms = {'purpose': 'Cannot Add value and Select', 'analyzed_text': 'Error!'}
        return render(request, 'error.html', parms)
