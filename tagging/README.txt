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

    Ejemplo de uso:
    python tagging/scripts/stats.py -c ancora-3.0.1es

    ACLARACION:
        - ancora-3.0.1es es el path al corpus en la máquina donde se hicieron las pruebas. El mismo 
        deberá reemplazarse por su correspondiente en caso de no ubicar el corpus en la carpeta bajada 
        del repo.

---------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------------------------
Ejercicio 2:

    Se le dió a la clase BaselineTagger las siguientes variables:

    - default_tag: Guarda el tag que se asignará a las palabras desconocidas.
    - wcount: Análogo al wcount del Ejercicio 1. La diferencia es que se usan diccionarios normales en
    lugar de defaultdicts debido a que estos últimos producían un error con pickle para guardar 
    el modelo.

    Para decidir el tag a asignar a una palabra w se itera wcount buscando el tag con más apariciones para 
    dicha w, en el caso de que w sea conocida. Si w es desconocida, se le asigna default_tag. Para 
    etiquetar una oración, simplemente se devuelve como lista el resultado de etiquetar cada palabra de
    de la manera antes descrita.

    Los resultados obtenidos con este modelo fueron los siguientes:

    ---------------------------------------------------------------------------------------
    Accuracy: 85.79% / 95.27% / 0.00% (total / known / unk)

    g \ m   sp000   nc0s000 da0000  aq0000  fc      nc0p000 rg      np00000 fp      cc
    sp000   14.28   0.00    -       -       -       -       0.01    -       -       -
    nc0s000 0.00    10.43   -       0.25    -       0.00    0.03    0.00    -       0.00
    da0000  -       -       9.54    -       -       -       -       -       -       -
    aq0000  0.01    0.24    -       4.84    -       0.13    0.00    -       -       -
    fc      -       -       -       -       5.85    -       -       -       -       -
    nc0p000 -       0.00    -       0.20    -       4.09    -       -       -       -
    rg      0.02    0.02    -       0.04    -       -       3.27    -       -       0.02
    np00000 0.00    0.01    -       0.00    -       0.00    -       1.52    -       0.00
    fp      -       -       -       -       -       -       -       -       3.55    -
    cc      0.00    0.00    -       -       -       -       0.05    0.00    -       3.34
    ---------------------------------------------------------------------------------------

    Se ve que este simple clasificador se desempeña decentemente para palabras conocidas pero muy mal para 
    palabras desconocidas. Los errores más presentes son confundir adjetivos con sustantivos y viceversa.
    
---------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------------------------
Ejercicio 3:

    A la clase ClassifierTagger se le dieron los siguientes atributos:

    - pipe: Un pipeline formado por un DictVectorizer y un classifier. El classifier puede ser uno entre:
        - LogisticRegression
        - LinearSVC
        - MultinomialNB
        
        Mediante el parámetro clf se elige cual de ellos usar. Al script train se le agregó la opción 
        --clf para poder elegirlo desde la línea de comandos.
    
    - words: Conjunto que guardará el vocavulario conocido.


    Para la parte de los features pedidos simplemente se utilizaron las funciones lower(), istitle(), 
    isupper() e isdigit(). Dado que el esqueleto de la función que construye el diccionario de features
    recibía una oración y un índice, se utilizó el mismo índice incrementado y decrementado para obtener 
    los features de la palabra siguiente y anterior respectivamente, teniendo cuidado de consultar dentro 
    de las posiciones válidas.

    De las tagged_sents, se separaron los diccionarios de features y los tags correctos para entrenar al
    pipeline del modelo.  

    A continuación se muestran tiempo de entrenamiento, tiempo de evaluación y resultados obtenidos para
    los features pedidos y los distintos classifiers:

    - LogisticRegression:
        
        Ejemplo de uso:
        python tagging/scripts/train.py -c ancora-3.0.1es -m class --clf lr -o class_lr
        python tagging/scripts/eval.py -c ancora-3.0.1es -i class_lr -p

        Entrenamiento:  8m38s
        Evaluación:     4.55s
        Resultados:     Accuracy: 91.69% / 95.01% / 61.68% (total / known / unk)

    - LinearSVC:

        Ejemplo de uso:
        python tagging/scripts/train.py -c ancora-3.0.1es -m class --clf svm -o class_svm
        python tagging/scripts/eval.py -c ancora-3.0.1es -i class_svm -p

        Entrenamiento:  2m42s
        Evaluación:     4.79s
        Resultados:     Accuracy: 94.11% / 97.57% / 62.76% (total / known / unk)

    - MultinomialNB:

        Ejemplo de uso:
        python tagging/scripts/train.py -c ancora-3.0.1es -m class --clf mnb -o class_mnb
        python tagging/scripts/eval.py -c ancora-3.0.1es -i class_mnb -p

        Entrenamiento:  16.68s
        Evaluación:     1m47.96s
        Resultados:     Accuracy: 84.28% / 88.07% / 49.99% (total / known / unk)

    ACLARACIONES:
        - Los tiempos se tomaron en un computadora con Ubunto 18.04, i5 4440 y 8GB DDR3 de RAM.
        - ancora-3.0.1es es el path al corpus en la máquina donde se hicieron las pruebas. El mismo 
        deberá reemplazarse por su correspondiente en caso de no ubicar el corpus en la carpeta bajada 
        del repo.
        - La versión actual del clasificador tiene features agregdos en el ejercicio 4, por lo que los 
        resultados podrían no coincidir con los acá mostrados. Se pueden comentar los nuevos features
        (señalizados en el código) para recrear estos resultados.

