from django.shortcuts import render
from django.core.mail import send_mail

def sendMailPage(request):
    user_email = "devrijumia@gmail.com"
    send_mail(
    "Test Mail",
    "This is the test message.",
    "shakil.eub.cse@gmail.com",
    [user_email],
    )
    return render(request, 'sendMail.html')
