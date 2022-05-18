# Your task is to write a function called valid_spacing() or validSpacing() which checks
# if a string has valid spacing. The function should return either True or False.

def valid_spacing(s):
    if s.startswith(' ') or s.endswith(' '):
        return False
    return '  ' not in s
