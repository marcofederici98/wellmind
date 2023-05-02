import pandas as pd
df = pd.read_csv('data/output/df_tradotto.csv').drop('Unnamed: 0', axis = 1)
diz_col = {'mh_coverage_flag': "Il tuo datore di lavoro offre benefits legati al benessere e alla salute mentale?",
 'mh_coverage_awareness_flag': "Conosci le opzioni di assistenza per la salute mentale forniti dal tuo datore di lavoro?",
 'mh_employer_discussion': "Il tuo datore di lavoro ha mai parlato formalmente di salute mentale (ad esempio, nell'ambito di una campagna di benessere o di altre comunicazioni ufficiali)?",
 'mh_resources_provided': 'Il tuo datore di lavoro offre risorse per saperne di più sui problemi di salute mentale e sulle possibilità di chiedere aiuto?',
 'mh_anonimity_flag': "Il tuo anonimato è protetto se scegli di usufruire delle risorse per la salute mentale o del trattamento per l'abuso di sostanze, fornite dal tuo datore di lavoro?",
 'mh_medical_leave': 'Se un problema di salute mentale ti ha spinto a richiedere un congedo medico dal lavoro, chiedere tale congedo sarebbe:',
 'mh_discussion_neg_impact': 'Pensi che parlare di un disturbo mentale con il tuo datore di lavoro possa avere conseguenze negative?',
 'mh_discussion_cowork': 'Parleresti di un disturbo della salute mentale con i tuoi colleghi?',
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


def grafici(domanda):
    dmd= diz_col[domanda]
    conto = (df[domanda].value_counts(normalize = True)*100).astype(int)
    valori = conto.values
    indici = conto.index
    code = ""
    for i in range(len(valori)):
        code += f"""
            <div class="w3-border">
      <div><p>{indici[i]}</p></div><div class="progress-bar" style="height:30px;width:{valori[i]}%">{valori[i]}%</div>
    </div>
    """
    return dmd, code
    