# ==============================================================================
# AVISO: Por favor, respeite o trabalho investido na criação deste
# código e evite copiá-lo ou utilizá-lo sem permissão. ass: Luchas.
# ==============================================================================
#   ▂▃▅▆▇█ K █ a █ n █ f █ e █ m █   █ S █ t █ u █ d █ i █ o █ s █▇▆▅▃▂
import random

player_health = 50
alien_health = 50
trainer_health = 50
giga_health = 80
bad_health = 90
bilu_health = 100




def main_menu():
    while True:
        choice = input('A Lenda do Combate Extraterrestre. (jogar/sobre/prólogo/sair) ').lower()

        if choice in ['sair','Sair']:
            break
        elif choice in ['sobre','Sobre']:
            about()
        elif choice in ['prólogo', 'prologo','Prólogo','Prologo']:
            prologue()
        elif choice in ['jogar','Jogar']:
            play_game()
        else:
            print("Escolha inválida.")

def about():
    while True:
        choice = input(f'Criado por: Luchas 2023 versão: 3.0 (voltar/sair) ')
        if choice.lower() in ['sair', 'Sair']:
            break
        elif choice.lower() in ['voltar', 'Voltar']:
            return  
        else:
            print("Escolha inválida.")

def prologue():
    while True:
        choice = input(f'Galdric de Tokitiry era um jovem que vagava pelas cidades do Reino de Kanfrem em busca de aventuras durante o período do sábio Airon. Um dia, quando vagava por Manteki, a capital de Kanfrem, ele foi convocado pelo Rei para combater extraterrestres que tomaram controle de algumas regiões de Kanfrem. E como recompensa, construirão uma escultura sua. Mas suas aventuras só irão começar depois de tirar um cochilo em sua cabana. (voltar/sair) ')
        if choice.lower() in ['sair', 'Sair']:
            break
        elif choice.lower() in ['voltar', 'Voltar']:
            return

def play_game():
    global player_health, alien_health
    print(f"Você acorda de seu cochilo e quando sai do quarto se depara com o Rei de Kanfrem, Kairit à sua frente.")
    ce = input("(fugir/conversar) ")
    if ce.lower() in ['conversar','Conversar']:
        ce2 = input(f"Olá Galdric! Eu queria lhe dar isso antes de você ir em sua jornada. Você aceita? (sim/não) ")
        if ce2.lower() in ['sim','Sim']:
            print("O Rei lhe entrega uma armadura dos cavaleiros reais.")
            alien_battle()
        elif ce2.lower() in ['não', 'nao', 'Nao', 'Não']:
            print(f"O Rei parece decepcionado, mas respeita sua decisão.")
        else:
            print("Escolha inválida.")
    elif ce.lower() in ['fugir','Fugir']:
        ce3 = input(f"Espere Galdric! Eu preciso te dar uma coisa. Você volta? (sim/não) ")
        if ce3.lower() in ['sim','Sim']:
            print("O Rei parece aliviado e lhe entrega uma armadura.")
            alien_battle()
        elif ce3.lower() in ['não', 'nao', 'Nao', 'Não']:
            print(f"Você corre para longe, deixando o Rei para trás.")
            exit()
        else:
            print("Escolha inválida.")
    else:
        print("Escolha inválida.")

