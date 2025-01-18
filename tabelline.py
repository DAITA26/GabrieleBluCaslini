# Scrivo un programma che mi mostra le tabelline da 1 a 10

# Chiedo quale tabellina voglio sapere
tabellina = int(input("""
Quale tabellina vuoi sapere? 
Inserisci un intero tra 1 e 10
""").strip())

# Stampo la tabellina richiesta
print(f"La tabellina del n°{tabellina} è")
for fattore in range(1,11):
    print(fattore * tabellina, end = " ")