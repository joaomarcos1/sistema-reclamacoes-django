
from django.db import models
from django.contrib import auth
import re
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
#from django.core import validators

from django.db import models
from django.contrib import auth 
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db.models.deletion import CASCADE
#from django.core import validators
from django.utils.translation import ugettext_lazy as _
import re


class situacaoAtendimento(models.Model):
	situacao = models.TextField(default='...')

	
	def __str__(self):
		return self.situacao

class Cliente(models.Model):
	#username = models.CharField(max_length=50,unique=True,null=True)
	#password = models.CharField(max_length=50,null=True)
	user = models.OneToOneField(User, on_delete=models.CASCADE, null = True)
	#idUser = models.TextField(unique=True,null=False, default='', primary_key=True)
	nome = models.CharField(max_length=50,null=True)
	cpf = models.TextField(unique=True,null=True)
	#curso = models.ManyToManyField(Curso)
	#curso = models.ForeignKey(Curso, default=2, on_delete = models.CASCADE)
	email = models.TextField()
	telefone = models.TextField()
	data_nascimento = models.DateField(max_length=20)
	#status = models.TextField()
	#funcao = models.ForeignKey(Funcao, default=2, on_delete = models.CASCADE)
	#funcao = models.TextField(default='')

	def setTelefone(self, telef):
		self.telefone = telef
	def getTelefone(self):
		return self.telefone

	def setUserName(self, username):
		self.username = username
	def getUserName(self):
		return self.username

	def setPassword(self, password):
		self.password = password
	def getPassword(password):
		return self.password


	#def setID(self, matricula):
	#	self.idUser = matricula
	#def getID(self):
	#	return self.idUser

	def setnNome(self, nome):
		self.nome = nome
	def getNome(self):
		return self.nome

	def setCPF(self, cpf):
		self.cpf = cpf
	def getCPF(self):
		return self.cpf

	def setEmail(self, email):
		self.email = email
	def getEmail(self):
		return self.email

	def setDataNascimento(self, data_nascimento):
		self.data_nascimento = data_nascimento
	def getDataNascimnto(self):
		return self.data_nascimento

	def setSenha(self, senha):
		self.senha = senha
	def getSenha(self):
		return self.senha




	def __str__(self):
		return self.nome


# Create your models here.
class Tecnico_Campo(models.Model):
    #idt = models.IntegerField(primary_key=True)
	nome = models.TextField()
	dataNascimento = models.TextField(default='01/01/0000')
	endereco = models.TextField(default='...')
	telefone = models.TextField(default='3333-3333')
	cpf = models.TextField(null=True, default='12345678901')
	#atendimentoRelacionado = models.ManyToManyField(atendimento)

	def setEndereco(self, end):
		self.endereco = end
	def getEndereco(self):
		return self.endereco


	def setNome(self, nome):
		self.nome = nome
		
	def getNome(self):
		return self.nome

	def setDataNascimento(self, dataN):
		self.dataNascimento = dataN
	def getDataNascimento(self):
		return self.dataNascimento

	def setCPF(self, cpf1):
		self.cpf = cpf1
	def getCPF(self):
		return self.cpf


	def setTelefone(self,telefone):
		self.telefone = telefone
		
	def getTelefone(self):
		return self.telefone

	def __str__(self):
		return self.nome



class atendimento(models.Model):
	#id = models.TextField(primary_key=True)
	
	situacao = models.TextField(null=False)
	cliente = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
	#situacao = models.ForeignKey(situacaoAtendimento, on_delete = models.CASCADE)
	hora_inicio = models.DateTimeField(null=True)
	hora_fim = models.DateTimeField(null=True)
	tecnico_resposavel = models.ForeignKey(Tecnico_Campo, on_delete=models.CASCADE, null=True)

	#def __str__(self):
	#	return self.cliente

	#def setCliente(self, User):#VERIFICAR COMO PEGAR A CHAVE DO CLIENTE
	#	self.nome = User
		
	#def getNome(self):
	#	return self.nome

	def setSituacaoAtendimento(self, sit):
		self.situacao = sit

	def getSituacaoAtendimento(self):
		return self.situacao	

	
	def setHoraInicioAtendimento(self, horaIni):
		self.hora_inicio = horaIni
	def getHoraFimAtendimento(self):
		return self.hora_inicio


	def setHoraFimAtendimento(self, horaFim):
		self.hora_fim = horaFim
	def getHoraFimAtendimento(self, horaFim):
		return self.hora_fim






