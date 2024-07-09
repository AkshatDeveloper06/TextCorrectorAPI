from flask import Flask, request, jsonify
import language_tool_python

app = Flask(__name__)
tool = language_tool_python.LanguageTool('en-US')

def correct_grammar(text):
    matches = tool.check(text)
    corrected_text = language_tool_python.utils.correct(text, matches)
    return corrected_text

@app.route('/api/correct_grammar', methods=['POST'])
def correct():
    data = request.get_json()
    if data is None or 'text' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    text = data.get('text', '')
    corrected_text = correct_grammar(text)
    return jsonify({'corrected_text': corrected_text})

if __name__ == "__main__":
    app.run()
