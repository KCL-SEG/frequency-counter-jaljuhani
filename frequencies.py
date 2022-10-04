"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    count=0
    for item in items:
        count=items.count(item);
        frequencies[item]=count;
