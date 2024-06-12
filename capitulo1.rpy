include "recursos.rpy"

default amizade_leopold = 0

define fade_in = Fade(0.5, 0.3, 0.5)

label start_visual_novel:

    scene ESQUINA_DE_CASA

    narrador "Você acabou de chegar em seu novo bairro onde iria viver sozinha."

    show LALITHA_FELIZ
    with dissolve
    lalitha "Uau ! Até que enfim consegui achar meu endereço!"

    show LALITHA_NORMAL
    with dissolve
    narrador "Lalitha tinha acabado de se mudar para sua nova casa"
    narrador "agora que ela estava no Ensino Médio, ja tinha responsabilidade de ter sua própria casa."
    
    lalitha "Preciso arrumar minhas coisas, mas também gostaria de explorar a cidade..."
    lalitha "O que devo fazer agora ?"
    menu:
        "Ir explorar o bairro":
            jump explorar_cidade

        "Ir para casa":
            jump ficar_em_casa

label ficar_em_casa:

    scene VISTA_DE_CASA
    with fade

    lalitha "Acho melhor ficar em casa por hoje..."

    scene SALA_CASA
    with dissolve
    lalitha "Que bagunça esse lugar ! Como pude ser tão descuidadosa??"

    scene COZINHA
    with dissolve
    lalitha "Bom, temos que arrumar isso até o fim da tarde."

    narrador "Algumas horas depois.."

    scene QUARTO_NOITE
    with fade
    show LALITHA_PERDIDA
    with dissolve
    lalitha "Já escureceu, eu estou bem cansadinha."

    show LALITHA_FELIZ
    with dissolve
    lalitha "Eu vou dormir pois amanhã já tenho aula."
    centered "{=custom_text}Nível de afeto com Leopold: [amizade_leopold]"
    menu:
        "Finalizar Capitulo 1":
            "Clique para continuar no Capítulo 2"
            jump capitulo2

    return

label explorar_cidade:
    scene RUA_DE_CASA
    show LALITHA_NORMAL
    with fade
    lalitha "Preciso decorar qual é o caminho de casa..."

    show LALITHA_SEM_GRACA
    with dissolve
    lalitha "Acho que vi um parque aqui perto! Talvez eu consiga fazer alguma amizade lá!"

    scene PARQUE_DIA
    lalitha "Uau, aqui é bem tranquilo, eu adoro parques"

    show LEOPOLD_NORMAL:
        zoom 0.4
    with fade
    
    lalitha "...."
    menu:
        "Falar com o garoto":
            jump conhecer_leopold
        "Voltar para casa":
            jump ficar_em_casa

label conhecer_leopold:
    leopold "Olá! Nunca vi você aqui pelo parque" 
    
    lalitha normal "Eu sou nova aqui, meu nome é Lalitha"

    show LEOPOLD_NORMAL
    with dissolve
    leopold "Legal! O meu é Leopold"

    leopold "Eu gosto de andar no parque durante a tarde... É bem tranquilo"
    lalitha normal "Sim..."
    with fade_in

    menu:
        "Puxar assunto com Leopold":
            lalitha normal "Você é daqui ?"
            centered "{=custom_text}Ganhou +10 pontos com Leopold"
            $ amizade_leopold += 10
            jump continuar_conversa_leopold

        "Ficar quieta":
            centered "{=custom_text}Ganhou +5 pontos com Leopold!"
            $ amizade_leopold += 5
            jump leopold_tenta_conversar

label leopold_tenta_conversar:
    narrador "Você estava tranquila na sua, só queria aproveitar o parque de boas, mas também tentou ser educada"

    show LEOPOLD_OLHO_FECHADO:
        zoom 0.4
    with dissolve
    leopold "De onde você é ?"

    lalitha normal "Eu vim do interior, eu e minha familia vivíamos numa Fazendinha, mas eu resolvi vir ate a cidade para morar."

    scene PARQUE_DIA

    show LEOPOLD_NORMAL:
        zoom 0.4
    with dissolve
    leopold "Que bacana! Como você veio de longe..."
    leopold "Você precisa de alguma ajuda com suas coisas? Você deve estar bem perdida."
    with fade_in
    menu:
        "Não, obrigada!":
            centered "{=custom_text}Você não ganhou pontos com Leopold."
            jump leopold_adeus
        "Você conhece alguma loja de produtos?":
            centered "{=custom_text}Ganhou +5 pontos com Leopold!"
            $ amizade_leopold += 5
            jump conhecendo_lojinha_com_leopold

label leopold_adeus:
    narrador "Foi legal conhecer Leopold, mas você não estava interessada em se envolver com ele!"
    centered "{=custom_text}Nível de afeto com Leopold: [amizade_leopold]!"
    menu:
        "Finalizar Capitulo 1":
            "Clique para continuar no Capítulo 2"
            jump capitulo2