---------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------------------------
Ejercicio 4:

    En la notebook analisis_error.ipynb está el código usado para estudiar los errores cometidos por el 
    modelo y los resultados de los nuevos features propuestos. A continuación los describo de manera 
    resumida:

    Aclaración: Todos los features mencionados se implementaron tanto para la palabra actual, como para la 
    anterior y la siguiente.

    - Uno de los errores más grandes era confundir sustantivos plurales y singulares. Para esto se
    pensó en un feature que me dice si una palabra termina con 's' o no. Se agregó entonces al diccioario 
    ese feature. 

    Resultados:     Accuracy: 94.49% / 97.59% / 66.42% (total / known / unk)

    Se preservó este feature para el resto del análisis pues se obtuvieron buenos resultados.


    - Otro error observado era confundir sustantivos propios con comunes. Dado que ya se estaba observando 
    si la letra inicial de la palabra es mayúscula (que es la idea más inmediata), se observaron algunos 
    ejemplos de las oraciones mal etiquetadas con este error. Se observó que muchos nombres propios mal
    etiquetados contenian guiones bajos y algunos guiones medios. Se agregaron entonces dos features que 
    determinen si una palabra tiene estos guiones y se los evaluaron juntos y por separado:

    Resultados (bajos):     Accuracy: 94.18% / 97.28% / 66.08% (total / known / unk)
    Resultados (medios):    Accuracy: 94.49% / 97.59% / 66.41% (total / known / unk)
    Resultados (ambos):     Accuracy: 94.18% / 97.28% / 66.08% (total / known / unk)

    Como ninguna combinación mejoró el desempeño del modelo, se decidió no conservar estos features.


    - Un feature agregao por intuición fue si la longitud de la palabra es "chicha" (se tomó menor a 4 letras).
    Esto fue bajo los artículos por ejemplo, suelen ser palabras cortas y quizás observar esto podía aportar 
    información sobre el rol de una palabra.

    Resultados:     Accuracy: 94.53% / 97.59% / 66.81% (total / known / unk)

    El rendimiento sobre palabras desconocidas mejora levemente, y como no se reduce el rendimiento global, 
    se decidió conservar el feature.


    - El error más presente es confundir adjetivos y sustantivos. Es el más presente pues se cometía en 
    ambas direcciones (confundir adjetivos por sustantivos y sustantivos por adjetivos) y se comete para 
    ambos tipos de sustantivos (propios y comunes). Luego de observar ejemplos de oraciones mal etiquetadas
    con este error, no se vió alguna propiedad que pueda explotarse como fueature, pero sí ocurrió que 
    varios sustantivos mal etiquetados llevaban tilde. Esto no significa que conozca una relación entre las
    tildes y si una palabra es un adjetivo o un sustantivo, pero sí es una característica del castellano que 
    valdría la pensa observar. Se implemento un feature que me diga si una palabra lleva tilde.

    Resultados:     Accuracy: 94.65% / 97.60% / 67.96% (total / known / unk)

    Este feature mejoró el rendimiento global (y particularmente sobre palabras desconocidas) con lo cual se 
    decidió dejar.


    Habiendo conseguido un accuracy de casi el 70% sobre palabras desconocidas y sin ideas que permitan 
    distinguir adjetivo de sustantivos.

    Hay que aclarar que una idea que se formó mientras se veían ejemplos de errores de etiquetado de adjetivos 
    confundidos con sustantivos, fue la de observar si la palabra tiene algún sufijo específico. Por ejemplo, 
    -al, -ado, etc. Pero al observador el error en el otro sentido, sustantivos confundidos con adjetivos, se 
    vieron ejemplos de sustantivos con esas terminaciones (que podrían también ser adjetivos). Por ejemplo, 
    personal, pasado, etc. Ante el temor de estar implementando un feature que sirve solo para los casos de prueba 
    y dado que la proporción de estos errores no era tan grande como los ejemplos vistos en clase, se decidió no 
    hacer dicha implementación.

---------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------------------------
Ejercicio 5:

    Se descargó un modelo pre-entrenado para el español del enlace en la página de la materia, pero se 
presentan errores al intentar leer el mismo. 