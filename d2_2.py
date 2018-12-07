from typing import Iterable
from collections import namedtuple


Match = namedtuple('Match', ['commonletters', 'diffcount', 'ids'])


class IDComparingMachine:
    def __init__(self):
        self.registry = []

    @classmethod
    def compare_ids(_, id1: str, id2: str) -> Match:
        """
        Returns a string of letters that are the same letter in the same
        position between two ids and a count of letters that are different
        """
        pairs = zip(id1, id2)
        matched_pairs = filter(lambda pair: pair[0] == pair[1], pairs)
        match_string = "".join([letter for letter, _ in matched_pairs])
        return Match(
            match_string,
            len(id1) - len(match_string),
            (id1, id2)
        )

    def register_id(self, id_: str) -> Iterable[Match]:
        """
        Add an id to the registry and return already registred ids in order
        of how close they are to the new id
        """

        result = sorted(
            [self.compare_ids(id_, old_id) for old_id in self.registry],
            key=lambda match: match.diffcount
        )

        self.registry.append(id_)

        return result


def find_correct_ids(ids: Iterable) -> IDComparingMachine:
    machine = IDComparingMachine()
    for id_ in ids:
        result = machine.register_id(id_)

        if len(result) == 0:
            continue

        # When we find the matches that differ by only one letter, return them
        if result[0].diffcount == 1:
            return result[0]


if __name__ == '__main__':
    with open('data/2.txt', 'r') as file:
        correct_ids = find_correct_ids([x.strip() for x in file.readlines()])

    print(
        "Common letters for correct ids: {}".format(correct_ids.commonletters)
    )
