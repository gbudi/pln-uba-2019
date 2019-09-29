"""Train a sequence tagger.

Usage:
  train.py [options] -c <path> -o <file>
  train.py -h | --help

Options:
  -m <model>    Model to use [default: badbase]:
                  badbase: Bad baseline
                  base: Baseline
                  class: Classifier
  --clf <class> Classifier model [default: lr]:
                  lr: Logistic Regression
                  svm: Linear SVC
                  mnb: Multinomial NB
  -c <path>     Ancora corpus path.
  -o <file>     Output model file.
  -h --help     Show this screen.
"""
from docopt import docopt
import pickle

from tagging.ancora import SimpleAncoraCorpusReader
from tagging.baseline import BaselineTagger, BadBaselineTagger
from tagging.classifier import ClassifierTagger


models = {
    'badbase': BadBaselineTagger,
    'base': BaselineTagger,
    'class': ClassifierTagger
}


if __name__ == '__main__':
    opts = docopt(__doc__)

    # load the data
    files = 'CESS-CAST-(A|AA|P)/.*\.tbf\.xml'
    corpus = SimpleAncoraCorpusReader(opts['-c'], files)
    sents = corpus.tagged_sents()

    # train the model
    model_class = models[opts['-m']]
    model = model_class(sents, opts['--clf']) if (opts['-m'] == 'class') else model_class(sents)

    # save it
    filename = opts['-o']
    f = open(filename, 'wb')
    pickle.dump(model, f)
    f.close()
