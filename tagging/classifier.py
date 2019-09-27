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
        'lower': sent[i].lower(),
        'istitle': sent[i].istitle(),
        'isupper': sent[i].isupper(),
        'isdigit': sent[i].isdigit() 
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

    def fit(self, tagged_sents):
        """
        Train.

        tagged_sents -- list of sentences, each one being a list of pairs.
        """
        # WORK HERE!!
        X = []
        y_true = []
        for sent in tagged_sents:
            for i in range(0, len(sent)):
                x = feature_dict(sent, i)
                X.append(x)
                y_true.append(sent[i][1])
                self._words.add(sent[i])
        
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
        ans = self._pipe.predict(X_test)[0]
        return ans

    def unknown(self, w):
        """Check if a word is unknown for the model.

        w -- the word.
        """
        # WORK HERE!!
        return not (w in self._words)
