from django.shortcuts import render,loader
from django.http import HttpResponse,HttpResponseRedirect
from web import models
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage

# Create your views here.

@login_required(login_url='http://127.0.0.1:8000/login/')
def dash(request):
    template = loader.get_template('adminview/dashboard.html')
    return HttpResponse(template.render({},request))

def header (request):
    user = User.objects.all()
    template = loader.get_template('adminview/header.html')
    return HttpResponse(template.render({'user':user}, request))


@login_required(login_url='http://127.0.0.1:8000/login/')
def department(request):
    pop = ''
    dp = models.Departments.objects.all()
    if request.method =="POST" and 'department' in request.POST:
        dep = request.POST.get('department')
        deprt = models.Departments()
        deprt.department = dep
        deprt.save()
        pop = 'add'
    if request.method =="POST" and 'dele' in request.POST:
        dprt = models.Departments.objects.get(id=int(request.POST.get('dele')))
        dprt.delete()
        pop = 'delete'

    template = loader.get_template('adminview/Department.html')
    return HttpResponse(template.render({'pop':pop, 'depp':dp},request))


@login_required(login_url='http://127.0.0.1:8000/login/')
def depView(request,id):
    pop = ''
    dep = models.Departments.objects.all()
    faculty = models.Faculty.objects.filter(department_id=id)
    if request.method =="POST" and 'facultyy' in request.POST:
        fac = request.POST.get('facultyy')
        depr = request.POST.get('departments')
        des = request.POST.get('designations')
        facc = models.Faculty()
        facc.name = fac
        facc.department_id = depr
        facc.designation =des
        facc.save()
        pop = 'add'
    if request.method =="POST" and 'editfac' in request.POST:
        faclty = models.Faculty.objects.get(id= int(request.POST.get('editfac')))
        faclty.name = request.POST.get('faculty')
        faclty.designation = request.POST.get('designation')
        faclty.department_id = request.POST.get('department')
        faclty.save()
    if request.method=="POST" and 'delefac' in request.POST:
        fa = models.Faculty.objects.get(id = int(request.POST.get('delefac')))
        fa.delete()
        pop = 'delete'
    template = loader.get_template('adminview/DeprtmntView.html')
    return HttpResponse(template.render({'pop':pop,'fac':faculty, 'dep':dep}, request))

@login_required(login_url='http://127.0.0.1:8000/login/')
def course(request):
    pop = ''
    cour = models.Courses.objects.all()
    dep = models.Departments.objects.all()
    if request.method=="POST" and 'coursee' in request.POST:
        name = request.POST.get('coursee')
        deprt = request.POST.get('departments')
        seat =request.POST.get('seat')
        dur= request.POST.get('duration')
        file = request.FILES['file']
        deta = request.POST.get('details')
        cou = models.Courses()
        cou.course = name
        cou.dep_id = deprt
        cou.duration = dur
        cou.seats= seat
        cou.details = deta
        cou.banner= file
        cou.save()
        pop = 'add'
    if request.method=="POST" and 'dele' in request.POST:
        cours = models.Courses.objects.get(id= int(request.POST.get('dele')))
        cours.delete()
        pop = 'delete'
    if request.method=="POST" and 'editid' in request.POST:
        co = models.Courses.objects.get(id=int(request.POST.get('editid')))
        co.course = request.POST.get('course')
        co.dep_id = request.POST.get('department')
        co.banner = request.FILES['file']
        co.seats = request.POST.get('seat')
        co.details = request.POST.get('details')
        co.duration = request.POST.get('duration')
        co.save()
        pop = 'edit'
    template = loader.get_template('adminview/Courses.html')
    return HttpResponse(template.render({'cou':cour, 'pop':pop, 'dep':dep},request))


