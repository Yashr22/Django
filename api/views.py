from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from api.models import SignupData,Note,Chat
from django.contrib import messages
from .form import NoteForm,ContactForm
from django.http import JsonResponse
import json
import openai
from django.utils import timezone

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        # Check if passwords match
        if password != confirm_password:
            # Handle password mismatch
            pass

        # Create a new SignupData instance and save it
        signup_data = SignupData(username=username, email=email, password=password,confirm_password=confirm_password)
        signup_data.save()

        # Redirect to home page or wherever appropriate
        return redirect('home')

    return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Check if username and password match a SignupData instance
        try:
            user = SignupData.objects.get(username=username, password=password)
            # Redirect to home page or wherever appropriate
            return redirect('home')
        except SignupData.DoesNotExist:
            # Handle invalid login
            messages.error(request, 'Incorrect username or password.')

    return render(request, 'login.html')

def homepage(request):
    return render(request, 'index.html')

def aboutpage(request):
    return render(request, 'about.html')

def servicepage(request):
    return render(request, 'service.html')

def contactpage(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('success')/
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
    # return render(request, 'contact.html')

def accountpage(request):
    return render(request, 'account.html')

def note_list(request):
    notes = Note.objects.all()
    return render(request, 'notes/note_list.html', {'notes': notes})

def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'notes/note_form.html', {'form': form})

def delete_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    if request.method == 'POST':
        note.delete()
        return redirect('note_list')
    return render(request, 'notes/delete_note.html', {'note': note})

def update_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/update_note.html', {'form': form})


openai_api_key = 'input-your-key'
openai.api_key = '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'

def ask_openai(message):
    response = openai.ChatCompletion.create(
        model = "gpt-4",
        messages=[
            {"role": "system", "content": "You are an helpful assistant."},
            {"role": "user", "content": message},
        ]
    )
    
    answer = response.choices[0].message.content.strip()
    return answer

# Create your views here.
def chatbot(request):


    return render(request, 'chatbot/chatbot.html')