def alien_battle():
    print("Um alienígena aparece! Prepare-se para a batalha!")
    global player_health, alien_health
    while player_health > 0 and alien_health > 0:
        attack_choice = input("Escolha seu ataque: (1) Soco (2) Chute (3) Defender-se ").lower()

        if attack_choice in ['1', 'soco']:
            player_attack = random.randint(5, 15)
            alien_attack = random.randint(5, 15)
        elif attack_choice in ['2', 'chute']:
            player_attack = random.randint(5, 30)
            alien_attack = random.randint(5, 15)
        elif attack_choice in ['3', 'defender-se']:
            print("Você se defende e reduz o dano do próximo ataque pela metade.")
            player_attack = 0
            alien_attack = random.randint(5, 15) // 2
        else:
            print("Escolha inválida.")
            continue

        alien_health -= player_attack
        player_health -= alien_attack

        print(f"Galdric ataca o alienígena e causa {player_attack} de dano. A saúde do alienígena agora é {alien_health}.")
        print(f"O alienígena ataca Bob e causa {alien_attack} de dano. A saúde de Galdric agora é {player_health}.")

        if alien_health <= 0:
            print('Você ganhou!')
            after_battle()
            break
        elif player_health <= 0:
            print('Você perdeu... GAME OVER')
            retry = input('Deseja tentar novamente? (sim/não) ').lower()
            if retry in ['sim','Sim']:
                player_health = 50
                alien_battle()
            elif retry in ['não', 'nao', 'Nao', 'Não']:
                break
            else:
                print('Escolha inválida')
def after_battle():
    global player_name
    choice = input(f"Muito bem Galdric! Você conseguiu provar suas capacidades. O Rei lhe informou que você precisa encontrar o sábio Airon em Watorok para receber instruções sobre como derrotar os alienígenas. Agora vá continuar a sua jornada Galdric! (continuar/sair) ")

    if choice.lower() in ['continuar', 'Continuar']:
        print(f'Você se despediu de Kairit e partiu para a cidade de Watorok.')
        watorok_intro()
    elif choice.lower() in ['sair', 'Sair']:
        exit()
    else:
        print('Escolha inválida. Por favor, escolha "continuar" ou "sair".')
        after_battle()

def watorok_intro():
    print("Você chegou à cidade de Watorok, uma cidade movimentada no Reino de Kanfrem. A cidade é conhecida por suas feiras e festivais. O que você deseja fazer em Watorok?")
    while True:
        watorok_choice = input("(comer/lutar/encontrar Airon) ")
        if watorok_choice in ['comer','Comer']:
            print("Você desfruta de uma refeição deliciosa em um dos restaurantes locais.")
        elif watorok_choice in ['lutar','Lutar']:
            trainer_battle()
        elif watorok_choice in ['encontrar airon', 'airon', 'encontrar','Airon','Encontrar','Encontrar Airon','Encontrar airon','encontrar airon']:
            print("Você decide procurar o sábio Airon para obter instruções sobre como derrotar os alienígenas.")
            fokotoro_instructions()
        else:
            print("Escolha inválida. Escolha 'comer', 'lutar' ou 'encontrar airon'.")
player_health = 50
def trainer_battle():
    global player_health, trainer_health
    print("Você encontra um treinador local desafiador. Prepare-se para a batalha!")

    while player_health > 0 and trainer_health > 0:
        attack_choice = input("Escolha seu ataque: (1) Soco (2) Chute (3) Defender-se ")

        if attack_choice in ['1', 'soco', 'Soco', 'glubar']:
            player_attack = random.randint(5, 15)
            trainer_attack = random.randint(5, 15)
        elif attack_choice in ['2', 'chute']:
            player_attack = random.randint(5, 30)
            trainer_attack = random.randint(5, 15)
        elif attack_choice in ['3', 'defender-se']:
            print("Você se defende e reduz o dano do próximo ataque pela metade.")
            player_attack = 0
            trainer_attack = random.randint(5, 15) // 2
        else:
            print("Escolha inválida.")
            continue

        player_health -= trainer_attack
        print(f"Galdric ataca o treinador e causa {player_attack} de dano. A saúde do treinador agora é {trainer_health}.")
        print(f"O treinador ataca Galdric e causa {trainer_attack} de dano. A saúde de Galdric agora é {player_health}.")

        if trainer_health <= 0:
            print('Você venceu o treinador!')
            break
        elif player_health <= 0:
            print('Você perdeu para o treinador... GAME OVER')
            retry = input('Deseja tentar novamente? (sim/não) ')
            if retry.lower() in ['sim', 'Sim']:
                player_health = 50
                trainer_battle()
            elif retry.lower() in ['não', 'nao', 'Nao', 'Não']:
                break
            else:
                print('Escolha inválida')