label continuar_conversa_leopold:
    narrador "Você perguntou na intenção de conhecer seu potêncial amigo Leopold"
    
    show LEOPOLD_NORMAL
    with fade    
    leopold "Eu moro aqui perto, vivo na cidade desde que nasci :)"
    narrador "Leopold também se interessa em fazer amizade com você."
    show LEOPOLD_OLHO_FECHADO:
        zoom 0.4
    with dissolve
    leopold "E você? O que te fez vir para cá?"

    hide LEOPOLD_OLHO_FECHADO with dissolve
    menu:
        "Vim estudar.":
            centered "{=custom_text}+5 pontos com Leopold"
            $ amizade_leopold += 5
            jump continuar_conversa_leopold_continuacao
        
        "Eu me mudei recentemente por conta de meus estudos, minha antiga cidade era muito pequena":
            centered "{=custom_text}Ganhou +15 pontos com Leopold!"
            $ amizade_leopold += 15
            jump sair_com_leopold

        "Cheguei hoje mesmo de mudança! Vim estudar numa escola melhor pois onde eu estudava antes era bem ruim... Ainda nem arrumei minhas coisas":
            centered "{=custom_text}Ganhou +30 pontos com Leopold!"
            $ amizade_leopold += 30
            jump leopold_te_ajuda_com_mudanca

label sair_com_leopold:
    show LEOPOLD_SEXY:
        zoom 0.4
    with dissolve
    leopold "hahaha aqui é bem diferente de uma cidade pequena, se quiser eu posso lhe ajudar em alguma coisa!"
    menu:
        "Você conhece um bom lugar para fazer compras?":
            centered "{=custom_text}Ganhou +10 pontos com Leopold!"
            $ amizade_leopold += 10
            jump conhecendo_lojinha_com_leopold
        "Eu preciso de ajuda com minha mudança, você gostaria de me ajudar?":
            centered "{=custom_text}Ganhou +15 pontos com Leopold!"
            $ amizade_leopold += 15
            jump leopold_te_ajuda_com_mudanca


label continuar_conversa_leopold_continuacao:
    show LEOPOLD_OLHO_FECHADO:
        zoom 0.4
    with dissolve
    leopold "Entendi..."
    leopold "Espero que você se acostume com a cidade, boa sorte com os estudos!"
    jump leopold_adeus
    with fade_in


label leopold_te_ajuda_com_mudanca:
    narrador "Seu interesse em passar mais tempo com Leopold aumenta!"

    scene PARQUE_DIA
    show LEOPOLD_OLHO_FECHADO:
        zoom 0.4
    with dissolve
    leopold "Interessante.."
    leopold "Você mora aqui perto, certo?"
    lalitha normal "SIMMM, não vamos demorar!"
    hide LEOPOLD_OLHO_FECHADO with dissolve
    with fade_in

    scene ESQUINA_DE_CASA
    show LEOPOLD_NORMAL:
        zoom 0.4
    with dissolve
    leopold "Tem bastante árvores aqui, gostei bastante!"
    lalitha normal "HEHEHEHE..."

    scene COZINHA
    show LALITHA_SORRINDO with dissolve
    lalitha "Seja bem vindo!"

    show LALITHA_SEM_GRACA with dissolve
    narrador "Você e Leopold passam um tempo se conhecendo"
    show LEOPOLD_NORMAL:
        zoom 0.4
    with dissolve
    narrador "E vocês acabam gostando bastante um do outro!"
    centered "{=custom_text}Nível de afeto com Leopold: [amizade_leopold]!"
    
    menu:
        "Finalizar Capitulo 1":
            "Clique para continuar no Capítulo 2"
            jump capitulo2


label conhecendo_lojinha_com_leopold:
    narrador "Você precisava fazer compras, nada melhor do que perguntar para o seu novo amigo"
    show LEOPOLD_OLHO_GRANDE:
        zoom 0.4
    with dissolve
    leopold "Conheço sim! Posso te levar lá rápidinho"

    lalitha normal "Vamos lá!!"

    scene LOJINHA_DIA
    with fade_in

    show LEOPOLD_NORMAL:
        zoom 0.4
    with dissolve
    leopold "Esse lugar é como se fosse a casa China, tem de tudo aqui!"
    lalitha normal "Nossa, me ajudou muito, obriga pela sua gentileza Leopold!"

    show LEOPOLD_OLHO_FECHADO:
        zoom 0.4
    with dissolve

    narrador "Leopold te achou muito querida e acabou se apaixonando por você..."

    hide LEOPOLD_OLHO_FECHADO with dissolve

    lalitha normal "Foi muito legal andar e vir até aqui com você Leopold"
    lalitha normal "Eu preciso voltar para casa agora, mas a gente se encotrará mais vezes!"

    show LEOPOLD_NORMAL
    with dissolve
    leopold "Eu também espero..."
    lalitha normal "Legal! Eu vou para casa agora"
    lalitha normal "Até mais Leo! Adorei te conhecer!"
    jump despedida_leopold
    with fade_in

label despedida_leopold:
    scene ESQUINA_DE_CASA

    lalitha "Que cara mais bacana..."
    narrador "Você ficou feliz com sua nova amizade com o garoto do parque!"
    centered "{=custom_text}Nível de afeto com Leopold: [amizade_leopold]!"
    menu:
        "Finalizar Capitulo 1":
            "Clique para continuar no Capítulo 2"
            jump capitulo2