'''
The word i18n is a common abbreviation of internationalization in the developer community, used instead of typing the whole word and trying to spell it correctly. Similarly, a11y is an abbreviation of accessibility.

Write a function that takes a string and turns any and all "words" (see below) within that string of length 4 or greater into an abbreviation, following these rules:

A "word" is a sequence of alphabetical characters. By this definition, any other character like a space or hyphen (eg. "elephant-ride") will split up a series of letters into two words (eg. "elephant" and "ride").
The abbreviated version of the word should have the first letter, then the number of removed characters, then the last letter (eg. "elephant ride" => "e6t r2e").
Example
abbreviate("elephant-rides are really fun!")
//          ^^^^^^^^*^^^^^*^^^*^^^^^^*^^^*
// words (^):   "elephant" "rides" "are" "really" "fun"
//                123456     123     1     1234     1
// ignore short words:               X              X

// abbreviate:    "e6t"     "r3s"  "are"  "r4y"   "fun"
// all non-word characters (*) remain in place
//                     "-"      " "    " "     " "     "!"
=== "e6t-r3s are r4y fun!"
'''

def abbreviate(s):
    import re
    wordlist = re.findall(r"([\W\d])|([A-Za-z]{,3}[^A-Za-z])|([A-Za-z]{4,})", s)
    for i, word in enumerate(wordlist):
        abbrev_word = word[2]
        if abbrev_word != "":
            wordlist[i] = abbrev_word[0] + str(len(abbrev_word) - 2) + abbrev_word[-1]
            continue
        wordlist[i] = word[0] + word[1]
        
    return "".join(wordlist)