def fokotoro_instructions():
    print(f"Você encontra o sábio Airon em sua humilde residência. Ele cumprimenta você calorosamente e começa a dar instruções sobre como derrotar os alienígenas.")
    print("Airon: 'Para derrotar os alienígenas, você precisa coletar a espada e o escudo. Para então usa-los contra o Rei Varginbilu")
    print("Airon: 'A Espada de Kanfram e o Escudo de Kordec estão escondidos em locais secretos, e você precisará resolver enigmas para encontrá-los.'")
    print("Airon: 'Lembre-se de que o destino do Reino de Kanfrem está em suas mãos. Boa sorte, jovem aventureiro!'")
    inp = input("Você agradece a Airon pelas instruções e parte em busca da espada e do escudo. (continuar/sair) ")
    if inp in ['continuar','Continuar']:
        journey_to_mountains()
    elif inp in ['sair','Sair']:
        exit()
    else:
        print('Escolha inválida')
        fokotoro_instructions()

def journey_to_mountains():
    print("Você parte em direção às Montanhas de Kanfrem em busca da Espada de Kanfram.")
    print("Ao chegar às montanhas, você encontra uma porta de pedra com uma inscrição misteriosa. Ela diz:")
    print("'O que corta de todo material menos ao que é atacado injustamente?'")
    answer = input("Qual é a sua resposta? ")
    if answer.lower() in ['espada de kanfram', 'espada', 'Espada', 'Espada de Kanfram']:
        the_sword()
    else:
        print('Resposta incorreta. Tente novamente.')
        journey_to_mountains()

def the_sword():
    print("A porta se abre, e você encontra a Espada de Kanfram! Parabéns, você resolveu o enigma e coletou a espada.")
    per = input('Deseja continuar? (sim/não)').lower()
    if per in ['não', 'nao', 'Nao', 'Não']:
        exit()
    elif per in ['sim','Sim']:
        return_to_king()

def return_to_king():
    print('Você retorna à capital e informa ao rei o seu feito.')
    print(f'Kairit: Parabéns Galdric! Você provou sua sabedoria e fez com que as profecias se tornassem verdadeiras. Agora você vai precisar do Escudo de Kordec para derrotar o maligno Rei dos aliens: Varginlu.') 
    kd = input('Kairit: Você vai ter que ir para a Floresta do desconhecido para encontrar o escudo. Então, você vai? (sim/não)') 
    if kd in ['não', 'nao', 'Nao', 'Não']:
        exit()
    elif kd in ['sim','Sim']:
        midle_of_journey()
    else:
        print('Código inválido')
import random

player_health = 50
giga_health = 70
def midle_of_journey():
    global player_health, giga_health, player_name
    print('Você está no caminho para a floresta e se depara com um grupo de exploradores sendo atacados por um alien gigante! Prepare-se para a batalha!')
    
    while player_health > 0 and giga_health > 0:
        attack_choice = input("Escolha seu ataque: (1) Soco (2) Espada (3) Defender-se ")

        if attack_choice in ['1', 'soco', 'Soco']:
            player_attack = random.randint(10, 20)
            giga_attack = random.randint(8, 10)
        elif attack_choice in ['2', 'chute']:
            player_attack = random.randint(10, 40)
            giga_attack = random.randint(10, 25)
        elif attack_choice in ['3', 'defender-se']:
            print("Você se defende e reduz o dano do próximo ataque pela metade.")
            player_attack = 0
            giga_attack = random.randint(5, 15) // 2
        else:
            print("Escolha inválida.")
            continue

        giga_health -= player_attack
        player_health -= giga_attack

        print(f"Galdric ataca o alien e causa {player_attack} de dano. A saúde do alien agora é {giga_health}.")
        print(f"O alien ataca galdric e causa {giga_attack} de dano. A saúde de Galdric agora é {player_health}.")
	
        if giga_health <= 0:
            print('Você venceu o alien gigante!')
            ab = input('Continuar? (sim/não)')
            if ab in ['sim', 'Sim']:
                the_group()
            elif ab in ['não', 'nao', 'Nao', 'Não']:
                break

        elif player_health <= 0:
            print('Você perdeu para o alien gigante...  GAME OVER')
            retry = input('Deseja tentar novamente? (sim/não) ')
            if retry in ['sim', 'Sim']:
                player_health = 50
                midle_of_journey()
            elif retry in ['não', 'nao', 'Nao', 'Não']:
                break
