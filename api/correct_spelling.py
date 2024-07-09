from flask import Flask, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

def correct_spelling(text):
    blob = TextBlob(text)
    corrected_text = str(blob.correct())
    return corrected_text

@app.route('/api/correct_spelling', methods=['POST'])
def correct():
    data = request.get_json()
    if data is None or 'text' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    text = data.get('text', '')
    corrected_text = correct_spelling(text)
    return jsonify({'corrected_text': corrected_text})

if __name__ != "__main__":
    app.run()
