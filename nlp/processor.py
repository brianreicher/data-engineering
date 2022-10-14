from collections import defaultdict, Counter
import random


class Processor:

    def __init__(self):
        """Constructor"""
        self.data = defaultdict(dict)  # extracted data

    @staticmethod
    def _default_parser(filename):
        return {
            'wordcount': Counter('my name is Jeff'.split(' ')),
            'numwords': random.randrange(10, 50)
        }

    def _save_results(self, label, text):
        for i, j in text.items():
            self.data[i][label] = j

    # label = A
    # results = {'wordcount': wcA. 'numwords': 25}
    # results = {'wordcount': wcB. 'numwords': 30}
    # data = {'wordcount': {'A': wcA, 'B':wcB}, 'numwords': {'A':25, 'B':30}}

    def load_text(self, file_name, label=None, parser=None):
        """
        Registers text file with NLP framework
        :param file_name:
        :param label:
        :param parser:
        :return:
        """
        if parser is None:
            text = Processor._default_parser(file_name)
        else:
            text = parser(file_name)

        if label is None:
            label = file_name

        self._save_results(label, text)