def the_group():
    print('Após derrotar o alien gigante, os grupos de exploradores vieram lhe agradecer. Eles lhe deram instruções de como entrar na floresta do desconhecido sem se perder, já que quem entra na mata sem o cuidado necessário, se torna servo da Árvore da Manipulação.')
    print('Você entra na mata e encontra um pedestal e nele está escrito: .--. .- .-. .- / -.-. --- -. ... . --. ..- .. .-. / --- / . ... -.-. ..- -.. --- / -.. . / -.- --- .-. -.. . -.-. --..-- / ... .. --. .- / .- --- / .-.. . ... - . .-.-.- ')
    vpl = input('Parece que este código está indicando a direção para o escudo! Para que lado você vai? (norte/sul/leste/oeste)')
    
    if vpl.lower() in ['leste','Leste']:
        print('Você foi para o leste e encontrou outro pedestal. Nele, você encontra o Escudo de Kordec! Parabéns! Agora você deve retornar com cuidado para não acordar a Árvore da manipulação.')
        bad_battle()
    elif vpl.lower() in ['sul', 'norte', 'oeste', 'Sul', 'Norte', 'Oeste']:
        print('Você foi para a direção errada e foi absolvido pela floresta... GAME OVER')
        retry = input('Tentar novamente (sim/não)')
        if retry.lower() == ['sim','Sim']:
            the_group()
        elif retry.lower() == ['não', 'nao', 'Nao', 'Não']:
            exit()
        else:
            print('Código inválido')
    else:
        print("Código inválido")
import random

player_health = 50
bad_health = 70
def bad_battle():
    global player_health, bad_health, player_name

    print("Quando você está perto da saída você sente um tremor ao seu redor. As árvores lhe cercam e você ouve uma voz dizendo:")
    print('???: Você entrou em um local no qual não lhe era bem-vindo. Agora, sofrerá as consequências.')
    print('Você se pergunta sobre quem estava falando e você acaba descobrindo que quem falava era a Árvore Manipuladora!')
    print('Árvore Manipuladora: Quem entra na Floresta do Desconhecido NUNCA vai embora!!!')
    print('A árvore avança para lhe atacar logo... Prepare-se para a batalha!')

    while player_health > 0 and bad_health > 0:
        print('Escolha seu ataque:')
        attack_choice = input("(1) Soco (2) Espada (3) Escudo ")

        if attack_choice in ['1', 'soco', 'Soco']:
            bob_attack = random.randint(15, 20)
            bad_attack = random.randint(10, 15)
        elif attack_choice in ['2', 'chute']:
            bob_attack = random.randint(20, 40)
            bad_attack = random.randint(10, 28)
        elif attack_choice in ['3', 'defender-se']:
            print("Você reflete o dano da árvore.")
            bob_attack = random.randint(15, 20)
            bad_attack = 0
        else:
            print("Escolha inválida.")
            continue

        bad_health -= bob_attack
        player_health -= bad_attack

        print(f"Galdric ataca a árvore e causa {bob_attack} de dano. A saúde da árvore agora é {bad_health}.")
        print(f"O Rei Varginbilu ataca Galdric e causa {bad_attack} de dano. A saúde de Galdric agora é {bob_health}.")
        if bad_health <= 0:
            print('Você ganhou para a Árvore Manipuladora!')
            retry = input('Deseja continuar? (sim/não) ').lower()
            if retry in ['sim', 'Sim']:
                player_health = 50
                preparation_to_final()
            elif retry in ['não', 'Não']:
                break
        elif player_health <= 0:
            print('Você perdeu para a Árvore Manipuladora... GAME OVER')
            retry = input('Deseja tentar novamente? (sim/não) ').lower()
            if retry in ['sim', 'Sim']:
                player_health = 50
                bad_health = 90
                bad_battle()
            elif retry in ['não', 'Sim']:
                break
