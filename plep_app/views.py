from django import forms
from django.http import request
from django.shortcuts import redirect, render
from .forms import ClientForm
from .models import Client
from django.contrib import messages
from django.core.mail import send_mail

from custom.unique_token import uniqid


def index(request):
    return render(request, 'plep_app/index.html')

def csc320(request):
    return render(request, 'plep_app/csc320.html')



def register(request):
    form = ClientForm()
    if request.method == "POST":
        print('traking..')
        print(request.POST)
    
        fullname = request.POST['fullname']
        supervisor_name = request.POST['supervisor_name']
        project_catg = request.POST['project_catg']
        others = request.POST['others']
        project_name = request.POST['project_name']
        project_description = request.POST['project_description']
        program_lang = request.POST['program_lang']
        email = request.POST['email']
        phone = request.POST['phone']
        project_mode = request.POST['project_mode']
        no_of_member = request.POST['no_of_member']
        uid = uniqid(8)

        print("fullname", fullname)
        print(uid)

        client = Client(
            fullname=fullname,
            supervisor_name=supervisor_name,
            project_catg=project_catg,
            others=others,
            project_name=project_name,
            project_description=project_description,
            program_lang=program_lang,
            email=email,
            phone=phone,
            project_mode=project_mode,
            no_of_member=no_of_member,
            uid=uid,
            is_verify=False
        )
        print(client.fullname)
        print(client.uid)
        client.save()

        send_mail(
            'PLEP (UID verification)',
            f'Hi, {fullname.title()} this is your UID.. {uid}',
            'daryor1000@gmail.com',
            [email],
            fail_silently=False
        )

        return redirect("plep_app:reg_success")
        
    return render(request, 'plep_app/register.html', dict(form=form))


def reg_success(request):
    return render(request, 'plep_app/reg_success.html')




def uid_verification(request):
    if request.method == 'POST':
        uid = request.POST['uid']
        clients = Client.objects.all()
        client = Client.objects.get(uid=uid)
        ids = [id.uid for id in clients]
        print(ids)
        if uid in ids:
            return redirect("dashboard/" + str(uid))
        else:
            err = "No such UID"
            return render(request, 'plep_app/uid_verification.html', {'err':err})
    return render(request, 'plep_app/uid_verification.html')



def dashboard(request, pk):
    client = Client.objects.get(uid=pk)
    return render(request, 'plep_app/dashboard.html', dict(client=client))