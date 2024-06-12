include "recursos.rpy"
define fade_in = Fade(0.5, 0.3, 0.5)
define fade_out = Fade(0.0, 0.0, 0.4)
default amizade_lazarus = 0
label capitulo3:
    scene SALA_DE_TARDE
    centered "{=custom_text}Bem vindo ao capítulo 3!"
    if amizade_leopold > amizade_laurence:
        narrador "Já era final da aula e você vai para casa."
        scene ESCOLA_TARDE with fade_in
        $ renpy.pause(2.0)
        show LEOPOLD_NORMAL:
            zoom 0.4
        with dissolve

        leopold "OH! Olá Lalitha!"
        lalitha normal "Oi Leopold! não sabia que você estudava por aqui"
        leopold "HAHAHAHAH... Estudo sim! Vi você mais cedo, você acabou sumindo"
        lalitha normal "Poxa que chato.."
        menu:
            "Recompensar Leopold o chamando para tomar um lanche.":
                centered "{=custom_text}Você ganhou +10 pontos com Leopold!"
                $ amizade_leopold += 10
                jump saindo_com_leo
            "Me despedir":
                centered "{=custom_text}Você não ganhou pontos com Leopold."
                jump conhecer_lazarus

    else:
        jump sair_com_laurence
        
label sair_com_laurence:
    scene ESCOLA_DIA_PORTAO 
    narrador "Era uma sexta-feira, você e Laurence iriam sair para andar no parque e escutar novas banda de Rock"
    narrador "Mas algo estava prestes a acontecer e você nem tem ideia...."
    show LAURENCE_OLHO_GRANDE:
        zoom 0.4
    with dissolve
    laurence "Aff cadê essa garota!"
    $ renpy.pause(2.0)
    show LALITHA_FELIZ with dissolve
    lalitha "Olá Laurece!"
    show LAURENCE_OLHO_FECHADO:
        zoom 0.4
    with dissolve
    laurence "AH.. Você veio mesmo, pensei que ia me deixar aqui."
    jump parque_com_laurence

label parque_com_laurence:
    scene PARQUE_DIA with fade_in
    if amizade_leopold != 0:
        show LAURENCE_NORMAL:
            zoom 0.4
        with dissolve
        lalitha normal "Nossa aqui é bem bonito! Me lembrou minha cidade natal."
        laurence "Fico feliz que gostou"
        laurence "Voltaremos aqui mais vezes se você quiser!"
        jump lalitha_dor_barriga
    else:
        show LAURENCE_NORMAL:
            zoom 0.4
        with dissolve
        lalitha normal "É, eu ja estive aqui, agora que me lembrei!"
        lalitha normal "Adoro como esse parque lembra minha cidade natal, com bastante árvores"
        show LAURENCE_OLHO_FECHADO:
            zoom 0.4
        with dissolve
        laurence "Fico feliz de estar aqui com você!"
        jump lalitha_dor_barriga

label lalitha_dor_barriga:
    scene PARQUE_DIA with fade_in
    narrador "Tudo estava indo bem até que você sentiu uma forte dor de barriga."
    show LALITHA_PERDIDA with dissolve
    lalitha "Ah...."
    show LALITHA_CHORANDO with dissolve
    narrador "Você lembrou que fazia um bom tempo que não ia ao banheiro"
    narrador "Droga, logo no seu primeiro encontro!"
    show LAURENCE_NORMAL:
        zoom 0.4
    with dissolve
    laurence "Tá tudo bem aí?"
    scene PARQUE_DIA with fade_in
    show LALITHA_SEM_GRACA with fade_in
    lalitha "AHHH SIMM, eu só vou no banheiro rapidinho e ja volto"
    narrador "Você mentiu para o garoto."
    show LAURENCE_OLHO_FECHADO:
        zoom 0.4
    with dissolve
    laurence "Certo, vou ficar por aqui...."
    jump lalitha_apurada

