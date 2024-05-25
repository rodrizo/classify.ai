from flask import Flask, request, jsonify
from textblob import TextBlob
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    # Obtener el comentario de la petición JSON
    data = request.json
    if not data or 'frase' not in data:
        return jsonify({'error': 'No se proporcionó una frase válida.'}), 400
    
    comment = data['frase']
    
    # Traducir del español al inglés
    try:
        translated_feedback = translator.translate(comment, src='es', dest='en')
        feedback_polarity = TextBlob(translated_feedback.text).sentiment.polarity
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    # Evaluar la polaridad para determinar si es positivo o negativo
    result = 'positivo' if feedback_polarity > 0 else 'negativo'
    return jsonify({'resultado': result})

if __name__ == '__main__':
    app.run(debug=True)
