from Modules import *;
"""
Issue: piedra, papel o tijera

    1- mostrar los tipos de elementos en el output ✔️ 
    2- mostrar los tipos de elementos en el output (Computadora) ✔️
    3- comparar los resultados user vs pc ✔️

"""

def main():
    
    chooseUser = input('\n 1-piedra:\n 2-papel:\n 3-tijera:\n');
    
    if chooseUser.isnumeric():
        if int(chooseUser) in range(1,4):
            chooseUserString = IsRockSisorsPaper(int(chooseUser));
            choosePcString = IsRockSisorsPaper();

            print("User choose: " + chooseUserString);
            print("PC choose:" + choosePcString);
            Compare(chooseUserString, choosePcString);

        else:
            print("NO está en el rango, BICHO DE UÑA");
    else:
        print(False);

main();