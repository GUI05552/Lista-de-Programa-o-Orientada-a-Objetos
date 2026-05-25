from video import Video
from podcast import Podcast
from texto_narrado import TextoNarrado
from plataforma import Plataforma

plataforma = Plataforma("EducaTech")

video = Video("Python Básico", "20 min", "1080p")
podcast = Podcast("Tecnologia Hoje", "35 min", "Carlos")
texto = TextoNarrado("História da Computação", "15 min", "Português")

plataforma.adicionar_midia(video)
plataforma.adicionar_midia(podcast)
plataforma.adicionar_midia(texto)

plataforma.listar_midias()

print("\nReproduzindo todas as mídias:\n")

plataforma.reproduzir_todas()