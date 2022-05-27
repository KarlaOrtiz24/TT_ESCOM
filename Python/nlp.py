import stanza

# La descarga del modelo debe realizarse solo en instalación o actualización
# stanza.download('es')

def nlp(Frase):
    #Creación objeto nlp
    nlp = stanza.Pipeline('es', processors='tokenize,lemma,pos,mwt', logging_level='WARN')
    doc = nlp(Frase)
    dicts = doc.to_dict()

    lemma = []

    for token in dicts[0]:

        try:
            lemma.append(token['lemma'])

            #Revisamos el tiempo verbal de la oración
            if (lemma[0] != 'pasado' and lemma[0] != 'futuro'):
                if(token['upos'] == "VERB" or token['upos'] == "AUX"):
                    if('Tense=Imp' in token['feats']):
                        lemma.insert(0, 'pasado')
                    if('Tense=Fut' in token['feats']):
                        lemma.insert(0, 'futuro')

            #Comprobamos que el sujeto este antes de los verbos
            pos = len(lemma)
            if(token['upos'] == "VERB" and (dicts[0][pos]['upos'] != "AUX" and dicts[0][pos]['upos'] != "NOUN")):

                if ('Number=Sing' in dicts[0][pos-1]['feats'] and 'Person=1' in dicts[0][pos-1]['feats']):
                    lemma.insert(pos - 1, "yo")

                if ('Number=Sing' in dicts[0][pos-1]['feats'] and 'Person=2' in dicts[0][pos-1]['feats']):
                    lemma.insert(pos - 1, "tú")

                if ('Number=Sing' in dicts[0][pos-1]['feats'] and 'Person=3' in dicts[0][pos-1]['feats']):
                    lemma.insert(pos - 1, "él")

                if ('Number=Plur' in dicts[0][pos-1]['feats'] and 'Person=1' in dicts[0][pos-1]['feats']):
                    lemma.insert(pos - 1, "nosotros")

                if ('Number=Plur' in dicts[0][pos-1]['feats'] and 'Person=2' in dicts[0][pos-1]['feats']):
                    lemma.insert(pos - 1, "ustedes")

                if ('Number=Plur' in dicts[0][pos-1]['feats'] and 'Person=3' in dicts[0][pos-1]['feats']):
                    lemma.insert(pos - 1, "ellos")

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
   

        except:
            continue


    return lemma
