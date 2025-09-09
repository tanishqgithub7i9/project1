from django.shortcuts import render,redirect
from mainapp.models import Student
from adminapp.models import study,News
from .models import Feedback
# Create your views here.
def index(request):
    try:
        if request.session['student'] == None:
            return redirect('mainapp:Login')
        else:
            stu = Student.objects.get(id= request.session['student'])
            st = study.objects.filter(course=stu.course,branch=stu.branch,session=stu.session)
            st1 =len(st)
            fe= Feedback.objects.filter(sid=stu.id,feedtype="Feedback")
            fel = len(fe)
            co = Feedback.objects.filter(sid=stu.id,feedtype="complain")
            col = len(co)
            su = Feedback.objects.filter(sid=stu.id,feedtype="suggestion")
            sul = len(su)
            n = News.objects.all()
            nl = len(n)
            
            return render(request,'studenthome.html',locals())
    except:
        return redirect('mainapp:Login')
    

def ststudy(request):
    stid = request.session['student']
    stu = Student.objects.get(id=stid)
    st = study.objects.filter(branch=stu.branch,session=stu.session,course=stu.course)
    
    return render(request,'ststudy.html',locals())

def viewnews(requets):
    news = News.objects.all()
    return render(requets,'stnews.html',locals())

def stfeed(request):
    if request.method=="POST":
        feedtype = request.POST['feedtype']
        title = request.POST['title']
        desc = request.POST['desc']
        sid = request.session['student']
        Feedback.objects.create(feedtype=feedtype,title=title,desc=desc,sid=sid)
        return redirect('studentapp:stfeed')
    return render(request,'stfeed.html')

def viewstfeed(request):
    sid = request.session['student']
    feed = Feedback.objects.filter(sid=sid)
    return render(request,'viewstfeed.html',locals())

def delfeed(request,id):
    Feedback.objects.filter(id=id).delete()
    return redirect(request,'studentapp:viewsfeed')