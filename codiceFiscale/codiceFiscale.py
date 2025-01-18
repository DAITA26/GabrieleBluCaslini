class StringaDiTesto:

    def __init__(self, nome, cognome):

        self.cognome = cognome
        self.nome = nome
        self.cognomeFiscale = self.doGeneralitaFiscale(self.cognome)
        self.nomeFiscale = self.doGeneralitaFiscale(self.nome)

        #debug
        print(f"cognome: {self.cognome}")
        print(f"nome: {self.nome}")
        print(f"cognomeFiscale: {self.cognomeFiscale}")
        print(f"nomeFiscale: {self.nomeFiscale}")

    def trova(self, gruppoDiLettere, parola):

        listaGruppoDiLettere = []

        for lettera in parola:
            for char in gruppoDiLettere:
                if lettera == char:
                    listaGruppoDiLettere.append(lettera)
                    break

        return listaGruppoDiLettere

    def ordina(self, parola):

        consonanti = ("B", "C", "D", "F", "G", "H", "J", "K", "L", "M",
                      "N", "P", "Q", "R", "S", "T", "V", "Z", "X", "Y", "W")
        vocali = ("A", "E", "I", "O", "U")

        listaConsonanti = self.trova(consonanti, parola)
        if parola == self.nome and len(listaConsonanti) > 3:
            listaConsonanti.pop(1)
        listaVocali = self.trova(vocali, parola)

        return listaConsonanti + listaVocali + ["X", "X", "X"]

    def doGeneralitaFiscale(self, generalita):

        generalitaFiscale = []
        lettereOrdinateGeneralita = self.ordina(generalita)

        for i in range(3):
            generalitaFiscale.append(lettereOrdinateGeneralita[i])

        return generalitaFiscale

    #ANCORA DA GESTIRE CARATTERI NON LETTERE

#debug
obj3 = StringaDiTesto("GABRIELE",  "CASLINI")
print("-------------------------------------------------------------")
obj4 = StringaDiTesto("LUCIA", "LI")
print("-------------------------------------------------------------")
obj5 = StringaDiTesto("DAVIDE", "CESANA")
print("-------------------------------------------------------------")
obj6 = StringaDiTesto("VALENTINA", "SPAGNOLI")
print("-------------------------------------------------------------")
obj7 = StringaDiTesto("AI", "UW")