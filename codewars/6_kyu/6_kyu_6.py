'''
Encrypt This!

Acknowledgments:
I thank yvonne-liu for the idea and for the example tests :)

Description:
Encrypt this!

You want to create secret messages which can be deciphered by the Decipher this! kata. Here are the conditions:

Your message is a string containing space separated words.
You need to encrypt each word in the message using the following rules:
The first letter must be converted to its ASCII code.
The second letter must be switched with the last letter
Keepin' it simple: There are no special characters in the input.
Examples:
encrypt_this("Hello") == "72olle"
encrypt_this("good") == "103doo"
encrypt_this("hello world") == "104olle 119drlo"
'''

def encrypt_this(text):
    if text == "": return ""

    import re
    words = text.split(" ")
    
    for i, word in enumerate(words):
        ascii = ord(word[0])
        word = re.sub(r"^(\w)(\w)(\w*)(\w)$",r"{}\4\3\2".format(ascii), word)
        if len(word) <= 2:
            word = re.sub("^(.)", f"{ascii}", word)
        words[i] = word
    return " ".join(words)