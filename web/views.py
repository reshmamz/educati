from django.shortcuts import render,loader
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.utils import timezone
import datetime
from pathlib import Path
import random
from . import models



# Create your views here.
def login_view(request):
    msg = ''
    if request.method=="POST":
            name = request.POST.get('name')
            password = request.POST.get('password')
            user = authenticate(username=name, password=password)
            if user is None:
                msg = "Account not found"
            else:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/adminvw/')
                else:
                    msg = "author not active"
    template = loader.get_template('web/Login.html')
    return HttpResponse(template.render({'msg':msg}, request))

def emailnoti(request):
    template = loader.get_template('web/emailnoti.html')
    return HttpResponse(template.render({},request))

def forgot(request):
    msg = ''
    if request.method == "POST":
        try:
            email = request.POST.get('email')
            user = User.objects.get(email=email)
            r = random.randint(100000, 999999)
            link = "http://" + str(request.get_host()) + "/pass/" + str(user.id) +'/' +str(r) + '/'
            mail = EmailMessage('Reset Password', 'Click on the link for reseting password:' + link, to=[email])
            mail.send()
            return HttpResponseRedirect('/notification/')
        except:
            msg = 'Email does not exist'

    template = loader.get_template('web/resetpassword.html')
    return HttpResponse(template.render({'msg': msg}, request))

def passwrd(request,uid,id):
    msg = ''
    user = User.objects.get(id=uid)
    if request.method == "POST":
        password = request.POST.get('password')
        user.set_password(password)
        user.save()
        return HttpResponseRedirect('/login/')

    template = loader.get_template('web/passwordset.html')
    return HttpResponse(template.render({'msg':msg},request))

def dashboard(request):
    dep = models.Departments.objects.all()
    template = loader.get_template('web/dashboard.html')
    return HttpResponse(template.render({'dep':dep},request))

def about(request):
    dep = models.Departments.objects.all()
    template = loader.get_template('web/aboutUs.html')
    return HttpResponse(template.render({'dep':dep},request))

def career(request):
    dep = models.Departments.objects.all()
    now = datetime.date.today()
    career = models.Career.objects.filter(lastdate__range=(now, now+datetime.timedelta(days=30)))
    template = loader.get_template('web/career.html')
    return HttpResponse(template.render({'career':career, 'dep':dep},request))

def contact(request):
    dep = models.Departments.objects.all()
    template = loader.get_template('web/contact.html')
    return HttpResponse(template.render({'dep':dep},request))

def events(request):
    dep = models.Departments.objects.all()
    event = models.Event.objects.all()
    template = loader.get_template('web/events.html')
    return HttpResponse(template.render({'event':event, 'dep':dep},request))

def courses(request):
    dep = models.Departments.objects.all()
    cou = models.Courses.objects.all()
    template = loader.get_template('web/courses.html')
    return HttpResponse(template.render({'cou':cou, 'dep':dep},request))

def faculy(request,id):
    data = models.Faculty.objects.filter(department_id=id)
    print(data)
    dep = models.Departments.objects.all()
    template = loader.get_template('web/faculty.html')
    return HttpResponse(template.render({'dep':dep, 'data':data},request))

def gallery(request):
    dep = models.Departments.objects.all()
    pic = models.Gallery.objects.all()
    template = loader.get_template('web/gallery.html')
    return HttpResponse(template.render({'pic':pic, 'dep':dep},request))

def coursedetails(request,id):
    dep = models.Departments.objects.all()
    data = models.Courses.objects.get(id = id)
    template = loader.get_template('web/coursedetails.html')
    return HttpResponse(template.render({'data':data, 'dep':dep},request))

def eventdetails(request,id):
    dep = models.Departments.objects.all()
    data = models.Event.objects.get(id = id)
    template = loader.get_template('web/eventdetails.html')
    return HttpResponse(template.render({'data':data, 'dep':dep},request))

def careerapply(request,id):
    pop =''
    msg =''
    now = datetime.date.today()
    dep = models.Departments.objects.all()
    pos = models.Career.objects.filter(lastdate__range=(now, now+datetime.timedelta(days=30)))
    data = models.Career.objects.get(id=int(id))
    if request.method=="POST" and 'name' in request.POST:
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        file = request.FILES['file']
        loc = request.POST.get('location')
        info = request.POST.get('details')
        car = models.CareerApplication()
        car.name = name
        car.email = email
        car.phone = phone
        car.cv = file
        car.post_id = id
        car.location = loc
        car.moreinfo = info
        car.save()
        pop = 'add'
        temp = loader.get_template('web/email.html')
        msgs = 'Hello ' + str(name)+','+'\n'+ "Welcome to Educati, You have successfully applied for the job"
        content = temp.render({'msg':msgs},request)
        email = EmailMessage('Welcome To Educati',content, to=[email])
        email.content_subtype ="html"
        email.send()
        return HttpResponseRedirect('/career/')
    template = loader.get_template('web/careerapply.html')
    return HttpResponse(template.render({'data':data, 'dep':dep, 'pos':pos,'pop':pop, 'msg':msg}, request))
