from random import randint

def IsRockSisorsPaper(num = None): # None = Null
    if(num != None):
        if(num == 1):
            return 'Piedra';
        elif(num == 2):
            return'Papel';
        else:
            return 'Tijera';
    else:
        if (randint(1, 3) == 1) :
            return 'Piedra';
        elif (randint(1, 3) == 2) :
            return 'Papel';
        else:
            return 'Tijera';

def Compare(chooseUser, choosePc):
    if chooseUser == choosePc:
        print("Empate")
    else:
        if chooseUser  == 'Piedra' and choosePc == 'Tijera':
            print("Gana Usuario");
        elif chooseUser  == 'Tijera' and choosePc == 'Papel':
            print("Gana Usuario");
        elif chooseUser  == 'Papel' and choosePc == 'Piedra':
            print("Gana Usuario");
        else:
            print("Gana PC");