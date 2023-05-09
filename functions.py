from random import randint as rnd
def genera_codice(nome_azienda):
    codice = nome_azienda
    numero = str(rnd(1000, 9999))
    codice += numero
    return codice


