# this is a module for parsing URL/URI

import re

def uriManipulation(num):

    if type(int((num)) not in [int]:
        raise TypeError(" Your input must be a number\n")
    if ( int(num) < 1 or int(num) > 6 ):
        raise ValueError(" Enter a number within the range\n")

    
    regex = r"(https?:\/\/(www\.)?)([^\/]+)\/([^\/]+)\/([^\/]+)\/(.*)"

    test_str = ("http://www.some_domain.com/some_other_slash/another_slash/\n"
    "https://www.some_domain.com/some_other_slash/another_slash/\n"
    "http://some_domain.co.uk/some_other_slash/another_slash/\n"
    "https://some_domain.co.uk/some_other_slash/another_slash/more_data_here")


    subst = '\\' + str(num)

    # manually specify the number of replacements by changing the 4th argument
    result = re.sub(regex, subst, test_str, 0, re.MULTILINE)

    if result:
        print (result)

    