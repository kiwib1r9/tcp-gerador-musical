from django import forms
from .consts import OITAVAS
from .consts import INSTRUMENTOS

INSTRUMENTOS_CHOICES = [(codigo, nome) for nome, codigo in INSTRUMENTOS.items()]
OITAVAS_CHOICES = [(valor, nome) for nome, valor in OITAVAS.items()]

class GerarMusicaForm(forms.Form):
    BPM_CHOICES = [(i, str(i)) for i in range(1, 201)]
    bpm = forms.IntegerField(initial=120, required=False, label='BPM')
    instrumento = forms.TypedChoiceField(choices=INSTRUMENTOS_CHOICES, coerce=int, label='Instrumento inicial')
    oitava = forms.TypedChoiceField(choices=OITAVAS_CHOICES, coerce=int, label='Oitava')
    volume = forms.IntegerField(min_value=0, max_value=100, initial=5, label='Volume',
            widget=forms.NumberInput(attrs={
            'type': 'range',
            'id': 'volume-slider',
            'class': 'input-volume',  
        }))
    texto = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'rows': 8, 'cols': 60, 'maxlength': '1000', 'style': 'resize: none;'}),
        label='Insira aqui seu texto',
        max_length=1000,
    )

