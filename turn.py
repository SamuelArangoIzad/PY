def invest(txt: str):
    num_txt=len(txt)
    print('Amount Words: ', num_txt) #DICE LA CANTIDAD DE LETRAS EN EL TXT
    final_txt=' '
    for i in range(0, num_txt):
        final_txt+=txt[num_txt-i-1]
    print(final_txt)
    
while True:
    print('PANEL INTERACTION')
    print('1. Turn Words')
    print('2. Exit')
    opcion=input("Chosse A Option: ")
    if opcion == '1':
        word = input("Write: ")
        invest(word)
    elif opcion == '2':
        print('Exit')
        break
    else:
        print('Negative Option')