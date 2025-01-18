# Programma che prevede il vincitore di Sanremo2025
# interpretando i tuoi sogni

i = 0
valSogno = 0

sogno = input("\nCosa hai appena sognato? ")

# interpretazione: somma valori ascii dei singoli caratteri
for char in sogno:
    valSogno += ord(char)

# oppure
# while i < len(sogno) :
#    valSogno = valSogno + (ord(sogno[i]))
#    i += 1

#assegno il cantante vincente in base alla classe di resto
idCantante = valSogno % 30
if idCantante == 0: cantante = "Achille Lauro"
elif idCantante == 1: cantante = "Bresh"
elif idCantante == 2: cantante = "Brunori Sas"
elif idCantante == 3: cantante = "Clara"
elif idCantante == 4: cantante = "Coma_Cose"
elif idCantante == 5: cantante = "Elodie"
elif idCantante == 6: cantante = "Emis Killa"
elif idCantante == 7: cantante = "Fedez"
elif idCantante == 8: cantante = "Francesca Michielin"
elif idCantante == 9: cantante = "Francesco Gabbani"
elif idCantante == 10: cantante = "Gaia"
elif idCantante == 11: cantante = "Giorgia"
elif idCantante == 12: cantante = "Irama"
elif idCantante == 13: cantante = "Joan Thiele"
elif idCantante == 14: cantante = "Lucio Corsi"
elif idCantante == 15: cantante = "Marcella Bella"
elif idCantante == 16: cantante = "Massimo Ranieri"
elif idCantante == 17: cantante = "Modà"
elif idCantante == 18: cantante = "Noemi"
elif idCantante == 19: cantante = "Olly"
elif idCantante == 20: cantante = "Rkomi"
elif idCantante == 21: cantante = "Rocco Hunt"
elif idCantante == 22: cantante = "Rose Villain"
elif idCantante == 23: cantante = "Sarah Toscano"
elif idCantante == 24: cantante = "Serena Brancale"
elif idCantante == 25: cantante = "Shablo con Guè, Joshua e Tormento"
elif idCantante == 26: cantante = "Simone Cristicchi"
elif idCantante == 27: cantante = "The Kolors"
elif idCantante == 28: cantante = "Tony Effe"
else: cantante = "Willie Peyote"

# stampa la previsione
print(f"Il tuo sogno vale {valSogno} euro!!!")
print(f"Secondo l'astrologo Paolo FireFox, la vittoria di Sanremo andrà a {cantante}!!!")
print(f"Schierare {cantante} al FantaSanremo ti costerà almeno {idCantante} Baud*.")

