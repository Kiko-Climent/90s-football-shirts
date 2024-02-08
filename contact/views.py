from django.shortcuts import render, redirect

from .forms import InquiryForm

def contact(request):
    if request.method == 'POST':
        form.InquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your inquiry has been submited')
            # Add logic for sending emails
            return redirect('contact_success')
        else:
            messages.error(request, 'Looks like your submission failed, please check the form')
    else:
        form = InquiryForm()
    
    return render(request, 'contact/contact_form.html', {'form':form})

def contact_success(request):
    messages.success(request, 'Thanks for your inquiry, we will get back to you asap')
    return render(request, 'contact/contact_success.html')


