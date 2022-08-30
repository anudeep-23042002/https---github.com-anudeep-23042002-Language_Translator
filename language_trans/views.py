from django.shortcuts import render
from googletrans import Translator
# Create your views here.
translated_text="type something to Translate"
def home(request):
    return render(request,'home.html',{'translated_text' : translated_text})
def translate(request):
    if(request.method=='POST'):
        text=request.POST["text"]
        option=request.POST["option"]
        translator=Translator();
        translated=translator.translate(text,dest=option);
        translated_text=translated.text;
        if(translated_text==''):
            translated_text="type something to translate"
    return render(request,'home.html',{'translated_text' : translated_text})