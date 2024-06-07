import random
seleccion = ('piedra', 'papel', 'tijera')

rondas = 0
partida_jugador = 0
partida_pc = 0


while  True:

    rondas += 1
    comp_election = random.choice(seleccion)
    print ('*' * 30)
    print ('ROUND ', rondas)
    print('Usuario:', partida_jugador,' Pc: ',partida_pc)
    user_election = input('piedra, papel o tijera => ')
    if not user_election in (seleccion):
        print('debes elegir entre una de las 3 opciones o no funciona (>.<)')
        continue
    print (f'el usuario ha elegido {user_election}')
    print (f'el equipo ha elegido {comp_election}')
    print ('*' * 30)

    if user_election == comp_election:
        print ('empate!')

    elif user_election == 'piedra':
        if comp_election == 'tijera':
            print('piedra gana a tijera')
            print('El usuario gana la ronda!!!')
            partida_jugador += 1
        if comp_election == 'papel':
            print('papel gana a piedra')
            print('El PC gana la ronda!!')
            partida_pc += 1

    elif user_election == 'papel':
        if comp_election == 'tijera':
            print('tijera  gana a papel')
            print('El PC gana la ronda!!')
            partida_pc += 1
        if comp_election == 'piedra':
            print('papel gana a piedra')
            print('El usuario gana la ronda!!!')
            partida_jugador += 1

    elif user_election == 'tijera':
        if comp_election == 'papel':
            print('tijera  gana a papel')
            print('El usuario gana la ronda!!!')
            partida_jugador += 1
        if comp_election == 'piedra':
            print('piedra gana a tijera')
            print('El PC gana la ronda!!')
            partida_pc += 1

    if partida_pc == 2:
        print('El ganador es el usuario!!')
        break

    if partida_pc == 2:
        print('El ganador es el PC!')
        break   
