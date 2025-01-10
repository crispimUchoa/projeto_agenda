from django.shortcuts import render, redirect
from contact.forms import RegisterForm, RegisterUpdateForm
from django.contrib import messages, auth
from django.contrib.auth.forms import AuthenticationForm

def register(request):
    form = RegisterForm()


    if request.method == 'POST':
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            messages.success(request, 'Usuario registrado com sucesso!')
            form.save()
            return redirect('contact:index')

    return render(
        request,
        'contact/register.html',
        {
            'form':form
        }
    )

def login_view(request):
    form = AuthenticationForm()


    if request.method == 'POST':
        form = AuthenticationForm(request)

        if request.method == 'POST':
            form = AuthenticationForm(request, request.POST)
            if form.is_valid():
                user = form.get_user()
                auth.login(request, user)
                messages.success(request, 'Usuario logado com sucesso!')
                return redirect('contact:index')
            
            messages.error(request, 'Login inválido!')

    return render(
        request,
        'contact/login.html',
        {
            'form':form
        }
    )

def logout_view(request):
    auth.logout(request)
    return redirect('contact:login')

def user_update(request):
    form = RegisterUpdateForm(instance=request.user)

    if request.method == 'POST':
        form = RegisterUpdateForm(data=request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('contact:user_update')

    return render(
            request,
            'contact/user_update.html',
            {
                'form': form
            }
            )


