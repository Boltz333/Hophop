import random


def d6():
    return random.randint(0,5)


#Simuluting the round
def Simround(Fast, Slow, Numer_players):
    Center = 20
    holes = [False]*5
    Players = [0]*Numer_players
    Current_player_index = 0
    while True:
        dice = d6()
        if dice == 0: #this is the Rabbit on the die
            Center -= 1
            Players[Current_player_index] += 1

        else:
            if holes[dice-1]:
                Players[Current_player_index] += 1
                holes[dice-1] = False

            else:
                Center -= 1
                holes[dice-1] = True
        if Fast and dice == 0:
            pass
        elif Slow and dice == 0:
            Current_player_index -= 1
            Center += 1
            pass
        else:
            Current_player_index += 1

        if Current_player_index >= Numer_players:
            Current_player_index = 0
        elif Current_player_index < 0:
            Current_player_index = Numer_players -1
        if Center == 0:
            break
    maxval = max(Players)
    Winners = [idx for idx, player in enumerate(Players) if player == maxval]
    return Winners


#det der monte carlo simulation
def startsimulator(Fast, Slow, Numer_players = 5, Number_of_simulations = 1000):
    Winnerscount=[0] * Numer_players
    Runningwinners=[]
    Singlewinner=[[]for _ in range(Numer_players)]
    for _ in range(Number_of_simulations):
        result = Simround(Fast, Slow, Numer_players)
        Total = 0
        for resultinindex in result:
            Winnerscount[resultinindex] += 1

        Total = sum(Winnerscount)
        Runningwinners.append([val / Total for val in Winnerscount])

    for winner in Runningwinners:
        for i in range(Numer_players):
            Singlewinner[i].append(winner[i]*100)

        


    return(Singlewinner)

    

    

    

            
    
        



