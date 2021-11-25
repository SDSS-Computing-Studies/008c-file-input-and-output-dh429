#!python3
'''
Read the data from the file task01.txt
Create a function called find().
Find will require 1 input parameter that is a string literal.
The return value is the line number (starting at 0) that the parameter to be found is on.

Example:
assert find('apple') == 0
assert find('fish') == 5
'''

fname = 'task01.txt'


def find(needle):
    file = open(fname, 'r')
    data = file.read()
    flist = data.split('\n')
    flook = 0
    check = True
    while check:
        if needle in flist[flook]:
            check = False
            return flook
        else:
            flook = flook + 1


if __name__ == "__main__":
    assert find('apple') == 0
    assert find('fish') == 5