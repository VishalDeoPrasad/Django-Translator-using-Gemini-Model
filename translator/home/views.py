from django.shortcuts import render, HttpResponse
import google.generativeai as genai

key = "AIzaSyALYYJCVyKQ08mwjHG-sOpae5zIGpbuAlw"
genai.configure(api_key=key)    
model = genai.GenerativeModel(model_name='gemini-2.5-flash')

def translator(text, target_lang):
    prompt = "translate the following text into " + target_lang + " '" + text + "'. do not explain anything"
    response = model.generate_content(prompt)
    return response.text

# Create your views here.
def home(request):
    response = ""
    if request.method == "POST":
        text = request.POST.get("user_input")
        language = request.POST.get("language")
        # print(text, language)
        response = translator(text, language)
        print(response)
    return render(request, 'home.html', {'response':response})