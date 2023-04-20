from flask import Flask, render_template, request
import functions
import questionario as q

global answers
answers = []

global num
num = -1

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    global num
    num = -1
    return render_template('index.html')

@app.route("/echo", methods =['POST', 'GET'])
def echo():
    global num
    num += 1
    """if num > 0 and num < 25:
        global answers
        #answers.append(request.form[domanda])"""
    domande = ['mh_coverage_flag',
    'mh_coverage_awareness_flag',
    'mh_employer_discussion',
    'mh_resources_provided',
    'mh_anonimity_flag',
    'mh_medical_leave',
    'mh_discussion_neg_impact',
    'mh_discussion_cowork',
    'mh_discussion_supervis',
    'mh_conseq_coworkers',
    'mh_eq_ph_employer',
    'prev_mh_benefits',
    'future_mh_specification',
    'mh_hurt_on_career',
    'mh_neg_view_cowork',
    'mh_sharing_friends/fam_flag',
    'mh_bad_response_workplace',
    'mh_family_hist',
    'mh_disorder_past',
    'mh_disorder_current',
    'mh_diagnos_proffesional',
    'mh_sought_proffes_treatm',
    'sex',
    'remote_flag',
    'age']
    if (num < len(domande)):
        domanda = domande[num]
        return render_template('questionario.html', numero = num + 1, progresso=q.progresso_gen(num/25*100), domanda=q.domanda_gen(domanda),
                                risposte=q.risposta_gen(domanda, num), pulsante=q.pulsante_gen(num))
    else:
        return f'{answers}'
@app.route("/echo_prev", methods =['POST', 'GET'])
def echo_prev():
    global num
    num -= 1
    domande = ['mh_coverage_flag',
 'mh_coverage_awareness_flag',
 'mh_employer_discussion',
 'mh_resources_provided',
 'mh_anonimity_flag',
 'mh_medical_leave',
 'mh_discussion_neg_impact',
 'mh_discussion_cowork',
 'mh_discussion_supervis',
 'mh_conseq_coworkers',
 'mh_eq_ph_employer',
 'prev_mh_benefits',
 'future_mh_specification',
 'mh_hurt_on_career',
 'mh_neg_view_cowork',
 'mh_sharing_friends/fam_flag',
 'mh_bad_response_workplace',
 'mh_family_hist',
 'mh_disorder_past',
 'mh_disorder_current',
 'mh_diagnos_proffesional',
 'mh_sought_proffes_treatm',
 'sex',
 'remote_flag',
 'age']
    domanda = domande[num]
    return render_template('questionario.html', numero = num +1, progresso=q.progresso_gen(num/25*100), domanda=q.domanda_gen(domanda),
                            risposte=q.risposta_gen(domanda, num), pulsante=q.pulsante_gen(num))

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template('dashboard.html', quest = questionario.quest_gen())


if __name__ == '__main__':
    app.run(debug=True)