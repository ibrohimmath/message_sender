from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpResponseNotFound, JsonResponse 
from django.shortcuts import render, redirect, get_object_or_404 

from django.core.mail import send_mail

def send(request):
    if request.method == 'POST':
        name = request.POST['name']
        subject = request.POST['subject']
        message = request.POST['message']
        emails = request.POST['emails'].split(',')
        # print(name, email, subject, message, emails)
        send_mail(subject, f'{name}:{message}', '', emails, fail_silently = True)
    return render(request, 'send_form.html')