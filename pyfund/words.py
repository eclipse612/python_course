#!/usr/bin/env python3.2

"""Retrieve and print words from a URL

Usage: 
    python3 words.py <URL> 
"""

import sys
from urllib.request import urlopen


def fetch_words(url):
    """Fetch a list of words from a UTF-8 text at a URL
    
    Args:
        The URL

    Returns:
        The list of words 
    """ 
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_items(items):
    """Print a list of items

    Args:
        An iterable object of printable items

    """
    for item in items:
        print(item)


def main(url):
    """Execute the functions in the module

    Args:
        The URL to fetch text from

    """
    words = fetch_words(url)
    print_items(words)


if (__name__) == '__main__':
    main(sys.argv[1]) 

