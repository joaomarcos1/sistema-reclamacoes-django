from django.conf.urls import url
#from django.conf import admin
#from django.conf.urls.static import static
#from django.conf import settings


from . import views

#from django.contrib.auth.views import login

urlpatterns = [
    url(r'^$', views.index, name='index.html'),
	url(r'^index$', views.index, name='index.html'),
	url(r'^login$', views.login_user, name='login.html'),
	url(r'^cadastro_reclamacao/(?P<id>\d+)/$', views.cadastro_reclamacao, name='cadastro_reclamacao.html'),
	url(r'^cadastro_evento$', views.cadastro_evento, name='cadastro_eventos.html'),
	url(r'^logout$', views.logout, name='logout'),
	url(r'^interface_usuario$', views.interface_usuario, name='interface_usuario.html'),
	url(r'^cadastro_usuario$', views.cadastro_usuario, name='cadastro_usuario.html'),
	url(r'^cadastro_noticias$', views.cadastro_noticias, name='cadastro_noticias.html'),
	url(r'^noticia/(?P<id>\d+)/$', views.noticia, name='noticia'),
	url(r'^cadastro_aluno$', views.cadastro_aluno, name='cadastro_aluno.html'),
	url(r'^cadastro_professor$', views.cadastro_professor, name='cadastro_professor.html'),
	url(r'^interface_professor/(?P<id>\d+)/$', views.interface_professor, name='interface_professor.html'),
	url(r'^artigos$', views.artigos, name='artigos.html'),
	url(r'^eventos$', views.eventos, name='eventos.html'),
	url(r'^cadastro_em_evento/(?P<id>\d+)/$', views.cadastro_em_evento, name='cadastro_em_evento.html'),
	url(r'^entrada_saida_laboratorio', views.entrada_saida_laboratorio, name='entrada_saida_laboratorio.html'),
	url(r'^sobre$', views.sobre, name='sobre.html'),
	url(r'^entradas_alunos$', views.entradas_alunos, name='entradas_alunos.html'),
	url(r'^editar_perfil_alunos/(?P<id>\d+)/', views.editar_perfil_alunos, name='editar_perfil_aluno.html'),
	url(r'^interface_atendente/', views.interface_atendente, name='interface_atendente.html'),
	url(r'^edicao_atendimento/(?P<id>\d+)/', views.edicao_atendimento, name='edicao_atendimento.html'),
	url(r'^cadastro_tecnico_campo/', views.cadastro_tecnico_campo, name='cadastro_tecnico_campo.html'),
	url(r'^edicao_tecnico_campo/(?P<id>\d+)/', views.edicao_tecnico_campo, name='edicao_tecnico_campo.html'),
	url(r'^cadastro_atendimento/', views.cadastro_atendimento, name='cadastro_atendimento.html'),
	url(r'^cadastro_atendente/', views.cadastro_atendente, name='cadastro_atendente.html')
]