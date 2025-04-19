from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, Quarto

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'exemplo@email.com'})
    )
    telefone = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(99) 99999-9999'})
    )

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'telefone', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nome de usuário'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Senha'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirme a senha'})

class QuartoForm(forms.ModelForm):
    class Meta:
        model = Quarto
        fields = ['titulo', 'descricao', 'endereco', 'preco', 'imagem']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Quarto aconchegante com vista para o mar'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Descreva detalhes do quarto...'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Rua Exemplo, 123 - Cidade/Estado'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'imagem': forms.FileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'imagem': 'Foto do Quarto'
        }