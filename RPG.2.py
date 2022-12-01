#todo Comando que retire acentos
print('Bem vindo ao menu de criação de personagem! \n'
      'Escolha a opção que mais se assemelha ao seu perfil!\n')
combate = input('Tipo de combate (longe, perto): ')
perfil = input('Tipo de perfil (barulhento, silencioso): ')
dano = input('Tipo de dano (Mágico, Físico): ')

if combate.lower() == "longe":
    if perfil.lower() == "barulhento":
        if dano.lower() == "magico":
            print(f"{'°' * 30}\n\t Classe: Piromante\n{'°' * 30}")
        elif dano. lower() == "fisico":
            print(f"{'°' * 30}\n\t Classe: Sniper\n{'°' * 30}")
        else:
            print(f"{'°' * 30}\n\t ERRO! TENTE NOVAMENTE!\n{'°' * 30}")

    elif perfil.lower() == "silencioso":
        if dano.lower() == "magico":
            print(f"{'°' * 30}\n\t Classe: Mago\n{'°' * 30}")
        elif dano.lower() == "fisico":
            print(f"{'°' * 30}\n\t Classe: Arqueiro\n{'°' * 30}")

        else:
            print(f"{'°' * 30}\n\t ERRO! TENTE NOVAMENTE!\n{'°' * 30}")

    else:
        print(f"{'°' * 30}\n\t ERRO! TENTE NOVAMENTE!\n{'°' * 30}")
elif combate.lower() == "perto":
    if perfil.lower() == "barulhento":
        if dano.lower() == "magico":
            print(f"{'°' * 30}\n\t Classe: Clerigo\n{'°' * 30}")
        elif dano.lower() == "fisico":
            print(f"{'°' * 30}\n\t Classe: Guerreiro\n{'°' * 30}")
        else:
            print(f"{'°' * 30}\n\t ERRO! TENTE NOVAMENTE!\n{'°' * 30}")
    elif perfil.lower() == "silencioso":
        if dano.lower() == "magico":
            print(f"{'°' * 30}\n\t Classe: Mago\n{'°' * 30}")
        elif dano.lower() == "fisico":
            print(f"{'°' * 30}\n\t Classe: Assassino\n{'°' * 30}")
        else:
            print(f"{'°' * 30}\n\t ERRO! TENTE NOVAMENTE!\n{'°' * 30}")

    else:
        print(f"{'°' * 30}\n\t ERRO! TENTE NOVAMENTE!\n{'°' * 30}")
else:
    print(f"{'°' * 30}\n\t ERRO! TENTE NOVAMENTE!\n{'°' * 30}")


# # Estrutura de dano
# import random
# vida_minima_monstro = 0
# vida_montro = 100
# arma = 10
# while vida_montro >= vida_minima_monstro:
#     print(f'Vida do monstro: {vida_montro}'.center(40,'°'))
#     dano = random.randint(1,6) * arma
#     print(F'Dano dado: {dano}'.center(40,'°'))
#     vida_montro -= dano
#     print(f'Vida do monstro: {vida_montro}'.center(40,'°'))
# print(f'Monstro derrotado!')