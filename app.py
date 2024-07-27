from flask import Flask, render_template, redirect, request, flash, url_for
from surveys import satisfaction_survey

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

responses = []

@app.route('/')
def home():
    return render_template('home.html', survey=satisfaction_survey)

@app.route('/questions/<int:qid>')
def question(qid):
    if qid != len(responses):
        flash(f"Invalid question id: {qid}.")
        return redirect(url_for('question', qid=len(responses)))
    question = satisfaction_survey.questions[qid]
    return render_template('question.html', question_num=qid, question=question)

@app.route('/answer', methods=['POST'])
def answer():
    choice = request.form['answer']
    responses.append(choice)

    if len(responses) == len(satisfaction_survey.questions):
        return redirect(url_for('thank_you'))
    else:
        return redirect(url_for('question', qid=len(responses)))

@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')

if __name__ == '__main__':
    app.run(debug=True)
