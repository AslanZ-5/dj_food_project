from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    form = UserCreationForm()
    context = {'form': form}
    return render(request, 'register.html', context=context)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        # username = request.POST.get('username')
        # password = request.POST.get('password')
        # print(username, password)
        # user = authenticate(request, username=username, password=password)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('home')

        # if user is None:
        #     context = {'error': 'password or username is incorrect'}
        #     return render(request, 'login.html', context=context)
        # else:
        #     login(request, user)
        #     return redirect('/')
    else:
        form = AuthenticationForm(request)
    context = {'form':form}
    return render(request, 'login.html', context=context)


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.info(request, 'logged out')
        return redirect('login')
    return render(request, 'login.html')
