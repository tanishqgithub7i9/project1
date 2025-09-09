from django.shortcuts import render,redirect
from .models import Admin,Student,login
from adminapp.models import Course,Branch,Session
# Create your views here.
def index(request):
    return render(request,'index.html')

def adlogin(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        ad = Admin.objects.get(email=email)
        if ad and ad.password == password:
            request.session['admin'] = "Active"
            return redirect('adminapp:dash')
        else:
            return redirect('mainapp.adlogin')
    return render(request,'adlogin.html')

def logout(request):
    request.session.flush()
    return redirect('mainapp:index')

def reg(request):
    if request.method=="POST":
        name=request.POST['name']
        fname=request.POST['fname']
        mname=request.POST['mname']
        number=request.POST['number']
        email=request.POST['email']
        password=request.POST['password']
        gender=request.POST['gen']
        course=request.POST['course']
        branch=request.POST['branch']
        session=request.POST['session']
        address=request.POST['address']
        pic = request.FILES['pic']
        stu = Student()
        stu.name=name
        stu.fname=fname
        stu.mname=mname
        stu.number=number
        stu.email=email
        stu.gender=gender
        stu.course=course
        stu.branch=branch
        stu.session=session
        stu.address=address
        stu.pic=pic
        lo=login.objects.create(email=email,password=password)
        stu.save()
        # Send Email After Successful Registration
        context = {
            'name': name,
            'email': email,
            'password': password,
            'year': datetime.datetime.now().year
        }
        html_content = render_to_string('email.html', context)
        subject = "Welcome to Biotech Park OLP"
        from_email = settings.EMAIL_HOST_USER
        to = [email]

        msg = EmailMultiAlternatives(subject, '', from_email, to)
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return redirect('mainapp:login')

    cr = Course.objects.all()
    br = Branch.objects.all()
    se = Session.objects.all()
    return render(request,'reg.html',locals())

def Login(request):
    if request.method=="POST":
        email = request.POST['email']
        password = request.POST['password']
        lo = login.objects.get(email=email)
        if(lo and lo.password==password):
            student = Student.objects.get(email=email)
            request.session['student'] = student.id
            return redirect('studentapp:index')
        else:
            return redirect('mainapp:Login')

    return render(request,'Login.html')

def home(request):
    return render(request,'home.html')
def org(request):
    return render(request,'org.html')

def why_biotech(request):
    return render(request,'why_biotech.html')
def home(request):
    return render(request,'home.html')

def location(request):
    return render(request,'location.html')\
    
def certification(request):
    return render(request,'certification.html')

def collaborators(request):
    return render(request,'collaborators.html')


def knowledge_network(request):
    return render(request,'knowledge_network.html')


def outreach_activity(request):
    return render(request,'outreach_activity.html')

from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
import datetime