label lalitha_apurada:
    scene PARQUE_DIA with fade_in
    show LALITHA_CHORANDO with dissolve
    lalitha "Deve ter algum banheiro aqui... To bastate apurada"
    scene BANHEIRO_PARQUE with dissolve
    $ renpy.pause(2.0)
    show LALITHA_FELIZ with dissolve
    lalitha "Olha só, é aqui mesmo!"
    scene BANHEIRO_PARQUE
    play sound "audio/desgarga.mp3" volume 0.5
    $ renpy.pause(2.0)
    stop sound
    show LALITHA_SORRINDO with dissolve
    lalitha "Agora estou me sentindo bem!"
    show LALITHA_NORMAL with dissolve
    lalitha "Agora estou preparada para caminhar pelo parque!"
    jump lalitha_perdida

label lalitha_perdida:
    scene PARQUE_DIA with fade_in
    show LALITHA_PERDIDA with dissolve
    narrador "Você olha ao redor mas seu amigo Laurence sumiu!"
    lalitha "É sério isso ?"
    show LALITHA_CHORANDO with dissolve
    lalitha "LAURENCE ONDE ESTÁ VOCÊÊÊ"
    jump lazarus_encontro


label saindo_com_leo:
    scene FAST_FOOD with fade_in
    show LEOPOLD_OLHO_FECHADO:
            zoom 0.4
    with dissolve
    lalitha normal "Acho que esse lugar é bom!"
    show LEOPOLD_OLHO_GRANDE:
            zoom 0.4
    with dissolve
    leopold "Vamos comer !"
    with fade_in
    narrador "Você e Leopold passaram um bom tempo de qualidade juntos! Vocês formavam um ótimo casal juntos!"
    menu:
        "FInalizar rotas":
            jump fim_jogo

label conhecer_lazarus:
    scene PARQUE_DIA
    narrador "Você pediu desculpas ao garoto pelo ocorrido e resolveu ir andar no parque"
    show LALITHA_SORRINDO with dissolve
    lalitha "Foi aqui que conheci meu primeiro amigo e acabei nem dando tanta bola pra ele assim.."
    show LALITHA_FELIZ with dissolve
    lalitha "O que devo fazer agora?"
    menu:
        "Andar pelo parque.":
            jump lazarus_encontro
        "Ir ao banheiro":
            jump ir_no_banheiro

label ir_no_banheiro:
    scene PARQUE_DIA with fade_in
    show LALITHA_CHORANDO with dissolve
    lalitha "Deve ter algum banheiro aqui... To bastate apurada"
    scene BANHEIRO_PARQUE with dissolve
    $ renpy.pause(2.0)
    show LALITHA_FELIZ with dissolve
    lalitha "Olha só, é aqui mesmo!"
    scene BANHEIRO_PARQUE
    play sound "audio/desgarga.mp3" volume 0.5
    $ renpy.pause(2.0)
    stop sound
    show LALITHA_SORRINDO with dissolve
    lalitha "Agora estou me sentindo bem!"
    show LALITHA_NORMAL with dissolve
    lalitha "Agora estou preparada para caminhar pelo parque!"
    jump lazarus_encontro


label lazarus_encontro:
    scene PISTA_SKATE with fade_in
    narrador "Andando mais pra frente dali, você encontra uma pista de skate."
    narrador "Era a sua primeira vez numa pista de skate."
    lalitha normal "Aqui só tem gente radical"
    show LAZARUS_SEXY:
        zoom 0.4
    with dissolve
    semNome "Ei você!"
    semNome "Saia daí! Você está ocupando o lugar onde vou realizar minha manobra!!!"
    show LAZARUS_NORMAL:
        zoom 0.4
    with dissolve
    narrador "Você levou um pequeno susto e acabou se esquivando."
    menu:
        "Pedir desculpa":
            centered "{=custom_text}Você ganhou +5 pontos com Lazarus!"
            $ amizade_lazarus += 5
            jump lalitha_pede_desculpa

label lalitha_pede_desculpa:
    scene PISTA_SKATE with fade_in
    show LALITHA_CHORANDO with dissolve
    lalitha "Desculpa ai ein..."
    hide LALITHA_CHORANDO with dissolve
    show LAZARUS_NORMAL:
        zoom 0.4
    with dissolve
    lazarus "HAHAHA Tudo bem! Você é bem lerdinha"
    lazarus "O meu nome é Lazarus, e o seu ?"
    lalitha "Lalitha.."
    lazarus "Não fica triste não, eu tava só brincando."
    narrador "Ele acabou mudando o tom de voz depois que percebeu o quão fofa você era!"
    hide LAZARUS_NORMAL with dissolve
    show LAZARUS_NORMAL:
        zoom 0.4
    with dissolve

    lazarus "O que uma linda como você faz aqui ?"
    menu:
        "Estava apenas explorando o parque":
            centered "{=custom_text}Você não ganhou pontos com Lazarus!"
            jump dialogo_lalitha_lazarus
        "Procurando algo ou alguém!":
            centered "{=custom_text}Você ganhou +10 pontos com Lazarus!"
            $ amizade_lazarus += 10
            jump dialogo_lalitha_lazarus_dois
            
