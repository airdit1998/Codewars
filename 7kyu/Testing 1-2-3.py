# Write a function which takes a list of strings and returns each line prepended by the correct number.
# The numbering starts at 1. The format is n: string. Notice the colon and space in between


def number(lines):
    return [str(int(x[0]) + 1) + ': ' + x[1] for x in enumerate(lines)]
