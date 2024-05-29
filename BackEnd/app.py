from flask import Flask, request, jsonify
from flask_cors import CORS
from textblob import TextBlob
from googletrans import Translator

app = Flask(__name__)
CORS(app)  # Habilita CORS para todos los dominios en todas las rutas

translator = Translator()

@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    data = request.json
    if not data or 'frase' not in data:
        return jsonify({'error': 'No se proporcionó una frase válida.'}), 400
    
    comment = data['frase']
    
    try:
        translated_feedback = translator.translate(comment, src='es', dest='en')
        feedback_polarity = TextBlob(translated_feedback.text).sentiment.polarity
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    result = 'positivo' if feedback_polarity > 0 else 'negativo'
    return jsonify({'resultado': result})

if __name__ == '__main__':
    app.run(debug=True)
