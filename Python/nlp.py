from spacy.lang.es import Spanish

#creación objeto nlp
nlp = Spanish()

#Creado procesando un string de texto con el objeto de nlp
doc = nlp("El abuelo come durazno")

for token in doc:
    print(token.text) 
    


# tok = doc[1]
# tok.i #indice
# tok.text #texto
# tok.is_alpha() #Alfabetivo
# tok.is_punct() #puntuacion
# tok.like_num() #es o parece numero

#https://www.youtube.com/watch?v=RNiLVCE5d4k