@login_required(login_url='http://127.0.0.1:8000/login/')
def events(request):
    pop = ''
    event = models.Event.objects.all()
    if request.method=='POST' and 'events' in request.POST:
        events = request.POST.get('events')
        date = request.POST.get('date')
        venue = request.POST.get('venue')
        time = request.POST.get('time')
        cost = request.POST.get('cost')
        pic= request.FILES['pic']
        details = request.POST.get('details')
        eve = models.Event()
        eve.event = events
        eve.date = date
        eve.venue = venue
        eve.pic = pic
        eve.time = time
        eve.cost = cost
        eve.details = details
        eve.save()
        pop = 'add'
    if request.method == "POST" and 'dele' in request.POST:
        evn = models.Event.objects.get(id=int(request.POST.get('dele')))
        evn.delete()
        pop = 'delete'
    if request.method =="POST" and 'editeveid' in request.POST:
        evee = models.Event.objects.get(id=int(request.POST.get('editeveid')))
        evee.event = request.POST.get('event')
        evee.date = request.POST.get('date')
        evee.time = request.POST.get('time')
        evee.venue = request.POST.get('venue')
        evee.cost = request.POST.get('cost')
        evee.pic = request.FILES['pic']
        evee.details = request.POST.get('details')
        evee.save()
        pop = 'edit'

    template = loader.get_template('adminview/Events.html')
    return HttpResponse(template.render({'eve':event,'pop':pop},request))

@login_required(login_url='http://127.0.0.1:8000/login/')
def career(request):
    pop = ''
    car = models.Career.objects.all()
    if request.method =="POST" and 'post' in request.POST:
        post = request.POST.get('post')
        type = request.POST.get('type')
        salary = request.POST.get('salary')
        lastdate = request.POST.get('date')
        loc = request.POST.get('location')
        req = request.POST.get('requirement')
        descrptn = request.POST.get('description')
        career = models.Career()
        career.post = post
        career.type = type
        career.salary = salary
        career.lastdate = lastdate
        career.location = loc
        career.requirements = req
        career.description = descrptn
        career.save()
        pop = 'add'
    if request.method =="POST" and 'dele' in request.POST:
        cr = models.Career.objects.get(id=int(request.POST.get('dele')))
        cr.delete()
        pop = 'delete'
    if request.method=="POST" and 'editcarid' in request.POST:
        ca = models.Career.objects.get(id=int(request.POST.get('editcarid')))
        ca.post = request.POST.get('postname')
        ca.type = request.POST.get('type')
        ca.location = request.POST.get('location')
        ca.salary = request.POST.get('salary')
        ca.requirements = request.POST.get('requirement')
        ca.save()
        pop = 'edit'
    template = loader.get_template('adminview/Career.html')
    return HttpResponse(template.render({'pop':pop, 'car':car},request))


@login_required(login_url='http://127.0.0.1:8000/login/')
def applicaton(request,id):
    pop =''
    app = models.CareerApplication.objects.filter(post_id = id)
    if request.method =="POST" and 'delefac' in request.POST:
        applictn = models.CareerApplication.objects.get(id = int(request.POST.get('delefac')))
        eml = applictn.email
        applictn.delete()
        email = EmailMessage('Reply to your job application', 'job application has Rejected', to=[eml])
        email.send()

    if request.method == "POST" and 'accept' in request.POST:
        appli = models.CareerApplication.objects.get(id = int(request.POST.get('accept')))
        em = appli.email
        date = request.POST.get('date')
        time = request.POST.get('time')
        loc = request.POST.get('loc')
        email = EmailMessage('Interview Call','Dear Candidate,'+'\n'+'This is to inform that you have been shortlisted to attend an Interview.'+'\n'+'\n' +'date:'+date+'\n'+'time:'+time +'\n'+'location:'+loc,to=[em])
        email.send()
        pop = 'ok'
    template = loader.get_template('adminview/application.html')
    return HttpResponse(template.render({'app':app, 'pop':pop}, request))

@login_required(login_url='/login/')
def gallery(request):
    pop = ''
    ga = models.Gallery.objects.all()
    if request.method =="POST" and 'title' in request.POST:
        tit = request.POST.get('title')
        imag = request.FILES['imag']
        gall = models.Gallery()
        gall.title = tit
        gall.pic = imag
        gall.save()
        pop = 'add'

    if request.method =="POST" and 'delegal' in request.POST:
        galle = models.Gallery.objects.get(id=int(request.POST.get('delegal')))
        galle.delete()
        pop = 'delete'
    template = loader.get_template('adminview/Gallery.html')
    return HttpResponse(template.render({'pop':pop, 'gal':ga}, request))

