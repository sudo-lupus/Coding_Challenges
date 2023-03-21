'''
Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. IPs should be considered valid if they consist of four octets, with values between 0 and 255, inclusive.

Valid inputs examples:
Examples of valid inputs:
1.2.3.4
123.45.67.89
Invalid input examples:
1.2.3
1.2.3.4.5
123.456.78.90
123.045.067.089
Notes:
Leading zeros (e.g. 01.02.03.04) are considered invalid
Inputs are guaranteed to be a single string
'''

def is_valid_IP(strng):
    import re
    valid = re.findall("^([\d]{1,3})\.([\d]{1,3})\.([\d]{1,3})\.([\d]{1,3})\Z", strng)
    if len(valid) == 0:
        return False
    octets = [valid[0][i] for i in range(0,4)]
    for octet in octets:
        if octet == "0":
            continue
        lstripped_octet = octet.lstrip("0")
        if octet != lstripped_octet:
            return False
        if int(octet) >= 0 and int(octet) <= 255:
            continue
        else:
            return False
    return True