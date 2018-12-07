from typing import Iterable
from collections import Counter


class Classifier:
    def __init__(self):
        self.contains_doubles = []
        self.contains_triples = []

    def add_id(self, id_: str):
        counter = Counter()

        for letter in id_:
            counter[letter] += 1

        if any(count == 2 for _, count in counter.items()):
            self.contains_doubles.append(id_)

        if any(count == 3 for _, count in counter.items()):
            self.contains_triples.append(id_)


def classify_ids(ids: Iterable) -> Classifier:
    classifier = Classifier()
    for id_ in ids:
        classifier.add_id(id_)
    return classifier


if __name__ == '__main__':
    with open('data/2.txt', 'r') as file:
        classifier = classify_ids([x.strip() for x in file.readlines()])

    print((
        "         Doubles: {}\n"
        "         Triples: {}\n"
        "Checksum (d * t): {}"
    ).format(
        len(classifier.contains_doubles),
        len(classifier.contains_triples),
        len(classifier.contains_doubles) * len(classifier.contains_triples)
    ))