class atendente(models.Model):
	#id = models.TextField(primary_key=True)
	nome = models.TextField()
	cpf = models.TextField(default='999999999999')
	endereco = models.TextField(default='...')
	atendimentosRelacionados = models.ManyToManyField(atendimento)


	def __str__(self):
		return self.nome

	def setNome(self, nome1):
		self.nome = nome1
	def getNome(self):
		return self.nome

	def setCPF(self, cpf1):
		self.cpf = cpf1
	def getCPF(self):
		return self.cpf

	def setEndereco(self, end):
		self.endereco = end
	def getEndereco(self):
		return self.endereco

	





class reclamacao(models.Model):
	problemaEnfrentado = models.TextField()
	comentarioProblema = models.TextField()
	clienteReclamante = models.ForeignKey(User, on_delete = models.CASCADE, null=True)

	def setProblemaEnfrentado(self, prob):
		self.problemaEnfrentado = prob
	def getProblemaEnfrentado(self):
		return self.problemaEnfrentado

	def setComentarioProblema(self, com):
		self.comentarioProblema = com
	def getCometarioProblema(self):
		return self.comentarioProblema

	def __str__(self):
		return self.problemaEnfrentado



class Curso(models.Model):
	curso = models.TextField()
	def __str__(self):
		return self.curso



class Funcao(models.Model):
	funcao = models.TextField()
	def __str__(self):
		return self.funcao



class StatusArtigo(models.Model):
	status = models.TextField()
	def __str__(self):
		return self.status



class Evento(models.Model):
	nome_evento = models.TextField(default='')
	data_inicio = models.DateTimeField()
	data_fim = models.DateTimeField()
	qualis = models.TextField(default='')
	area = models.TextField(default='')
	local = models.TextField(default='')
	descricao = models.TextField(default='')

	def setLocal(self, local):
		self.local = local
	def getLocal(self):
		return self.local

	def setDescricao(self, descricao):
		self.descricao = descricao
	def getDescricao(self):
		return self.descricao

	def setNomeEvento(self, nome_evento):
		self.nome_evento = nome_evento
	def getNomeEvento(self):
		return self.nome_evento

	def setDataInicioEvento(self, data_inicio):
		self.data_inicio = data_inicio
	def getDataInicioEvento(self):
		return self.data_inicio

	def setDataFimEvento(self, data_fim):
		self.data_fim = data_fim
	def getDataFimEvento(self):
		return self.data_fim

	def setQualis(self, qualis):
		self.qualis = qualis
	def getQualis(self):
		return self.qualis

	def setArea(self, area):
		self.area = area
	def getArea(self):
		return self.area


	def __str__(self):
		return self.nome_evento



class Aluno(models.Model):
	#username = models.CharField(max_length=50,unique=True,null=True)
	#password = models.CharField(max_length=50,null=True)
	#user = models.OneToOneField(User, on_delete = models.CASCADE)
	#usuario_u = models.ForeignKey(User, on_delete = models.CASCADE, default=1)
	usuario = models.TextField(default='')
	senha = models.TextField(default='')
	matricula = models.TextField(default='')
	nome = models.CharField(max_length=50,null=True)
	cpf = models.IntegerField(null=True)
	#curso = models.ManyToManyField(Curso)
	#curso = models.ForeignKey(Curso, default=2, on_delete = models.CASCADE)
	curso = models.TextField(default='')
	#email = models.TextField()
	data_nascimento = models.TextField(max_length=20)
	#status = models.TextField()
	#funcao = models.ForeignKey(Funcao, default=2, on_delete = models.CASCADE)
	eventos_cadastrado = models.ManyToManyField(Evento)

	def setEventoCadastrado(self, eventos_cadastrado=''):
		self.eventos_cadastrado = eventos_cadastrado
	def getEventoCadastrado(self):
		return self.eventos_cadastrado


	def setCurso(self, curso):
		self.curso = curso
	def getCurso(self):
		return self.curso


	def setUsuario(self, usuario):
		self.usuario = usuario
	def getUsuario(self):
		return self.usuario

	def setSenha(self, senha):
		self.senha = senha
	def getSenha(senha):
		return self.senha


	def setMatricula(self, matricula):
		self.matricula = matricula
	def getMatricula(self):
		return self.matricula

	def setNome(self, nome):
		self.nome = nome
	def getNome(self):
		return self.nome

	def setCPF(self, cpf):
		self.cpf = cpf
	def getCPF(self):
		return self.cpf



	def setDataNascimento(self, data_nascimento):
		self.data_nascimento = data_nascimento
	def getDataNascimnto(self):
		return self.data_nascimento

	def setSenha(self, senha):
		self.senha = senha
	def getSenha(self):
		return self.senha


	def __str__(self):
		return self.nome



