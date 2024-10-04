from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail



# Create your views here.
def home(request):
    
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid:
            form.save()
            
            subject = 'Nouveau Message de contact'
            message = f"Nom :  {form.cleaned_data['name']}\nEmail: {form.cleaned_data['email']}\nMessage: {form.cleaned_data['message']}"
            from_email = "agohchris90@gmail.com"
            recipient_list = ["agohchris90@gmail.com"]
            
            send_mail(subject, message, from_email, recipient_list)
            
            
            
            return redirect('home')
    else:
        form = ContactForm()
    
    
    return render(request, 'index.html', {'form' : form})