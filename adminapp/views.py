from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def index(request):
     try:
          if request.session['admin']== None:
               return redirect('mainapp:adlogin')
          return render(request,'adminhome.html')
     except:
          return redirect('mainapp:adlogin')

def adnews(request):
     if request.method == "POST":
          title = request.POST['title']
          desc = request.POST['desc']
          n = News.objects.create(title=title,desc=desc)
          n.save()
          return redirect('adminapp:adnews')
     news= News.objects.all()
     return render(request,'adnews.html',{'news':news})

def adbranch(request):
     if request.method=="POST":
          name= request.POST['name']
          br = Branch.objects.create(name=name)
          return redirect('adminapp:adbranch')
     br = Branch.objects.all()
     return render(request,'adbranch.html',{'br':br})

def adcourse(request):
     if request.method=="POST":
          name= request.POST['name']
          br = Course.objects.create(name=name)
          return redirect('adminapp:adcourse')
     br = Course.objects.all()
     return render(request,'adcourse.html',{'br':br})



def adsession(request):
     if request.method=="POST":
          name= request.POST['name']
          br = Session.objects.create(name=name)
          return redirect('adminapp:adcourse')
     br = Session.objects.all()
     return render(request,'adsession.html',{'br':br})

def adstudy(request):
     if request.method=="POST":
          course = request.POST['course']
          branch = request.POST['branch']
          session = request.POST['session']
          subject = request.POST['subject']
          file_name = request.POST['file_name']
          file = request.FILES['file']
          stu = study()
          stu .course=course
          stu . session=session
          stu . branch=branch
          stu . subject=subject
          stu . file_name=file_name
          stu . file=file
          stu.save()
          return redirect('adminapp:adstudy')
     cr = Course.objects.all()
     br = Branch.objects.all()
     se = Session.objects.all()

     return render(request,'adstudy.html',{'cr': cr, 'br': br, 'se': se})

def editbranch(request,id):
     if request.method=="POST":
          name=request.POST['name']
          Branch.objects.filter(id=id).update(name=name)
          return redirect('adminapp:adbranch')
     br = Branch.objects.all()
     b = Branch.objects.get(id=id)
     return render(request,'adbranch.html',{'b':b,'br':br})

def editcourse(request,id):
     if request.method=="POST":
          name=request.POST['name']
          Course.objects.filter(id=id).update(name=name)
          return redirect('adminapp:adcourse')
     br = Course.objects.all()
     b = Course.objects.get(id=id)
     return render(request,'adcourse.html',{'b':b,'br':br})

def editsession(request,id):
     if request.method=="POST":
          name=request.POST['name']
          Session.objects.filter(id=id).update(name=name)
          return redirect('adminapp:adsession')
     br = Session.objects.all()
     b = Session.objects.get(id=id)
     return render(request,'adsession.html',{'b':b,'br':br})

def deletebranch(request,id):
     Branch.objects.filter(id=id).delete()
     return redirect('adminapp:adbranch')

def deletecourse(request,id):
     Course.objects.filter(id=id).delete()
     return redirect('adminapp:adcourse')

def deletesession(request,id):
     Session.objects.filter(id=id).delete()
     return redirect('adminapp:adsession')

def viewstudy(request):
     st = study.objects.all()
     return render(request,'viewstudy.html',locals())

def editstudy(request,id):
     if request.method=="POST":
          course = request.POST['course']
          branch = request.POST['branch']
          session = request.POST['session']
          subject = request.POST['subject']
          file_name = request.POST['file_name']
          study = study.objects.get(id=id)
          study.course=course
          study.branch=branch
          study.session=session
          study.subject=subject
          study.file_name=file_name
          file = request.FILES['file']
          try:
           if(request.FILES['file']):
               study.file=request.FILES[file]
          except:
           pass
           study.save()
     
          

     st = study.objects.get(id=id)
     cr = Course.objects.all()
     br = Branch.objects.all()
     se = Session.objects.all()

     return render(request,'adstudy.html',locals())


def deletestudy(request,id):
     study.objects.filter(id=id).delete()
     return redirect('adminapp:adstudy')

# def editnews(request,id):
#      if request.method=="POST":
#           name=request.POST['name']
#           Session.objects.filter(id=id).update(name=name)
#           return redirect('adminapp:adnews')
#      br = Session.objects.all()
#      b = Session.objects.get(id=id)
#      return render(request,'adnews.html',{'b':b,'br':br})

# def deletenews(request,id):
#      study.objects.filter(id=id).delete()
#      return redirect('adminapp:adnews')



