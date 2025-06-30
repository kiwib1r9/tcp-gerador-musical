from django import forms
from .consts import OITAVAS
from .consts import INSTRUMENTOS
from .consts import DEFAULT_VOLUME, VOLUME_MIN, VOLUME_MAX
from .consts import DEFAULT_BPM
from .consts import DEFAULT_OITAVA

INSTRUMENTOS_CHOICES = [(codigo, nome) for nome, codigo in INSTRUMENTOS.items()]
OITAVAS_CHOICES = [(valor, nome) for nome, valor in OITAVAS.items()]

class GerarMusicaForm(forms.Form):
    BPM_CHOICES = [(i, str(i)) for i in range(1, 201)]
    bpm = forms.IntegerField(initial=DEFAULT_BPM, required=False, label='BPM')
    instrumento = forms.TypedChoiceField(choices=INSTRUMENTOS_CHOICES, coerce=int, label='Instrumento inicial')
    oitava = forms.TypedChoiceField(choices=OITAVAS_CHOICES, initial=OITAVAS[DEFAULT_OITAVA], coerce=int, label='Oitava')
    volume = forms.IntegerField(min_value=VOLUME_MIN, max_value=VOLUME_MAX, initial=DEFAULT_VOLUME, label='Volume',
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

