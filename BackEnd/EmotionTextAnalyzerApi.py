from textblob import TextBlob
from googletrans import Translator

# Ejemplo de comentarios en español
feedbacks = ['No me encanta la aplicación, no es increíble',
             "La experiencia fue horrible",
             "Esta aplicación es realmente útil",
             "Maldita sea, la aplicación es una porquería",
             "Por favor no descargues la aplicación, te arrepentirás"]

positive_feedbacks = []
negative_feedbacks = []

translator = Translator()

for feedback in feedbacks:
    # Traduciendo del español al inglés
    translated_feedback = translator.translate(feedback, src='es', dest='en')
    
    # Análisis de sentimiento en el texto traducido
    feedback_polarity = TextBlob(translated_feedback.text).sentiment.polarity
    
    if feedback_polarity > 0:
        positive_feedbacks.append(feedback)
    else:
        negative_feedbacks.append(feedback)

print('Conteo de comentarios positivos:', len(positive_feedbacks))
print(positive_feedbacks)
print('Conteo de comentarios negativos:', len(negative_feedbacks))
print(negative_feedbacks)
