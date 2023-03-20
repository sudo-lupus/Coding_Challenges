'''
Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples
The output expected would be:

apples, pears
grapes
bananas
The code would be called like so:

result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
'''

def solution(string,markers):
    print([string, markers])
    import re
    print(string)
    for marker in markers:
        string = re.sub(r"([\{}]).*".format(marker), "", string)            # Replaces anything after marker until EoL with ""
    lines = re.findall(r"(.*\n|.*$)", string)                               # Splits strings into individual lines at line breaks
    lines = [re.sub(r"( *|\t*)\n", "\n", line) for line in lines][:-1]      # Removes tabs and spaces at EoL
    try:
        lines[-1] = re.sub("( *|\t*)$", "", lines[-1])                      # Removes Spaces and tabs at end of last line
    except IndexError:
        pass
    return "".join(lines)