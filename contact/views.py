from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

from .forms import InquiryForm

def contact(request):
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            inquiry = form.save()

            """ Send confirmation emails for the users """
            subject = render_to_string(
                'contact/inquiry_emails/inquiry_confirmation_subject.txt', {'inquiry': inquiry}).strip()
            message = render_to_string(
                'contact/inquiry_emails/inquiry_confirmation_body.txt', {'inquiry': inquiry})
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = inquiry.email
            send_mail(subject, message, from_email, [to_email])

            """ Send notification email to owner shop """
            owner_subject = 'New Inquiry Received'
            owner_message = render_to_string(
                'contact/inquiry_emails/notification_body.txt', {'inquiry': inquiry})
            owner_email = 'ninetiesfootballshirts@example.com'
            send_mail(owner_subject, owner_message, from_email, [owner_email])

            messages.success(request, 'Your inquiry has been submited')
            return redirect('contact_success')
        else:
            messages.error(request, 'Looks like your submission failed, please check the form')
    else:
        form = InquiryForm()
    
    return render(request, 'contact/contact_form.html', {'form':form})

def contact_success(request):
    return render(request, 'contact/contact_success.html')


