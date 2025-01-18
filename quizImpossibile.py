import random

# dobbiamo fare 5 domande, ciascuna con 4 opzioni di risposta
# le domande vanno salvate in una tupla
# le opzioni vanno salvate in un dizionario
# per ogni domanda la macchina sceglie a caso una risposta giusta,
# e si salva la risposta in una lista
# per ogni domanda viene richiesto all'utente di scegliere una risposta
# e quella risposta viene salvata in una lista
# per ogni domanda bisogna fare il confronto tra le due risposte comunicando giusto o sbagliato
# alla fine bisogna far vedere il punteggio (percentuale di risposte giuste)

domande = ("A quale COLORE sto pensando?",
           "A quale CITTA' sto pensando?",
           "A quale FRUTTO sto pensando?",
           "A quale ANIMALE sto pensando?",
           "A quale PROFESSIONE sto pensando?")

risposte = ("A", "B", "C", "D")

colori = {"A": "magenta",
          "B": "vinaccia",
          "C": "bordeaux",
          "D": "cremisi"}

citta = {"A": "milano",
         "B": "roma",
         "C": "bari",
         "D": "catania"}

frutti = {"A": "mango",
          "B": "cocco",
          "C": "mela",
          "D": "pera"}

animali = {"A": "elefante",
          "B": "volpe",
          "C": "leone",
          "D": "tigre"}

professioni = {"A": "idraulico",
               "B": "cameriere",
               "C": "manager",
               "D": "avvocato"}

def incolonnaOpzioni(dictOpz):
    stringaOpzioni = "A: " + dictOpz["A"] + "\nB: " + dictOpz["B"] + "\nC: " + dictOpz["C"] + "\nD: " + dictOpz["D"]
    return stringaOpzioni

tutteLeRisposte = (colori, citta, frutti, animali, professioni)

elencoRispCPU = []
elencoRispUSER = []
giuste = 0

for i in range(5):
    rispCPU = risposte[random.randint(0, 3)]
    elencoRispCPU.append(rispCPU)
    print(elencoRispCPU[i])

for i in range(5):
    print("\n" + domande[i])
    isRispUSERvalid = False
    while not isRispUSERvalid:
        rispUSER = input(incolonnaOpzioni(tutteLeRisposte[i]) + " ").strip().upper()
        if rispUSER == "A" or rispUSER == "B" or rispUSER == "C" or rispUSER == "D":
            isRispUSERvalid = True
            elencoRispUSER.append(rispUSER)
        else:
            print("Opzione non valida. Scegli tra A, B, C, D:")

for i in range(5):
    if elencoRispCPU[i] == elencoRispUSER[i]:
        print("GIUSTO! Hai indovinato!")
        giuste += 1
    else:
        print("SBAGLIATO! Peccato...")

print(str(int(giuste * 100 / 5)) + "% di risposte esatte!")








