PLN-Trabajo Práctico 1

---------------------------------------------------------------------------------------------------------
Ejercicio 1: 

    Para obtener las estadísticas pedidas se le dió a la clase POSStats las siguientes
estructuras de datos y variables:

    - wcount: dicc(palabra, dicc(tag, cantidad))
        La idea es, para cada palabra, saber con qué tags aparece y en qué cantidad 
    con cada uno de ellos.

    - tcount: dicc(tag, dicc(palabra, cantidad))
        La idea es, para tag, saber qué palabras aparecen con el mismo y en qué 
    cantidad.

    - sentcount: Contador de oraciones

    En el __init__ de la clase de iteran las tagged_sents y se modifican las estructuras 
y el contador descriptos anteriormente.


    A continuación se explica brevemente como se resuelve cada consulta pedida:

    - sent_count: La cantidad de oraciones. Se devuelve el contador sentcount inicializado en 
    __init__.

    - token_count: La cantidad total de palabras. Se itera wcount y se suman la cantidad de
    apariciones de cada palabra.

    - words: El vocavulario. Se devuelve las claves de wcount.

    - word_count: Tamaño del vocavulario. Se devuelve len() del inciso anterior.

    - word_freq: Similar a token_count pero para una palabra en específico.

    - unambiguous_words: Se itera wcount y se guarda en un conjunto aquellas palabras con solo 
    un tag registrado. Dado que se usa defaultdict, y el mismo agrega una clave con valor por 
    defecto ante una consulta por la misma, hay que tener cuidado de no contar estos casos.

    - ambiguous_words: Similar al anterior pero nos quedamos con las palabras que tengan n tags 
    registrados. Nuevamente, hay que tener cuidado con los casos agregados con el valor por 
    defecto.

    - tags, tag_count, tag_freq: Análogos a words, word_count y word_freq pero usando el diccionario
    tcount.

    - tag_word_dict: se devuelve tcount.


    A continuación, se muestran las estadísticas obtenidas de ejecutar el script:

        Basic Statistics                                                                                                                                                                                                                                                              

        ================                                                                                                                                                                                                                                                              
        sents: 17378                                                                                                                                                                                                                                                                  
        tokens: 517194                                                                                                                                                                                                                                                                
        words: 46501                                                                                                                                                                                                                                                                  
        tags: 85                                                                                                                                                                                                                                                                      

        Most Frequent POS Tags                                                                                                                                                                                                                                                        
        ======================                                                                                                                                                                                                                                                        
        tag     freq    %       top                                                                                                                                                                                                                                                   
        sp000   79884   15.45   (de, en, a, del, con)                                                                                                                                                                                                                                 
        nc0s000 63452   12.27   (presidente, equipo, partido, país, año)                                                                                                                                                                                                              
        da0000  54549   10.55   (la, el, los, las, El)                                                                                                                                                                                                                                
        aq0000  33906   6.56    (pasado, gran, mayor, nuevo, próximo)                                                                                                                                                                                                                 
        fc      30147   5.83    (,)                                                                                                                                                                                                                                                   
        np00000 29111   5.63    (Gobierno, España, PP, Barcelona, Madrid)                                                                                                                                                                                                             
        nc0p000 27736   5.36    (años, millones, personas, países, días)                                                                                                                                                                                                              
        fp      17512   3.39    (.)                                                                                                                                                                                                                                                   
        rg      15336   2.97    (más, hoy, también, ayer, ya)                                                                                                                                                                                                                         
        cc      15023   2.90    (y, pero, o, Pero, e)                                                                                                                                                                                                                                 

        Word Ambiguity Levels                                                                                                                                                                                                                                                         
        =====================                                                                                                                                                                                                                                                         
        n       words   %       top                                                                                                                                                                                                                                                   
        1       43972   94.56   (,, con, por, su, El)                                                                                                                                                                                                                                 
        2       2318    4.98    (el, en, y, ", los)                                                                                                                                                                                                                                   
        3       180     0.39    (de, la, ., un, no)                                                                                                                                                                                                                                   
        4       23      0.05    (que, a, dos, este, fue)                                                                                                                                                                                                                              
        5       5       0.01    (mismo, cinco, medio, ocho, vista)
        6       3       0.01    (una, como, uno)
        7       0       0.00    ()
        8       0       0.00    ()
        9       0       0.00    ()

    Tags:
    - sp000:    Preposición
    - nc0s000:  Sustantivo común singular
    - da0000:   Artículo
    - aq0000:   Adjetivo descriptivo
    - fc:       Coma (,)
    - np00000:  Sustantivo propio
    - nc0p000:  Sustantivo común plural
    - fp:       Punto (.)
    - rg:       Advervio general
    - cc:       Conjunción coordinante

    ---------------------------------------------------------------------------------------------------------
