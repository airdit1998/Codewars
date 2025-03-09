# Write a function named first_non_repeating_letter that takes a string input,
# and returns the first character that is not repeated anywhere in the string.
#
# For example, if given the input 'stress', the function should return 't',
# since the letter t only occurs once in the string, and occurs first in the string.
#
# As an added challenge, upper- and lowercase letters are considered the same character,
# but the function should return the correct case for the initial letter.
# For example, the input 'sTreSS' should return 'T'.
#
# If a string contains all repeating characters, it should return an empty string ("") or None

def first_non_repeating_letter(s: str):
    if s != '':
        non_duplicated_list = [x for x in list(s) if s.lower().count(x.lower()) < 2]
        return non_duplicated_list[0] if non_duplicated_list else ''
    else:
        return ""