from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, Quarto 

class UserRegistrationForm(UserCreationForm):
    USER_TYPE_CHOICES = [
        ('Locador', 'Sou Proprietário'),
        ('Locatario', 'Sou Estudante'),
    ]
    
    user_type = forms.ChoiceField(
        label="Tipo de Conta",
        choices=USER_TYPE_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
        initial='Locatario'
    )
    
    faculdade = forms.CharField(
        label='Faculdade/Universidade',
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    curso = forms.CharField(
        label='Curso',
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    matricula = forms.CharField(
        label='Número de Matrícula',
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Usuario
        fields = [
            'username', 'email', 'telefone', 'user_type',
            'faculdade', 'curso', 'matricula', 'password1', 'password2'
        ]
    
    def clean(self):
        cleaned_data = super().clean()
        user_type = cleaned_data.get('user_type')
        
        if user_type == 'Locatario':
            campos_obrigatorios = {
                'faculdade': 'Informe sua faculdade',
                'curso': 'Informe seu curso',
                'matricula': 'Informe sua matrícula'
            }
            
            for campo, mensagem in campos_obrigatorios.items():
                if not cleaned_data.get(campo):
                    self.add_error(campo, mensagem)
        return cleaned_data
    
class QuartoForm(forms.ModelForm):
    class Meta:
        model = Quarto
        fields = ['titulo', 'descricao', 'endereco', 'preco', 'imagem', 'data_disponivel']
        
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Descreva detalhes do quarto...'
            }),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control'}),
            'imagem': forms.FileInput(attrs={'class': 'form-control'}),
            'data_disponivel': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            })
        }
        
        labels = {
            'data_disponivel': 'Data Disponível',
            'imagem': 'Foto do Quarto'
        }
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'email', 'telefone', 'foto', 'faculdade', 'curso', 'matricula']
        widgets = {
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'faculdade': forms.TextInput(attrs={'class': 'form-control'}),
            'curso': forms.TextInput(attrs={'class': 'form-control'}),
            'matricula': forms.TextInput(attrs={'class': 'form-control'}),
        }