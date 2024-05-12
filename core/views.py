from decouple import config  # type: ignore

from django.core.mail import send_mail
from django.shortcuts import render
from django.template.loader import render_to_string

from .forms import ContactForm


def home(request):
    form = ContactForm()
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

    return render(request, 'core/home.html', {'form': form})
