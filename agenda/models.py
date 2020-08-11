from django.db import models
from cliente.models import Pessoa
from consultor.models import Consultor, Servico

class Agenda(models.Model):
	cliente = models.ForeignKey(Pessoa, on_delete=models.CASCADE,null=True,blank=True)
	consultor = models.ForeignKey(Consultor, on_delete=models.CASCADE,null=True,blank=True)
	servico = models.ForeignKey(Servico, on_delete=models.CASCADE,null=True,blank=True)
	data = models.DateField(auto_now_add=False, null=True)
	hora = models.TimeField(auto_now_add=False, null=True)
	status = (
		('A', 'Aberto'),
		('E', 'Andamento'),
		('F', 'Fechado'),
		)
	status = models.CharField('Status', max_length=1, choices=status, null=True,blank=True)
	preco = models.DecimalField('Preço', max_digits=7, decimal_places=2,null=True,blank=True)
	pag = (
    	('D', 'Dinheiro'),
    	('CD', 'Cartão Debito'),
    	('CC', 'Cartão Credito'),
    	)
	pagamento = models.CharField('Pagamento', max_length=2, choices=pag, null=True,blank=True)
	class Meta:
		verbose_name_plural = 'Agendas'
		verbose_name = 'Agenda'

	

	def __str__(self):
		return "%s" % self.cliente