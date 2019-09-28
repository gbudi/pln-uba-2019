from sklearn.pipeline import Pipeline
from sklearn.feature_extraction import DictVectorizer
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB


classifiers = {
    'lr': LogisticRegression,
    'svm': LinearSVC,
}


def feature_dict(sent, i):
    """Feature dictionary for a given sentence and position.

    sent -- the sentence.
    i -- the position.
    """
    # WORK HERE!!
    return {
        'lower':    sent[i].lower(),
        'istitle':  sent[i].istitle(),
        'isupper':  sent[i].isupper(),
        'isdigit':  sent[i].isdigit(),
        'prev_lower':   sent[i-1].lower()   if (i > 0) else '',
        'prev_istitle': sent[i-1].istitle() if (i > 0) else False,
        'prev_isupper': sent[i-1].isupper() if (i > 0) else False,
        'prev_isdigit': sent[i-1].isdigit() if (i > 0) else False,
        'next_lower':   sent[i+1].lower()   if (i < len(sent) - 1) else '',
        'next_istitle': sent[i+1].istitle() if (i < len(sent) - 1) else False,
        'next_isupper': sent[i+1].isupper() if (i < len(sent) - 1) else False,
        'next_isdigit': sent[i+1].isdigit() if (i < len(sent) - 1) else False,  
    }

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
            ('clf', MultinomialNB())
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
