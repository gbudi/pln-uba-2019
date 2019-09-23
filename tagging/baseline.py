from collections import defaultdict


class BadBaselineTagger:

    def __init__(self, tagged_sents, default_tag='nc0s000'):
        """
        tagged_sents -- training sentences, each one being a list of pairs.
        default_tag -- tag for all words.
        """
        self._default_tag = default_tag

    def tag(self, sent):
        """Tag a sentence.

        sent -- the sentence.
        """
        return [self.tag_word(w) for w in sent]

    def tag_word(self, w):
        """Tag a word.

        w -- the word.
        """
        return self._default_tag

    def unknown(self, w):
        """Check if a word is unknown for the model.

        w -- the word.
        """
        return True

class BaselineTagger:

    def __init__(self, tagged_sents, default_tag=None):
        """
        tagged_sents -- training sentences, each one being a list of pairs.
        default_tag -- tag for unknown words.
        """
        # WORK HERE!!
        self._default_tag = default_tag
        self._wcount = {}
        
        for sent in tagged_sents:
            for word in sent:
                if word[0] not in self._wcount:
                    self._wcount[word[0]] = {}
                if word[1] not in self._wcount[word[0]]:
                    self._wcount[word[0]][word[1]] = 0
                self._wcount[word[0]][word[1]] += 1
        

    def tag(self, sent):
        """Tag a sentence.

        sent -- the sentence.
        """
        return [self.tag_word(w) for w in sent]

    def tag_word(self, w):
        """Tag a word.

        w -- the word.
        """
        # WORK HERE!!
        ans = self._default_tag
        
        if not self.unknown(w):
            max = 0
            for tag in self._wcount[w]:
                if self._wcount[w][tag] > max:
                    max = self._wcount[w][tag]
                    ans = tag
        
        return ans


    def unknown(self, w):
        """Check if a word is unknown for the model.

        w -- the word.
        """
        # WORK HERE!!
        return not (w in self._wcount)
        