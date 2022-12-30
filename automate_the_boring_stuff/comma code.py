import sys


def comma_code(choice_list):
    """ Take any python list and print it out without brackets and separate
    each index with a comma"""

    for object in choice_list:
        sys.stdout.write(object)
        if object != choice_list[-1]:
            sys.stdout.write(', ')


spam = ['apples', 'bananas', 'tofu', 'cats']

comma_code(spam)
