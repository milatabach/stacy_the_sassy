from flask import Flask, redirect, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/camera')
def camera():
    return render_template('camera.html')

@app.route('/back')
def back_of_camera():
    return render_template('back_of_camera.html')

@app.route('/learning')
def learning():
    return render_template('learning.html')

# these three match your layout.html’s menu items
@app.route('/aperture_opening')
def aperture_opening():
    return render_template('aperture.html')

@app.route('/iso_opening')
def iso_opening():
    return render_template('iso.html')

@app.route('/shutter_opening')
def shutter_opening():
    return render_template('shutter.html')

# ——— QUIZ FLOW ———

# 1) start with MCQ
@app.route('/quiz/start')
def mcq_quiz():
    return render_template('mcq_quiz.html')

# 2) /quiz → MCQ
@app.route('/quiz')
def quiz():
    return redirect('/quiz/start')

# 3) questions 1–5
@app.route('/quiz/<int:qid>')
def quiz_page(qid):
    if 1 <= qid <= 5:
        return render_template(f'quiz_{qid}.html')
    elif qid == 6:
        # after question 5, go to results
        return redirect('/quiz/results')
    else:
        # out-of-range → restart
        return redirect('/quiz/start')

# 4) final results
@app.route('/quiz/results')
def quiz_results():
    return render_template('results.html')

if __name__ == '__main__':
    app.run(debug=True)
