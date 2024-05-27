define lalitha = Character("Lalitha", image = "lali")
define leopold = Character("Leopold")
define narrador = Character("Narrador")

image side lali normal = im.Scale("Lalitha/LalithaNormal.png",150, 325, xoffset=0, yoffset=100)
# personagens
image LALITHA_FELIZ = "Lalitha/LalithaSorrisoSemDente.png"
image LALITHA_NORMAL = "Lalitha/LalithaNormal.png"
image LALITHA_SORRINDO = "Lalitha/LalithaSorrisoSemDente.png" 
image LALITHA_PERDIDA = "Lalitha/LalithaPerdida.png"
image LALITHA_SEM_GRACA = "Lalitha/LalithaSemGraca.png"
image LALITHA_CHORANDO = "Lalitha/LalithaTristeChorando.png"

image LEOPOLD_NORMAL = "Masculinos/LeopoldNormal.png"
image LEOPOLD_OLHO_FECHADO = "Masculinos/LeopoldOlhoFechado.png"
image LEOPOLD_OLHO_GRANDE = "Masculinos/LeopoldComOlhoGrande.png"
image LEOPOLD_SEXY = "Masculinos/LeopoldSexy.png"

# backgrounds
image ESQUINA_DE_CASA = "vizinhancaDia.jpg"
image RUA_DE_CASA = "RuaParaCasaDia.jpg"
image PARQUE_DIA = "parqueDia.jpg"
image VISTA_DE_CASA = "esquinhaCasaDia.jpg"
image SALA_CASA = "salaCasa.jpg"
image COZINHA = "cozinhaCasa.jpg"
image QUARTO_NOITE = "QuartoLalithaNoite.jpg"
image QUARTO_DIA = "QuartoLalithaDia.jpg"
image LOJINHA_DIA = "LojinhaDia.jpg"
image ESCOLA_DIA_PORTAO = "escolaDia.jpg"
image SALA_DE_AULA_ESCURA = "salaDeAulaNoite.jpg"
image SACADA_ESCOLA = "VistaCidadeDia.jpg"

init python:
    style.custom_text.color = "#ff8080"
    style.custom_text.bold = True
    style.custom_text.size = 40