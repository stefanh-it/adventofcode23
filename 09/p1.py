"""Puzzle Day 9 part 1 solution."""


def process_acc_sum(histories, acc_sum):
    """Calculate the specified game result value."""
    for history in histories:
        acc_sum += history[-1]
    return acc_sum


def process_history(history):
    """Process the history of a dataset in a row."""
    next_sequence = []
    for i, val in enumerate(history):
        if i < len(history) - 1:
            new_val = history[i+1] - val
            next_sequence.append(new_val)
        else:
            break
    return next_sequence


def process_row(row, acc_sum):
    """Process the rows from the input file."""
    history = row.split(" ")
    history = [int(i) for i in history]
    histories = []
    histories.append(history)
    next_sequence = process_history(history)
    while all(digit == 0 for digit in next_sequence) is False:
        histories.append(next_sequence)
        next_sequence = process_history(next_sequence)
    histories = histories[::-1]
    acc_sum += process_acc_sum(histories, acc_sum)
    return acc_sum


def main(data):
    """Entering point of puzzle solution."""
    prediction = ''
    acc_sum = 0
    total_sum = 0
    rows = data.splitlines()
    for row in rows:
        prediction = process_row(row, acc_sum)
        total_sum += prediction
    return total_sum


if __name__ == "__main__":
    main(data)
