from typing import List


def first_frequency_reached_twice(
    changes: List[str],
    initial_value: int = 0
) -> int:
    value = initial_value
    frequencies_reached = ()
    num_changes = len(changes)
    change_ints = [int(n) for n in changes]

    i = 0
    while value not in frequencies_reached:
        # Add the new frequency to the list of frequencies seen
        frequencies_reached += (value,)
        # Update the frequency with the next change in our list
        value += change_ints[i % num_changes]
        # Increment the counter
        i += 1

    return value


if __name__ == '__main__':
    with open('data/1.txt', 'r') as file:
        print(
            first_frequency_reached_twice(
                [x.strip() for x in file.readlines()]
            )
        )
