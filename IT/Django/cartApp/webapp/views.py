from django.shortcuts import render,redirect
from .forms import LoginForm,RegisterForm
from .models import User,Item
from django.http import HttpResponse

# AUTH
def register(request):
    form1=RegisterForm()
    form=RegisterForm(request.POST)
    if form.is_valid():
        name=form.cleaned_data['name']
        password=form.cleaned_data['password']
        cash=form.cleaned_data['cash']
        User.objects.create(name=name,password=password,cash=cash)
    
    return render(request,"register.html",{"form":form1})

def login(request):
    name="not loggedin"
    isAuth=0
    if request.method == 'POST':
        MyLoginForm = LoginForm(request.POST)
        if MyLoginForm.is_valid():
            chkname = MyLoginForm.cleaned_data['name']
            chkpassword=MyLoginForm.cleaned_data['password']
            user=User.objects.get(name=chkname)
            if not user:
                return HttpResponse("<h1>User Not Registered</h1>")
            if chkpassword==user.password :
                isAuth=1
        if isAuth==1:
            request.session['name']=user.name
            request.session['cash']=user.cash
            return render(request,'loggedin.html',{"name":user.name,"cash":user.cash})
        else:
            return HttpResponse("<h1>Wrong Password</h1>")
    if request.session.has_key('name'):
        name=request.session['name']
        cash=request.session['cash']
        return render(request,'loggedin.html',{"name":name,"cash":cash})
    else:
        return render(request,'login.html',{ })

def logout(request):
    try:
        del request.session['name']
    except:
        pass
    return render(request,"login.html")

# OTHER
def cart(request):
    if request.session.has_key('name'):
        name=request.session['name']
        items=Item.objects.all()
        print(items)
        bill=0
        
        return render(request,'cart.html',{'items':items,'name':name})
    else:
        return render(request,'login.html',{ })

def index(request):
    return render(request,'index.html')