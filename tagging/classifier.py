from sklearn.pipeline import Pipeline
from sklearn.feature_extraction import DictVectorizer
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB


classifiers = {
    'lr': LogisticRegression,
    'svm': LinearSVC,
    'mnb': MultinomialNB
}

def word_features(sent, i, prefijo):
    return {
        (prefijo + 'lower'):        sent[i].lower()     if (i >= 0 and i < len(sent)) else '',
        (prefijo + 'istitle'):      sent[i].istitle()   if (i >= 0 and i < len(sent)) else False,
        (prefijo + 'isupper'):      sent[i].isupper()   if (i >= 0 and i < len(sent)) else False,
        (prefijo + 'isdigit'):      sent[i].isdigit()   if (i >= 0 and i < len(sent)) else False,
        (prefijo + 'isplural'):     sent[i][-1:] == 's' if (i >= 0 and i < len(sent)) else False,
        #(prefijo + 'hashyphen'):    '-' in sent[i]      if (i >= 0 and i < len(sent)) else False,
        #(prefijo + 'hasunderscore'): '_' in sent[i]     if (i >= 0 and i < len(sent)) else False,
    }

def feature_dict(sent, i):
    fdict = word_features(sent, i, '')
    fdict.update(word_features(sent, i-1, 'prev_'))
    fdict.update(word_features(sent, i+1, 'next_'))
    return fdict

class ClassifierTagger:
    """Simple and fast classifier based tagger.
    """

    def __init__(self, tagged_sents, clf='lr'):
        """
        clf -- classifying model, one of 'svm', 'lr' (default: 'lr').
        """
        # WORK HERE!!
        self._pipe = Pipeline([
            ('vect', DictVectorizer()),
            ('clf', classifiers[clf]())
        ])
        self._words = set()
        self.fit(tagged_sents)

    def fit(self, tagged_sents):
        """
        Train.

        tagged_sents -- list of sentences, each one being a list of pairs.
        """
        # WORK HERE!!
        X = []
        y_true = []
        for sent in tagged_sents:
            word_sent = [word[0] for word in sent]
            for i in range(0, len(sent)):
                x = feature_dict(word_sent, i)
                X.append(x)
                y_true.append(sent[i][1])
                self._words.add(word_sent[i])
        
        self._pipe.fit(X, y_true)

    def tag_sents(self, sents):
        """Tag sentences.

        sents -- the sentences.
        """
        # WORK HERE!!
        return [self.tag(sent) for sent in sents]

    def tag(self, sent):
        """Tag a sentence.

        sent -- the sentence.
        """
        # WORK HERE!!
        X_test = [feature_dict(sent, i) for i in range(0,len(sent))]
        ans = self._pipe.predict(X_test)
        return ans

    def unknown(self, w):
        """Check if a word is unknown for the model.

        w -- the word.
        """
        # WORK HERE!!
        return not (w in self._words)
