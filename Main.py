from Modules import *;
"""
Issue: piedra, papel o tijera

    1- mostrar los tipos de elementos en el output ✔️ 
    2- mostrar los tipos de elementos en el output (Computadora) ✔️
    3- comparar los resultados user vs pc ✔️
    4- el sistema se para cuando se presiona [4] ✔️

"""

def main():
    # comentario de prueba para el git hub
    chooseUser = input('\n 1-piedra:\n 2-papel:\n 3-tijera:\n 4-salir:\n');
    while True:
        if chooseUser.isnumeric():
            if int(chooseUser) in range(1,4):
                
                chooseUserString = IsRockSisorsPaper(int(chooseUser));
                choosePcString = IsRockSisorsPaper();

                print("User choose: " + chooseUserString);
                print("PC choose:" + choosePcString);
                Compare(chooseUserString, choosePcString);
                chooseUser = input('\n 1-piedra:\n 2-papel:\n 3-tijera:\n 4-salir:\n');

            elif int(chooseUser) == 4:
                break;
            else:
                print("No está en las opciones requeridas");
                chooseUser = input('\n 1-piedra:\n 2-papel:\n 3-tijera:\n 4-salir:\n');
        else:
           print("No está en las opciones requeridas");
           chooseUser = input('\n 1-piedra:\n 2-papel:\n 3-tijera:\n 4-salir:\n');

    

main();