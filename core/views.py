from decouple import config  # type: ignore

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from project.models import Project

from .forms import ContactForm


def home(request):
    form = ContactForm()
    projects = Project.objects.filter(is_featured=True)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')

            html = render_to_string('core/emails/contactform.html', {
                'name': name,
                'email': email,
                'message': message,
            })
            send_mail(
                'Portfolio - Messaged Received!', 'this is the message',
                'noreply@rizalargadas.com', ['rmlargadas@gmail.com'], html_message=html, fail_silently=False
            )
            return render(request, 'core/contact_success.html')

        return render(request, 'core/contact_success.html')

    return render(request, 'core/home.html', {'form': form, 'projects': projects})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "You are successfully logged in.")
                return redirect('home')

        messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'core/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')
