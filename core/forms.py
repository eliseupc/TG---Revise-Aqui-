from django.forms import ModelForm
from cliente.models import Pessoa
from consultor.models import Consultor, Servico
from agenda.models import Agenda

class ClienteForm(ModelForm):
	class Meta:
		model = Pessoa
		fields = '__all__'

class ConsultorForm(ModelForm):
	class Meta:
		model = Consultor
		fields = '__all__'

class ServicoForm(ModelForm):
	class Meta:
		model = Servico
		fields = '__all__'

class AgendaForm(ModelForm):
	class Meta:
		model = Agenda
		fields = '__all__'