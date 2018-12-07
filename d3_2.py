import re
from typing import Iterable, Tuple, List
from itertools import product
from collections import namedtuple, Counter


CLAIM_RE = re.compile(r'#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)')


Claim = namedtuple('Claim', ['id', 'x', 'y', 'w', 'h'])


def parse_claim_string(claim_string: str) -> Claim:
    match = CLAIM_RE.fullmatch(claim_string)
    return Claim(*[int(x) for x in match.groups()])


def inner_squares(claim: Claim) -> List[Tuple[int, int]]:
    """
    Given a Claim object, return a list of all integer cartesian coordinate
    within the rectangle of that claim
    """
    xrange = range(claim.x, claim.x + claim.w)
    yrange = range(claim.y, claim.y + claim.h)
    return product(xrange, yrange)


def count_claims(claims: Iterable[Claim]) -> Counter:
    """
    Returns a Counter where keys are in cartesian coordinate tuples (x, y) and
    entries are integer counts of the number of claims on that grid square
    """
    fabric = Counter()
    for claim in claims:
        # Increment every square in the rectangle within the claim range
        for coords in inner_squares(claim):
            fabric[coords] += 1

    return fabric


def find_uncontested_claim(claims: Iterable[Claim]) -> int:
    # Mark up a grid with all the competing claims
    fabric = count_claims(claims)

    # Now iterate through the claims again and stop when we find one that
    # contains only 1s
    for claim in claims:
        if all(fabric[coords] == 1 for coords in inner_squares(claim)):
            return claim


if __name__ == '__main__':
    with open('data/3.txt', 'r') as file:
        claims = [parse_claim_string(c.strip()) for c in file.readlines()]

    uncontested_claim = find_uncontested_claim(claims)
    print('Uncontested claim ID: {}'.format(uncontested_claim.id))
