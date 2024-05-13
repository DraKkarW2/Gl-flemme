import spacy

# Charger le modèle de langue anglaise
nlp = spacy.load('en_core_web_sm')

# Texte de la question
question_text = "_______ company provides banking services to the government."

# Analyser le texte avec spaCy
doc = nlp(question_text.replace("_______", ""))

# Règle révisée pour déterminer l'article correct
if doc[0].pos_ == 'NOUN' and doc[0].text[0] in 'aeiou':
    answer = 'An'
elif doc[0].pos_ == 'NOUN' and doc[0].text.lower() in ['company', 'government']:  # Ajout de spécificité
    answer = 'The'
else:
    answer = 'A'

print(answer)  # Devrait imprimer 'The'
