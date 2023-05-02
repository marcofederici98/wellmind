import pandas as pd
diz_col = {'mh_coverage_flag': "Il tuo datore di lavoro offre benefits legati al benessere e alla salute mentale?",
 'mh_coverage_awareness_flag': "Conosci le opzioni di assistenza per la salute mentale forniti dal tuo datore di lavoro?",
 'mh_employer_discussion': "Il tuo datore di lavoro ha mai parlato formalmente di salute mentale (ad esempio, nell'ambito di una campagna di benessere o di altre comunicazioni ufficiali)?",
 'mh_resources_provided': 'Il tuo datore di lavoro offre risorse per saperne di più sui problemi di salute mentale e sulle possibilità di chiedere aiuto?',
 'mh_anonimity_flag': "Il tuo anonimato è protetto se scegli di usufruire delle risorse per la salute mentale o del trattamento per l'abuso di sostanze, fornite dal tuo datore di lavoro?",
 'mh_medical_leave': 'Se un problema di salute mentale ti ha spinto a richiedere un congedo medico dal lavoro, chiedere tale congedo sarebbe:',
 'mh_discussion_neg_impact': 'Pensi che parlare di un disturbo mentale con il tuo datore di lavoro possa avere conseguenze negative?',
 'mh_discussion_cowork': 'Parlresti di un disturbo della salute mentale con i tuoi colleghi?',
 'mh_discussion_supervis': 'Ti sentiresti a tuo agio a parlare di un disturbo della salute mentale con il tuo supervisore?',
 'mh_conseq_coworkers': 'Hai mai sentito parlare o osservato conseguenze negative per i colleghi che hanno parlato apertamente di problemi di salute mentale sul posto di lavoro?',
 'mh_eq_ph_employer': 'Ritieni che il tuo datore di lavoro prenda la salute mentale con la stessa serietà della salute fisica?',
 'prev_mh_benefits': 'I tuoi precedenti datori di lavoro hanno mai fornito benefits per la salute mentale?',
 'future_mh_specification': 'Dichiareresti un problema di salute mentale con un potenziale datore di lavoro in un colloquio?',
 'mh_hurt_on_career': 'Ritieni che essere identificato come una persona con un problema di salute mentale danneggerebbe la tua carriera?',
 'mh_neg_view_cowork': 'Pensi che i membri del team/colleghi ti vedrebbero in modo più negativo se sapessero che soffri di un disturbo di salute mentale?',
 'mh_sharing_friends/fam_flag': 'Quanto saresti aperto nel condividere con amici e familiari che soffri di un disturbo della salute mentale?',
 'mh_bad_response_workplace': 'Hai osservato o sperimentato una risposta negativa o mal gestita a un problema di salute mentale nel tuo posto di lavoro attuale o precedente?',
 'mh_family_hist': 'Ci sono persone nella tua famiglia che hanno sofferto di disturbi legati alla salute mentale?',
 'mh_disorder_past': 'Hai avuto un disturbo della salute mentale in passato?',
 'mh_disorder_current': 'Attualmente soffri di un disturbo della salute mentale?',
 'mh_diagnos_proffesional': 'Ti è stato diagnosticato un disturbo di salute mentale da un medico?',
 'mh_sought_proffes_treatm': 'Hai mai richiesto un trattamento per un problema di salute mentale da un professionista?',
 'sex': 'Qual è il tuo sesso?',
 'remote_flag': 'Lavori da remoto?',
 'age': "Qual è la tua fascia d'età?"}

df = pd.read_csv(r".\data\output\df_tradotto.csv")
df = df.drop('Unnamed: 0', axis = 1)
"""mh_medical_leave mh_sharing_friends/fam_flag"""
diz_domanda1 = {'Somewhat open' : "Abbastanza aperto", "Very open" : "Molto aperto", "Neutral": "Neutrale",
                "Not open at all" : "Per niente aperto", "Somewhat not open" : "Poco aperto"
}
diz_domanda2 = {
    "Very easy": "Molto facile", "Somewhat easy": "Abbastanza facile", "Very difficult": "Molto difficile",
    "Somewhat difficult": "Abbastanza difficile", "Neither easy nor difficult" : "Neutrale"  
}

