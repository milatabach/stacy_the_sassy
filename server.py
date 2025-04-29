from flask import Flask
from flask import render_template
from flask import Response, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/camera')
def camera():
    return render_template('camera.html')

@app.route('/learning')
def learning():
    return render_template('learning.html')


@app.route('/shutter')
def shutter():
    return render_template('shutter.html')

# 1) Start of quiz: MCQ
@app.route('/quiz/start')
def mcq_quiz():
    return render_template('mcq_quiz.html')

# 2) /quiz should kick off at the MCQ
@app.route('/quiz')
def quiz():
    return redirect('/quiz/start')

# 3) Dynamic handler for Stacy quizzes 1–5, then results on 6
@app.route('/quiz/<int:qid>')
def quiz_page(qid):
    if 1 <= qid <= 5:
        return render_template(f'quiz_{qid}.html')
    elif qid == 6:
        return redirect('/quiz/results')
    else:
        # any out-of-range id goes back to the MCQ
        return redirect('/quiz/start')

# 4) Final results
@app.route('/quiz/results')
def quiz_results():
    return render_template('results.html')

# other static routes
@app.route('/back')
def back_of_camera():
    return render_template('back_of_camera.html')

@app.route('/aperture')
def aperture():
    return render_template('aperture.html')

@app.route('/iso_grain')
def iso_grain():
    return render_template('iso_grain.html')

@app.route('/aperture2')
def aperture2():
    return render_template('aperture2.html')

@app.route('/aperture3')
def aperture3():
    return render_template('aperture3.html')

@app.route('/aperturehome')
def aperturehome():
    return render_template('aperturehome.html')

if __name__ == '__main__':
    app.run(debug=True)
