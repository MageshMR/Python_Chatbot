from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import render
from rest_framework import status


def get_bot_response(user_input):
    if user_input is None:
        return "Please provide a message."

    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "your name" in user_input:
        return "I'm a chatbot"
    elif "what are the top product in salon" in user_input:
        return "shampoo ,sunscreen,facewash,hair color"
    elif "help" in user_input:
        return "Sure, I'm here to help. What do you need assistance with?"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    elif "what are services is there" in user_input:
        return "hair care,skin car,nail care,Massage"
    elif "what is your purpose" in user_input:
        return "I'm here to answer your questions and help you learn!"
    elif "what can you do" in user_input:
        return "I can respond to simple questions, guide you about Django and Python, and simulate a chatbot conversation."
    else:
        return "I'm not sure I understand. Could you please rephrase?"

@csrf_exempt
def chat_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_input = data.get('message', None)

            bot_response = get_bot_response(user_input)
            return JsonResponse({'reply': bot_response})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

    from django.shortcuts import render

def chat_page(request):
    return render(request, 'chat.html')

