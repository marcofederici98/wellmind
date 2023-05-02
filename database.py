import mysql.connector
import pandas as pd
from random import randint as rnd

df = pd.read_csv('data/output/df_tradotto.csv')
df = df.drop('Unnamed: 0', axis = 1)

lista_tuple = []
for j in range(len(df)):
    tupla = []
    tupla.append('0000')
    for i in df:
        tupla.append(str(df[i][j]))
    tupla = tuple(tupla)
    lista_tuple.append(tupla)
#print(lista_tuple)

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root'
)
mycursor = mydb.cursor()

try:
    mycursor.execute("CREATE DATABASE WELLMIND")
except:
    pass
mycursor.execute("USE WELLMIND")
try:
    sql1 = "CREATE TABLE QUESTIONARIO(ID int NOT NULL AUTO_INCREMENT, codice_azienda VARCHAR(255),mh_coverage_flag VARCHAR(255),mh_coverage_awareness_flag VARCHAR(255),mh_employer_discussion VARCHAR(255),mh_resources_provided VARCHAR(255),mh_anonimity_flag VARCHAR(255),mh_medical_leave VARCHAR(255),mh_discussion_neg_impact VARCHAR(255),mh_discussion_cowork VARCHAR(255),mh_discussion_supervis VARCHAR(255),mh_conseq_coworkers VARCHAR(255),mh_eq_ph_employer VARCHAR(255),prev_mh_benefits VARCHAR(255),future_mh_specification VARCHAR(255),mh_hurt_on_career VARCHAR(255),mh_neg_view_cowork VARCHAR(255),mh_sharing_friends_fam_flag VARCHAR(255),mh_bad_response_workplace VARCHAR(255),mh_family_hist VARCHAR(255),mh_disorder_past VARCHAR(255),mh_disorder_current VARCHAR(255),mh_diagnos_proffesional VARCHAR(255),mh_sought_proffes_treatm VARCHAR(255),sex VARCHAR(255),remote_flag VARCHAR(255),age VARCHAR(255),PRIMARY KEY (ID));"
    mycursor.execute(sql1)
    mydb.commit()
except:
    pass
"""
sql1A = "INSERT INTO QUESTIONARIO (codice_azienda, mh_coverage_flag,mh_coverage_awareness_flag,mh_employer_discussion,mh_resources_provided,mh_anonimity_flag,mh_medical_leave,mh_discussion_neg_impact,mh_discussion_cowork,mh_discussion_supervis,mh_conseq_coworkers,mh_eq_ph_employer,prev_mh_benefits,future_mh_specification,mh_hurt_on_career,mh_neg_view_cowork,mh_sharing_friends_fam_flag,mh_bad_response_workplace,mh_family_hist,mh_disorder_past,mh_disorder_current,mh_diagnos_proffesional,mh_sought_proffes_treatm,sex,remote_flag,age) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
mycursor.executemany(sql1A, lista_tuple)
mydb.commit()
"""
mycursor.execute("SELECT * FROM QUESTIONARIO;")
myresult = mycursor.fetchall()
data_result = pd.DataFrame(myresult)

def carica_dati(dato):
    sql = "INSERT INTO QUESTIONARIO (codice_azienda, mh_coverage_flag,mh_coverage_awareness_flag,mh_employer_discussion,mh_resources_provided,mh_anonimity_flag,mh_medical_leave,mh_discussion_neg_impact,mh_discussion_cowork,mh_discussion_supervis,mh_conseq_coworkers,mh_eq_ph_employer,prev_mh_benefits,future_mh_specification,mh_hurt_on_career,mh_neg_view_cowork,mh_sharing_friends_fam_flag,mh_bad_response_workplace,mh_family_hist,mh_disorder_past,mh_disorder_current,mh_diagnos_proffesional,mh_sought_proffes_treatm,sex,remote_flag,age) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
    mycursor.executemany(sql, dato)
    mydb.commit()
    return None


try:
    sql1 = "CREATE TABLE CODICE(ID int NOT NULL AUTO_INCREMENT, Codice VARCHAR(255), PRIMARY KEY (ID));"
    mycursor.execute(sql1)
    mydb.commit()
except:
    pass

def carica_codice(codice):
    sql = "INSERT INTO CODICE (codice) VALUES(%s);"
    mycursor.executemany(sql, [(codice,)])
    mydb.commit()
    return None


def scarica_codice():
    mycursor.execute("SELECT * FROM CODICE;")
    myresult = mycursor.fetchall()
    return myresult
risultato = scarica_codice()

def lista_codici(risultatox):
    lista = []
    for i in risultatox:
        lista.append(i[1])
    return lista

def codice_presente(codice, lista):
    if codice in lista:
        return False
    else:
        return True
    
def genera_codice():
    codice = ""
    for i in range(6):
        codice += str(rnd(0,9))
    return codice

def codice_pipeline():
    risultato = scarica_codice()
    lista = lista_codici(risultato)
    codice = genera_codice()
    if codice_presente(codice, lista):
        carica_codice(codice)
        return codice
    else:
        codice_pipeline()
    



