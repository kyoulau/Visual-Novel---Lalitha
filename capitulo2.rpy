include "recursos.rpy"
default amizade_laurence = 0
define fade_in = Fade(0.5, 0.3, 0.5)
define fade_out = Fade(0.0, 0.0, 0.4)

label capitulo2:

    scene QUARTO_DIA
    centered "{size=45} {color=#FF7350D3}{b}Bem vindo ao capitulo 2{/size} {/color} {/b}" with fade_in
    narrador "{b}{size=30 } {color=#8731B9} Nível de afeto com Leopold: [amizade_leopold]{/size} {/color} {/b}" 

    show LALITHA_CHORANDO
    with dissolve
    narrador "O relógio marcava 7:00am e você acaba de acordar para ir à escola"

    play sound "audio/alarme.mp3" volume 0.5
    $ renpy.pause(2.0)
    stop sound

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
    play sound "audio/pessoasFalando.mp3" volume 0.25
    $ renpy.pause(2.0)
    show LALITHA_PERDIDA with dissolve
    lalitha "uau quanta gente..."
    stop sound
    scene SALA_DE_AULA_ESCURA
    with fade_in
    play sound "audio/pessoasFalando.mp3" volume 0.25
    narrador "Diferente da sua antiga escola, as pessoas da nova cidade costumavam falar alto."
    narrador "Você não soube muito bem como se enturmar, então ficou na sua."
    if amizade_leopold > 0:
        lalitha normal "Gostaria de ver meu amigo Leopold agora..."
        with dissolve
        jump fuga_de_lalitha
    else:
        lalitha normal "Assim que o intervalo chegar, vou procurar um lugar calmo para me acalmar."
        with dissolve
        jump laurence_no_terraco
    stop sound

label fuga_de_lalitha:
    if amizade_leopold > 30:
        scene SALA_DE_AULA_ESCURA with fade_in
        show LALITHA_CHORANDO with dissolve
        narrador "As horas vão passando e você vai para o intervalo pensando no seu amor Leopold.."
        play sound "audio/alarmeEscola.mp3" volume 0.5
        $ renpy.pause(2.0)
        stop sound
        narrador "Na fulga, acaba indo para  o teraço onde fica sozinha"
        jump lalitha_terraco_conheceu_leopold
    else:
        scene SALA_DE_AULA_ESCURA with fade_in
        show LALITHA_PERDIDA with dissolve
        lalitha "Será que o Leopold estuda por aqui? Impossível."
        play sound "audio/alarmeEscola.mp3" volume 0.5
        $ renpy.pause(2.0)
        stop sound
        narrador "Na fulga, acaba indo para  o teraço onde fica sozinha"
        jump lalitha_terraco_conheceu_leopold

label lalitha_terraco_conheceu_leopold:
    scene SACADA_ESCOLA with fade_in
    lalitha "Aqui parece um bom lugar para ficar, calmo e tranquilo!"
    show LAURENCE_OLHO_GRANDE:
        zoom 0.4
    with dissolve
    narrador "Um garoto cabeludo meio estranho aparece."
    laurence "Oh! eu pensei que eu era o único que conhecia esse lugar"
    menu:
        "Ignorar.":
            centered "{=custom_text}Você ganhou +0 pontos com Laurece!"
            jump leopold_puxa_assunto_com_lali
        "Que isso, pode ficar a vontade.":
            centered "{=custom_text}Você ganhou +5 pontos com Laurece!"
            jump dialogo_lalitha_laurence

label leopold_puxa_assunto_com_lali:
    scene SACADA_ESCOLA with fade_in
    narrador "Você apenas olhou o garoto de canto sem falar nada."
    lalitha normal "..."
    show LAURENCE_NORMAL:
        zoom 0.4
    with dissolve
    laurence "O que você ta fazendo aqui sozinha ?"
    menu:
        "Vim relaxar.":
            centered "{=custom_text}Você ganhou +10 pontos com Laurece!"
            $ amizade_laurence += 10
            jump dialogo_lalitha_laurence

        "Vim refletir sobre alguém.":
            centered "{=custom_text}Você ganhou +5 pontos com Laurece!"
            $ amizade_laurence += 5
            jump dialogo_lalitha_apaixonada_laurence

