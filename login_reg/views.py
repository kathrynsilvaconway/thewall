from django.shortcuts import render, redirect
from .models import User, UserManager
from django.contrib import messages
import bcrypt

def index(request):
    context = {
        'users': User.objects.all(),
    }
    return render(request, 'index.html', context)

def process_reg(request):
    errors = User.objects.reg_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        this_user = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = pw_hash)
        request.session['first_name'] = this_user.first_name
        request.session['id'] = this_user.id
        return redirect('/wall')

def process_login(request):
    if request.method == "POST":
        errors = User.objects.login_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        one_user = User.objects.filter(email = request.POST['email'])
        request.session['id'] = one_user[0].id
        request.session['first_name'] = one_user[0].first_name
        return redirect('/wall')
    return redirect('/')


    

def render_success_page(request):
    user_id=request.session['id']
    context = {
        'user': User.objects.get(id=user_id)
    }
    return render(request, 'success.html', context)

def log_out(request):
    request.session.flush()
    return redirect('/')



# Create your views here.
