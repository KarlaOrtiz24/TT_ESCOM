import stanza

# La descarga del modelo debe realizarse solo en instalación o actualización
# stanza.download('es')

def nlp(Frase):
    #Creación objeto nlp
    nlp = stanza.Pipeline('es', processors='tokenize,lemma,pos,mwt', logging_level='WARN')
    doc = nlp(Frase)
    dicts = doc.to_dict()

    lemma = []
    aux = 0
    for token in dicts[0]:
        print(token)
        try:
            lemma.append(token['lemma'])

            #Comprobamos que el token no sea un articulo
            if(token['upos'] == "DET" and 'PronType=Art' in token['feats']):
                lemma.pop()

            #Comprobamos que el token no sea una preposición
            if(token['upos'] == "ADP"):
                lemma.pop()

            #Comprobamos que no aparezcan los verbos ser o estar
            if(token['lemma'] == "estar" or token['lemma'] == "ser"):
                lemma.pop()

            #Comprobamos la cantidad de los sustantivos
            if (token['upos'] == "NOUN" and 'Number=Plur' in token['feats']):
                lemma.append('muchos')
                
            #Comprobamos que el sujeto este antes de los verbos
            # lemma.insert(posición, "nuevo elemento")
            

        except:
            continue

        aux += 1


    return lemma

glosa = nlp("La construcción de la escuela ya está avanzada")
print (glosa)