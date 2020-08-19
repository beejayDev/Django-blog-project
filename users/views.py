from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from users.forms import CreationForm, AuthForm

# Create your views here
def register(request):
    form = CreationForm()
    if request.method == 'POST':
        form = CreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! you can now proceed to login')
            return redirect('login')
    else:
        form = CreationForm()
    return render(request, 'users/register.html', {'forms': form})


def signin(request):
    if request.user.is_authenticated:
        return render(request, 'blog/home.html')
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('blog-home')
        else:
            form = AuthForm(request.POST)
            return render(request, 'users/login.html', {'form': form})
    else:
        form = AuthForm()
        return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return render(request, 'users/logout.html')

def profile(request):
    return render(request, 'users/profile.html')    
