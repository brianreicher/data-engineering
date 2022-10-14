import json
from collections import Counter


class Parser():
# CAN TOTALLY IMPLEMENT WITH SOME ABSTRACTION
    def __init__(self) -> None:
        pass

    @staticmethod
    def json_parser(filename):
        f =  open(filename)
        raw = json.load(f)
        text = raw['text']
        words = text.split(" ")
        wc = Counter(words)
        num = len(words)
        return {'wordcount':wc, 'numwords':num}