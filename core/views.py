from django.shortcuts import render, redirect, get_object_or_404
from cliente.models import Pessoa
from consultor.models import Consultor, Servico
from .forms import ClienteForm, ConsultorForm, ServicoForm, AgendaForm
from conta.forms import UsuarioForm, User
from agenda.models import Agenda
from datetime import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
	data = datetime.now()
	lista = Pessoa.objects.all()
	total_clientes = Pessoa.objects.count()
	total_servicos = Servico.objects.count()
	total_agendamentos = Agenda.objects.count()
	total_consultores = Consultor.objects.count()
	paginator = Paginator(lista,5)
	page = request.GET.get('page')
	lista = paginator.get_page(page)
	return render(request, 'index.html',{'lista':lista,'data':data,'total_clientes':total_clientes,'total_servicos':total_servicos,
	'total_agendamentos':total_agendamentos,'total_consultores':total_consultores})


def base(request):
	data_base = datetime.now()
	return render(request,'base.html',{'data_base':data_base})

@login_required
def cliente(request):
	if request.method == 'POST':
		form = ClienteForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = ClienteForm()
	return render(request, 'core/clienteform.html',{'form':form})

@login_required
def consultor(request):
	if request.method == 'POST':
		form = ConsultorForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = ConsultorForm()
	return render(request, 'core/consultorform.html',{'form':form})

@login_required
def servico(request):
	if request.method == 'POST':
		form = ServicoForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = ServicoForm()
	return render(request, 'core/servicoform.html',{'form':form})

@login_required
def agenda(request):
	if request.method == 'POST':
		form = AgendaForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('lista')
	else:
		form = AgendaForm()
	return render(request, 'core/agendaform.html',{'form':form})

@login_required
def lista(request):
	relacao = Agenda.objects.all()
	paginator = Paginator(relacao,5)
	page = request.GET.get('page')
	relacao = paginator.get_page(page)
	return render(request, 'core/lista.html',{'relacao':relacao})

@login_required
def editar(request, id_agenda):
	edite = get_object_or_404(Agenda, id=id_agenda)
	if request.method == 'POST':
		form = AgendaForm(request.POST, instance=edite)
		if form.is_valid():
			form.save()
			return redirect('lista')
	else:
		form = AgendaForm(instance=edite)
	return render(request, 'core/agendaform.html',{'form':form})

@login_required
def deletar(request, id_agenda):
	exclui = Agenda.objects.get(id=id_agenda).delete()
	return redirect('lista')

@login_required
def edita_cliente_home(request, id_cliente):
	ed = get_object_or_404(Pessoa, id=id_cliente)
	if request.method == 'POST':
		form = ClienteForm(request.POST, instance=ed)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = ClienteForm(instance=ed)
	return render(request, 'core/clienteform.html',{'form':form})
	
@login_required
def deleta_cliente_home(request, id_cliente):
	exclui_cliente = Pessoa.objects.get(id=id_cliente).delete()
	return redirect('home')

@login_required
def edita_cliente(request, id_cliente):
	ed = get_object_or_404(Pessoa, id=id_cliente)
	if request.method == 'POST':
		form = ClienteForm(request.POST, instance=ed)
		if form.is_valid():
			form.save()
			return redirect('lista_cliente')
	else:
		form = ClienteForm(instance=ed)
	return render(request, 'core/clienteform.html',{'form':form})
	
@login_required
def deleta_cliente(request, id_cliente):
	exclui_cliente = Pessoa.objects.get(id=id_cliente).delete()
	return redirect('lista_cliente')


#Editar Consultor
@login_required
def edita_consultor(request, id_consultor):
	ed = get_object_or_404(Consultor, id=id_consultor)
	if request.method == 'POST':
		form = ConsultorForm(request.POST, instance=ed)
		if form.is_valid():
			form.save()
			return redirect('lista_consultor')
	else:
		form = ConsultorForm(instance=ed)
	return render(request, 'core/consultorform.html',{'form':form})
	
@login_required
def deleta_consultor(request, id_consultor):
	exclui_consultor = Consultor.objects.get(id=id_consultor).delete()
	return redirect('lista_consultor')


#Editar Servico
@login_required
def edita_servico(request, id_servico):
	ed = get_object_or_404(Servico, id=id_servico)
	if request.method == 'POST':
		form = ServicoForm(request.POST, instance=ed)
		if form.is_valid():
			form.save()
			return redirect('lista_servico')
	else:
		form = ServicoForm(instance=ed)
	return render(request, 'core/servicoform.html',{'form':form})
	
@login_required
def deleta_servico(request, id_servico):
	exclui_servico = Servico.objects.get(id=id_servico).delete()
	return redirect('lista_servico')

#Editar Usuário
@login_required
def edita_usuario(request, id_user):
	ed = get_object_or_404(User, id=id_user)
	if request.method == 'POST':
		form = UsuarioForm(request.POST, instance=ed)
		if form.is_valid():
			form.save()
			return redirect('lista_usuario')
	else:
		form = UsuarioForm(instance=ed)
	return render(request, 'conta/add_usuario.html',{'form':form})
	
@login_required
def deleta_usuario(request, id_user):
	exclui_usuario = User.objects.get(id=id_user).delete()
	return redirect('lista_usuario')


