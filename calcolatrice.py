operazione = input("""Quale operazione vuoi fare?
s: somma
d: differenza
p: prodotto
r: rapporto
""")
# Diamo per scontato che non ci siano errori di digitazione
op1 = float(input("Inserisci il primo operando:"))
op2 = float(input("Inserisci il secondo operando:"))
# Diamo per scontato che si digitino int o float
if operazione == "s":
    risultato = op1 + op2
elif operazione == "d":
    risultato = op1 - op2
elif operazione == "p":
    risultato = op1 * op2
elif operazione == "r":
    risultato = op1 / op2 if op2 != 0 else "impossibile"
else: risultato = "operazione non supportata!!"
print(risultato)
