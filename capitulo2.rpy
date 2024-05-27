include "recursos.rpy"
define fade_in = Fade(0.5, 0.3, 0.5)
define fade_out = Fade(0.0, 0.0, 0.4)
label capitulo2:

    scene QUARTO_DIA
    centered "{size=45} {color=#FF7350D3}{b}Bem vindo ao capitulo 2{/size} {/color} {/b}" with fade_in
    narrador "{b}{size=30 } {color=#8731B9} Nível de afeto com Leopold: [amizade_leopold]{/size} {/color} {/b}" 

    show LALITHA_CHORANDO
    with dissolve
    narrador "O relógio marcava 7:00am e você acaba de acordar para ir à escola"
    # aqui da pra por o som de um despertador
    lalitha "Aff odeio acordar cedo.."
    show LALITHA_PERDIDA
    with dissolve
    if amizade_leopold > 20:
        lalitha "Será que verei Leopold hoje?..."
        lalitha "Acho melhor me arrumar logo se não me atraso para aula"
        jump conhecendo_escola
    else:
        lalitha "Um novo dia, novas responsabilidades! Quem sabe uma amizade nova..."
        lalitha "Acho melhor me arrumar logo se não me atraso para aula"
        jump conhecendo_escola

label conhecendo_escola:
    scene ESCOLA_DIA_PORTAO with fade_in
    #  som de pessoas conversando
    show LALITHA_PERDIDA with dissolve
    lalitha "uau quanta gente..."

    scene SALA_DE_AULA_ESCURA
    with fade_in
    # som sala de aula
    narrador "Diferente da sua antiga escola, as pessoas da nova cidade costumavam falar alto."
    narrador "Você não soube muito bem como se enturmar, então ficou na sua."
    if amizade_leopold > 0:
        lalitha normal "Gostaria de ver meu amigo Leopold agora..."
        with dissolve
        
    else:
        lalitha normal "Assim que o intervalo chegar, vou procurar um lugar calmo para me acalmar."
        with dissolve
        jump laurence_no_terraco

label laurence_no_terraco:
    scene SACADA_ESCOLA with fade_in
    show LALITHA_NORMAL with dissolve
    lalitha "Aqui parece um bom lugar para ficar, adoro pegar um solzinho!"