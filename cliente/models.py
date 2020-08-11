from django.db import models


class Pessoa(models.Model):
	nome = models.CharField('Nome', max_length=100,blank=True)
	cpf = models.CharField('CPF', max_length=14,blank=True)
	telefone = models.CharField('Telefone', max_length=9,blank=True)
	endereco = models.CharField('Endereco', max_length=250,blank=True)
	cep = models.CharField('CEP', max_length=13,blank=True)
	cidade = models.CharField('Cidade', max_length=100,blank=True)
	bairro = models.CharField('Bairro', max_length=100,blank=True)
	estado = models.CharField('estado', max_length=2,blank=True)
	email = models.EmailField('Email', max_length=200,blank=True)

	class Meta:
		verbose_name_plural = 'Clientes'
		verbose_name = 'Cliente'

	def __str__(self):
		return self.nome