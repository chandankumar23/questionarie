from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# A dictionary to hold quiz subjects for the landing page
practice_tests = {
    'New ISEB PreTest Practice Test 1': 'PracticeTest1',
    'New ISEB PreTest Practice Test 2': 'PracticeTest2',
    'New ISEB PreTest Practice Test 3': 'PracticeTest3'
}

module_list = {
    'English': 'English',
    'Maths': 'Maths',
    'Science': 'Science',
    'History': 'History'
}


# Sample questions
questions = [
    {
        'id': 1,
        'question': 'What is 7*7?',
        'choices': ['44', '49', '56', '42'],
        'correct_answer': '49'
    },
    {
        'id': 2,
        'question': 'What is the capital of France?',
        'choices': ['London', 'Berlin', 'Paris', 'Rome'],
        'correct_answer': 'Paris'
    }
]

# Track user answers
user_answers = {}






# Mock user credentials
valid_credentials = {
    'username': 'admin',
    'password': 'admin'
}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == valid_credentials['username'] and password == valid_credentials['password']:
            return redirect(url_for('landing'))
    return render_template('login.html')

@app.route('/landing')
def landing():
    return render_template('landing.html', practice_tests=practice_tests)

@app.route('/PracticeTest')  # Placeholder route for the math quiz
def PracticeTest1():
    # Add your logic for the math quiz here
    return render_template('PracticeTest1.html', module_list=module_list)
    # return "Practice Test 1"

@app.route('/PracticeTest2')  # Placeholder route for the math quiz
def PracticeTest2():
    # return "Science Quiz Page"
    return render_template('PracticeTest2.html',module_list=module_list)

@app.route('/PracticeTest3')  # Placeholder route for the math quiz
def PracticeTest3():
    # Add your logic for the math quiz here
    return render_template('PracticeTest3.html',module_list=module_list)


@app.route('/English')  # Placeholder route for the math quiz
def English():
    # Add your logic for the math quiz here
    return render_template('English.html',questions=questions)
@app.route('/Maths')  # Placeholder route for the math quiz
def Maths():
    # Add your logic for the math quiz here
    return render_template('Maths.html')

@app.route('/Science')  # Placeholder route for the math quiz
def Science():
    # Add your logic for the math quiz here
    return render_template('Science.html')


@app.route('/History')  # Placeholder route for the math quiz
def History():
    # Add your logic for the math quiz here
    return render_template('History.html')


@app.route('/question/<int:qid>', methods=['GET', 'POST'])

@app.route('/result')
def result():
    score = 0
    for qid, answer in user_answers.items():
        if questions[qid - 1]['correct_answer'] == answer:
            score += 1
    return render_template('result.html', score=score, total=len(questions))


def question(qid):
    if request.method == 'POST':
        user_answer = request.form['answer']
        user_answers[qid] = user_answer
        if qid < len(questions):
            return redirect(url_for('question', qid=qid + 1))
        else:
            return redirect(url_for('result'))
    if qid <= len(questions):
        return render_template('question.html', question=questions[qid - 1])
    else:
        return redirect(url_for('result'))


if __name__ == '__main__':
    app.run(debug=True)
