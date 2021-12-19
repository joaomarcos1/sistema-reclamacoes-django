from django.contrib import admin

# Register your models here.
from .models import reclamacao, situacaoAtendimento, atendente, Cliente, Tecnico_Campo, atendimento


admin.site.register(reclamacao)
#admin.site.register(situacaoAtendimento)
admin.site.register(atendente)
admin.site.register(Cliente)
admin.site.register(Tecnico_Campo)
admin.site.register(atendimento)