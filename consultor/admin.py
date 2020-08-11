from django.contrib import admin
from .models import Consultor, Servico

@admin.register(Consultor)
class ConsultorAdmin(admin.ModelAdmin):
	list_display = ('nome', 'telefone')
	search_fields = ('nome', 'telefone')

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
	list_display = ('nome', 'pagamento', 'valor_servico')
	search_fields = ('nome',)