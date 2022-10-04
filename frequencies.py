"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    stringitem=[];
    for i in items:
        stringitem.append(str(i))

    frequencies = {}
    count = 0
    for item in stringitem:
        count= stringitem.count(item)
        frequencies[item]=count
    return frequencies
