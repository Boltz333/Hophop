import random


def d6():
    return random.randint(0,5)


#Simuluting the round
def Simround(Fast):
    Center = 20
    holes = [False]*5
    Players = [0]*5
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
        else:
            Current_player_index += 1

        if Current_player_index >= 5:
            Current_player_index = 0
        if Center == 0:
            break
    maxval = 0
    for player in Players:
        if maxval < player:
            maxval = player
    Winners=[]
    for idx,player in enumerate(Players):
        if maxval == player:
            Winners.append(idx)
    return Winners


#det der satans navn for en 'random simulation' jeg altid glæmmer
def startsimulator(Fast):
    Winnerscount=[0] * 5
    Runningwinners=[]
    Singlewinner=[[]for _ in range(5)]
    for i in range(1000):
        result = Simround(Fast)
        Total = 0
        for resultinindex in result:
            Winnerscount[resultinindex] += 1
        for player in Winnerscount:
            Total += player
        
        Runningwinners.append([(val/Total)for val in Winnerscount])
    for winner in Runningwinners:
        for i in range(5):
            Singlewinner[i].append(winner[i]*100)
        


    return(Singlewinner)

    

    

    

            
    
        