df['mh_medical_leave'] = df['mh_medical_leave'].replace(diz_domanda2)
df['mh_sharing_friends/fam_flag'] = df['mh_sharing_friends/fam_flag'].replace(diz_domanda1)

codice_azienda = "Inserisci il codice aziendale:"

def quest_gen():
    code = ""
    code += '<form action="/echo" method="POST" class="quest">'
    code += '<h3>Inserire codice aziendale: <h3>'
    code += f'<input type="text" id="codiceaz" name="codiceaz"><br>'
    for i in range(df.shape[1]):
        code += f'<h3>{i+1}. {diz_col[df.columns[i]]}</h3>'
        risposte = df[df.columns[i]].unique()
        if i == 5:
            code += "<p>Molto difficle - Difficile - Neutrale - Facile - Molto facile</p><br>"
            code += '<span>Molto difficile</span>'
            code += f'<input type="range" name="{df.columns[i]}" min="0" max="4" value="0" step="1" onchange="updateTextInput(this.value);">'
            code += '<span>Molto facile</span>'
        elif i == 7:
            code += "<p>Molto difficile - Difficile - Neutrale - Facile - Molto facile</p><br>"
            code += '<span>Molto difficile</span>'
            code += f'<input type="range" name="{df.columns[i]}" min="0" max="4" value="0" step="1" onchange="updateTextInput(this.value);">'
            code += '<span>Molto facile</span>'
        elif i == 15:
            code += "<p>Per niente aperto - Poco aperto - Neutrale - Abbastanza aperto - Estremamente aperto</p><br>"
            code += '<span> Per niente aperto</span>'
            code += f'<input type="range" name="{df.columns[i]}" min="0" max="4" value="0" step="1" onchange="updateTextInput(this.value);">'
            code += '<span> Estremamente aperto</span>'
        else:
            for j in risposte:
                code += f'<input type="radio" name="{df.columns[i]}" value="{j}">{j}'
        code+= "<br>"
    code += '<br><input type="submit" value="Invia" ></form>'
    return code


def progresso_gen(prog=0):
    code = f'<div class="w3-blue" style="height:24px;width: {prog}%"></div>'

    code = f'<div class="progress-bar" style="width: {prog}%;"> </div>'

    return code
def domanda_gen(domanda):
    code = f'<h2>{diz_col[domanda]}</h2>'
    return code
def risposta_gen(domanda, n=0):
    risposte = df[domanda].unique()
    code = ""
    if n == 5:
        code += "<p>Molto difficile - Difficile - Neutrale - Facile - Molto facile</p><br>"
        code += '<span>Molto difficile</span>'
        code += f'<input type="range" name="{domanda}" min="0" max="4" value="0" step="1" onchange="updateTextInput(this.value);">'
        code += '<span>Molto facile</span>'
    elif n == 15:
        code += "<p>Per niente aperto - Poco aperto - Neutrale - Abbastanza aperto - Estremamente aperto</p><br>"
        code += '<span> Per niente aperto</span>'
        code += f'<input type="range" name="{domanda}" min="0" max="4" value="0" step="1" onchange="updateTextInput(this.value);">'
        code += '<span> Estremamente aperto</span>'
    else:
        code += "<p>"
        for r in risposte:
            code += f'<input type="radio" name="{domanda}" value="{r}">{r}'
    code += "</p><br>"
    return code


def pulsante_gen(n):
    code = '<input type="submit" value="&gt" ></form>'
    code = """<div class="navigation_btn"><a href="/echo_prev">&lt;</a>
      <span class="divider_btn">|</span>
      <input type="submit" value="&gt" ></form>"""
    return code