class Professor(models.Model):
	#username = models.CharField(max_length=50,unique=True,null=True)
	#password = models.CharField(max_length=50,null=True)
	#usuario = models.OneToOneField(User, on_delete = models.CASCADE)
	usuario = models.TextField(default='')
	senha = models.TextField(default='')
	matricula = models.TextField()
	nome = models.CharField(max_length=50,null=True)
	cpf = models.IntegerField(null=True)
	#curso = models.ManyToManyField(Curso)
	#curso = models.ForeignKey(Curso, default=2, on_delete = models.CASCADE)
	curso = models.TextField(default='')
	email = models.TextField()
	data_nascimento = models.TextField(max_length=20)
	#status = models.TextField()
	#funcao = models.ForeignKey(Funcao, default=2, on_delete = models.CASCADE)
	funcao = models.TextField(default='')

	def setEmail(self, email):
		self.email= email
	def getEmail(self):
		return self.email


	def setCurso(self, curso):
		self.curso = curso
	def getCurso(self):
		return self.curso


	def setFuncao(self, funcao):
		self.funcao = funcao
	def getFuncao(self):
		return self.funcao

	def setUsuario(self, usuario):
		self.usuario = usuario
	def getUsuario(self):
		return self.getUsuario

	def setSenha(self, senha):
		self.senha = senha
	def getSenha(senha):
		return self.senha


	def setMatricula(self, matricula):
		self.matricula = matricula
	def getMatricula(self):
		return self.matricula

	def setNome(self, nome):
		self.nome = nome
	def getNome(self):
		return self.nome

	def setCPF(self, cpf):
		self.cpf = cpf
	def getCPF(self):
		return self.cpf

	def setEmail(self, email):
		self.email = email
	def getEmail(self):
		return self.email

	def setDataNascimento(self, data_nascimento):
		self.data_nascimento = data_nascimento
	def getDataNascimnto(self):
		return self.data_nascimento



	def __str__(self):
		return self.nome



class horarios_laboratorio(models.Model):
	#aluno = models.ForeignKey(Aluno, on_delete = models.CASCADE)
	aluno = models.TextField(default='')
	hora_entrada = models.DateTimeField(default='')
	hora_saida = models.DateTimeField(default='')


	def setAluno(self, aluno=''):
		self.aluno = aluno

	def setHorarioEntrada(self, hora_entrada=''):
		self.hora_entrada = hora_entrada
	def setHorarioSaida(self, hora_saida=''):
		self.hora_saida = hora_saida



class Artigo(models.Model):
	autor = models.ForeignKey(Professor, default=2, on_delete=models.CASCADE)
	titulo = models.TextField(default='')
	coautor = models.TextField(default='')
	
	orientador = models.TextField(default='')
	status = models.ForeignKey(StatusArtigo, default=1, on_delete=models.CASCADE)
	#status = models.TextField(default='')

	def setAutor(self, autor):
		self.autor = autor
	def getAutor(self):
		return self.autor

	def setTitulo(self, titulo):
		self.titulo = titulo
	def getTitulo(self):
		return self.titulo

	def setCoautor(self, coautor):
		self.coautor = coautor
	def getCoautor(self):
		return self.coautor

	def setOrientador(self, orientador):
		self.orientador = orientador
	def getOrientador(self):
		return self.orientador

	def setStatus(self, status):
		self.status = status
	def getStatus(self):
		return self.status



	def __str__(self):
		return self.titulo



class Noticia(models.Model):
    autor = models.ForeignKey(Professor, default=1, on_delete = models.CASCADE)
    descricao = models.CharField(max_length=100, null=True)
    titulo = models.TextField()
    corpo = models.TextField()
    data_lancamento_noticia = models.DateTimeField(null=True)
    imagem = models.ImageField(upload_to='media')
    

    def setImagem(self, imagem=''):
        self.imagem = imagem

    def setTitulo(self, titulo=''):
        self.titulo = titulo
    def getTitulo(self):
        return self.titulo

    def setCorpo(self, corpo=''):
        self.corpo = corpo
    def getCorpo(self):
        return self.corpo

    def setDataLancamentoNoticia(self, data_lancamento_noticia=''):
        self.data_lancamento_noticia = data_lancamento_noticia
    def getDataLancamentoNoticia(self):
        return self.data_lancamento_noticia


    def __str__(self):
        return self.titulo



class Area(models.Model):
	area = models.TextField()

	def __str__(self):
		return self.area




