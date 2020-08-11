from django.db import models


class Consultor(models.Model):
	nome = models.CharField('Consultor', max_length=100,blank=True)
	telefone = models.CharField('Telefone', max_length=9,blank=True)

	class Meta:
		verbose_name = 'Consultor'
		verbose_name_plural = 'Consultores'

	def __str__(self):
		return self.nome

class Servico(models.Model):
	nome = models.CharField('Seviço', max_length=100)
	pag = (
    	('D', 'Dinheiro'),
    	('CD', 'Cartão Debito'),
    	('CC', 'Cartão Credito'),
    	)
	pagamento = models.CharField('Pagamento', max_length=2, choices=pag,blank=True)
	valor_servico = models.CharField('Valor Serviço', max_length=100,blank=True)
	class Meta:
		verbose_name = 'Serviço'
		verbose_name_plural = 'Serviços'

	def __str__(self):
		return self.nome