label dialogo_lalitha_lazarus:
    scene PISTA_SKATE with fade_in
    show LAZARUS_NORMAL:
        zoom 0.4
    with dissolve
    lazarus "Aqui é mais afastado do parque, mas também tem uma galera bacana demais hahaha"
    lazarus "Você anda de skate?"
    jump lalitha_skatista

label dialogo_lalitha_lazarus_dois:
    scene PISTA_SKATE with fade_in
    show LAZARUS_OLHO_FECHADO:
        zoom 0.4
    with dissolve
    lazarus "Bom, hoje é seu dia de sorte pois você acabou de conhecer o cara mais bacana de toda cidade"
    lalitha "HAHAHA Que engraçado..."
    show LAZARUS_NORMAL:
        zoom 0.4
    with dissolve
    lazarus "Então, me diga ai.. Você curte andar de skate?"
    jump lalitha_skatista

label lalitha_skatista:
    scene PISTA_SKATE with fade_in
    menu:
        "Nunca tentei, tenho medo de cair!":
            centered "{=custom_text}Você não ganhou pontos com Lazarus!"
            jump lalitha_nao_gosta_de_lazarus
        "Eu gosto apenas de apreciar os esportes radicais":
            centered "{=custom_text}Você ganhou +10 pontos com Lazarus!"
            $ amizade_lazarus += 10
            jump lalitha_apreciadora
        "Gosto, mas não sou tenho tanta habilidade!":
            centered "{=custom_text}Você ganhou +20 pontos com Lazarus!"
            $ amizade_lazarus += 15
            jump lazarus_oferece_ajuda

label lalitha_nao_gosta_de_lazarus:
    scene PISTA_SKATE with fade_in
    narrador "Você achou o garoto um pouco maluco, preferiu não se envolver tanto."
    show LAZARUS_OLHO_GRANDE:
        zoom 0.4
    with dissolve
    lazarus "Entendi..."
    lazarus "Já caí muitas vezes aqui, mas faz parte do estilo de vida Hardcore!"
    lalitha normal "Que cara malucão."
    
label lalitha_apreciadora:
    scene PISTA_SKATE with fade_in
    show LAZARUS_NORMAL:
        zoom 0.4
    with dissolve
    lazarus "HAHAHA Bacana!"
    lazarus "Se continuar vindo aqui para me ver pode ter certeza que algum dia você vai querer tentar também"
    menu:
        "Fazer piada":
            centered "{=custom_text}Você ganhou +10 pontos com Lazarus!"
            $ amizade_lazarus += 10
            jump piadoca_lalitha
        "Ficar quieta":
            centered "{=custom_text}Você não ganhou pontos com Lazarus!"
            jump despedida_lazarus

label piadoca_lalitha:
    scene PISTA_SKATE
    show LAZARUS_NORMAL:
        zoom 0.4
    lalitha normal "Talvez se um dia você for para os Olimpíadas.. Sim!"
    show LAZARUS_OLHO_GRANDE:
        zoom 0.4
    with dissolve
    lazarus "AHAHA essa foi boa, você é bem engraçada. Gosto disso."
    jump despedida_lazarus

label despedida_lazarus:
    scene PISTA_SKATE with fade_in
    show LAZARUS_OLHO_GRANDE:
        zoom 0.4
    with dissolve
    lazarus "Bom.."
    lazarus "Foi um bom papo, mas agora preciso treinar minhas manobras."
    lalitha normal "Ah sim.."
    if amizade_lazarus > 15:
        jump lazarus_pergunta_para_anda_com_lali
    else:
        show LAZARUS_OLHO_FECHADO:
            zoom 0.4
        lazarus "A gente se vê por aí Lalitha"
        scene PISTA_SKATE with dissolve
        centered "{=custom_text}Nível de afeto com Lazarus: [amizade_lazarus]!"
        jump fim_jogo

