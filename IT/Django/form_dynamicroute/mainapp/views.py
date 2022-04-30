from django.shortcuts import render
from mainapp.forms import LoginForm
from django.http import HttpResponse
def login(request):
    MyLoginForm = LoginForm()
    print('req1',request)
    return render(request, 'login.html')

def dashboard(request):
    print('req2',request)
    username = "not logged in"
    cn="not found"
    if request.method == "POST":
     #Get the posted form
        MyLoginForm = LoginForm(request.POST)
        if MyLoginForm.is_valid():
            username = MyLoginForm.cleaned_data['username']
            cn= MyLoginForm.cleaned_data['contact_num']
            context = {'username': username,'contact_num':cn}
            return render(request, 'loggedin.html',context)

def x(request,x_num):
    print('req3',request)
    con={'x_num':x_num}
    return render(request,'x.html',con)