from midiutil import MIDIFile
from ..consts import *
from .Tom import Tom
from .Instrumento import Instrumento
from midi2audio import FluidSynth
import random

class GeradorMusical:
    def __init__(self):
        self.text = ''
        self.midi = MIDIFile(DEFAULT_NUM_TRACKS)
        self.bpm = DEFAULT_BPM
        self.volume = DEFAULT_VOLUME
        self.tom = Tom()  # default
        self.default_volume = DEFAULT_VOLUME
        self.oitava = OITAVAS['Oitava C-1']     #default
        self.instrumento = Instrumento()

    def configura(self, texto, bpm, oitava, volume, valor_instrumento):
        self.set_texto(texto)
        self.set_bpm(bpm)
        self.set_oitava(oitava)
        self.set_volume(volume)
        self.set_default_volume()
        self.instrumento.set_codigo(valor_instrumento)

    def set_texto(self, texto):
        if isinstance(texto, str) and TEXT_MIN_LENGTH <= len(texto) <= TEXT_MAX_LENGTH:
            self.texto = texto
        else:
            raise ValueError("Texto deve ter de 1 até 1000 caracteres.")
    
    def set_bpm(self, bpm):
        if (isinstance(bpm, int) and BPM_MIN <= bpm <= BPM_MAX):
            self.bpm = bpm
        else:
            raise ValueError("BPM deve ser um número inteiro entre 1 e 200.")

    def set_oitava(self, oitava):
        if isinstance(oitava, int) and oitava in OITAVAS.values():
            self.oitava = oitava
        else:
            raise ValueError("Oitava deve ser um valor válido.")

    def set_volume(self, volume):
        if isinstance(volume, int) and VOLUME_MIN <= volume <= VOLUME_MAX:
            self.volume = volume
        else:
            raise ValueError("Volume deve ser um número inteiro entre 0 e 100.")
    
    def set_default_volume(self):
        self.default_volume = self.volume
        
    def inicializa_MIDI(self):
        self.midi.addTempo(DEFAULT_TRACK, DEFAULT_CHANNEL, self.bpm)
        self.midi.addProgramChange(DEFAULT_TRACK, DEFAULT_CHANNEL, 0, self.instrumento.codigo)

    # ---------------------------------------------------------------------------
   
    def dobra_volume(self):
        self.volume = min(self.volume * VOLUME_DELTA, VOLUME_MAX)

    def restaura_volume(self):
        self.volume = self.default_volume

    def sobe_oitava(self):
       self.oitava = min(self.oitava + OCTAVE_DELTA, OITAVAS['Oitava C8'])

    def desce_oitava(self):
        self.oitava = max(self.oitava - OCTAVE_DELTA, OITAVAS['Oitava C-1'])

    def sobe_bpm(self):
        self.bpm = min(self.bpm + BPM_DELTA, BPM_MAX)

    def set_bpm_aleatorio(self):
        self.set_bpm (random.randint(BPM_MIN, BPM_MAX))



    def gera_MIDI(self):
        self.inicializa_MIDI()
        tempo_atual = 0
        bpm_atual = self.bpm
        oitava_atual = self.oitava
        volume_atual = self.volume
        volume_inicial = self.volume
        instrumento_atual = self.instrumento
        tom_anterior = None
        texto = self.texto

        for posicao, caractere in enumerate(texto):
            tom_atual = None

            if caractere.upper() in NOTAS and texto[posicao:posicao+4] != "BPM+":
                nota = NOTAS[caractere.upper()]
                tom_atual = Tom()
                tom_atual.set_nota(nota)
                tom_atual.set_oitava(oitava_atual)
                self.midi.addNote(DEFAULT_TRACK, DEFAULT_CHANNEL,
                                tom_atual.obter_valor_midi(), tempo_atual, DEFAULT_DURATION, volume_atual)
                tempo_atual += 1

            elif caractere == " ":
                tempo_atual += 1

            elif caractere == "+":
                if posicao >= 3 and texto[posicao-3:posicao+1] == "BPM+":
                    bpm_atual = min(bpm_atual + BPM_DELTA, BPM_MAX)
                    self.midi.addTempo(DEFAULT_TRACK, tempo_atual, bpm_atual)
                elif posicao >= 1 and texto[posicao-1] == 'R':
                    oitava_atual = min(oitava_atual + 12, OITAVAS['Oitava C8'])
                else:
                    volume_atual = min(volume_atual * VOLUME_DELTA, VOLUME_MAX)

            elif caractere == "-":
                if posicao >= 1 and texto[posicao-1] == 'R':
                    oitava_atual = max(oitava_atual - 12, OITAVAS['Oitava C-1'])
                else:
                    volume_atual = volume_inicial

            elif caractere in "OoIiUu":
                if tom_anterior is not None:
                    self.midi.addNote(DEFAULT_TRACK, DEFAULT_CHANNEL,
                                    tom_anterior.obter_valor_midi(), tempo_atual, DEFAULT_DURATION, volume_atual)
                    tempo_atual += 1
                else:
                    self.midi.addProgramChange(DEFAULT_TRACK, DEFAULT_CHANNEL, tempo_atual,
                                            INSTRUMENTOS['Telefone tocando'])
                    self.midi.addNote(DEFAULT_TRACK, DEFAULT_CHANNEL,
                                    NOTAS['A'] + oitava_atual, tempo_atual, DEFAULT_DURATION, volume_atual)
                    tempo_atual += 1
                    self.midi.addProgramChange(DEFAULT_TRACK, DEFAULT_CHANNEL, tempo_atual, instrumento_atual.codigo)

            elif caractere == '?':
                nota_aleatoria = random.choice(list(NOTAS.values()))
                self.midi.addNote(DEFAULT_TRACK, DEFAULT_CHANNEL,
                                nota_aleatoria + oitava_atual, tempo_atual, DEFAULT_DURATION, volume_atual)

            elif caractere == '\n':
                instrumento_atual.trocar()
                self.midi.addProgramChange(DEFAULT_TRACK, DEFAULT_CHANNEL, tempo_atual, instrumento_atual.codigo)

            elif caractere == ';':
                bpm_aleatorio = random.randint(BPM_MIN, BPM_MAX)
                self.midi.addTempo(DEFAULT_TRACK, tempo_atual, bpm_aleatorio)

            tom_anterior = tom_atual

        return self.salvar_arquivo()
    
    def midi_to_MP3(self):
        fs = FluidSynth()
        fs.midi_to_audio(AUDIO_PATH, AUDIO_PATH.replace('.mid', '.mp3'))
        return AUDIO_PATH.replace('.mid', '.mp3')

    def salvar_arquivo(self):
        with open(AUDIO_PATH, "wb") as f:
            self.midi.writeFile(f)
        return AUDIO_PATH
