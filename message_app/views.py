from django.shortcuts import render,HttpResponse,redirect
from .models import Msg

# Create your views here.
def demo(request):
    return HttpResponse("Hello !! working properly")

def create(request):
    #print("Request is:",request.method)
    if request.method=='POST':
        #fetch values from the form
        n=request.POST['uname']
        mail=request.POST['uemail']
        mob=request.POST['mobile']
        msg=request.POST['msg']
        #insert query
        m=Msg.objects.create(name=n,email=mail,mobile=mob,msg=msg)
        m.save()
        return redirect('/')
        #return HttpResponse("successfully Fetched")
    else:    
        return render(request,'create.html')  

def dashboard(request):
    m=Msg.objects.all()
    print(m)
    context={}
    context['data']=m
   # return HttpResponse("Data fetched")
    return render(request,'dashboard.html',context)

def delete(request,rid):
    m=Msg.objects.filter(id=rid)
    print(m)
    m.delete()
    return redirect('/')
    return HttpResponse("Id deleted is: "+rid)

def edit(request,rid):
    if request.method=='POST':
        #update data
        #fetch values from form
        un=request.POST['uname']
        umail=request.POST['uemail']
        umob=request.POST['mobile']
        umsg=request.POST['msg']
        #update query
        m=Msg.objects.filter(id=rid)
        m.update(name=un,email=umail,mobile=umob,msg=umsg)
    
        return redirect('/')
        
    else:
       # m=Msg.objects.filter(id=rid)
        m=Msg.objects.get(id=rid)
        print(m)
        context={}
        context['data']=m 
        return render(request,'edit.html',context)   
    #return HttpResponse("Id to be edited:"+rid)        