label dialogo_lalitha_laurence:
    scene SACADA_ESCOLA with fade_in
    show LAURENCE_OLHO_FECHADO:
        zoom 0.4
    with dissolve
    laurence "Poxa você parece bem chateda logo no primeiro dia de aula."
    laurence "Eu me chamo Laurence, e você?"
    lalitha normal "Lalitha!"
    show LAURENCE_NORMAL:
        zoom 0.4
    with dissolve
    laurence "Ano passado, no segundo ano eu e meus parças costumavamos vir aqui para jogar bola."
    laurence "Mas eles mudaram de escola esse ano, então eu sigo como Lobo Solitário, venho aqui para escutar música sozinho."
    lalitha normal "Aqui é bacana mesmo..."
    hide LAURENCE_NORMAL with dissolve
    show LAURENCE_OLHO_FECHADO:
        zoom 0.4
    with dissolve
    lalitha normal "O que você escuta ?"
    laurence "Gosto bastante de Rock and Roll, e você ?"
    show LAURENCE_NORMAL:
        zoom 0.4
    with dissolve
    lalitha normal "Legal, nunca escutei muitos.."
    laurence "Posso compartilhar minha música com você se quiser, depois você diz o que achou!"
    menu:
        "Pode ser... (meio suspeito)":
            centered "{=custom_text}Você ganhou +5 pontos com Laurece!"
            $ amizade_laurence += 5
            jump escutando_musica_juntos
        "Só uma música se não a aula ja volta e eu perco o horário!":
            centered "{=custom_text}Você ganhou +10 pontos com Laurece!"
            laurence "HAHA relaxa, você vai curtir!"
            $ amizade_laurence += 10
            jump escutando_musica_juntos

label dialogo_lalitha_apaixonada_laurence:
    scene SACADA_ESCOLA with fade_in
    show LAURENCE_NORMAL:
            zoom 0.4
    with dissolve
    laurence "Refletir sobre alguém?? Você ta gostando de alguém??"
    narrador "O garoto foi um pouco invasivo, e você não estava afim de ficar se expondo daquela maneira."
    lalitha normal "Ah deixa pra lá.."
    lalitha normal "Meu nome é Lalitha"
    show LAURENCE_OLHO_FECHADO:
        zoom 0.4
    with dissolve
    laurence "O meu é Laurence"
    hide LAURENCE_OLHO_FECHADO with dissolve
    laurence "Ano passado, no segundo ano eu e meus parças costumavamos vir aqui para jogar bola."
    laurence "Mas eles mudaram de escola esse ano, então eu sigo como Lobo Solitário, venho aqui para escutar música sozinho."
    lalitha normal "Aqui é bacana mesmo..."
    show LAURENCE_SEXY:
        zoom 0.4
    laurence "Se quiser podemos escutar um som dahora agora."
    laurence "Você é do rock??"
    menu: 
        "Nâo :()":
            centered "{=custom_text}Você não ganhou pontos com Laurece!"
            $ amizade_laurence += 0
        "Sim!":
            centered "{=custom_text}Você ganhou +5 pontos com Laurece!"
            $ amizade_laurence += 5
    show LAURENCE_NORMAL:
        zoom 0.4
    with dissolve
    laurence "Vou te mostrar um som bem dahora então."
    jump escutando_musica_juntos

label laurence_no_terraco:
    scene SACADA_ESCOLA with fade_in
    show LALITHA_NORMAL with dissolve
    lalitha "Aqui parece um bom lugar para ficar, adoro pegar um solzinho!"
    show LALITHA_SORRINDO with dissolve
    narrador "Você aproveitou seus momentos de paz sozinha até ver que não estava sozinha."
    hide LALITHA_SORRINDO with dissolve
    show LAURENCE_NORMAL:
        zoom 0.4
    with dissolve

    laurence "..."
    menu:
        "Falar com Laurence":
            centered "{=custom_text}Você ganhou +10 pontos com Laurece!"
            $ amizade_laurence += 10
            jump conhecer_laurence
        "Ficar na minha":
            centered "{=custom_text}Você não ganhou nenhum ponto com Laurece :( )"
            jump laurence_fala_com_lalitha

