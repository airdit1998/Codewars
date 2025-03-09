# ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters
# after it in the alphabet. ROT13 is an example of the Caesar cipher.

def search_string(pattern, variable):
    pattern_index = pattern.index(variable) + 13
    return pattern[pattern_index if pattern_index < len(pattern) else pattern_index % len(pattern)]


def rot13(message):
    upper_pattern = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_pattern = 'abcdefghijklmnopqrstuvwxyz'
    bad_pattern = "123456789~!@#$%^&*()_+[]{}|\\,./?-=:;\'\""
    new_string = []
    for var in list(message):
        if var in upper_pattern:
            new_string.append(search_string(upper_pattern, var))
        elif var in lower_pattern:
            new_string.append(search_string(lower_pattern, var))
        elif var in bad_pattern:
            new_string.append(var)
        else:
            new_string.append(var)
    return ''.join(new_string)
