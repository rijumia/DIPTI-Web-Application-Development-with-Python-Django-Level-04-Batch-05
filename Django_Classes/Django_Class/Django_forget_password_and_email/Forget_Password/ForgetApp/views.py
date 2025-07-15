from django.shortcuts import render
from django.core.mail import send_mail

def sendMailPage(request):
    user_email = "devrijumia@gmail.com"
    send_mail(
    "Test Mail", #Email Subject Here
    "This is the test message.", #Email Body Message
    "shakil.eub.cse@gmail.com", #Sender Mail
    [user_email],
    )
    return render(request, 'sendMail.html')
