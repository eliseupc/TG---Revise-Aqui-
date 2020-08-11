from django.shortcuts import render
from cliente.models import Pessoa
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def lista_cliente(request):
	relacao = Pessoa.objects.all()
	paginator = Paginator(relacao,5)
	page = request.GET.get('page')
	relacao = paginator.get_page(page)
	return render(request, 'core/lista_cliente.html',{'relacao':relacao})
