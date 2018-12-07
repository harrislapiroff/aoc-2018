import re
from typing import Iterable
from itertools import product
from collections import namedtuple, Counter


CLAIM_RE = re.compile(r'#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)')


Claim = namedtuple('Claim', ['id', 'x', 'y', 'w', 'h'])


def parse_claim_string(claim_string: str) -> Claim:
    match = CLAIM_RE.fullmatch(claim_string)
    return Claim(*[int(x) for x in match.groups()])


def count_claims(claim_strings: Iterable[str]) -> Counter:
    """
    Returns a Counter where keys are in cartesian coordinate tuples (x, y) and
    entries are integer counts of the number of claims on that grid square
    """
    fabric = Counter()
    claims = [parse_claim_string(c) for c in claim_strings]
    for claim in claims:
        # Increment every square in the rectangle within the claim range
        xrange = range(claim.x, claim.x + claim.w)
        yrange = range(claim.y, claim.y + claim.h)
        for x, y in product(xrange, yrange):
            fabric[x, y] += 1

    return fabric


if __name__ == '__main__':
    with open('data/3.txt', 'r') as file:
        fabric = count_claims([x.strip() for x in file.readlines()])

    # Find all the squares where the number of claims is 2 or more
    contested_squares = list(filter(
        lambda x: x[1] >= 2,
        fabric.items()
    ))

    print('Contested sqare inches: {}'.format(len(contested_squares)))
