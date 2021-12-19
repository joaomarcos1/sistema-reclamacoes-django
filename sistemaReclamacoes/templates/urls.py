from django.conf.urls import url

from . import views

#from django.contrib.auth.views import login

urlpatterns = [
    url(r'^$', views.index, name='index.html'),
	url(r'^index$', views.index, name='index.html'),
	url(r'^login$', views.login_user, name='login.html'),
	url(r'^cadastro_artigo$', views.cadastro_artigo, name='cadastro_artigo.html'),
	url(r'^cadastro_evento$', views.cadastro_evento, name='cadastro_eventos.html'),
	url(r'^logout$', views.logout, name='logout'),
	url(r'^interface_usuario$', views.interface_usuario, name='interface_usuario.html'),
	url(r'^cadastro_usuario$', views.cadastro_usuario, name='cadastro_usuario.html'),
	url(r'^cadastro_noticias$', views.cadastro_noticias, name='cadastro_noticias.html'),
	url(r'^noticia/(?P<id>\d+)/$', views.noticia, name='noticia'),
	url(r'^cadastro_aluno$', views.cadastro_aluno, name='cadastro_aluno.html'),
	url(r'^cadastro_professor$', views.cadastro_professor, name='cadastro_professor.html'),
	url(r'^interface_professor/(?P<id>\d+)/$', views.interface_professor, name='interface_professor.html')
]