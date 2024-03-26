from django.shortcuts import render,redirect
from django.http import HttpResponse
from story.models import *
# Create your views here.

def test(request):  
    return HttpResponse('testing')
    
def login(request):
    return render (request,'login.html')

def mainpg(request):
    return render(request,'mainpg.html')
    
def fgpwd(request):
    return render(request,'fgpwd.html')

def menu(request):
    return render(request,'menu.html')
    
def reservation(request):
    return render(request,'reservation.html')
    name="Your table is booked."
    name="Thank You for booking😊😀"
    
def contactus(request):
    return render(request,'contactus.html')
    
def aboutus(request):
    return render(request,'aboutus.html')
    
def adminlog(request):
    return render(request,'adminlog.html')
    
def loghome(request):
    return render(request,'loghome.html')
    
 
def log(request):
    return render(request,'login.html')
def sign(request):
    return render(request,'signin.html')
def reserv(request):
    return render(request,'reservation.html')
def men(request):
    return render(request,'menu.html')
def main(request):
    return render(request,'mainpg.html') 
def fp(request):
    return render(request,'fgpwd.html')
def contact(request):
    return render(request,'contactus.html')
def about(request):
    return render(request,'aboutus.html')
def admin(request):
   return render(request,'adminlog.html')
    
def signin(request):
    return render(request,'signin.html')


def inser(request):
    c=customer()
    c.name=request.GET['a1']
    c.phno=request.GET['a2']
    #c.address=request.GET['a3']
    c.city=request.GET['a4']
    c.pin=request.GET['a5']
    c.email=request.GET['a6']
    c.pwd=request.GET['a7']
    c.psd=request.GET['a8']
    c.save()
    return render(request,'signin.html')

def adminlogin(request):
    a=admins()
    a.email=request.GET['a1']
    a.pswd=request.GET['a2']
    a.save()
    return render(request,'adminlog.html')
    
def adminlogin(request):
    c=request.GET['a1']
    d=request.GET['a2']
    try:
        t=admins.objects.get(email=c)
        if t is not None:
            if t.pswd==d:
                x=reserve.objects.all()
                return render(request,'showres.html',{'s':x})
            else: 
                return HttpResponse('<html><h2><center>You have given a wrong email or password. Please Enter the correct Email id or password.</center></h2></html>')
        else:
            return HttpResponse('<html><h2><center>You have given a wrong email or password. Please Enter the correct Email or password.</center></h2></html>')
    except:
        return HttpResponse('<html><h2><center>You have given a wrong email or password. Please Enter the correct Email or password.</center></h2></html>')
    
    
def reservv(request):
    r=reserve()
    r.name=request.GET['a1']
    r.phno=request.GET['a2']
    r.date=request.GET['a3']
    r.seats=request.GET['a4']
    r.save()
    return render(request,'reservation.html')
    
def cont(request):
    n=contactt()
    n.name=request.GET['n1']
    n.email=request.GET['n2']
    n.comment=request.GET['n3']
    n.save()
    return render(request,'contactus.html')
    

    
def showcust(request):
    x=customer.objects.all()
    return render(request,'showcust.html',{'q':x})
def delecust(request,id):
    x=customer.objects.get(id=id)
    x.delete()
    return redirect('../showcust')
def editcust(request,id):
    x=customer.objects.get(id=id)
    return render(request,'editcust.html',{'c':x})
def editc(request,id):
    x=customer.objects.get(id=id)
    return render(request,'editc.html',{'c':x})

def edcode(request,id):
    try:
        t=customer.objects.get(id=id)
        form=form(request.GET,instance=t)
        if form.is_valid():
            form.save()
            return redirect('../showcust')
    except Exception as e:
        return HttpResponse(e)
    return render(request,'editc.html',{'c':t})
        
    
def showad(request):
    y=admins.objects.all()
    return render(request,'showad.html',{'r':y})
def delead(request,id):
    y=admins.objects.get(id=id)
    y.delete()
    return redirect('../showad')
def editad(request,id):
    y=admins.objects.get(id=id)
    return render(request,'editad.html',{'r':y})
    
def showres(request):
    z=reserve.objects.all()
    return render(request,'showres.html',{'s':z})
def deleres(request,id):
    z=reserve.objects.get(id=id)
    z.delete()
    return redirect('../showres')
    #return HttpResponseRedirect(reverse('showres'))
def editres(request,id):
    z=reserve.objects.get(id=id)
    return render(request,'editres.html',{'s':z})

def showfeedback(request):
    b=contactt.objects.all()
    return render(request,'showfeedback.html',{'a':b})

def logg(request):
    a=request.GET['l1']
    b=request.GET['l2']
    try:
        t=customer.objects.get(email=a)
        if t is not None:
            if t.pwd or t.psd==b:
                return render(request,'loghome.html',{'c':t})
            else: 
                return HttpResponse('<html><h2><center>You have given a wrong email or password. Please Enter the correct Email id or password.</center></h2></html>')
        else:
            return HttpResponse('<html><h2><center>You have given a wrong email or password. Please Enter the correct Email or password.</center></h2></html>')
    except:
        return HttpResponse('<html><h2><center>You have given a wrong email or password. Please Enter the correct Email or password.</center></h2></html>')