from flask import Flask, redirect, render_template

app = Flask(__name__)

# ——— HOME ———
@app.route('/')
def home():
    return render_template('home.html')


# ——— CAMERA ANATOMY ———
@app.route('/camera')
def camera():
    return render_template('camera.html')

@app.route('/back')
def back_of_camera():
    return render_template('back_of_camera.html')


# ——— LEARNING MODULES ———
@app.route('/learning')
def learning():
    return render_template('learning.html')

@app.route('/learning2')
def learning2():
    return render_template('learning2.html')


# ——— APERTURE / ISO / SHUTTER ———
@app.route('/aperture_opening')
def aperture_opening():
    return render_template('aperture.html')

@app.route('/aperture')
def aperture():
    return render_template('aperture.html')

@app.route('/aperture2')
def aperture2():
    return render_template('aperture2.html')

@app.route('/aperture3')
def aperture3():
    return render_template('aperture3.html')

@app.route('/aperturehome')
def aperturehome():
    return render_template('aperturehome.html')

@app.route('/iso_opening')
def iso_opening():
    return render_template('iso.html')

@app.route('/iso_grain')
def iso_grain():
    return render_template('iso_grain.html')

@app.route('/shutter_opening')
def shutter_opening():
    return render_template('shutter.html')


# ——— QUIZ FLOW ———

# 1) Start with MCQ
@app.route('/quiz/start')
def mcq_quiz():
    return render_template('mcq_quiz.html')

# 2) /quiz → redirect to start
@app.route('/quiz')
def quiz():
    return redirect('/quiz/start')

# 3) Questions 1–5
@app.route('/quiz/<int:qid>')
def quiz_page(qid):
    if 1 <= qid <= 5:
        return render_template(f'quiz_{qid}.html')
    elif qid == 6:
        # After question 5, go to results
        return redirect('/quiz/results')
    else:
        # Out-of-range → restart
        return redirect('/quiz/start')

# 4) Final results
@app.route('/quiz/results')
def quiz_results():
    return render_template('results.html')

# ——— MAIN ———
if __name__ == '__main__':
    app.run(debug=True)
