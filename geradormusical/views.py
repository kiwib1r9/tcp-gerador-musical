from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from .forms import GerarMusicaForm
from django.urls import reverse_lazy
from .classes.GeradorMusical import GeradorMusical
from django.contrib import messages

class TelaDeEntrada(FormView):
    template_name = 'geradormusical/entrada.html'
    form_class = GerarMusicaForm
    success_url = reverse_lazy('TelaDeReproducao') 

    def form_valid(self, form):
        try:
            gerador_musical = GeradorMusical()
            gerador_musical.configura(
                form.cleaned_data['texto'],
                form.cleaned_data['bpm'],
                form.cleaned_data['oitava'],
                form.cleaned_data['volume'],
                form.cleaned_data['instrumento']
            )
            midi_path = gerador_musical.gera_MIDI()
            mp3_path = gerador_musical.midi_to_MP3()
            self.request.session['mp3_path'] = mp3_path
            self.request.session['midi_path'] = midi_path
        except ValueError as e:
            messages.error(self.request, f"Erro: {str(e)}")
            return self.form_invalid(form)

        return super().form_valid(form)


class TelaDeReproducao(TemplateView):
    template_name = "geradormusical/saida.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        midi_path = self.request.session.get('midi_path')
        mp3_path = self.request.session.get('mp3_path')
        if midi_path:
            context['midi_path'] = midi_path
        else:
            context['error_midi'] = "Nenhum arquivo MIDI gerado. Por favor, tente novamente."
        if mp3_path:
            context['mp3_path'] = mp3_path
        else:
            context['error_mp3'] = "Nenhum arquivo MP3 gerado. Por favor, tente novamente."
        return context