label conhecer_laurence:
    scene SACADA_ESCOLA with fade_in
    show LAURENCE_NORMAL:
        zoom 0.4
    with dissolve
    lalitha normal "EI! O VOCÊ FAZ AQUI????"

    show LAURENCE_OLHO_FECHADO:
        zoom 0.4
    with dissolve
    laurence "Ei! Calma, eu gosto daqui porque é silencioso..."
    hide LAURENCE_OLHO_FECHADO with dissolve
    show LAURENCE_NORMAL:
        zoom 0.4
    with dissolve
    laurence "Ano passado, no segundo ano eu e meus parças costumavamos vir aqui para jogar bola."
    laurence "Mas eles mudaram de escola esse ano, então eu sigo como Lobo Solitário, venho aqui para escutar música sozinho."
    lalitha normal "Aqui é bacana mesmo..."

    laurence "O meu nome é Laurece"

    lalitha normal "O meu é Lalitha!"

    laurence "Nome bacana..."
    show LAURENCE_OLHO_FECHADO:
        zoom 0.4
    with dissolve
    laurence "HMmmm.. Você gostaria de ouvir música comigo? Já que estamos aqui"

    lalitha normal "Eu adoro ouvir música!"

    hide LAURENCE_OLHO_FECHADO with dissolve
    show LAURENCE_NORMAL:
        zoom 0.4
    with dissolve

    laurence "Legal!! Qual seu gênero musical favorito ?"
    menu:
        "Dizer que gosta de Rock 🤘":
            centered "{=custom_text}Você ganhou +30 pontos com Laurece!"
            $ amizade_laurence += 30
            jump lalitha_rockeira
        "Dizer que gosta de música clássica 🎹":
            centered "{=custom_text}Você ganhou +15 pontos com Laurece!"
            $ amizade_laurence += 15
            jump lalitha_classica
        "Dizer que gosta de pop":
            centered "{=custom_text}Você ganhou +5 pontos com Laurece!"
            $ amizade_laurence += 5
            jump lalitha_pop

label lalitha_rockeira:
    scene SACADA_ESCOLA with fade_in
    show LAURENCE_NORMAL:
        zoom 0.4
    with dissolve
    narrador "Sem saber, você e Laurence tinha o mesmo gosto musical."

    lalitha normal "Eu gosto muito de Rock and Roll!!🤘🤘"

    laurence "HAHAHAHHA"
    laurence "Você é demais mesmo!"
    show LAURENCE_OLHO_FECHADO:
        zoom 0.4
    with dissolve
    laurence "Nada melhor do que os clássicos como Metallica, Queen, AC/DC e Beatles.."
    jump escutando_musica_juntos

label lalitha_classica:
    scene SACADA_ESCOLA with fade_in
    show LAURENCE_OLHO_FECHADO:
        zoom 0.4
    with dissolve
    laurence "Os clássicos da música são bons... Acho bem culto quem escuta."

    show LAURENCE_NORMAL:
        zoom 0.4
    with dissolve
    laurence "Mas eu gosto de escutar Rock! Que pena não termos o mesmo gosto musical."
    jump escutando_musica_juntos

label lalitha_pop:
    scene SACADA_ESCOLA with fade_in
    show LAURENCE_OLHO_FECHADO:
        zoom 0.4
    with dissolve
    laurence "Nossa pop é bem sua cara mesmo..."
    show LAURENCE_NORMAL:
        zoom 0.4
    with dissolve
    laurence "Eu não sou gão fã, HAHAHA... Gosto mais do Rock and Roll!!"
    laurence "Agora estou com medo de você não gostar da minha música"
    jump escutando_musica_juntos

label escutando_musica_juntos:
    scene SACADA_ESCOLA
    narrador "Você e Laurence escutam Legião Urbana juntos."
    jump musica_tocando

label musica_tocando:
    play sound "audio/musica.mp3"
    lalitha "Esse som... Conheço de algum lugar!"
    jump lalitha_opina

