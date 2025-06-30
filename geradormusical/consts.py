INSTRUMENTOS = {
    # Pianos
    'Piano': 0, 
    'Piano (som mais agudo)': 1 ,
    'Piano eléctro-acústico': 2 ,
    'Piano desafinado': 3, 
    'Piano eléctrico (tipo Fender Rhodes': 4,
    'Piano eléctrico (sintético, tipo DX7)': 5,
    'Cravo': 6,
    'Clavineta (um Clavicórdio elétrico)': 7,

    # Percussão cromática:

    'Celesta': 8,
    'Glockenspiel': 9,
    'Caixa de música': 10,
    'Vibrafone': 11,
    'Marimba': 12,
    'Xilofone': 13,
    'Carrilhão de orquestra': 14,
    'Dulcimer': 15,

    # Órgãos:

    'Órgão Hammond': 16,
    'Órgão percussivo': 17,
    'Órgão de rock': 18,
    'Órgão de tubos': 19,
    'Harmônio': 20,
    'Acordeão': 21,
    'Harmônica': 22,
    'Bandoneón': 23,

    # Guitarras:

    'Guitarra de cordas de nylon': 24,
    'Guitarra de cordas de aço': 25,
    'Guitarra semi-acústica': 26,
    'Guitarra elétrica': 27,
    'Guitarra abafada': 28,
    'Guitarra elétrica com saturação': 29,
    'Guitarra elétrica com distorção': 30,
    'Harmônicos': 31,

    # Baixos:

    'Contrabaixo (dedilhado)': 32,
    'Baixo elétrico dedilhado': 33,
    'Baixo elétrico beliscado com palheta': 34,
    'Baixo elétrico sem trastos': 35,
    'Baixo elétrico percutido 1 (pop)': 36,
    'Baixo elétrico percutido 2 (thump)': 37,
    'Baixo sintético 1 (analógico)': 38,
    'Baixo sintético 2 (digital)': 39,

    # Cordas:

    'Violino': 40,
    'Viola': 41,
    'Violoncelo': 42,
    'Contrabaixo': 43,
    'Cordas em trêmulo': 44,
    'Cordas em pizzicatto': 45,
    'Harpa': 46,
    'Tímpanos': 47,

    # Orquestra sinf�nica:

    'Orquestra de cordas 1': 48,
    'Orquestra de cordas 2': 49,
    'Cordas sintéticas 1': 50,
    'Cordas sintéticas 2': 51,
    'Coro': 52,
    'Voz humana (solista)': 53,
    'Voz humana (sintética)': 54,
    'Batida orquestral': 55,

    # Metais:

    'Trompete': 56,
    'Trombone': 57,
    'Tuba': 58,
    'Trompete com surdina': 59,
    'Trompa': 60,
    'Metais': 61,
    'Metais sintéticos 1': 62,
    'Metais sintéticos 2': 63,

    # Palhetas:

    'Saxofone soprano': 64,
    'Saxofone alto': 65,
    'Saxofone tenor': 66,
    'Saxofone barítono': 67,
    'Oboé': 68,
    'Corne inglês': 69,
    'Fagote': 70,
    'Clarinete': 71,

    # Flautas:

    'Flautim': 72,
    'Flauta transversal': 73,
    'Flauta de bisel': 74,
    'Flauta de Pâ': 75,
    'Sopro em gargalo de garrafa': 76,
    'Shakuhachi': 77,
    'Assobio': 78,
    'Ocarina': 79,

    # Solos sint�ticos:

    'Onda quadrada': 80,
    'Onda dente de serra': 81,
    'Calliope': 82,
    'Chiff Lead': 83,
    'Charango sintético': 84,
    'Solo vox': 85,
    'Onda dente de serra em quintas paralelas': 86,
    'Baixo e solo': 87,

    # Fundos sint�ticos:

    'Fundo New Age': 88,
    'Fundo morno': 89,
    'Polysynth': 90,
    'Space voice': 91,
    'Vidro friccionado': 92,
    'Fundo metálico': 93,
    'Fundo halo': 94,
    'Fundo com abertura do filtro': 95,

    # Efeitos sonoros sintéticos:

    'Chuva de gelo': 96,
    'Trilha sonora': 97,
    'Cristal': 98,
    'Atmosfera': 99,
    'Brilhos': 100,
    'Goblins': 101,
    'Ecos': 102,
    'Ficção científica': 103,

    # Instrumentos étnicos:

    'Sitar': 104,
    'Banjo': 105,
    'Shamisen': 106,
    'Koto': 107,
    'Kalimba': 108,
    'Gaita de foles': 109,
    'Rabeca': 110,
    'Shehnai': 111,

    # Percussão não-cromática:

    'Sino': 112,
    'Agogô': 113,
    'Tambor de aço': 114,
    'Bloco de madeira': 115,
    'Taiko': 116,
    'Timbalões acústicos': 117,
    'Timbalões sintéticos': 118,
    'Prato revertido': 119,

    # Efeitos sonoros:

    'Corda de violão riscada': 120,
    'Respiração': 121,
    'Ondas do mar': 122,
    'Pássaro piando': 123,
    'Telefone tocando': 124,
    'Helicóptero': 125,
    'Aplausos': 126,
    'Tiro (arma de fogo)': 127,
}

OITAVAS = {
    'Oitava C-1': 0,
    'Oitava C0': 12,
    'Oitava C1': 24,
    'Oitava C2': 36,
    'Oitava C3': 48,
    'Oitava C4': 60,
    'Oitava C5': 72,
    'Oitava C6': 84,
    'Oitava C7': 96,
    'Oitava C8': 108,
}

NOTAS = {
    'C': 0,
    'D': 2,
    'E': 4,
    'F': 5,
    'G': 7,
    'A': 9,
    'B': 11,
}

TOM_MAXIMO = 127 

DEFAULT_DURATION = 1
DEFAULT_NUM_TRACKS = 1
DEFAULT_CHANNEL = 0
DEFAULT_TRACK = 0
DEFAULT_VOLUME = 5
DEFAULT_BPM = 120

BPM_MIN = 1
BPM_MAX = 200

VOLUME_MIN = 0
VOLUME_MAX = 100

TEXT_MAX_LENGTH = 1000
TEXT_MIN_LENGTH = 1

VOLUME_DELTA = 2
OCTAVE_DELTA = 12
BPM_DELTA = 80

AUDIO_PATH = "geradormusical/static/geradormusical/audio/musica_gerada.mid"