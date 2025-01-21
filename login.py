#Dizionario Nome Utente & Password
utentePass = {
    'MarioMerlo85': 'Merluzzo1',
    'Jacopone77': 'Passwordissima',
    'Lucano123': 'Pippoide201'
}

#simulazione del signup
def sign_up():
    # Richiesta dell'username
    username = input("Inserisci il tuo username: ")

    # Richiesta della password (la password sarà visibile)
    password = input("Inserisci la tua password: ")

    # Apre il file in modalità append per aggiungere i dati
    with open("utenti.txt", "a") as file:
        file.write(f"{username}:{password}\n")

    print(f"Registrazione completata per {username}")

sign_up()

def login():
    username = input("Inserisci il tuo username: ")
    password = input("Inserisci la tua password: ")

    try:
        stored_password = utentePass.get(username)

        if stored_password == password:
            print("Login effettuato con successo!")
        else:
            raise ValueError("Password errata")

    except KeyError:
        print("Nome utente non esistente.")

    except ValueError as ve:
        print(str(ve))

    except Exception as ex:
        print(f"Errore imprevisto!: {ex}")


#Esecuzione
login()