from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"index.html")

def analyse(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc',"off")
    fullcaps = request.POST.get('fullcaps', "off")
    newlineremover = request.POST.get('newlineremover', "off")
    if removepunc =="on":
        punctuations ='''!@#$%^&*(){}[]<>?/"':;.\/_~'''
        analysed=" "
        for char in djtext:
            if char not in punctuations:
                analysed=analysed+char
        params = {'purpose':'Removed Punctuations', 'analyzed_text':analysed}
        djtext = analysed
        #return render(request,'analyse.html',params)

    if (fullcaps=="on"):
        analysed = ""
        for char in djtext:
            analysed = analysed + char.upper()
        params = {'purpose': 'Changed to uppercase', 'analyzed_text': analysed}
        djtext = analysed
        #return render(request, 'analyse.html', params)

    if (newlineremover == "on"):
        analysed = ""
        for char in djtext:
            if (char!="\n"):
                analysed = analysed + char
        params = {'purpose': 'Changed to uppercase', 'analyzed_text': analysed}
        djtext=analysed

    if(newlineremover != "on" and fullcaps!="on" and removepunc!="on"):
        return HttpResponse("Please select ay operation and try again")
    return render(request, 'analyse.html', params)
