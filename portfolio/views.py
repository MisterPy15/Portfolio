from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail



# Create your views here.
def home(request):
    
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid:
            form.save()
            try:
                subject = f'Nouveau Message de contact Portfolio'
                message = f"Nom :  {form.cleaned_data['name']}\nEmail: {form.cleaned_data['email']}\nMessage: {form.cleaned_data['message']}"
                from_email = "agohchris90@gmail.com"
                recipient_list = ["agihchris90@gmail.com"]                
                send_mail(subject, message, from_email, recipient_list)
                messages.success(request,'Votre méssage à été envoyé ✅')
            except:
                messages.error(request, 'Érreur lors de l\'envoie du méssagge')
            return redirect('home')
        else:
            messages.error(request,'Érreur dans le formulaire')
                
                   
    else:
        form = ContactForm()
    
    
    return render(request, 'index.html', {'form' : form})