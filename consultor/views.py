from django.shortcuts import render
from consultor.models import Consultor, Servico
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def lista_consultor(request):
	relacao = Consultor.objects.all()
	paginator = Paginator(relacao,5)
	page = request.GET.get('page')
	relacao = paginator.get_page(page)
	return render(request, 'core/lista_consultor.html',{'relacao':relacao})


def lista_servico(request):
	relacao = Servico.objects.all()
	paginator = Paginator(relacao,5)
	page = request.GET.get('page')
	relacao = paginator.get_page(page)
	return render(request, 'core/lista_servico.html',{'relacao':relacao})