label lazarus_pergunta_para_anda_com_lali:
    scene PISTA_SKATE
    show LAZARUS_OLHO_FECHADO:
        zoom 0.4
    lazarus "Você precisa de ajuda para fazer o caminho de volta?"
    menu:
        "Adoraria a companhia!":
            jump lazarus_anda_com_lali
        "Eu consigo achar!":
            jump fim_jogo

label lazarus_anda_com_lali:
    scene PARQUE_DIA with fade_in
    show LALITHA_FELIZ with dissolve
    narrador "Você conseguiu conhecer o lado gentil de Lazarus, e uma nova amizade!"
    hide LALITHA_FELIZ with dissolve
    show LAZARUS_NORMAL:
        zoom 0.4
    with dissolve
    lazarus "Até mais Lalitha!"
    lalitha normal "Tchau!"
    jump fim_jogo

label lazarus_oferece_ajuda:
    scene PISTA_SKATE with fade_in
    show LAZARUS_NORMAL:
        zoom 0.4
    with dissolve
    lazarus "É errando que se aprende!"
    show LAZARUS_OLHO_FECHADO:
        zoom 0.4
    with dissolve
    lazarus "Se você quiser eu posso te dar umas aulinhas de manobras radicais HAHAHA"
    lalitha normal "Quem sabe um dia!"
    jump despedida_lazarus
    

label fim_jogo:
    scene ESQUINA_DE_CASA with fade_in
    centered "{=custom_text}Parabéns por chegar ao fim do Jogo!"
    centered "{=custom_text}Veja agora o nível de afeto com cada garoto :)"
    centered "{=custom_text}Nível de afeto com Laurence: [amizade_laurence]!"
    centered "{=custom_text}Nível de afeto com Leopold: [amizade_leopold]!"
    centered "{=custom_text}Nível de afeto com Lazarus: [amizade_lazarus]!"

    if amizade_leopold > amizade_laurence and amizade_leopold > amizade_lazarus:
        centered "{=custom_text}Você ficou com Leopold"
        show LEOPOLD_NORMAL:
            zoom 0.4
        with dissolve
        leopold "Obrigada por me escolher <3"
    elif amizade_laurence > amizade_leopold and amizade_laurence > amizade_lazarus:
        centered "{=custom_text}Você ficou com Laurence"
        show LAURENCE_NORMAL:
            zoom 0.4
        with dissolve
        laurence "Viva o Rock and Roll!"
    elif amizade_lazarus > amizade_leopold and amizade_lazarus > amizade_laurence:
        centered "{=custom_text}Você ficou com Lazarus"
        show LAZARUS_NORMAL:
            zoom 0.4
        with dissolve
        lazarus "Obrigada por me escolher <3"
    else:
        centered "{=custom_text}Houve um empate nos níveis de afeto!"

    centered "{=custom_text}Laura também agradece!"

    return
    scene ESQUINA_DE_CASA with fade_in
    centered "{=custom_text}Parabéns por chegar ao fim do Jogo!"
    centered "{=custom_text}Veja agora o nível de afeto com cada garoto :)"
    centered "{=custom_text}Nível de afeto com Laurence: [amizade_laurence]!"
    centered "{=custom_text}Nível de afeto com Leopold: [amizade_leopold]!"
    centered "{=custom_text}Nível de afeto com Lazarus: [amizade_lazarus]!"
    if amizade_leopold > amizade_laurence and amizade_lazarus:
        centered "{=custom_text}Você ficoi com Leopold"
        show LEOPOLD_NORMAL:
            zoom 0.4
        with dissolve
        leopold "Obrigada por me escolher <3"
    elif amizade_laurence > amizade_leopold and amizade_lazarus:
        centered "{=custom_text}Você ficoi com Laurence"
        show LAURENCE_NORMAL:
            zoom 0.4
        with dissolve
        leopold "Viva o Rock and Roll!"
    elif amizade_lazarus > amizade_leopold and amizade_laurence:
        centered "{=custom_text}Você ficoi com Lazarus"
        show LAZARUS_NORMAL:
            zoom 0.4
        with dissolve
        leopold "Obrigada por me escolher <3"
    centered "{=custom_text}Laura também agradece!"
    
    return


