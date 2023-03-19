'''
Remove exclamation Marks

Write function RemoveExclamationMarks which removes all exclamation marks from a given string.
'''

def remove_exclamation_marks(s):
    import re
    return re.sub("!", "", s)