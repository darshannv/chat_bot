from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from openai import OpenAI
from django.conf import settings
import openai as openai


OpenAI.api_key = ''

def home(request):
    return render(request, "index.html")


def chatApi(request):
    if request.method == "POST":
        user_message = request.POST.get('user_message', '')

        openai.api_key = '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' 

        response = openai.Completion.create(
            engine="text-davinci-003", 
            prompt=user_message,
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        return JsonResponse(response)
    return JsonResponse({'error': 'Bad request'})