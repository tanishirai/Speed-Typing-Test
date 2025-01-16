from flask import Flask, render_template, request, jsonify, redirect, url_for
import random
import database

app = Flask(__name__)

passages = [
    "The quick brown fox jumps over the lazy dog.",
    "A journey of a thousand miles begins with a single step.",
    "To be or not to be, that is the question.",
    "All that glitters is not gold.",
    "The only way to do great work is to love what you do."
]

@app.route('/')
def home():
    varUser = request.args.get('varUser', 'Login')
    random_passage = random.choice(passages)
    return render_template('index.html', passage=[random_passage,varUser])

@app.route('/submit', methods=['POST'])
def submit():
    typed_text = request.json['typedText']
    passage = request.json['passage']
    time_taken = request.json['timeTaken']

    # Calculate WPM
    words = len(typed_text.split())
    wpm = (words / time_taken) * 60 if time_taken > 0 else 0

    # Calculate accuracy
    correct_chars = sum(1 for a, b in zip(typed_text, passage) if a == b)
    accuracy = (correct_chars / len(passage)) * 100 if len(passage) > 0 else 0

    return jsonify({'wpm': wpm, 'accuracy': accuracy})

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        newUser = 'newUser' in request.form

        # print(newUser)
        if(newUser):
            database.initialiseNewUser(username,password)

            if(not database.checkUniqueUser(username)):
                return redirect(url_for('home', varUser=username))
            else:
                return redirect(url_for('login'))
        else:
            if(database.checkUniqueUser(username)):
                return redirect(url_for('home', varUser=username))
            else:
                return redirect(url_for('login'))
            
    return render_template("login.html")

@app.route('/sync', methods=['POST'])
def sync():
    # Get data from the POST request
    data = request.get_json()
    username = data.get('username')
    wpm = data.get('wpm')
    accuracy = data.get('accuracy')

    # Process or store the data as needed (e.g., save to database)
    # print(f"Sync data: Username: {username}, WPM: {wpm}, Accuracy: {accuracy}")

    database.uploadCurrentData(username,wpm,accuracy)

    # Respond with success message
    return jsonify({'status': 'success', 'message': 'Data synced successfully'}), 200


@app.route("/history")
def history():
    return render_template("user_history.html")

if __name__ == '__main__':
    app.run(debug=True)

