from django import forms
from django.contrib.auth.models import User
from .models import Curso, Funcao, StatusArtigo, Artigo, Noticia, Evento, Area
from django.contrib.auth.forms import UserCreationForm, UserChangeForm 





class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',

            )




    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

'''
class ProfileForm(forms.ModelForm):
    habilidades = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Pessoa.objects.all())
    biografia = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Pessoa
        fields = ('user',
                  'cpf',
                  'tipo_usuario',
                  'telefone',
                  'endereco', 
                  'data_nascimento',  
                  'eventos_cadastrado'
                  )
        
class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email',
                  'first_name',
                  'last_name',
                  'password'
                  )

'''