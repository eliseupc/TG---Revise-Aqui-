from django.shortcuts import render, redirect
from .forms import UsuarioForm, User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from cliente.models import Pessoa


def add_usuario(request):
	if request.method == 'POST':
		form = UsuarioForm(request.POST)
		if form.is_valid():
			u = form.save()
			u.set_password(u.password)
			u.save()
			return redirect('home')
	else:
		form = UsuarioForm()
	return render(request, 'conta/add_usuario.html',{'form':form})

def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user:
			login(request,user)
			return redirect('home')
		else:
			messages.error(request, 'usuário ou senha invalidos!')
	return render(request, 'conta/login.html')

def logout_user(request):
	logout(request)
	return redirect('user_login')

def lista_usuario(request):
	relacao = User.objects.all()
	paginator = Paginator(relacao,5)
	page = request.GET.get('page')
	relacao = paginator.get_page(page)
	return render(request, 'core/lista_usuario.html',{'relacao':relacao})




