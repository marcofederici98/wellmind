from flask import Flask, render_template, request
import functions
import questionario as q
import dashboard as dsh
import database as db
import mysql.connector



navbar = """  <div class="container">
    <header class="d-flex flex-wrap justify-content-center py-3 mb-4 border-bottom">
      <a href="/" class="d-flex align-items-center mb-3 mb-md-0 me-md-auto link-body-emphasis text-decoration-none">
        <span>    <img src="./static/assets/logo_black.png" alt="wellmind" width="150">
        </span>
      </a>

      <ul class="nav nav-pills">
        <li class="nav-item"><a href="/" class="nav-link">Home</a></li>
        <li class="nav-item"><a href="/about" class="nav-link">About</a></li>
        <li class="nav-item"><a href="/dashboard" class="nav-link">Dashboard</a></li>
      </ul>
    </header>
  </div>"""


global domande
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
global dash_n
dash_n = -1
global answers
answers = []

global num
num = -2

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    global answers
    answers = []
    global num
    num = -2
    global dash_n
    dash_n = -1
    return render_template('index.html', navbar = navbar)

@app.route("/echo", methods =['POST', 'GET'])
def echo():
    global num
    if num ==-2:
        num +=1
        return render_template('questionario.html', domanda = "<h2>Inserisci codice aziendale</h2>",
                               risposte = '<input type="text" name="codaz">',
                               pulsante = """<div class="navigation_btn">
      <input type="submit" value="&gt" ></form>""")
    global domande
    num += 1
    if num == 0:
        global answers
        answers = []
        try:
            answers.append(request.form['codaz'])
        except:
            return "non preso"

    if num > 0 and num <= len(domande):
        try:
            answers.append(request.form[domande[num-1]])
        except:
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
    if (num < len(domande)):
        domanda = domande[num]
        return render_template('questionario.html', numero = num + 1, progresso=q.progresso_gen(num/25*100), domanda=q.domanda_gen(domanda),
                                risposte=q.risposta_gen(domanda, num), pulsante=q.pulsante_gen(num))
    else:
        
        mydb = mysql.connector.connect(
            host = 'localhost',
            user = 'root')
        mycursor = mydb.cursor()
        answers = tuple(answers)
        lanswers = [answers]
        db.carica_dati(lanswers)
        return render_template('successo.html')
        


@app.route("/echo_prev", methods =['POST', 'GET'])
def echo_prev():
    global num
    if num >= 1:
        num -=1
    else:
        num = -2
        return echo()
    global answers
    try:
        answers.pop()
    except:
        pass
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
    global domande
    global dash_n
    try:
        dash_n += 1
        dmd, code = dsh.grafici(domande[dash_n])
        return render_template('dashboard.html', dmd = dmd, code = code, navbar = navbar)
    except:
        dash_n = len(domande) - 1
        dmd, code = dsh.grafici(domande[dash_n])
        return render_template('dashboard.html', dmd = dmd, code = code, navbar = navbar)

@app.route('/dashboard_prev', methods=['GET', 'POST'])
def dashboard_prev():
    global domande
    global dash_n
    try:
        dash_n -= 1
    except:
        dash_n = 0
    if dash_n < 0:
        dash_n = 0
    dmd, code = dsh.grafici(domande[dash_n])
    return render_template('dashboard.html', dmd = dmd, code = code, navbar = navbar)

@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('contributors.html', navbar = navbar)


if __name__ == '__main__':
    app.run(debug=True)

'''ciao'''