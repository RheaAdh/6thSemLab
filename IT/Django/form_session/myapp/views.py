from django.shortcuts import render
from myapp.forms import LoginForm
from django.http import HttpResponse

def login(request):
    username = 'not logged in'
    if request.method == 'POST':
        MyLoginForm = LoginForm(request.POST)
        if MyLoginForm.is_valid():
            username = MyLoginForm.cleaned_data['username']
            request.session['username'] = username
            # return HttpResponse('<h1>Hello HttpResponse</h1>',username)    
            return render(request, 'loggedin.html', {"username" : username})


def formView(request):
    print("here2")
    print(request)
    if request.session.has_key('username'):
        print("has key")
        username=request.session['username']
        print("USERRRRR:",username)
        return render(request,'loggedin.html',{"username":username})
    else:
        print("has no key")
        return render(request,'login.html',{ })
def logout(request):
    try:
        del request.session['username']
    except:
        pass
    return HttpResponse("<strong>You are logged out.</strong>")