def preparation_to_final():
    global player_name
    print('Você retorna para Watorok e informa ao sábio Airon que você coletou o Escudo de Kordec.')
    print(f'Muito bem Galdric! Agora você ter que ir a nave do Rei Varginbilu e dar um fim no reinado dele, mas vá rápido!')
    print('Você vai para a montanha Tomokiyo e ao chegar ao topo você se depara com Varginbilu equipado com a armadura extraterrestre e a espada 51 lhe aguardando para a batalha. logo... Prepare-se para a Batalha Final!!')
    gran_finale()
bob_health = 60
def gran_finale():
    global bob_health, bilu_health, player_name
    while bob_health > 0 and bilu_health > 0:
        attack_choice = input("Escolha seu ataque: (1) Soco (2) Espada (3) Escudo ")

        if attack_choice in ['1', 'soco', 'Soco']:
            bob_attack = random.randint(15, 30)
            bilu_attack = random.randint(10, 16)
        elif attack_choice in ['2', 'chute']:
            bob_attack = random.randint(20, 50)
            bilu_attack = random.randint(12, 28)
        elif attack_choice in ['3', 'defender-se']:
            print("Você se defende com o escudo e transfere o dano para Varginbilu.")
            bob_attack = random.randint(15, 30)
            bilu_attack = 0
        else:
            print("Escolha inválida.")
            continue

        bilu_health -= bob_attack
        bob_health -= bilu_attack

        print(f"Galdric ataca o Rei Variginbilu e causa {bob_attack} de dano. A saúde do Rei Varginbilu agora é {bilu_health}.")
        print(f"O Rei Varginbilu ataca Bob e causa {bilu_attack} de dano. A saúde de Bob agora é {bob_health}.")

        if bilu_health <= 0:
            print('Você venceu o malicioso Rei Varginbilu!')
            ab = input('Continuar? (sim/não) ')
            if ab in ['sim','Sim']:
                credit_roll()
            elif ab in ['não', 'nao', 'Nao', 'Não']:
                break
        elif bob_health <= 0:
            print('Você perdeu para o Rei Varginbilu... GAME OVER')
            retry = input('Deseja tentar novamente? (sim/não) ')
            if retry in ['sim','Sim']:
                bob_health = 50
                bilu_health = 100
                gran_finale()
            elif retry in ['não', 'nao', 'Nao', 'Não']:
                break
def credit_roll():
    global player_name
    print('Você retorna a Manteki e visualiza uma multidão comemorando a derrota de Varginbilu. O Rei aparece no meio da multidão e o puxa para seguir com as festividades.')
    print(f'Kairit: Obrigado Galdric por ter salvo Kanfrem! Os seus feitos não serão esquecidos por gerações!')
    print('Kairit: E como era o combinado, já esculpiram a sua escultura que irá ficar na praça central!')
    print('O reino comemorou por dias e agora você finalmente poderá tirar outro cochilo.')
    print('Créditos-----------')
    print('Criado por: Lucas Catelan------Game tester: Rogerio Cassio------Feito em  Python------29/11/2023-04/12/2023')
    print(f'Obrigado por jogar!')
    while True:
        fd = input('Deseja jogar novamente? (sim/não)')
        if fd in ['sim','Sim']:
            main_menu()
        elif fd in ['não', 'nao', 'Nao', 'Não']:
            break

main_menu() 