label lalitha_opina:
    stop sound fadeout 1.0
    scene SACADA_ESCOLA
    show LAURENCE_SEXY:
        zoom 0.4
    with dissolve
    laurence "E aí o que achou Lalitha?"
    menu: 
        "Gostei bastante!":
            centered "{=custom_text}Você ganhou +10 pontos com Laurece!"
            $ amizade_laurence += 10
            jump laurence_feliz
        "Eu prefiro ouvir outra coisa!":
            centered "{=custom_text}Você ganhou +5 pontos com Laurece!"
            $ amizade_laurence += 5
            jump laurence_triste
        "Muito lega! Ouvirei mais vezes, qual é o nome da música ?":
            centered "{=custom_text}Você ganhou +15 pontos com Laurece!"
            $ amizade_laurence += 15
            jump laurence_apaixonado

label laurence_feliz:
    scene SACADA_ESCOLA
    show LAURENCE_NORMAL:
        zoom 0.4
    with dissolve
    narrador "Você gostou da música que Laurence te apresentou e também está muito feliz de conhecê-lo"
    laurence "Fico feliz que gostou! Não costumo compartilhar minhas músicas com pessoas que acabei de conhecer HAHAHA"
    lalitha normal "Que isso, tamo junto!"
    jump despedida_laurence_apaixonado

label laurence_triste:
    scene SACADA_ESCOLA
    show LAURENCE_OLHO_FECHADO:
        zoom 0.4
    with dissolve
    narrador "Você não curtiu muito a música de Laurence, poderia ser melhor!"
    narrador "Ele até era bonitinho mas não sabia escutar música direito."
    laurence "UAU! Estou surpreso."
    show LAURENCE_OLHO_GRANDE:
        zoom 0.4
    with dissolve
    laurence "E um pouco chocado também, talvez o rock brasileiro não seja para você."
    lalitha normal "..."
    jump despedida_laurence_apaixonado

label laurence_apaixonado:
    scene SACADA_ESCOLA
    show LAURENCE_NORMAL:
        zoom 0.4
    with dissolve

    narrador "Você adorou a música! E Laurence ficou surpreso de finalmente encontrar alguém com o mesmo estilo musical"

    laurence "Essa música é do Legião Urbana, se chama Tempo Perdido!"
    lalitha normal "Valeu Laurence! Seu gosto musical é bom igual ao meu HAHAHA"
    show LAURENCE_OLHO_GRANDE:
        zoom 0.4
    with dissolve
    narrador "Laurence acaba criando uma pequena paixão por você !"
    jump despedida_laurence_apaixonado

label despedida_laurence_apaixonado:
    scene SACADA_ESCOLA
    show LAURENCE_NORMAL:
        zoom 0.4
    with dissolve
    if amizade_laurence == 55:
        lalitha normal "Bom,minha aula já vai começar! Até.."
        laurence "Nós vamos nos encontrar de novo :)"
        scene SALA_DE_AULA_ESCURA with fade_in
        narrador "com o passar dos dias você e laurence sempre ouviam música na hora do intervalo e vocês ficaram bastante próximos !"
    elif amizade_laurence in range(40):
        lalitha normal "Bom, minha aula já vai começar! Até.."
        laurence "Até Lalitha !"
        scene SALA_DE_AULA_ESCURA with fade_in
        narrador "com o passar dos dias você e laurence se tornaram bons colegas, ele era um rockeiro dahora!"
    elif amizade_laurence in range(20):
        lalitha normal "Certo, minha aula já vai começar! Até.."
        laurence "Tchau.."
        scene SALA_DE_AULA_ESCURA with fade_in
        narrador "com o passar dos dias você e laurence não trocaram tantas palavras, tornaram-se apenas colegas distantes !"
    elif amizade_laurence in range(10):
        laurence"Certo, minha aula já vai começar! Até.."
        lalitha normal "Tchau.."
        scene SALA_DE_AULA_ESCURA with fade_in
        narrador "Laurence te achou demasiada rude! Sempre que seus olhares se cruzam ele tenta fingir que não te viu, uma pena."
    centered "{=custom_text}Nível de afeto com Laurence: [amizade_laurence]!"
        
