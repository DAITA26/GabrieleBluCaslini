import random

# Gioca a carta-forbice-sasso contro il computer
print("\nProva a battere il computer a morra cinese!!")
play = True
vittorie = 0
sconfitte = 0

# Imposta il ciclo per poter fare più partite
while play:

    # situazione all'inizio di ogni nuova sfida:
    mossaTua = ""
    mossaCPU = ""
    isMossaValida = False
    again = ""
    isAgainChiuso = False

    # Scegli la tua mossa
    while not isMossaValida:
        mossaTua = input("\nCosa scegli? 'sasso', 'carta' o 'forbice'? ").strip().lower()
        isMossaValida = (mossaTua == "sasso" or mossaTua == "carta" or mossaTua == "forbice")
        if not isMossaValida: print("Mossa non valida. Riprova. ")

    # Il computer sceglie la sua mossa
    idCPU = random.randint(0,2)
    if idCPU == 0: mossaCPU = "sasso"
    elif idCPU == 1: mossaCPU = "carta"
    else: mossaCPU = "forbice"
    print("\nCARTA, FORBICE, SASSO!!!!")
    print(f"Il computer ha scelto {mossaCPU}...")

    # Confronta le mosse
    isPareggio = (mossaTua == mossaCPU)
    isVittoria = (mossaTua == "carta" and mossaCPU == "sasso"
                or mossaTua == "forbice" and mossaCPU == "carta"
                or mossaTua == "sasso" and mossaCPU == "forbice")

    # Stampa l'esito
    if isPareggio: print("pareggio!")
    elif isVittoria: print("Hai vinto! :)")
    else: print("Hai perso :(")

    # Conteggio vittorie
    if isVittoria: vittorie += 1
    elif not isPareggio: sconfitte += 1
    print(f"Tu vs computer {vittorie}-{sconfitte}")

    # Ripeti la partita
    while not isAgainChiuso:
        print("\nVuoi giocare ancora?")
        again = input("rispondi 'si' oppure 'no'. ").strip().lower()
        isAgainChiuso = (again == "si" or again == "no")
        if not isAgainChiuso: print("Risposta non valida. Riprova. ")
    if again == "no": play = False

else: print("\nGrazie per aver giocato. A presto! =owo=")