from flask import Flask, render_template, request, jsonify
import random

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
    random_passage = random.choice(passages)
    return render_template('index.html', passage=random_passage)

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

if __name__ == '__main__':
    app.run(debug=True)

